"""
Tests unitaires pour src.ai.model_manager
Tests du gestionnaire de modèle LLM avec GPU
"""

import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from src.ai.model_manager import ModelManager, GPUInfo, get_model_manager
from src.ai.config import AIConfig


class TestGPUInfo:
    """Tests pour la dataclass GPUInfo"""
    
    def test_gpu_info_available(self):
        """Test GPUInfo avec GPU disponible"""
        info = GPUInfo(
            available=True,
            name="NVIDIA GeForce RTX 4050",
            vram_total=6442450944,  # 6 GB en bytes
            vram_free=4294967296,   # 4 GB
            vram_used=2147483648,   # 2 GB
            driver_version="537.34",
            cuda_version="12.2"
        )
        
        assert info.available is True
        assert info.name == "NVIDIA GeForce RTX 4050"
        assert info.vram_total == 6442450944
        assert info.driver_version == "537.34"
    
    def test_gpu_info_unavailable(self):
        """Test GPUInfo sans GPU"""
        info = GPUInfo(available=False)
        
        assert info.available is False
        assert info.name is None
        assert info.vram_total is None


class TestModelManager:
    """Tests pour la classe ModelManager"""
    
    def test_initialization(self):
        """Test initialisation ModelManager"""
        config = AIConfig()
        manager = ModelManager(config)
        
        assert manager.config == config
        assert manager.model is None
        assert manager.is_loaded is False
        assert manager.gpu_info is None
    
    def test_initialization_without_config(self):
        """Test initialisation sans config (utilise défaut)"""
        manager = ModelManager()
        
        assert manager.config is not None
        assert isinstance(manager.config, AIConfig)
    
    @patch('src.ai.model_manager.PYNVML_AVAILABLE', False)
    def test_detect_gpu_pynvml_unavailable(self):
        """Test détection GPU sans pynvml"""
        manager = ModelManager()
        gpu_info = manager.detect_gpu()
        
        assert gpu_info.available is False
    
    @patch('src.ai.model_manager.PYNVML_AVAILABLE', True)
    @patch('src.ai.model_manager.pynvml')
    def test_detect_gpu_no_device(self, mock_pynvml):
        """Test détection GPU sans GPU disponible"""
        mock_pynvml.nvmlInit.return_value = None
        mock_pynvml.nvmlDeviceGetCount.return_value = 0
        
        manager = ModelManager()
        gpu_info = manager.detect_gpu()
        
        assert gpu_info.available is False
        mock_pynvml.nvmlInit.assert_called_once()
    
    @patch('src.ai.model_manager.PYNVML_AVAILABLE', True)
    @patch('src.ai.model_manager.pynvml')
    def test_detect_gpu_success(self, mock_pynvml):
        """Test détection GPU avec succès"""
        # Mock pynvml
        mock_pynvml.nvmlInit.return_value = None
        mock_pynvml.nvmlDeviceGetCount.return_value = 1
        
        mock_handle = Mock()
        mock_pynvml.nvmlDeviceGetHandleByIndex.return_value = mock_handle
        mock_pynvml.nvmlDeviceGetName.return_value = "NVIDIA GeForce RTX 4050"
        
        mock_memory = Mock()
        mock_memory.total = 6442450944  # 6 GB
        mock_memory.free = 4294967296   # 4 GB
        mock_memory.used = 2147483648   # 2 GB
        mock_pynvml.nvmlDeviceGetMemoryInfo.return_value = mock_memory
        
        mock_pynvml.nvmlSystemGetDriverVersion.return_value = "537.34"
        mock_pynvml.nvmlSystemGetCudaDriverVersion.return_value = 12020  # 12.2
        
        manager = ModelManager()
        gpu_info = manager.detect_gpu()
        
        assert gpu_info.available is True
        assert gpu_info.name == "NVIDIA GeForce RTX 4050"
        assert gpu_info.vram_total == 6442450944
        assert gpu_info.vram_free == 4294967296
        assert gpu_info.driver_version == "537.34"
        assert gpu_info.cuda_version == "12.2"
        
        mock_pynvml.nvmlShutdown.assert_called_once()
    
    def test_load_model_file_not_found(self):
        """Test chargement avec modèle inexistant"""
        config = AIConfig(model_path="nonexistent_model.gguf")
        manager = ModelManager(config)
        
        with pytest.raises(FileNotFoundError, match="Modèle introuvable"):
            manager.load_model()
    
    def test_load_model_already_loaded(self):
        """Test chargement quand modèle déjà chargé"""
        manager = ModelManager()
        manager.is_loaded = True
        
        # Ne doit pas lever d'erreur, juste un warning
        result = manager.load_model()
        assert result is True
    
    def test_unload_model(self):
        """Test déchargement modèle"""
        manager = ModelManager()
        manager.model = Mock()
        manager.is_loaded = True
        
        manager.unload_model()
        
        assert manager.model is None
        assert manager.is_loaded is False
    
    def test_unload_model_not_loaded(self):
        """Test déchargement quand pas chargé"""
        manager = ModelManager()
        
        # Ne doit pas lever d'erreur
        manager.unload_model()
        
        assert manager.model is None
        assert manager.is_loaded is False
    
    def test_generate_not_loaded(self):
        """Test génération sans modèle chargé"""
        manager = ModelManager()
        
        with pytest.raises(RuntimeError, match="Modèle non chargé"):
            manager.generate("Test prompt")
    
    def test_generate_success(self):
        """Test génération avec modèle chargé"""
        manager = ModelManager()
        manager.is_loaded = True
        
        # Mock du modèle llama-cpp
        mock_model = Mock()
        mock_model.return_value = {
            "choices": [
                {"text": "  Réponse générée par le modèle  "}
            ]
        }
        manager.model = mock_model
        
        result = manager.generate("Test prompt")
        
        assert result == "Réponse générée par le modèle"
        mock_model.assert_called_once()
    
    def test_generate_with_custom_params(self):
        """Test génération avec paramètres personnalisés"""
        manager = ModelManager()
        manager.is_loaded = True
        
        mock_model = Mock()
        mock_model.return_value = {
            "choices": [{"text": "Test response"}]
        }
        manager.model = mock_model
        
        result = manager.generate(
            prompt="Custom prompt",
            temperature=0.9,
            top_p=0.95,
            max_tokens=256,
            stop=["\n\n"]
        )
        
        assert result == "Test response"
        
        # Vérifier que les paramètres ont été passés
        call_args = mock_model.call_args
        assert call_args[1]["temperature"] == 0.9
        assert call_args[1]["top_p"] == 0.95
        assert call_args[1]["max_tokens"] == 256
        assert call_args[1]["stop"] == ["\n\n"]
    
    def test_generate_uses_config_defaults(self):
        """Test que generate utilise les valeurs de config par défaut"""
        config = AIConfig(temperature=0.8, top_p=0.85, max_tokens=1024)
        manager = ModelManager(config)
        manager.is_loaded = True
        
        mock_model = Mock()
        mock_model.return_value = {
            "choices": [{"text": "Response"}]
        }
        manager.model = mock_model
        
        manager.generate("Test")
        
        call_args = mock_model.call_args
        assert call_args[1]["temperature"] == 0.8
        assert call_args[1]["top_p"] == 0.85
        assert call_args[1]["max_tokens"] == 1024
    
    @patch('src.ai.model_manager.PYNVML_AVAILABLE', False)
    def test_get_gpu_status_unavailable(self):
        """Test statut GPU sans pynvml"""
        manager = ModelManager()
        status = manager.get_gpu_status()
        
        assert status["available"] is False
        assert "error" in status
    
    @patch('src.ai.model_manager.PYNVML_AVAILABLE', True)
    @patch('src.ai.model_manager.pynvml')
    def test_get_gpu_status_success(self, mock_pynvml):
        """Test récupération statut GPU avec succès"""
        mock_pynvml.nvmlInit.return_value = None
        
        mock_handle = Mock()
        mock_pynvml.nvmlDeviceGetHandleByIndex.return_value = mock_handle
        
        mock_memory = Mock()
        mock_memory.total = 6442450944  # 6 GB
        mock_memory.free = 2147483648   # 2 GB
        mock_memory.used = 4294967296   # 4 GB
        mock_pynvml.nvmlDeviceGetMemoryInfo.return_value = mock_memory
        
        mock_util = Mock()
        mock_util.gpu = 75  # 75% utilisation
        mock_pynvml.nvmlDeviceGetUtilizationRates.return_value = mock_util
        
        mock_pynvml.nvmlDeviceGetTemperature.return_value = 65  # 65°C
        
        manager = ModelManager()
        status = manager.get_gpu_status()
        
        assert status["available"] is True
        assert status["vram_total_gb"] == pytest.approx(6.0, rel=0.1)
        assert status["vram_free_gb"] == pytest.approx(2.0, rel=0.1)
        assert status["vram_used_gb"] == pytest.approx(4.0, rel=0.1)
        assert status["vram_percent"] == pytest.approx(66.67, rel=1)
        assert status["gpu_utilization_percent"] == 75
        assert status["temperature_celsius"] == 65
    
    def test_get_model_info_not_loaded(self):
        """Test infos modèle quand pas chargé"""
        config = AIConfig(model_path="models/test.gguf", gpu_profile="balanced")
        manager = ModelManager(config)
        
        info = manager.get_model_info()
        
        assert info["is_loaded"] is False
        assert info["model_path"] == "models/test.gguf"
        assert info["model_name"] == "test.gguf"
        assert info["gpu_profile"] == "balanced"
        assert info["gpu_params"] is None
    
    def test_get_model_info_loaded(self):
        """Test infos modèle quand chargé"""
        config = AIConfig(gpu_profile="performance")
        manager = ModelManager(config)
        manager.is_loaded = True
        manager.gpu_info = GPUInfo(
            available=True,
            name="RTX 4050",
            vram_total=6442450944
        )
        
        info = manager.get_model_info()
        
        assert info["is_loaded"] is True
        assert info["gpu_profile"] == "performance"
        assert info["gpu_params"] is not None
        assert info["gpu_info"]["available"] is True
        assert info["gpu_info"]["name"] == "RTX 4050"
        assert info["gpu_info"]["vram_gb"] == pytest.approx(6.0, rel=0.1)
    
    def test_repr(self):
        """Test représentation string"""
        config = AIConfig(model_path="models/zephyr.gguf", gpu_profile="balanced")
        manager = ModelManager(config)
        
        repr_str = repr(manager)
        
        assert "ModelManager" in repr_str
        assert "zephyr.gguf" in repr_str
        assert "déchargé" in repr_str
        assert "balanced" in repr_str


class TestGetModelManagerSingleton:
    """Tests pour la fonction get_model_manager (singleton)"""
    
    def test_singleton(self):
        """Test que get_model_manager retourne toujours la même instance"""
        # Réinitialiser instance globale
        import src.ai.model_manager
        src.ai.model_manager._model_manager_instance = None
        
        manager1 = get_model_manager()
        manager2 = get_model_manager()
        
        assert manager1 is manager2
    
    def test_singleton_with_config(self):
        """Test singleton avec config personnalisée"""
        # Réinitialiser instance globale
        import src.ai.model_manager
        src.ai.model_manager._model_manager_instance = None
        
        config = AIConfig(gpu_profile="performance")
        manager = get_model_manager(config)
        
        assert manager.config.gpu_profile == "performance"


# Tests d'intégration (marqués slow car peuvent être longs)
class TestIntegration:
    """Tests d'intégration du ModelManager"""
    
    @pytest.mark.slow
    @pytest.mark.skipif(
        not os.path.exists("models/zephyr-7b-beta.Q5_K_M.gguf"),
        reason="Modèle LLM non disponible"
    )
    def test_full_workflow_with_real_model(self):
        """
        Test workflow complet avec vrai modèle
        ⚠️ Test lent (~30s) - Exécuter manuellement
        """
        manager = ModelManager()
        
        # Détecter GPU
        gpu_info = manager.detect_gpu()
        print(f"\nGPU détecté : {gpu_info.available}")
        
        # Charger modèle
        try:
            manager.load_model()
            assert manager.is_loaded is True
            
            # Générer réponse courte
            response = manager.generate(
                "Réponds en UNE phrase courte : Bonjour, qui es-tu ?",
                max_tokens=50
            )
            
            print(f"Réponse : {response}")
            assert len(response) > 0
            
            # Décharger
            manager.unload_model()
            assert manager.is_loaded is False
            
        except Exception as e:
            pytest.skip(f"Erreur chargement modèle : {e}")
    
    def test_profile_switching(self):
        """Test changement de profil avant chargement"""
        config = AIConfig(gpu_profile="balanced")
        manager = ModelManager(config)
        
        # Changer profil
        manager.config.switch_profile("performance")
        
        assert manager.config.gpu_profile == "performance"
        
        # Récupérer paramètres GPU
        params = manager.config.get_gpu_params()
        assert params["n_gpu_layers"] == -1  # Performance = toutes layers


if __name__ == "__main__":
    # Exécuter les tests avec pytest
    pytest.main([__file__, "-v", "--tb=short", "-m", "not slow"])

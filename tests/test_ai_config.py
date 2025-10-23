"""
Tests unitaires pour src.ai.config
Tests de la configuration IA et des profils GPU
"""

import pytest
import json
import os
import tempfile
from src.ai.config import AIConfig, GPU_PROFILES, get_config, list_profiles


class TestAIConfig:
    """Tests pour la classe AIConfig"""
    
    def test_default_values(self):
        """Test des valeurs par défaut"""
        config = AIConfig()
        
        assert config.model_path == "models/zephyr-7b-beta.Q5_K_M.gguf"
        assert config.context_limit == 10
        assert config.gpu_profile == "balanced"
        assert config.temperature == 0.7
        assert config.top_p == 0.9
        assert config.max_tokens == 512
        assert isinstance(config.system_prompt, str)
        assert len(config.system_prompt) > 0
    
    def test_custom_values(self):
        """Test avec valeurs personnalisées"""
        config = AIConfig(
            model_path="models/custom_model.gguf",
            context_limit=20,
            gpu_profile="performance",
            temperature=0.9,
            top_p=0.95,
            max_tokens=1024,
            system_prompt="Tu es un assistant test."
        )
        
        assert config.model_path == "models/custom_model.gguf"
        assert config.context_limit == 20
        assert config.gpu_profile == "performance"
        assert config.temperature == 0.9
        assert config.top_p == 0.95
        assert config.max_tokens == 1024
        assert config.system_prompt == "Tu es un assistant test."
    
    def test_validation_success(self):
        """Test validation avec paramètres valides"""
        config = AIConfig()
        assert config.validate() is True
    
    def test_validation_context_limit_invalid(self):
        """Test validation avec context_limit invalide"""
        with pytest.raises(ValueError, match="context_limit doit être un entier"):
            AIConfig(context_limit=0)
        
        with pytest.raises(ValueError, match="context_limit doit être un entier"):
            AIConfig(context_limit=-5)
    
    def test_validation_gpu_profile_invalid(self):
        """Test validation avec gpu_profile invalide"""
        with pytest.raises(ValueError, match="gpu_profile invalide"):
            AIConfig(gpu_profile="invalid_profile")
    
    def test_validation_temperature_invalid(self):
        """Test validation avec temperature invalide"""
        with pytest.raises(ValueError, match="temperature doit être entre"):
            AIConfig(temperature=-0.5)
        
        with pytest.raises(ValueError, match="temperature doit être entre"):
            AIConfig(temperature=2.5)
    
    def test_validation_top_p_invalid(self):
        """Test validation avec top_p invalide"""
        with pytest.raises(ValueError, match="top_p doit être entre"):
            AIConfig(top_p=-0.1)
        
        with pytest.raises(ValueError, match="top_p doit être entre"):
            AIConfig(top_p=1.5)
    
    def test_validation_max_tokens_invalid(self):
        """Test validation avec max_tokens invalide"""
        with pytest.raises(ValueError, match="max_tokens doit être un entier"):
            AIConfig(max_tokens=0)
        
        with pytest.raises(ValueError, match="max_tokens doit être un entier"):
            AIConfig(max_tokens=-100)
    
    def test_validation_system_prompt_empty(self):
        """Test validation avec system_prompt vide"""
        with pytest.raises(ValueError, match="system_prompt ne peut pas être vide"):
            AIConfig(system_prompt="")
        
        with pytest.raises(ValueError, match="system_prompt ne peut pas être vide"):
            AIConfig(system_prompt="   ")
    
    def test_get_gpu_params_balanced(self):
        """Test récupération paramètres GPU (balanced)"""
        config = AIConfig(gpu_profile="balanced")
        params = config.get_gpu_params()
        
        assert isinstance(params, dict)
        assert params["n_gpu_layers"] == 35
        assert params["n_ctx"] == 2048
        assert params["n_batch"] == 256
        assert params["n_threads"] == 6
        assert params["use_mlock"] is True
    
    def test_get_gpu_params_performance(self):
        """Test récupération paramètres GPU (performance)"""
        config = AIConfig(gpu_profile="performance")
        params = config.get_gpu_params()
        
        assert params["n_gpu_layers"] == -1  # Toutes les couches
        assert params["n_ctx"] == 4096
        assert params["n_batch"] == 512
    
    def test_get_gpu_params_cpu_fallback(self):
        """Test récupération paramètres GPU (cpu_fallback)"""
        config = AIConfig(gpu_profile="cpu_fallback")
        params = config.get_gpu_params()
        
        assert params["n_gpu_layers"] == 0  # Aucune couche GPU
        assert params["n_ctx"] == 2048
        assert params["n_batch"] == 128
        assert params["use_mlock"] is False
    
    def test_get_profile_info(self):
        """Test récupération informations profil"""
        config = AIConfig(gpu_profile="balanced")
        info = config.get_profile_info()
        
        assert isinstance(info, dict)
        assert info["name"] == "Balanced"
        assert "description" in info
        assert "vram_estimate" in info
        assert "speed_estimate" in info
        assert "recommended_for" in info
    
    def test_switch_profile(self):
        """Test changement de profil"""
        config = AIConfig(gpu_profile="balanced")
        assert config.gpu_profile == "balanced"
        
        config.switch_profile("performance")
        assert config.gpu_profile == "performance"
        
        config.switch_profile("cpu_fallback")
        assert config.gpu_profile == "cpu_fallback"
    
    def test_switch_profile_invalid(self):
        """Test changement vers profil invalide"""
        config = AIConfig()
        
        with pytest.raises(ValueError, match="Profil GPU invalide"):
            config.switch_profile("nonexistent_profile")
    
    def test_to_dict(self):
        """Test conversion en dictionnaire"""
        config = AIConfig(
            model_path="models/test.gguf",
            context_limit=15,
            gpu_profile="performance",
            temperature=0.8,
            top_p=0.95,
            max_tokens=256,
            system_prompt="Test prompt"
        )
        
        config_dict = config.to_dict()
        
        assert isinstance(config_dict, dict)
        assert config_dict["model_path"] == "models/test.gguf"
        assert config_dict["context_limit"] == 15
        assert config_dict["gpu_profile"] == "performance"
        assert config_dict["temperature"] == 0.8
        assert config_dict["top_p"] == 0.95
        assert config_dict["max_tokens"] == 256
        assert config_dict["system_prompt"] == "Test prompt"
    
    def test_repr(self):
        """Test représentation string"""
        config = AIConfig()
        repr_str = repr(config)
        
        assert "AIConfig" in repr_str
        assert "balanced" in repr_str
        assert "10" in repr_str  # context_limit
        assert "0.7" in repr_str  # temperature


class TestAIConfigJSON:
    """Tests pour le chargement/sauvegarde JSON"""
    
    def test_from_json_file_not_found(self):
        """Test chargement avec fichier inexistant"""
        config = AIConfig.from_json("nonexistent_file.json")
        
        # Doit retourner config par défaut sans erreur
        assert config.gpu_profile == "balanced"
        assert config.temperature == 0.7
    
    def test_from_json_valid(self, tmp_path):
        """Test chargement depuis JSON valide"""
        # Créer fichier JSON temporaire
        config_file = tmp_path / "test_config.json"
        test_data = {
            "ai": {
                "model_path": "models/test_model.gguf",
                "context_limit": 20,
                "gpu_profile": "performance",
                "temperature": 0.9,
                "top_p": 0.95,
                "max_tokens": 1024,
                "system_prompt": "Test system prompt"
            }
        }
        
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        # Charger config
        config = AIConfig.from_json(str(config_file))
        
        assert config.model_path == "models/test_model.gguf"
        assert config.context_limit == 20
        assert config.gpu_profile == "performance"
        assert config.temperature == 0.9
        assert config.top_p == 0.95
        assert config.max_tokens == 1024
        assert config.system_prompt == "Test system prompt"
    
    def test_from_json_missing_ai_section(self, tmp_path):
        """Test chargement avec section 'ai' manquante"""
        config_file = tmp_path / "test_config.json"
        test_data = {
            "other_section": {
                "value": 123
            }
        }
        
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        # Doit retourner config par défaut
        config = AIConfig.from_json(str(config_file))
        assert config.gpu_profile == "balanced"
    
    def test_from_json_partial_config(self, tmp_path):
        """Test chargement avec config partielle (certains champs manquants)"""
        config_file = tmp_path / "test_config.json"
        test_data = {
            "ai": {
                "gpu_profile": "performance",
                "temperature": 0.5
                # Autres champs manquants
            }
        }
        
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        config = AIConfig.from_json(str(config_file))
        
        # Valeurs spécifiées
        assert config.gpu_profile == "performance"
        assert config.temperature == 0.5
        
        # Valeurs par défaut
        assert config.context_limit == 10
        assert config.top_p == 0.9
        assert config.max_tokens == 512
    
    def test_from_json_invalid_json(self, tmp_path):
        """Test chargement avec JSON invalide"""
        config_file = tmp_path / "test_config.json"
        
        with open(config_file, 'w') as f:
            f.write("{ invalid json }")
        
        # Doit retourner config par défaut sans crash
        config = AIConfig.from_json(str(config_file))
        assert config.gpu_profile == "balanced"
    
    def test_save_to_json(self, tmp_path):
        """Test sauvegarde dans JSON"""
        config_file = tmp_path / "test_config.json"
        
        # Créer config
        config = AIConfig(
            model_path="models/saved_model.gguf",
            context_limit=25,
            gpu_profile="cpu_fallback",
            temperature=0.6,
            top_p=0.85,
            max_tokens=768,
            system_prompt="Saved prompt"
        )
        
        # Sauvegarder
        config.save_to_json(str(config_file))
        
        # Vérifier fichier créé
        assert config_file.exists()
        
        # Charger et vérifier
        with open(config_file, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
        
        assert "ai" in saved_data
        assert saved_data["ai"]["model_path"] == "models/saved_model.gguf"
        assert saved_data["ai"]["context_limit"] == 25
        assert saved_data["ai"]["gpu_profile"] == "cpu_fallback"
        assert saved_data["ai"]["temperature"] == 0.6
        assert saved_data["ai"]["top_p"] == 0.85
        assert saved_data["ai"]["max_tokens"] == 768
        assert saved_data["ai"]["system_prompt"] == "Saved prompt"
    
    def test_save_preserves_other_sections(self, tmp_path):
        """Test que save_to_json préserve les autres sections"""
        config_file = tmp_path / "test_config.json"
        
        # Créer config avec d'autres sections
        initial_data = {
            "unity": {
                "host": "127.0.0.1",
                "port": 5555
            },
            "avatar": {
                "default_model": "test.vrm"
            }
        }
        
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f)
        
        # Sauvegarder config IA
        config = AIConfig()
        config.save_to_json(str(config_file))
        
        # Vérifier que les autres sections sont préservées
        with open(config_file, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
        
        assert "unity" in saved_data
        assert saved_data["unity"]["host"] == "127.0.0.1"
        assert "avatar" in saved_data
        assert saved_data["avatar"]["default_model"] == "test.vrm"
        assert "ai" in saved_data


class TestGPUProfiles:
    """Tests pour les profils GPU"""
    
    def test_all_profiles_exist(self):
        """Test que tous les profils attendus existent"""
        assert "performance" in GPU_PROFILES
        assert "balanced" in GPU_PROFILES
        assert "cpu_fallback" in GPU_PROFILES
    
    def test_profile_structure(self):
        """Test structure de chaque profil"""
        required_keys = [
            "name", "description", "n_gpu_layers", "n_ctx",
            "n_batch", "n_threads", "use_mlock",
            "vram_estimate", "speed_estimate", "recommended_for"
        ]
        
        for profile_name, profile_data in GPU_PROFILES.items():
            for key in required_keys:
                assert key in profile_data, (
                    f"Clé manquante '{key}' dans profil '{profile_name}'"
                )
    
    def test_list_profiles(self):
        """Test fonction list_profiles()"""
        profiles = list_profiles()
        
        assert isinstance(profiles, dict)
        assert len(profiles) == 3
        assert "performance" in profiles
        assert "balanced" in profiles
        assert "cpu_fallback" in profiles


class TestGetConfigSingleton:
    """Tests pour la fonction get_config (singleton)"""
    
    def test_get_config_singleton(self):
        """Test que get_config retourne toujours la même instance"""
        # Réinitialiser instance globale
        import src.ai.config
        src.ai.config._config_instance = None
        
        config1 = get_config("data/config.json")
        config2 = get_config("data/config.json")
        
        # Doit être la même instance (singleton)
        assert config1 is config2
    
    def test_get_config_returns_valid_config(self):
        """Test que get_config retourne une config valide"""
        # Réinitialiser instance globale
        import src.ai.config
        src.ai.config._config_instance = None
        
        config = get_config("data/config.json")
        
        assert isinstance(config, AIConfig)
        assert config.validate() is True


# Tests d'intégration
class TestIntegration:
    """Tests d'intégration du système de configuration"""
    
    def test_full_workflow(self, tmp_path):
        """Test workflow complet : création → sauvegarde → chargement"""
        config_file = tmp_path / "workflow_config.json"
        
        # 1. Créer config
        config1 = AIConfig(
            model_path="models/workflow.gguf",
            context_limit=15,
            gpu_profile="performance",
            temperature=0.8
        )
        
        # 2. Sauvegarder
        config1.save_to_json(str(config_file))
        
        # 3. Charger dans nouvelle instance
        config2 = AIConfig.from_json(str(config_file))
        
        # 4. Vérifier égalité
        assert config2.model_path == config1.model_path
        assert config2.context_limit == config1.context_limit
        assert config2.gpu_profile == config1.gpu_profile
        assert config2.temperature == config1.temperature
    
    def test_switch_profile_and_get_params(self):
        """Test switch profil + récupération paramètres"""
        config = AIConfig()
        
        # Balanced
        config.switch_profile("balanced")
        params_balanced = config.get_gpu_params()
        assert params_balanced["n_gpu_layers"] == 35
        
        # Performance
        config.switch_profile("performance")
        params_perf = config.get_gpu_params()
        assert params_perf["n_gpu_layers"] == -1
        assert params_perf["n_ctx"] > params_balanced["n_ctx"]
        
        # CPU Fallback
        config.switch_profile("cpu_fallback")
        params_cpu = config.get_gpu_params()
        assert params_cpu["n_gpu_layers"] == 0
        assert params_cpu["use_mlock"] is False


if __name__ == "__main__":
    # Exécuter les tests avec pytest
    pytest.main([__file__, "-v", "--tb=short"])

"""
Test script to verify CUDA support in llama-cpp-python
"""

import sys

print("=" * 60)
print("🧪 Test du support CUDA dans llama-cpp-python")
print("=" * 60)

try:
    import llama_cpp
    print(f"✅ llama-cpp-python version: {llama_cpp.__version__}")
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

# Test 1: Check CUDA support
print("\n📋 Test 1: Vérification support CUDA")
has_cuda = hasattr(llama_cpp.llama_cpp, 'llama_backend_cuda_init')
print(f"   CUDA support: {'✅ OUI' if has_cuda else '❌ NON'}")

# Test 2: Check backend info
print("\n📋 Test 2: Informations backend")
try:
    # Try to get backend info
    from llama_cpp import llama_cpp
    
    # Check for CUDA-specific functions
    cuda_functions = [
        'llama_backend_cuda_init',
        'llama_backend_cuda_free',
    ]
    
    found_funcs = []
    for func_name in cuda_functions:
        if hasattr(llama_cpp, func_name):
            found_funcs.append(func_name)
    
    if found_funcs:
        print(f"   ✅ Fonctions CUDA trouvées: {len(found_funcs)}")
        for func in found_funcs:
            print(f"      - {func}")
    else:
        print("   ❌ Aucune fonction CUDA trouvée")
        
except Exception as e:
    print(f"   ⚠️ Impossible de vérifier: {e}")

# Test 3: Try to load a model with GPU layers
print("\n📋 Test 3: Test chargement modèle avec GPU layers")
print("   (Nécessite le modèle Zephyr-7B)")

import os
model_path = "models/zephyr-7b-beta.Q5_K_M.gguf"

if os.path.exists(model_path):
    print(f"   ✅ Modèle trouvé: {model_path}")
    
    try:
        print("   ⏳ Tentative de chargement avec 5 GPU layers...")
        from llama_cpp import Llama
        
        model = Llama(
            model_path=model_path,
            n_gpu_layers=5,  # Juste 5 couches pour test rapide
            n_ctx=512,       # Contexte réduit pour test rapide
            verbose=True     # Voir les logs détaillés
        )
        
        print("   ✅ Modèle chargé avec succès !")
        
        # Vérifier si GPU est vraiment utilisé
        print("\n   📊 Vérification utilisation GPU...")
        
        # Test simple de génération
        print("   ⏳ Test génération...")
        output = model("Hello", max_tokens=10, echo=False)
        print(f"   ✅ Génération réussie: {output['choices'][0]['text'][:50]}...")
        
        # Cleanup
        del model
        print("   ✅ Modèle déchargé")
        
    except Exception as e:
        print(f"   ❌ Erreur lors du chargement: {e}")
        import traceback
        traceback.print_exc()
else:
    print(f"   ⚠️ Modèle non trouvé: {model_path}")
    print("   Skipping test...")

print("\n" + "=" * 60)
print("🎯 Résumé:")
if has_cuda:
    print("✅ llama-cpp-python est compilé AVEC support CUDA")
    print("✅ Le modèle peut utiliser la VRAM du GPU NVIDIA")
else:
    print("❌ llama-cpp-python est compilé SANS support CUDA")
    print("❌ Le modèle utilisera uniquement le CPU (RAM)")
print("=" * 60)

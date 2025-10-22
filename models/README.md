# Modèles LLM pour Desktop-Mate (Kira)

Ce dossier contient les modèles de langage (LLM) utilisés par Kira.

## 📦 Modèle Actuel

**`zephyr-7b-beta.Q5_K_M.gguf`**
- Taille : 6.8 GB
- Format : GGUF (llama.cpp compatible)
- Quantification : Q5_K_M (bon équilibre qualité/taille)
- Source : Mistral 7B fine-tuné

## 📥 Installation

### Méthode 1 : Copie depuis Kira-Bot (recommandée)

```bash
# PowerShell
Copy-Item "C:\Dev\IA-chatbot\models\zephyr-7b-beta.Q5_K_M.gguf" "C:\Dev\desktop-mate\models\"
```

### Méthode 2 : Téléchargement direct

Si le fichier n'existe pas dans Kira-Bot, téléchargez-le depuis Hugging Face :

```bash
# URL : https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF
# Fichier : zephyr-7b-beta.Q5_K_M.gguf (6.8 GB)
```

## ⚠️ Important

**Ce dossier est dans `.gitignore` !**

Les modèles LLM sont trop volumineux pour Git (6+ GB).
- ✅ Ils doivent être copiés/téléchargés manuellement
- ❌ Ne JAMAIS les commit dans Git

## 🎯 Utilisation

Le modèle est chargé automatiquement par `ModelManager` :
- Chemin configuré dans `data/config.json` → `ai.model_path`
- Détection GPU automatique
- Profils d'optimisation adaptatifs (Performance, Balanced, CPU Fallback)

## 🔄 Changer de Modèle

Pour utiliser un autre modèle :

1. Télécharger/copier le nouveau modèle dans `models/`
2. Modifier `data/config.json` :
   ```json
   {
     "ai": {
       "model_path": "models/nouveau_modele.gguf"
     }
   }
   ```
3. Redémarrer Desktop-Mate

## 📊 Modèles Compatibles

Tous les modèles GGUF sont compatibles :
- Zephyr 7B (recommandé)
- Mistral 7B
- Phi-2 (plus petit, plus rapide)
- Llama 2/3 (diverses tailles)

**Critère** : Taille < VRAM disponible (RTX 4050 = 6 GB VRAM)

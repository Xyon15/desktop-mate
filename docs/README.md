# 📚 Documentation Desktop-Mate

Organisation de la documentation par sessions de développement.

---

## ⚠️ IMPORTANT - Pour l'IA et les Développeurs

- 📋 **[DOCUMENTATION_CHECKLIST.md](DOCUMENTATION_CHECKLIST.md)** - Checklist systématique à suivre
- 🤖 **[AI_DOCUMENTATION_PROMPT.md](AI_DOCUMENTATION_PROMPT.md)** - Instructions pour maintenir la doc à jour
- 🔧 **[.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)** - Template PR avec vérifications doc

**Règle :** Toujours consulter la checklist avant de terminer une tâche !

---

## 🎯 Système Anti-Oubli Documentation

Ce projet utilise un **système à 3 niveaux** pour garantir que la documentation reste toujours à jour :

1. **GitHub Copilot Chat** → Lit automatiquement `.github/instructions/copilot-instructions.instructions.md`
2. **VS Code Copilot** → Suit `DOCUMENTATION_CHECKLIST.md` et `AI_DOCUMENTATION_PROMPT.md`
3. **Pull Requests** → Template obligatoire avec checklist documentation

**Objectif :** L'utilisateur ne devrait **JAMAIS** avoir à demander "as-tu mis à jour la documentation ?"

---

## 📁 Structure des dossiers

### 📂 chat_transistions/
**Historique des transitions entre chats**
- Archive de chaque session de chat avec documentation complète
- Prompts de transition pour continuité entre chats
- **chat_1_python_unity_start_session_0_to_5/** - Premier chat (MVP)
  - `CURRENT_STATE.md` - État technique complet
  - `prompt_chat1_vers_chat_2.txt` - Prompt pour Chat 2
  - `CHAT_SUMMARY.md` - Résumé détaillé du chat

---

### 📂 session_0_git_configuration/
**Configuration Git pour Unity**
- `GIT_UNITY_FIX.md` - Résolution problème .gitignore Unity
- `README.md` - Vue d'ensemble de la session

**Réalisations :**
- ✅ Configuration `.gitignore` pour Unity
- ✅ Exclusion Library/, Temp/, PackageCache/
- ✅ Documentation bonnes pratiques Git + Unity

---

### 📂 session_1_setup/
**Mise en place initiale du projet Python**
- `SUCCESS_SESSION_1.md` - Récapitulatif de la session 1
- `architecture.md` - Architecture globale du projet

**Réalisations :**
- ✅ Création de la structure du projet Python
- ✅ Configuration de l'environnement virtuel (venv)
- ✅ Installation des dépendances (PySide6, pytest, etc.)
- ✅ Création de l'interface graphique Qt
- ✅ Système de configuration et logging

---

### 📂 session_2_unity_installation/
**Installation et configuration de Unity**
- Documentation de l'installation Unity 2022.3 LTS
- Configuration du projet Unity avec URP (Universal Render Pipeline)

**Réalisations :**
- ✅ Installation Unity Hub
- ✅ Installation Unity 2022.3 LTS
- ✅ Création du projet Unity avec template URP
- ✅ Configuration initiale de la scène

---

### 📂 session_3_univrm_installation/
**Installation du package UniVRM**
- Guide d'installation UniVRM pour le support VRM
- Configuration du package dans Unity

**Réalisations :**
- ✅ Installation UniVRM via .unitypackage
- ✅ Import du package dans le projet Unity
- ✅ Configuration des dépendances (UniGLTF, VRMShaders, etc.)

---

### 📂 session_4_python_unity_connection/
**Communication IPC Python ↔ Unity**
- `TEST_CONNECTION.md` - Guide de test de connexion
- `DEBUG_CONNECTION.md` - Résolution des problèmes de connexion
- `FIX_SCRIPT_NOT_RUNNING.md` - Fix du problème de script Unity non exécuté

**Réalisations :**
- ✅ Création de PythonBridge.cs (serveur socket Unity)
- ✅ Création de unity_bridge.py (client socket Python)
- ✅ Protocole de communication JSON sur TCP (port 5555)
- ✅ Test de connexion réussi
- ✅ Résolution du problème de checkbox du script Unity

**Architecture IPC :**
```
Python (Client) ←→ Socket TCP (127.0.0.1:5555) ←→ Unity (Server)
      │                                                    │
   GUI Button                                    PythonBridge.cs
      │                                                    │
   JSON Message                                   HandleMessage()
```

---

### 📂 session_5_vrm_loading/
**Chargement et affichage des modèles VRM**
- `LOAD_VRM_MODEL.md` - Guide de chargement VRM
- `SESSION_VRM_LOADING_SUCCESS.md` - Récapitulatif complet de la session 5
- `scripts/VRMLoader_CLEAN.cs` - Script VRMLoader propre et commenté

**Réalisations :**
- ✅ Création de VRMLoader.cs pour gérer les modèles VRM
- ✅ Résolution du problème de threading (main thread Unity)
- ✅ Implémentation de la commande `load_model` dans PythonBridge
- ✅ Import du modèle "Mura Mura - Model.vrm" dans Unity
- ✅ Test complet Python → Unity → Affichage VRM réussi ! 🎭

**Problèmes résolus :**
- Threading Unity (Queue + Update() pattern)
- API UniVRM variable selon versions
- Appel GameObject depuis thread réseau

---

### 📂 session_6_expressions/
**Contrôle des expressions faciales via blendshapes VRM**
- `BLENDSHAPES_GUIDE.md` - Guide technique complet des blendshapes
- `UNITY_SETUP_GUIDE.md` - Configuration Unity pas-à-pas
- `SESSION_SUCCESS.md` - Récapitulatif complet de la session 6
- `scripts/VRMBlendshapeController.cs` - Script de référence v1.6

**Réalisations :**
- ✅ Création de VRMBlendshapeController.cs pour gérer les expressions
- ✅ Support de 5 expressions : Joy, Angry, Sorrow, Fun, Surprised
- ✅ Interface Python avec sliders pour contrôler chaque expression
- ✅ Commandes IPC : `set_expression`, `reset_expressions`
- ✅ Thread-safety avec Queue pattern
- ✅ Tests complets : 8/8 tests Python passés

**Architecture expressions :**
```
Python Slider → IPC JSON → PythonBridge → VRMBlendshapeController
                                                    ↓
                                          BlendShapeProxy (UniVRM)
                                                    ↓
                                             VRM 3D Model (expressions)
```

---

### 📂 session_7_animations/
**Système d'animations fluides et transitions** 🎬
- `README.md` - Vue d'ensemble complète de la session 7
- `TRANSITIONS_GUIDE.md` - Guide technique Lerp et interpolation
- `SESSION_SUCCESS.md` - Récapitulatif de succès complet

**Réalisations :**
- ✅ **Transitions fluides** : Interpolation Lerp pour expressions naturelles
- ✅ **Contrôle de vitesse** : Slider 1.0-10.0 (défaut 3.0)
- ✅ **Chargement/Déchargement** : Toggle VRM avec thread-safety
- ✅ **Modèle par défaut** : Sauvegarde config, chargement instantané
- ✅ **VRMBlendshapeController v2.0** : Dictionnaires currentValues/targetValues
- ✅ **PythonBridge amélioré** : Queue mainThreadActions pour thread-safety
- ✅ **UX professionnelle** : Icône app, interface française, messages d'aide

**Innovations techniques :**
- Lerp dans `Update()` pour transitions smooth chaque frame
- Système de modèle par défaut (Menu Fichier → Définir/Utiliser autre)
- Thread-safety complet (Destroy, GetComponent depuis thread principal)
- Slider calibré avec label "3.0 (Normal)" positionné précisément

---

### 📂 Unity_docs/ (legacy)
Ancienne documentation Unity - À réorganiser ou supprimer

### 📂 1st/ (legacy)
Ancien dossier - À vérifier et réorganiser si nécessaire

---

## 🎯 État actuel du projet

### ✅ Phase 1 - MVP Complet
- **Sessions 0-5 terminées** (Chat 1)
- Application Python avec interface Qt
- Communication Python ↔ Unity via socket TCP
- Chargement de modèles VRM depuis Python
- Affichage 3D de l'avatar dans Unity
- Thread-safety résolu (Queue + Update pattern)
- Documentation complète (30+ fichiers)

### ✅ Phase 2 - Expressions & Animations Complètes
- **Session 6 terminée** : Contrôle des expressions faciales (5 expressions)
- **Session 7 terminée** : Animations fluides (Lerp, transitions, vitesse ajustable)
- **Fonctionnalités** :
  - Transitions smooth entre expressions (Lerp interpolation)
  - Contrôle de vitesse en temps réel (1.0-10.0)
  - Système de modèle VRM par défaut
  - Chargement/Déchargement dynamique
  - Interface française complète avec icône
  
### 🚧 Phase 3 - À venir (Chat 3+)
- **Session 8** : Lip-sync avec microphone (analyse audio, phonèmes)
- **Session 9** : Clignement automatique (timer, animations yeux)
- **Session 10** : Face tracking (MediaPipe, expression mirroring)
- **Sessions 11-12** : Intégration IA conversationnelle (chatbot)

---

## 📖 Comment utiliser cette documentation

1. **Nouveau sur le projet :** 
   - Commence par `START_HERE.md`
   - Lis `chat_transistions/chat_1.../CHAT_SUMMARY.md`
   
2. **Reprendre le développement :**
   - Lis `CURRENT_STATE.md` pour l'état actuel
   - Consulte la roadmap dans `README.md` principal
   
3. **Débutant :** Lis les sessions dans l'ordre (0 → 5)

4. **Problème spécifique :** Consulte les fichiers DEBUG_ et FIX_

5. **Référence rapide :** Utilise `INDEX.md` pour navigation

6. **Code propre :** Les scripts finaux sont dans les dossiers `scripts/`

---

## 🔗 Liens utiles

- [Repository GitHub](https://github.com/Xyon15/desktop-mate)
- [État actuel du projet](CURRENT_STATE.md)
- [Index de navigation](INDEX.md)
- [Documentation UniVRM](https://github.com/vrm-c/UniVRM)
- [Documentation Unity](https://docs.unity3d.com/)
- [Documentation PySide6](https://doc.qt.io/qtforpython/)

---

**Dernière mise à jour :** 18 octobre 2025  
**Version du projet :** 0.1.0-alpha  
**Status :** ✅ MVP Complet - Chat 1 terminé (Sessions 0-5)  
**Prochain :** Session 6 - Expressions faciales (Chat 2)

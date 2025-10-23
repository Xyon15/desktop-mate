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

### 📂 chat_transitions/
**Historique des transitions entre chats**
- Archive de chaque session de chat avec documentation complète
- Prompts de transition pour continuité entre chats
- **chat_1_python_unity_start_session_0_to_5/** - Premier chat (MVP)
  - `CURRENT_STATE.md` - État technique complet
  - `prompt_chat1_vers_chat_2.txt` - Prompt pour Chat 2
  - `CHAT_SUMMARY.md` - Résumé détaillé du chat

---

### 📂 docs/sessions/session_0_git_configuration/
**Configuration Git pour Unity**
- `GIT_UNITY_FIX.md` - Résolution problème .gitignore Unity
- `README.md` - Vue d'ensemble de la session

**Réalisations :**
- ✅ Configuration `.gitignore` pour Unity
- ✅ Exclusion Library/, Temp/, PackageCache/
- ✅ Documentation bonnes pratiques Git + Unity

---

### 📂 docs/sessions/session_1_setup/
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

### 📂 docs/sessions/session_2_unity_installation/
**Installation et configuration de Unity**
- Documentation de l'installation Unity 2022.3 LTS
- Configuration du projet Unity avec URP (Universal Render Pipeline)

**Réalisations :**
- ✅ Installation Unity Hub
- ✅ Installation Unity 2022.3 LTS
- ✅ Création du projet Unity avec template URP
- ✅ Configuration initiale de la scène

---

### 📂 docs/sessions/session_3_univrm_installation/
**Installation du package UniVRM**
- Guide d'installation UniVRM pour le support VRM
- Configuration du package dans Unity

**Réalisations :**
- ✅ Installation UniVRM via .unitypackage
- ✅ Import du package dans le projet Unity
- ✅ Configuration des dépendances (UniGLTF, VRMShaders, etc.)

---

### 📂 docs/sessions/session_4_python_unity_connection/
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

### 📂 docs/sessions/session_5_vrm_loading/
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

### 📂 docs/sessions/session_6_expressions/
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

### 📂 docs/sessions/session_7_animations/
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

### 📂 docs/sessions/session_8_auto_blink/
**Clignement automatique des yeux** 👁️
- `README.md` - Vue d'ensemble complète de la session 8
- `BLINK_GUIDE.md` - Guide rapide d'implémentation
- `TECHNICAL_GUIDE.md` - Architecture détaillée avec SmoothStep
- `TROUBLESHOOTING.md` - Résolution complète de tous les problèmes

**Réalisations :**
- ✅ **Animation réaliste** : SmoothStep (courbes Hermite) en 160ms
- ✅ **Timings optimisés** : 50ms fermeture + 30ms pause + 80ms ouverture
- ✅ **Intervalles aléatoires** : 2-5 secondes entre clignements
- ✅ **Toggle on/off** : Checkbox dans interface Python
- ✅ **Sauvegarde config** : État persisté dans config.json
- ✅ **Manipulation directe** : Bypass Lerp pour contrôle précis du timing
- ✅ **Coroutines Unity** : BlinkLoop + PerformBlink pour animations non-bloquantes

**Innovations techniques :**
- Courbe SmoothStep (3t² - 2t³) pour mouvement naturel
- Manipulation directe VRMBlendShapeProxy (ImmediatelySetValue + Apply)
- Cohabitation pacifique avec système Lerp (expressions ≠ clignement)
- Mapping BlendShape critique : Blink/Blink_L/Blink_R dans switch statement
- Délai d'initialisation 2.5s pour attendre chargement Unity

**Problèmes résolus :**
1. Blendshapes non appliqués → Fix mapping GetBlendShapeKey()
2. Animation trop lente (2s) → Bypass Lerp + manipulation directe
3. Animation robotique → SmoothStep au lieu de linéaire

---

### 📂 docs/sessions/session_9_head_movements/
**Mouvements de Tête Automatiques + Réorganisation Interface** 🎭
- `README.md` - Vue d'ensemble complète de la session 9
- `INTERFACE_REORGANIZATION.md` - Guide réorganisation 3 onglets
- `HEAD_MOVEMENT_GUIDE.md` - Guide technique (SmoothStep, Coroutine, IPC)
- `DEBUG_ISSUES.md` - Problèmes résolus (VRMAutoBlinkController, déconnexion)
- `scripts/` - Tous les scripts finaux (Unity C# + Python)

**Réalisations :**
- ✅ **Mouvements naturels** : VRMHeadMovementController.cs avec Coroutines + SmoothStep
- ✅ **Paramètres configurables** : Fréquence (3-10s) et Amplitude (2-10°)
- ✅ **Animations fluides** : Yaw (-5° à +5°) et Pitch (-2.5° à +2.5°)
- ✅ **IPC fonctionnel** : Commande `set_auto_head_movement` avec 4 paramètres
- ✅ **Interface réorganisée** : 3 onglets logiques (Expressions, Animations, Options)
- ✅ **Boutons reset** : 3 boutons contextuels (reset_expressions, reset_animations, reset_options)
- ✅ **Code propre** : ~137 lignes dupliquées supprimées

**Nouvelle structure interface :**
- **Onglet "Expressions"** : 5 sliders expressions + reset
- **Onglet "Animations"** : Auto-blink (checkbox) + Head movements (checkbox + 2 sliders) + reset
- **Onglet "Options"** : Vitesse transition (slider) + reset

**Problèmes résolus :**
1. Conflit VRMAutoBlinkController → Désactiver dans Unity Inspector
2. État VRM après déconnexion → Reset vrm_loaded + texte bouton
3. Code dupliqué interface → Suppression ~137 lignes

**Innovations techniques :**
- Coroutine RandomHeadMovement() avec cycle complet (mouvement → hold → retour)
- Interpolation SmoothStep pour accélération/décélération naturelle
- Recherche head bone via Animator.GetBoneTransform(HumanBodyBones.Head)
- Durées aléatoires pour éviter prévisibilité (0.3-0.8s movement, 0.2-0.5s hold)
- Architecture 3 onglets modulaire et extensible

---

### 📂 docs/sessions/session_10_ai_chat/
**IA Conversationnelle Complète (Kira)** 🤖💬
- `README.md` - Vue d'ensemble Session 10 (14 phases)
- `PLAN_SESSION_10.md` - Plan détaillé complet
- `CHAT_ENGINE_GUIDE.md` - Guide utilisation ChatEngine
- `scripts/` - Scripts finaux (config.py, model_manager.py, chat_engine.py, tests)

**Réalisations (Phases 1-5) :**
- ✅ **Phase 1 : Architecture** (30 min)
  - Dossiers : src/ai/, src/discord_bot/, src/auth/, models/
  - Modèle LLM : Zephyr-7B (6.8 GB)
  - Configuration : .env, requirements.txt, 8 nouvelles dépendances
- ✅ **Phase 2 : Mémoire** (1h)
  - ConversationMemory (SQLite, 430 lignes)
  - 11 tests unitaires passent
- ✅ **Phase 3 : Configuration IA** (45 min)
  - AIConfig avec 3 profils GPU (performance/balanced/cpu_fallback)
  - data/config.json étendu
  - 31 tests unitaires passent
- ✅ **Phase 4 : Model Manager** (1.5h)
  - ModelManager avec détection GPU (RTX 4050 6GB détecté)
  - Chargement LLM avec auto-fallback CPU
  - 23 tests unitaires passent
- ✅ **Phase 5 : Chat Engine** (2h)
  - ChatEngine + EmotionDetector (6 émotions)
  - Format prompt ChatML (Zephyr)
  - Support multi-utilisateurs et multi-sources
  - 23 tests unitaires passent

**Tests globaux** : ✅ **97/97 passent (100%)** 🎉

**Système complet** :
- Charger modèle LLM (Zephyr-7B)
- Détecter GPU et adapter performances
- Sauvegarder conversations (SQLite)
- Détecter émotions (joy, angry, sorrow, surprised, fun, neutral)
- Générer réponses avec contexte historique
- Support multi-utilisateurs avec isolation

**Prochaines phases (Chat 8)** :
- Phase 6 : Emotion Analyzer avancé (intensité 0-100, mapping VRM)
- Phase 7 : Bot Discord (commandes !chat, !stats, !clear)
- Phase 8 : GUI Chat Desktop (interface PySide6)
- Phase 9 : GUI Discord Control (contrôle bot depuis GUI)

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
- **Session 8 terminée** : Clignement automatique des yeux (SmoothStep, 160ms)
- **Session 9 terminée** : Mouvements de tête + Réorganisation interface (3 onglets)
- **Fonctionnalités** :
  - Transitions smooth entre expressions (Lerp interpolation)
  - Contrôle de vitesse en temps réel (1.0-10.0)
  - Système de modèle VRM par défaut
  - Chargement/Déchargement dynamique
  - Interface française complète avec icône
  - **Clignement automatique naturel** (intervalles 2-5s, animation fluide)
  - **Mouvements de tête naturels** (fréquence 3-10s, amplitude 2-10°, SmoothStep)
  - **Interface 3 onglets** (Expressions, Animations, Options)
  - **3 boutons reset contextuels**
  
### ✅ Phase 3 - IA Conversationnelle (Chat 6-7) - EN COURS
- **Session 10 (Phases 1-5)** : Système IA Complet ✅
  - ✅ **Architecture IA** (src/ai/, models/, dépendances LLM)
  - ✅ **Mémoire conversationnelle** (SQLite, 11 tests)
  - ✅ **Configuration IA** (GPU profiles, 31 tests)
  - ✅ **Model Manager** (GPU detection RTX 4050, 23 tests)
  - ✅ **Chat Engine** (EmotionDetector, 23 tests)
  - ✅ **97/97 tests passent (100%)**
  - Kira peut parler avec LLM Zephyr-7B !
- **Chat 8 (Phases 6-9)** : ✅ **TERMINÉ**
  - ✅ **Phase 6** : Emotion Analyzer avancé (intensité, confiance, contexte, mapping VRM)
  - ✅ **Phase 7** : Bot Discord (auto-reply, rate limiting, intégration Unity)
  - ✅ **Phase 8** : GUI Chat Desktop (chargement manuel IA, émotions temps réel)
  - ✅ **Phase 9** : Fix Chargement GPU (CUDA) - **6-7x plus rapide !**
  - ✅ **158/158 tests passent (100%)**
  - 🎮 **GPU CUDA actif** : RTX 4050, 35 layers, 33 tok/s
  - Kira discute sur Discord ET Desktop avec accélération GPU !
- **Prochaine (Chat 9 - Phase 10)** :
  - GUI Discord Control (interface contrôle bot Discord)
  - Tests intégration Phase 10
  - Documentation Phase 10

### 🔜 Phase 4 - À venir (Chat 9-10)
- **Session 10 (Phases 10-14)** : Finition IA
  - Phase 10 : GUI Discord Control
  - Phase 11 : Tests Intégration
  - Phase 12 : Optimisations
  - Phase 13 : Documentation Finale
  - Phase 14 : Polish & Release
- **Session 11** : Audio & Lip-sync 🎤
  - Capture audio microphone
  - Analyse amplitude/fréquence
  - Lip-sync VRM (blendshapes bouche : A, I, U, E, O)
- **Session 12** : Interactions Souris 🖱️
  - Avatar suit le curseur
  - Réaction aux clics
  - Drag & drop sur desktop

---

## 📖 Comment utiliser cette documentation

1. **Nouveau sur le projet :** 
   - Commence par `START_HERE.md`
   - Lis `chat_transitions/chat_1.../CHAT_SUMMARY.md`
   
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

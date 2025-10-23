# Desktop-Mate

🎭 **Interactive VRM Desktop Companion** - Une application hybride Unity + Python qui donne vie à votre avatar VRM sur votre bureau !

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Unity 2022.3+](https://img.shields.io/badge/unity-2022.3+-black.svg)](https://unity.com/)
[![Status](https://img.shields.io/badge/status-MVP%20Complete-success.svg)](https://github.com/Xyon15/desktop-mate)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Description

Desktop-Mate est une application qui permet d'afficher un avatar VRM interactif sur votre bureau Windows. L'avatar peut :
- 🎤 Synchroniser ses lèvres avec votre microphone (lip-sync)
- 😊 Afficher des expressions et émotions
- 👁️ Suivre votre visage via webcam
- 🎮 Réagir à des commandes et interactions

**Objectif final :** 🤖 Connecter l'avatar à une **IA conversationnelle (chatbot)** pour créer un assistant virtuel qui peut **parler, réagir émotionnellement et se déplacer librement** sur le bureau. L'avatar deviendra un véritable compagnon interactif intelligent !

**Status actuel :** ✅ Phases 1-2-3 terminées ! L'avatar s'affiche, exprime des émotions avec **transitions fluides**, **cligne des yeux naturellement** avec animation SmoothStep et **bouge la tête de manière vivante** ! Interface réorganisée en 3 onglets logiques. ✨👁️🎭

## ⚡ Quick Start

```powershell
# 1. Cloner le repo
git clone https://github.com/Xyon15/desktop-mate.git
cd desktop-mate

# 2. Setup Python
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. Lancer Unity (ouvrir unity/DesktopMateUnity/ et cliquer Play)

# 4. Lancer Python
python main.py
# → Cliquer "Connect to Unity" puis "Load VRM Model"
```

📖 **[Documentation complète](docs/START_HERE.md)**

## 🏗️ Architecture

Le projet utilise une **architecture hybride** pour combiner les forces de Unity et Python :

### Unity (Rendu 3D)
- Chargement et rendu des modèles VRM
- Gestion des animations et blendshapes
- Physique et effets visuels avancés

### Python (Logique & UI)
- Interface de contrôle (PySide6/Qt)
- Capture audio et traitement
- Communication IPC avec Unity
- Gestion de configuration

```
┌─────────────────┐         ┌──────────────────┐
│   Python App    │◄───────►│   Unity Engine   │
│  (PySide6 GUI)  │  Socket │  (VRM Renderer)  │
│  • Audio Input  │   IPC   │  • 3D Display    │
│  • Controls     │         │  • Animations    │
└─────────────────┘         └──────────────────┘
```

## 📁 Structure du Projet

```
desktop-mate/
├── main.py                 # Point d'entrée de l'application Python
├── requirements.txt        # Dépendances Python
├── README.md              # Ce fichier
├── LICENSE                # Licence MIT
│
├── src/                   # Code source Python
│   ├── gui/              # Interface utilisateur Qt
│   │   └── app.py        # Application principale avec MainWindow
│   ├── ipc/              # Communication Unity ↔ Python
│   │   └── unity_bridge.py  # Client socket TCP
│   ├── audio/            # Capture et traitement audio (à venir)
│   ├── avatar/           # Gestion avatar et VRM (à venir)
│   └── utils/            # Utilitaires
│       ├── config.py     # Gestion configuration JSON
│       └── logger.py     # Système de logs
│
├── unity/                 # Projet Unity
│   ├── PythonBridge.cs   # Template script IPC
│   └── DesktopMateUnity/ # Projet Unity 2022.3 LTS (URP)
│       └── Assets/
│           ├── Scripts/
│           │   ├── IPC/PythonBridge.cs  # Serveur socket
│           │   └── VRMLoader.cs         # Chargeur VRM
│           ├── Models/
│           │   └── Mura Mura - Model.vrm
│           ├── VRM/              # Package UniVRM
│           ├── UniGLTF/          # Dépendance UniVRM
│           └── VRMShaders/       # Shaders VRM
│
├── assets/               # Assets partagés
│   └── Mura Mura - Model.vrm
│
├── tests/                # Tests unitaires (8 tests)
├── docs/                 # Documentation détaillée
│   ├── START_HERE.md    # 👈 Commence ici !
│   ├── INDEX.md         # Navigation rapide
│   ├── README.md        # Vue d'ensemble
│   ├── docs/sessions/session_0_git_configuration/ # ⚙️ Configuration Git Unity
│   ├── docs/sessions/session_1_setup/ # Setup Python + GUI
│   ├── docs/sessions/session_2_unity_installation/
│   ├── docs/sessions/session_3_univrm_installation/
│   ├── docs/sessions/session_4_python_unity_connection/
│   └── docs/sessions/session_5_vrm_loading/  # ✅ Dernière session complète
│
└── .github/              # CI/CD et workflows
    ├── workflows/
    └── instructions/
        └── copilot-instructions.instructions.md  # Instructions IA (inclut système anti-oubli doc)
```

**📋 Système de Documentation Anti-Oubli :**
- `docs/DOCUMENTATION_CHECKLIST.md` - Checklist systématique pour l'IA
- `docs/AI_DOCUMENTATION_PROMPT.md` - Prompt système pour maintenir la doc à jour
- `docs/.github/PULL_REQUEST_TEMPLATE.md` - Template PR avec vérifications doc obligatoires
- `.github/instructions/copilot-instructions.instructions.md` - Instructions Copilot (applyTo: `**`)

**Système 3 niveaux garantissant la synchronisation documentation ↔ code.**

## 🚀 Installation

### Prérequis

- **Python 3.10+** ✅ (Installé : 3.10.9)
- **Unity 2022.3 LTS** ou plus récent
- **Windows 10/11** (support Linux prévu plus tard)

### Étape 1 : Cloner le repository

```powershell
git clone https://github.com/Xyon15/desktop-mate.git
cd desktop-mate
```

### Étape 2 : Créer l'environnement virtuel Python

```powershell
# Créer le venv
python -m venv venv

# Activer le venv
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

### Étape 3 : Configurer Unity

1. Ouvrir **Unity Hub**
2. Installer **Unity 2022.3 LTS**
3. Ouvrir le projet existant dans `unity/DesktopMateUnity/`
4. **UniVRM est déjà installé** ✅
5. **PythonBridge.cs est déjà configuré** ✅
6. **VRMLoader.cs est déjà créé** ✅

> 💡 **Le projet Unity est déjà prêt !** Pas besoin de configuration supplémentaire.

### Étape 4 : Lancer l'application

**Terminal 1 - Unity :**
1. Ouvrir le projet Unity dans `unity/DesktopMateUnity/`
2. Cliquer sur **Play** ▶️
3. Vérifier que la console affiche : `[PythonBridge] Serveur démarré avec succès`

**Terminal 2 - Python :**
```powershell
# Activer le venv
.\venv\Scripts\Activate.ps1

# Lancer l'application Python
python main.py
```

**Dans l'interface Python :**
1. Cliquer sur **"Connect to Unity"**
2. Attendre le message de succès
3. Cliquer sur **"Load VRM Model"**
4. Sélectionner `assets/Mura Mura - Model.vrm`
5. **Ton avatar apparaît dans Unity !** 🎭✨

## 🎯 Roadmap

### Phase 1 : MVP ✅ **TERMINÉE !**
- [x] Structure du projet Python
- [x] Interface Qt de base
- [x] Communication IPC Unity ↔ Python (socket TCP)
- [x] Installation Unity 2022.3 LTS
- [x] Installation UniVRM
- [x] Script PythonBridge.cs (serveur socket Unity)
- [x] Chargement d'un modèle VRM dans Unity
- [x] **Affichage de l'avatar 3D fonctionnel !** 🎭

### Phase 2 : Expressions & Animations 😊 ✅ **TERMINÉE !**
- [x] **Session 6** : Expressions faciales (blendshapes) ✅
  - VRMBlendshapeController.cs v1.6 avec thread-safety
  - Interface GUI avec sliders (joy, angry, sorrow, surprised, fun)
  - Contrôle précis 0-100% pour chaque expression
  - Bouton "Reset All Expressions"
  - Documentation complète
- [x] **Session 7** : Animations fluides ✅
  - VRMBlendshapeController.cs v2.0 avec Lerp interpolation
  - Transitions smooth entre expressions
  - Slider de vitesse ajustable (1.0-10.0)
  - Interface française complète avec icône
  - Système de modèle VRM par défaut
  - Chargement/déchargement dynamique
  - Documentation complète (900+ lignes de guides techniques)
- [x] **Session 8** : Clignement automatique ✅
  - VRMAutoBlinkController.cs avec coroutines Unity
  - Animation SmoothStep (courbes de Hermite)
  - Timing naturel (2-5s entre clignements, 160ms par cycle)
  - Checkbox "Auto Blink" dans l'interface
  - Sauvegarde configuration
  - Documentation technique massive (TECHNICAL_GUIDE.md 900+ lignes)
  - Guide résolution problèmes (TROUBLESHOOTING.md avec 5 bugs résolus)
- [x] **Session 9** : Mouvements de Tête + Réorganisation Interface ✅ **TERMINÉE !**
  - VRMHeadMovementController.cs avec Coroutines + SmoothStep
  - Mouvements naturels aléatoires (yaw/pitch)
  - Contrôle fréquence (3-10s) et amplitude (2-10°)
  - Interface réorganisée en 3 onglets (Expressions, Animations, Options)
  - 3 boutons reset contextuels
  - Résolution conflit VRMAutoBlinkController
  - Gestion déconnexion Unity (reset état VRM)
  - Documentation complète (4 guides techniques + scripts)

### Phase 3 : Audio & Lip-Sync 🎤
- [ ] **Session 10** : Capture audio et lip-sync
  - Capture audio microphone
  - Détection d'amplitude vocale
  - Lip-sync basique avec phonèmes (A, I, U, E, O)
  - VU-meter dans l'UI
  - TTS (Text-to-Speech)

### Phase 4 : Intégration IA Conversationnelle 🤖 (Objectif Final)
- [ ] **Session 10** : Connexion chatbot IA
  - Intégration LLM (GPT, Claude, LLaMA local, etc.)
  - Reconnaissance vocale (speech-to-text)
  - Synthèse vocale IA (text-to-speech)
  - Synchronisation lip-sync avec voix IA
- [ ] **Session 11** : Émotions intelligentes
  - Analyse sentiment des réponses IA
  - Mapping émotions → expressions faciales
  - Réactions contextuelles dynamiques
- [ ] **Session 12** : Mouvement libre sur bureau
  - Fenêtre Unity sans bordures (transparent)
  - Déplacement autonome intelligent
  - Animations marche/vol
  - Interactions avec fenêtres
  - Comportements autonomes (l'avatar décide où aller)

### Phase 5 : Tracking & Avancé 👁️
- [ ] Face tracking via webcam (MediaPipe)
- [ ] Eye tracking basique
- [ ] Suivi du regard utilisateur
- [ ] Système de plugins

### Phase 6 : Polish & Release 🚀
- [ ] Packaging .exe
- [ ] Installeur Windows
- [ ] Documentation complète
- [ ] Tutoriels vidéo
- [ ] Support multi-plateformes (Linux, macOS)

## 🛠️ Technologies Utilisées

### Python Stack
- **PySide6** : Interface graphique Qt
- **sounddevice** : Capture audio
- **numpy** : Traitement numérique
- **opencv-python** : Traitement d'image et webcam (optionnel)
- **pytest** : Tests unitaires

### Unity Stack
- **Unity 2022.3 LTS** : Moteur de rendu
- **UniVRM** : Support modèles VRM
- **URP** : Universal Render Pipeline

### Communication
- **Sockets TCP** : IPC Python ↔ Unity (port 5555)
- **Format JSON** : Messages structurés
- **Threading** : Queue + Update() pour thread-safety Unity
- *(Futur : OSC ou gRPC pour plus de fonctionnalités)*

## 🎭 Fonctionnalités Actuelles

### ✅ Opérationnel
- **Interface Python Qt** : Fenêtre de contrôle avec onglets, 100% en français, icône personnalisée
- **Connexion Unity** : Communication bidirectionnelle stable avec thread-safety
- **Chargement VRM** : Import, affichage et déchargement dynamique de modèles VRM
- **Modèle par défaut** : Système de modèle VRM par défaut (pas besoin de naviguer à chaque fois) ✨ **SESSION 7**
- **Avatar 3D** : Modèle "Mura Mura" affiché dans Unity avec rendu optimisé
- **Expressions faciales** : Contrôle blendshapes VRM (joy, angry, sorrow, surprised, fun)
- **Transitions smooth** : Interpolation Lerp pour animations fluides ✨ **SESSION 7**
- **Vitesse ajustable** : Slider 1.0-10.0 pour contrôler la rapidité des transitions ✨ **SESSION 7**
- **Clignement automatique** : Yeux qui clignent naturellement (2-5s) avec animation SmoothStep (160ms) ✨ **SESSION 8**
- **Checkbox Auto Blink** : Activation/désactivation du clignement dans l'interface ✨ **SESSION 8**
- **Interface sliders** : Contrôle précis 0-100% pour chaque expression
- **Logs détaillés** : Console + fichiers pour debugging
- **Tests unitaires** : 8 tests Python qui passent (100%)

### 🚧 En développement
- Lip-sync audio (analyse FFT + phonèmes)
- Mouvements de tête subtils (head bobbing)
- Eye tracking (suivi curseur)

## 🔧 Architecture Technique

### Communication IPC

```
┌─────────────────────────────┐
│      Python (Client)        │
│                             │
│  ┌───────────────────────┐  │
│  │   MainWindow (Qt)     │  │
│  │  - Connect button     │  │
│  │  - Load VRM button    │  │
│  └───────────┬───────────┘  │
│              │              │
│  ┌───────────▼───────────┐  │
│  │   UnityBridge         │  │
│  │  - send_command()     │  │
│  │  - Socket client      │  │
│  └───────────┬───────────┘  │
└──────────────┼──────────────┘
               │
          JSON/TCP
       127.0.0.1:5555
               │
┌──────────────▼──────────────┐
│     Unity (Serveur)         │
│                             │
│  ┌───────────────────────┐  │
│  │   PythonBridge.cs     │  │
│  │  - TcpListener        │  │
│  │  - HandleMessage()    │  │
│  └───────────┬───────────┘  │
│              │              │
│  ┌───────────▼───────────┐  │
│  │   VRMLoader.cs        │  │
│  │  - LoadVRMModel()     │  │
│  │  - Queue<Action>      │  │
│  │  - Update() thread    │  │
│  └───────────┬───────────┘  │
│              │              │
│  ┌───────────▼───────────┐  │
│  │   Scene Unity         │  │
│  │   🎭 Avatar VRM       │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

### Thread Safety

Unity nécessite l'exécution sur le **main thread** pour les opérations GameObject. VRMLoader utilise un pattern **Queue + Update()** :

```csharp
// Appelé depuis le thread réseau
public void LoadVRMFromPath(string path) {
    lock (mainThreadActions) {
        mainThreadActions.Enqueue(() => LoadVRMModel());
    }
}

// Exécuté sur le main thread Unity
void Update() {
    lock (mainThreadActions) {
        while (mainThreadActions.Count > 0) {
            mainThreadActions.Dequeue()?.Invoke();
        }
    }
}
```

## 📖 Documentation

Documentation complète et organisée par sessions de développement :

- 📄 **[START_HERE.md](docs/START_HERE.md)** - Point d'entrée de la documentation
- 📑 **[INDEX.md](docs/INDEX.md)** - Navigation rapide et recherche
- 📚 **[docs/README.md](docs/README.md)** - Vue d'ensemble complète

### Sessions documentées

0. **[Session 0 - Configuration Git Unity](docs/sessions/session_0_git_configuration/)** ⚙️
   - Configuration `.gitignore` pour Unity
   - Exclusion des fichiers générés (Library/, Temp/)
   - Bonnes pratiques Git pour projets Unity

1. **[Session 1 - Setup Python + GUI](docs/sessions/session_1_setup/)** ✅
   - Configuration environnement Python
   - Interface Qt avec PySide6
   - Système de configuration et logs

2. **[Session 2 - Installation Unity](docs/sessions/session_2_unity_installation/)** ✅
   - Installation Unity 2022.3 LTS
   - Création projet URP
   - Configuration de base

3. **[Session 3 - Installation UniVRM](docs/sessions/session_3_univrm_installation/)** ✅
   - Installation du package UniVRM
   - Support des modèles VRM
   - Configuration des shaders

4. **[Session 4 - Connexion Python ↔ Unity](docs/sessions/session_4_python_unity_connection/)** ✅
   - Communication IPC via socket TCP
   - PythonBridge.cs (serveur Unity)
   - unity_bridge.py (client Python)
   - Résolution des problèmes de connexion

5. **[Session 5 - Chargement VRM](docs/sessions/session_5_vrm_loading/)** ✅
   - VRMLoader.cs avec thread-safety
   - Chargement dynamique des modèles VRM
   - Affichage de l'avatar 3D
   - **Application fonctionnelle !** 🎉

6. **[Session 6 - Expressions Faciales](docs/sessions/session_6_expressions/)** ✅
   - VRMBlendshapeController.cs v1.6 pour expressions
   - Interface GUI avec sliders
   - Contrôle émotions en temps réel
   - **L'avatar exprime des émotions !** 😊😠😢😲😄

7. **[Session 7 - Animations Fluides](docs/sessions/session_7_animations/)** ✅
   - VRMBlendshapeController.cs v2.0 avec Lerp interpolation
   - Transitions smooth entre expressions
   - Slider de vitesse (1.0-10.0)
   - Interface française + icône
   - Système modèle VRM par défaut
   - Thread-safety complet (Queue<Action> pattern)
   - **L'avatar anime ses expressions de façon fluide !** ✨🎭

8. **[Session 8 - Clignement Automatique](docs/sessions/session_8_auto_blink/)** ✅
   - VRMAutoBlinkController.cs avec coroutines Unity
   - Animation SmoothStep (courbes de Hermite) pour réalisme
   - Timing paramétrable (2-5s entre clignements, 160ms par cycle)
   - Checkbox "Auto Blink" dans l'interface Python
   - Sauvegarde de configuration
   - Documentation technique complète (TECHNICAL_GUIDE.md 900+ lignes)
   - Résolution de 5 problèmes majeurs documentés (TROUBLESHOOTING.md)
   - **L'avatar cligne naturellement des yeux !** 👁️✨

9. **[Session 9 - Mouvements de Tête + Réorganisation Interface](docs/sessions/session_9_head_movements/)** ✅
   - VRMHeadMovementController.cs avec Coroutines + SmoothStep
   - Mouvements naturels aléatoires (yaw/pitch)
   - Contrôle fréquence (3-10s) et amplitude (2-10°)
   - Interface réorganisée en 3 onglets (Expressions, Animations, Options)
   - 3 boutons reset contextuels pour chaque onglet
   - Résolution conflit VRMAutoBlinkController
   - Gestion propre de la déconnexion Unity (reset état VRM)
   - Documentation complète (4 guides techniques + scripts archivés)
   - **L'avatar bouge naturellement la tête + interface moderne !** 🎭✨

10. **[Session 10 - IA Conversationnelle (Kira)](docs/sessions/session_10_ai_chat/)** ✅ **EN COURS - Chat 8 (Phase 6) TERMINÉ**
   - **Phase 1** : Architecture de Base (30 min) ✅
     - Dossiers : src/ai/, src/discord_bot/, src/auth/, models/
     - Modèle LLM copié (Zephyr-7B, 6.8 GB)
     - Configuration : .env, requirements.txt, .gitignore
   - **Phase 2** : Base de Données & Mémoire (1h) ✅
     - src/ai/memory.py (430 lignes)
     - SQLite chat_history avec 4 indexes
     - Tests : 11/11 passés
     - Singleton pattern + Context manager thread-safe
   - **Phase 3** : Configuration IA (45 min) ✅
     - src/ai/config.py (420 lignes) avec GPU_PROFILES
     - 3 profils GPU (performance/balanced/cpu_fallback)
     - data/config.json configuration complète
     - Tests : 31/31 passés
   - **Phase 4** : Model Manager (1.5h) ✅
     - src/ai/model_manager.py (470 lignes)
     - Détection GPU NVIDIA (RTX 4050 6GB détecté)
     - Chargement LLM avec auto-fallback CPU
     - Tests : 23/23 passés
   - **Phase 5** : Chat Engine (2h) ✅
     - src/ai/chat_engine.py (480 lignes)
     - EmotionDetector avec 6 émotions (joy/angry/sorrow/surprised/fun/neutral)
     - Format prompt ChatML (Zephyr)
     - Support multi-utilisateurs et multi-sources
     - Tests : 23/23 passés
   - **Phase 6** : Emotion Analyzer (1h) ✅
     - src/ai/emotion_analyzer.py (680 lignes)
     - Analyse émotionnelle avancée avec intensité 0-100 et confiance
     - Historique émotionnel par utilisateur avec lissage transitions
     - Mapping complet vers Blendshapes VRM (6 émotions)
     - Tests : 39/39 passés
   - **Phase 7** : Discord Bot (1.5h) ✅
     - src/discord_bot/bot.py (417 lignes) - Bot Discord Kira
     - Auto-reply configurable + rate limiting
     - Intégration ChatEngine + émotions Unity
     - Tests : 21/21 passés
   - **Phase 8** : GUI Chat Desktop (1.5h + chargement manuel) ✅
     - Nouvel onglet "💬 Chat" avec interface complète
     - Chargement manuel IA (bouton + économie VRAM)
     - Indicateurs émotions + statistiques temps réel
     - Tests : 158/158 passés (100%)
   - **Phase 9** : Fix Chargement GPU (45 min) ✅
     - **Problème résolu** : Modèle chargeait sur RAM CPU au lieu de VRAM GPU
     - Recompilation llama-cpp-python avec CMAKE_ARGS="-DGGML_CUDA=on"
     - Durée compilation : 18min 40s (CUDA Toolkit 12.9 + Visual Studio 2022)
     - **Performance** : 6-7x plus rapide (33 tok/s vs 5 tok/s)
     - GPU détecté : RTX 4050 Laptop (6GB), 35 layers, ~3-4 GB VRAM
     - Documentation : README.md + CUDA_INSTALLATION_GUIDE.md complets
   - **Tests globaux** : 158/158 passés (100%) ✅
   - **Prochaine (Chat 9)** : Phase 10 (GUI Discord Control)
   - **L'avatar peut maintenant parler intelligemment avec émotions avancées ET accélération GPU 6-7x !** 🤖💬🎭🎮✨

### Guides spécifiques

- [Configuration Git Unity](docs/sessions/session_0_git_configuration/GIT_UNITY_FIX.md)
- [Architecture technique](docs/sessions/session_1_setup/architecture.md)
- [Debug connexion Unity](docs/sessions/session_4_python_unity_connection/DEBUG_CONNECTION.md)
- [Fix script Unity](docs/sessions/session_4_python_unity_connection/FIX_SCRIPT_NOT_RUNNING.md)
- [Récapitulatif Session 5](docs/sessions/session_5_vrm_loading/SESSION_VRM_LOADING_SUCCESS.md)
- [Guide expressions Session 6](docs/sessions/session_6_expressions/BLENDSHAPES_GUIDE.md)
- [Guide transitions Session 7](docs/sessions/session_7_animations/TRANSITIONS_GUIDE.md) ✨ **900+ lignes !**
- [Guide technique Session 8](docs/sessions/session_8_auto_blink/TECHNICAL_GUIDE.md) ✨ **Architecture SmoothStep détaillée !**
- [Résolution problèmes Session 8](docs/sessions/session_8_auto_blink/TROUBLESHOOTING.md) ✨ **5 problèmes résolus !**
- [Réorganisation interface Session 9](docs/sessions/session_9_head_movements/INTERFACE_REORGANIZATION.md) ✨ **Nouvelle architecture 3 onglets !**
- [Guide mouvements tête Session 9](docs/sessions/session_9_head_movements/HEAD_MOVEMENT_GUIDE.md) ✨ **Animations naturelles !**
- [Guide Chat Engine Session 10](docs/sessions/session_10_ai_chat/CHAT_ENGINE_GUIDE.md) ✨ **Utilisation ChatEngine IA !**
- [Résolution problèmes Session 9](docs/sessions/session_9_head_movements/DEBUG_ISSUES.md) ✨ **3 bugs critiques résolus !**
- [Plan Session 10](docs/sessions/session_10_ai_chat/PLAN_SESSION_10.md) ✨ **14 phases IA conversationnelle détaillées !**
- [Contexte Chat 7](docs/chat_transitions/chat_6_session_10_phases_1_2/CONTEXT_FOR_NEXT_CHAT.md) ✨ **Instructions complètes Phase 3-5 !**
- [Guide installation CUDA Session 10 Phase 9](docs/sessions/session_10_ai_chat/phase_9_cuda_fix/CUDA_INSTALLATION_GUIDE.md) ✨ **Compilation CUDA Windows complète !**

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment participer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'feat: add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Conventions de Commit

Nous utilisons [Conventional Commits](https://www.conventionalcommits.org/) :

- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `style:` Formatage, typos
- `refactor:` Refactoring
- `test:` Ajout de tests
- `chore:` Maintenance

## 💾 Screenshots

### Interface Python
Interface de contrôle avec connexion Unity et bouton de chargement VRM.

### Console Unity
```
[PythonBridge] Serveur démarré avec succès sur 127.0.0.1:5555
[PythonBridge] 🔗 Client Python connecté !
[PythonBridge] 📨 Reçu : {"command": "load_model", "data": {"path": "..."}}
[VRMLoader] 📋 Demande de chargement reçue
[VRMLoader] 🎭 Exécution du chargement sur le thread principal
[VRMLoader] ✅ Modèle chargé avec succès : Mura Mura - Model(Clone)
[VRMLoader] 📍 Position : (0.0, 0.0, 0.0)
```

### Avatar dans Unity
Avatar VRM "Mura Mura" affiché dans la fenêtre Game de Unity 🎭

## 🎓 Leçons Apprises

### Threading Unity
Unity nécessite que toutes les opérations GameObject soient sur le main thread. Solution : Pattern Queue + Update().

### API UniVRM
L'API UniVRM varie selon les versions. Pour le MVP, approche simplifiée avec prefab pré-importé.

### IPC Robuste
Socket TCP + JSON fonctionne bien pour la communication bidirectionnelle Python ↔ Unity.

### Documentation
Organisation par sessions chronologiques facilite la compréhension et la maintenance du projet.

## 🎯 Vision du Projet

Ce projet a pour **objectif final** de créer un **assistant virtuel IA complet** :
- 🤖 **Conversation intelligente** : L'avatar pourra discuter naturellement grâce à un LLM (chatbot IA)
- 😊 **Émotions réactives** : Analyse du sentiment et expressions faciales adaptées
- 🚶 **Mobilité libre** : Déplacement autonome sur le bureau, interactions avec l'environnement
- 🎤 **Voix naturelle** : Reconnaissance vocale + synthèse vocale synchronisée
- 🧠 **Comportements intelligents** : Décisions autonomes basées sur le contexte

**L'avatar deviendra un véritable compagnon numérique interactif et intelligent !**

## 👤 Auteur

**Xyon15**
- GitHub: [@Xyon15](https://github.com/Xyon15)

## 🙏 Remerciements

- [UniVRM](https://github.com/vrm-c/UniVRM) pour le support VRM
- [AcidicDoll](https://acidicdollz.booth.pm/) pour le modèle VRM "Mura Mura"
- La communauté VRM pour les ressources et tutoriels

## 📞 Support

Si vous rencontrez des problèmes ou avez des questions :
- 📖 Consultez la [documentation complète](docs/START_HERE.md)
- 🐛 Ouvrez une [issue](https://github.com/Xyon15/desktop-mate/issues)
- 💬 Regardez les fichiers DEBUG_ et FIX_ dans docs/

## 📝 Changelog

### Version 0.9.0-alpha (23 octobre 2025) ✨ **NOUVEAU - SESSION 10 (Chat 8 - Phases 6-9) TERMINÉE**
- ✅ **Chat 8 - Session 10 (Phases 6-9) terminée !**
- ✅ **Phase 6 : Emotion Analyzer (1h)**
  - src/ai/emotion_analyzer.py (680 lignes) avec analyse émotionnelle avancée
  - Analyse intensité (0-100) + confiance (0.0-1.0)
  - Historique émotionnel par utilisateur avec lissage transitions
  - Mapping complet vers Blendshapes VRM (6 émotions)
  - Tests : 39/39 passés
- ✅ **Phase 7 : Discord Bot (1.5h)**
  - src/discord_bot/bot.py (417 lignes) - Bot Discord complet pour Kira
  - Classe KiraDiscordBot avec intégration ChatEngine complète
  - **Fonctionnalités Discord** :
    * Auto-reply configurable par salon (whitelist)
    * Réponse aux mentions utilisateur
    * Rate limiting (délai minimum entre messages)
    * Nettoyage prompts (suppression mentions/URLs)
    * Détection émotions + envoi Unity VRM si connecté
  - **Architecture asynchrone** :
    * Support discord.py async/await
    * Handlers on_ready() + on_message()
    * Gestion erreurs robuste
  - **Statistiques détaillées** :
    * Messages reçus/traités/ignorés
    * Réponses générées
    * Émotions envoyées Unity
    * Tracking salons + mentions
  - Singleton pattern : get_discord_bot()
  - tests/test_discord_bot.py - 21 tests unitaires (pytest-asyncio)
  - ✅ **Tous les tests passent (21/21) !**
- ✅ **Phase 8 : GUI Chat Desktop (1.5h + amélioration chargement manuel)**
  - src/gui/app.py - Nouvel onglet "💬 Chat" intégré
  - **Interface chat complète** :
    * QTextEdit pour messages (HTML avec couleurs Material Design)
    * QLineEdit pour saisie utilisateur
    * Bouton envoi + support Enter
    * Indicateur émotion en temps réel (emoji + nom + intensité)
    * Statistiques messages/émotions en footer
    * Historique effaçable avec confirmation
  - **Thread-safety Qt** :
    * Signaux personnalisés (message_received, emotion_updated, stats_updated)
    * Threading pour traitement chat (évite freeze UI)
    * QTimer.singleShot() pour ré-activation boutons
  - **Thème dark harmonisé** :
    * Fond #2b2b2b, texte #e0e0e0
    * Messages : Vous=#64B5F6, Kira=#CE93D8, Système=#EF5350
    * Timestamps gris #888
    * Indicateur émotion : fond #3a3a3a, bordure #555
  - **🚀 Chargement manuel IA (amélioration majeure)** :
    * Suppression chargement automatique (économie 4-6 GB VRAM)
    * Nouvel onglet "🤖 Modèle IA (LLM)" dans Connexion tab
    * Bouton "📥 Charger IA (Zephyr-7B)" pour chargement manuel
    * Bouton "🗑️ Décharger IA" pour libérer mémoire
    * Labels statut dynamiques (Non chargé / ⏳ / ✅ / ❌)
    * Info utilisateur : "Chargement : ~15-30 secondes | Mémoire : ~4-6 GB VRAM"
    * Chat input désactivé par défaut avec placeholder explicite
    * Gestion ImportError avec QMessageBox si llama-cpp-python manquant
    * Messages système dans chat pour confirmer opérations
  - **Méthodes nouvelles** :
    * load_ai_model() - Chargement ChatEngine + EmotionAnalyzer on-demand
    * unload_ai_model() - Libération mémoire complète
    * Mise à jour UI automatique (statuts, boutons, inputs)
  - **Intégration VRM Unity** :
    * Vérification connexion + VRM chargé
    * get_vrm_blendshape() pour mapping optimal
    * set_expression() automatique lors des réponses
  - ✅ **Gestion erreurs robuste** : ImportError, ConnectionError, génération échec
  - ✅ **Bug fixes** : timing signal emotion_updated, ImportError handling, dark theme
- ✅ **Tests globaux : 158/158 passés (100%) en 14.85s** 🎉
  - +21 tests Discord bot
  - Tests précédents intacts (config, model, chat, emotion, memory, etc.)
- ✅ **Documentation complète Phases 7-8**
  - README.md Session 10 mis à jour avec Phases 7-8 détaillées
  - Section chargement manuel IA (80+ lignes)
  - Tableau états système (4 états : Démarrage/Chargement/Chargé/Erreur)
  - Scripts copiés : bot.py, test_discord_bot.py, app.py
  - docs/INDEX.md mis à jour
  - README.md racine mis à jour (4 sections : Sessions, Guides, Changelog, Status)
- ✅ **Phase 9 : Fix Chargement GPU (CUDA) - 45 minutes**
  - ❌ **Problème** : Modèle chargeait sur RAM CPU au lieu de VRAM GPU malgré config correcte
  - 🔍 **Diagnostic** : llama-cpp-python v0.3.16 installé SANS support CUDA (wheel précompilé CPU-only)
  - ✅ **Solution** : Recompilation depuis sources avec CMAKE_ARGS="-DGGML_CUDA=on"
  - **Compilation réussie** :
    * Durée : 18min 40s
    * CUDA Toolkit v12.9.86
    * Visual Studio 2022 (MSVC 19.44.35217.0)
    * 1349 warnings (normaux), 0 erreurs
    * DLL CUDA générées : ggml-cuda.lib/dll ✅
  - **Tests de vérification** :
    * llama_supports_gpu_offload() → True ✅
    * GPU détecté : NVIDIA GeForce RTX 4050 Laptop GPU (6GB VRAM)
    * Modèle charge 35 layers GPU (balanced profile)
    * VRAM utilisée : ~3-4 GB pendant inférence
  - **Performance** :
    * Avant (CPU) : ~20s pour 100 tokens (~5 tok/s)
    * Après (GPU) : ~3s pour 100 tokens (~33 tok/s)
    * **Amélioration : 6-7x plus rapide !** ⚡
  - **Documentation complète** :
    * docs/sessions/session_10_ai_chat/phase_9_cuda_fix/README.md
    * docs/sessions/session_10_ai_chat/phase_9_cuda_fix/CUDA_INSTALLATION_GUIDE.md
    * Guide installation CUDA complet (Windows, prérequis, dépannage)
    * Scripts diagnostics (test_cuda_support.py, monitor_vram.py)
- 🎮 **Kira utilise maintenant la VRAM GPU (RTX 4050) pour générer les réponses 6-7x plus vite !** ✨🚀
- 🎭 **Kira peut maintenant discuter sur Discord ET dans le Desktop-Mate GUI avec contrôle utilisateur complet et accélération GPU !** ✨👁️🤖🎮✨

### Version 0.8.0-alpha (23 octobre 2025) ✨ **NOUVEAU - SESSION 10 (Phase 6) - CHAT 8**
- ✅ **Session 10 - IA Conversationnelle (Chat 8 - Phase 6) terminée !**
- ✅ **Phase 6 : Emotion Analyzer (1h)**
  - src/ai/emotion_analyzer.py (680 lignes) - Analyseur émotionnel avancé
  - Classe EmotionAnalyzer avec analyse contextuelle complète
  - Dataclass EmotionResult (emotion, intensity 0-100, confidence 0-100, keywords_found, context_score, timestamp)
  - **Analyse émotionnelle avancée** :
    * Détection 6 émotions avec mots-clés pondérés (poids 1-3)
    * Support emojis français (😊😠😢😲😂)
    * Calcul intensité 0-100 basé sur densité mots-clés
    * Bonus contexte renforcé (+10-20% si ≥2 mots-clés)
  - **Calcul confiance multi-facteurs** :
    * 40% intensité détectée
    * 30% nombre mots-clés trouvés
    * 30% score contextuel historique
  - **Analyse contextuelle avec historique** :
    * Historique émotionnel par utilisateur (deque max size 5)
    * Score contextuel dynamique (50-80/100 selon cohérence)
    * Détection transitions émotionnelles
  - **Lissage des transitions (smoothing)** :
    * Smoothing factor configurable 0-1 (défaut 0.3)
    * Lissage intensité si émotion répétée
    * Réduction 10% lors changement émotion
    * Transitions douces pour expérience VRM fluide
  - **Mapping VRM Blendshapes complet** :
    * 6 Blendshapes Unity : Joy/Angry/Sorrow/Surprised/Fun/Neutral
    * Multiplicateurs d'intensité personnalisés par émotion (0.5-1.2x)
    * Seuils minimaux et ranges optimaux configurables
    * Valeurs VRM 0.0-1.0 (conversion automatique)
    * Flag 'recommended' si dans range optimal
  - Singleton pattern : get_emotion_analyzer()
  - tests/test_emotion_analyzer.py - 39 tests unitaires
  - ✅ **Tous les tests passent (39/39 en 0.11s) !**
- ✅ **Tests globaux : 137/137 passés (100%) en 15.43s** 🎉
  - +39 tests emotion analyzer
  - Tests précédents intacts (config, model, chat engine, memory, etc.)
- ✅ **Documentation complète Phase 6**
  - README.md Session 10 mis à jour avec détails Phase 6
  - Section complète dans README.md (150+ lignes)
  - Tableau comparatif EmotionDetector vs EmotionAnalyzer
  - Scripts copiés : emotion_analyzer.py, test_emotion_analyzer.py
  - docs/INDEX.md mis à jour (arborescence + scripts)
  - README.md racine mis à jour (4 sections : Sessions, Guides, Changelog, Status)
- 🎭 **Kira analyse maintenant les émotions avec précision ! Intensité, confiance, contexte et mapping VRM complet !** ✨

### Version 0.7.0-alpha (23 octobre 2025) ✨ **NOUVEAU - SESSION 10 (Phases 3-5) - CHAT 7**
- ✅ **Session 10 - IA Conversationnelle (Chat 7 - Phases 3-5) terminée !**
- ✅ **Phase 3 : Configuration IA (45 min)**
  - src/ai/config.py (420 lignes) - AIConfig avec dataclass
  - 3 profils GPU prédéfinis : performance/balanced/cpu_fallback
  - GPU_PROFILES avec n_gpu_layers, n_ctx, estimations vitesse/VRAM
  - Chargement depuis JSON avec valeurs par défaut
  - Validation complète paramètres (context_limit, temperature, top_p, max_tokens)
  - Switch profil dynamique avec get_gpu_params()
  - Singleton pattern : get_config()
  - data/config.json étendu avec section "ai" complète
  - System prompt détaillé pour personnalité Kira
  - tests/test_ai_config.py - 31 tests unitaires
  - ✅ **Tous les tests passent (31/31 en 0.21s) !**
- ✅ **Phase 4 : Model Manager (1.5h)**
  - src/ai/model_manager.py (470 lignes) - Gestionnaire LLM + GPU
  - Classe ModelManager avec détection GPU automatique (pynvml)
  - **GPU détecté : NVIDIA GeForce RTX 4050 Laptop GPU (6.0 GB VRAM, Driver 581.57)**
  - Chargement modèle avec profil GPU configuré (llama-cpp-python)
  - Auto-fallback CPU si OOM GPU
  - Génération texte avec paramètres configurables
  - Déchargement propre avec unload_model()
  - Monitoring VRAM temps réel avec get_gpu_status()
  - Singleton pattern : get_model_manager()
  - tests/test_model_manager.py - 23 tests unitaires (avec mocks)
  - ✅ **Tous les tests passent (23/23 en 1.32s) !**
- ✅ **Phase 5 : Chat Engine (2h)**
  - src/ai/chat_engine.py (480 lignes) - Moteur conversationnel unifié
  - Classe ChatEngine orchestrant mémoire + modèle + émotions
  - Classe EmotionDetector avec 6 émotions (joy/angry/sorrow/surprised/fun/neutral)
  - Détection par mots-clés français + emojis
  - Format prompt ChatML (Zephyr) avec historique
  - Construction prompts : <|system|> + <|user|> + <|assistant|>
  - Génération réponses avec contexte historique (10 messages par défaut)
  - Sauvegarde automatique conversations dans SQLite
  - Support multi-utilisateurs (isolation complète)
  - Support multi-sources (desktop, discord)
  - Dataclass ChatResponse (response, emotion, tokens_used, context_messages, processing_time)
  - Singleton pattern : get_chat_engine()
  - tests/test_chat_engine.py - 23 tests unitaires
  - tests/test_integration_phase5.py - Test intégration complet
  - ✅ **Tous les tests passent (23/23 en 0.33s) !**
- ✅ **Tests globaux : 97/97 passés (100%) en 36.64s** 🎉
  - 31 tests config
  - 23 tests model manager
  - 23 tests chat engine
  - 11 tests memory
  - 5 tests unity bridge
  - 4 tests config général
- ✅ **Documentation complète Chat 7**
  - CHAT_ENGINE_GUIDE.md - Guide utilisation complet
  - Transition Chat 7 → Chat 8 complète (5 fichiers)
  - CONTEXT_FOR_NEXT_CHAT.md avec instructions Phases 6-9
  - CURRENT_STATE.md avec architecture complète
  - prompt_transition.txt prêt pour Chat 8
  - Scripts copiés : config.py, model_manager.py, chat_engine.py, tests
  - docs/INDEX.md, README.md, chat_transitions/README.md mis à jour
- 🤖 **Kira peut maintenant parler intelligemment ! Système IA 100% fonctionnel !** 💬✨

### Version 0.6.0-alpha (22 octobre 2025) ✨ **SESSION 10 (Phases 1-2) - CHAT 6**
- ✅ **Session 10 - IA Conversationnelle (Chat 6 - Phases 1-2) démarrée !**
- ✅ **Phase 1 : Architecture de Base (30 min)**
  - Création dossiers : src/ai/, src/discord_bot/, src/auth/, models/
  - Fichiers __init__.py pour tous les modules
  - Modèle LLM copié : models/zephyr-7b-beta.Q5_K_M.gguf (6.8 GB, Mistral 7B)
  - Configuration : .env, .env.example, .gitignore étendu
  - requirements.txt avec 8 nouvelles dépendances (llama-cpp-python, discord.py, pyotp, etc.)
  - Documentation : PLAN_SESSION_10.md (14 phases détaillées), README.md Session 10
- ✅ **Phase 2 : Base de Données & Mémoire (1h)**
  - src/ai/memory.py (430 lignes) - Système conversationnel complet
  - Classe ConversationMemory avec 10 méthodes CRUD
  - Base SQLite : data/chat_history.db (7 colonnes, 4 indexes optimisés)
  - Singleton pattern avec get_memory()
  - Context manager thread-safe
  - Support multi-source (desktop + discord)
  - Support émotions pour chaque interaction
  - tests/test_memory.py - 11 tests unitaires
  - ✅ **Tous les tests passent (11/11 en 0.71s) !**
- ✅ **Documentation complète Chat 6**
  - Transition Chat 6 → Chat 7 complète (5 fichiers)
  - CONTEXT_FOR_NEXT_CHAT.md avec instructions détaillées Phase 3-5
  - CURRENT_STATE.md avec état technique complet
  - prompt_transition.txt prêt à copier
  - docs/INDEX.md, README.md mis à jour
- ✅ **Dépendances installées** : llama-cpp-python, pynvml, discord.py, pyotp, python-dotenv, qrcode, pillow, psutil
- 🤖 **Bases solides pour IA conversationnelle ! Prochaine étape : Config + LLM + Chat Engine !** ✨

### Version 0.5.0-alpha (22 octobre 2025) ✨ **SESSION 9**
- ✅ **Session 9 - Mouvements de tête + Réorganisation interface terminée !**
- ✅ VRMHeadMovementController.cs avec système de Coroutines Unity
- ✅ Animation SmoothStep pour mouvements naturels (yaw/pitch)
- ✅ Mouvements aléatoires : yaw (-5° à +5°), pitch (-2.5° à +2.5°)
- ✅ Contrôle fréquence (3-10s) et amplitude (2-10°) dans l'interface
- ✅ **Interface réorganisée en 3 onglets** : Expressions, Animations, Options
- ✅ **3 boutons reset contextuels** (un par onglet avec valeurs par défaut)
- ✅ Checkbox "Auto Head Movement" dans l'onglet Animations
- ✅ 2 sliders pour paramétrer fréquence et amplitude
- ✅ Commande IPC `set_auto_head_movement` (enabled, min_interval, max_interval, max_angle)
- ✅ **3 bugs critiques résolus** :
  - Conflit VRMAutoBlinkController (double clignement)
  - État bouton VRM après déconnexion Unity
  - Code dupliqué lors du refactoring (~137 lignes nettoyées)
- ✅ Documentation complète (4 guides techniques + scripts archivés)
- ✅ Transition Chat 6 préparée avec CONTEXT_FOR_NEXT_CHAT
- 🎭 **L'avatar bouge maintenant naturellement la tête + interface moderne et organisée !** ✨

### Version 0.4.0-alpha (21 octobre 2025) ✨ **SESSION 8**
- ✅ **Session 8 - Clignement automatique terminée !**
- ✅ VRMAutoBlinkController.cs avec système de coroutines Unity
- ✅ Animation SmoothStep (courbes de Hermite cubiques) pour réalisme maximal
- ✅ Timing naturel paramétrable (2-5s entre clignements, 160ms par cycle)
- ✅ Checkbox "Auto Blink" dans l'onglet Options de l'interface Python
- ✅ Sauvegarde automatique de configuration (config.json)
- ✅ Commande IPC `set_auto_blink` (true/false)
- ✅ **5 problèmes majeurs résolus** :
  - Blendshapes non appliqués (mapping Blink)
  - Animation trop lente (bypass Lerp)
  - Animation robotique (SmoothStep vs Lerp)
  - Configuration non sauvegardée
  - Unity ne reçoit pas commandes (délai 2.5s)
- ✅ Documentation technique massive (TECHNICAL_GUIDE.md 900+ lignes)
- ✅ Guide résolution problèmes (TROUBLESHOOTING.md complet)
- ✅ Transition Chat 4 documentée avec CONTEXT_FOR_NEXT_CHAT
- 👁️ **L'avatar cligne maintenant naturellement des yeux !** ✨

### Version 0.3.0-alpha (20 octobre 2025) ✨ **SESSION 7**
- ✅ **Session 7 - Animations fluides terminée !**
- ✅ VRMBlendshapeController.cs v2.0 avec Lerp interpolation
- ✅ Transitions smooth entre expressions (dictionnaires currentValues/targetValues)
- ✅ Slider de vitesse ajustable (1.0-10.0, défaut 3.0)
- ✅ Interface 100% en français
- ✅ Icône personnalisée (avec fix AppUserModelID Windows)
- ✅ Système de modèle VRM par défaut (menu-based)
- ✅ Chargement/déchargement dynamique (toggle)
- ✅ Thread-safety complet (Queue<Action> pattern)
- ✅ 7 bugs résolus (calibration slider, thread-safety, etc.)
- ✅ Documentation massive (README, TRANSITIONS_GUIDE 900+ lignes, SESSION_SUCCESS)
- ✅ Transition Chat 3 → Chat 4 documentée
- 🎭 **L'avatar anime maintenant ses expressions de façon fluide !** ✨

### Version 0.2.0-alpha (19 octobre 2025)
- ✅ **Session 6 - Expressions faciales terminée !**
- ✅ VRMBlendshapeController.cs v1.6 avec contrôle expressions VRM
- ✅ Interface GUI avec onglet "Expressions"
- ✅ 5 sliders pour émotions (joy, angry, sorrow, surprised, fun)
- ✅ Contrôle précis 0-100% pour chaque expression
- ✅ Bouton "Reset All Expressions"
- ✅ Commandes IPC : set_expression, reset_expressions
- ✅ Documentation Session 6 complète
- 🎭 **L'avatar peut maintenant exprimer des émotions !** 😊😠😢😲😄

### Version 0.1.0-alpha (18 octobre 2025)
- ✅ **MVP terminé !**
- ✅ Interface Python Qt fonctionnelle
- ✅ Communication IPC Python ↔ Unity stable
- ✅ Chargement et affichage de modèles VRM
- ✅ Documentation complète par sessions (0-5)
- ✅ Configuration Git optimisée pour Unity
- ✅ 8 tests unitaires Python
- 🎭 **Premier avatar affiché avec succès !**

### Session 0 - Configuration Git (18 octobre 2025)
- ⚙️ Configuration `.gitignore` pour Unity
- 📦 Exclusion Library/, Temp/, PackageCache/
- 📚 Documentation bonnes pratiques Git + Unity

---

**🎊 Status actuel : [Phase 9] COMPLÈTE ! L'avatar s'affiche, exprime des émotions avec transitions fluides, cligne naturellement des yeux, bouge la tête de manière vivante ET peut maintenant PARLER INTELLIGEMMENT grâce à un système d'IA conversationnelle complet (LLM Zephyr-7B optimisé GPU RTX 4050 avec 6-7x accélération !) avec analyse émotionnelle AVANCÉE (intensité, confiance, contexte, lissage, mapping VRM) + BOT DISCORD fonctionnel + INTERFACE CHAT GUI DESKTOP avec chargement manuel IA (contrôle utilisateur complet) ! Interface moderne en onglets ! 158/158 tests passent ! ✨👁️🎭💬🤖🎯🎮✨🎊**

**🚀 Prochaine étape (Chat 9 - Phase 10) : GUI Discord Control (panneau de contrôle du bot Discord dans l'interface Desktop-Mate) ! 🎮🤖**

⭐ **N'oubliez pas de mettre une étoile si ce projet vous plaît !** ⭐
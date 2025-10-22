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

10. **[Session 10 - IA Conversationnelle (Kira)](docs/sessions/session_10_ai_chat/)** ✅ **EN COURS - Chat 6 (Phases 1-2)**
   - **Phase 1** : Architecture de Base (30 min) ✅
     - Dossiers : src/ai/, src/discord_bot/, src/auth/, models/
     - Modèle LLM copié (Zephyr-7B, 6.8 GB)
     - Configuration : .env, requirements.txt, .gitignore
   - **Phase 2** : Base de Données & Mémoire (1h) ✅
     - src/ai/memory.py (430 lignes)
     - SQLite chat_history avec 4 indexes
     - Tests : 11/11 passés
     - Singleton pattern + Context manager thread-safe
   - **Prochaine (Chat 7)** : Phases 3-5 (Config + LLM + Chat Engine)
   - **L'avatar aura bientôt une IA conversationnelle intelligente !** 🤖✨

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
- [Résolution problèmes Session 9](docs/sessions/session_9_head_movements/DEBUG_ISSUES.md) ✨ **3 bugs critiques résolus !**
- [Plan Session 10](docs/sessions/session_10_ai_chat/PLAN_SESSION_10.md) ✨ **14 phases IA conversationnelle détaillées !**
- [Contexte Chat 7](docs/chat_transitions/chat_6_session_10_phases_1_2/CONTEXT_FOR_NEXT_CHAT.md) ✨ **Instructions complètes Phase 3-5 !**

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

### Version 0.6.0-alpha (22 octobre 2025) ✨ **NOUVEAU - SESSION 10 (Phases 1-2)**
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

**🎊 Status actuel : [Phase 4] COMPLÈTE ! L'avatar s'affiche, exprime 5 émotions avec transitions fluides, cligne naturellement des yeux, bouge la tête de manière vivante ET possède maintenant un système de mémoire conversationnelle SQLite complet ! Interface moderne en 3 onglets ! Architecture IA prête pour LLM ! ✨👁️�🤖�🎊**

**🚀 Prochaine étape (Chat 7 - Phase 3) : Configuration IA + Model Manager + Chat Engine (donner vie à l'IA de Kira) ! 🧠💬🤖**

⭐ **N'oubliez pas de mettre une étoile si ce projet vous plaît !** ⭐
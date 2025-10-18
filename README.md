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

**Status actuel :** ✅ Phase 1 (MVP) terminée ! L'avatar VRM s'affiche et répond aux commandes Python.

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
│   ├── session_0_git_configuration/ # ⚙️ Configuration Git Unity
│   ├── session_1_setup/ # Setup Python + GUI
│   ├── session_2_unity_installation/
│   ├── session_3_univrm_installation/
│   ├── session_4_python_unity_connection/
│   └── session_5_vrm_loading/  # ✅ Dernière session complète
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

### Phase 2 : Expressions & Animations 😊 (En cours)
- [ ] Contrôle des blendshapes VRM
- [ ] Système d'émotions prédéfinies
- [ ] Boutons d'expressions dans l'UI Python
- [ ] Animations idle (respiration, clignement)
- [ ] Timeline d'animations

### Phase 3 : Audio & Lip-Sync 🎤
- [ ] Capture audio microphone
- [ ] Détection d'amplitude vocale
- [ ] Lip-sync basique (ouverture bouche)
- [ ] VU-meter dans l'UI
- [ ] TTS (Text-to-Speech)

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
- **Interface Python Qt** : Fenêtre de contrôle avec boutons
- **Connexion Unity** : Communication bidirectionnelle stable
- **Chargement VRM** : Import et affichage de modèles VRM
- **Avatar 3D** : Modèle "Mura Mura" affiché dans Unity
- **Logs détaillés** : Console + fichiers pour debugging
- **Tests unitaires** : 8 tests Python qui passent

### 🚧 En développement
- Contrôle des blendshapes (expressions faciales)
- Animations et mouvements
- Capture audio et lip-sync

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

0. **[Session 0 - Configuration Git Unity](docs/session_0_git_configuration/)** ⚙️
   - Configuration `.gitignore` pour Unity
   - Exclusion des fichiers générés (Library/, Temp/)
   - Bonnes pratiques Git pour projets Unity

1. **[Session 1 - Setup Python + GUI](docs/session_1_setup/)** ✅
   - Configuration environnement Python
   - Interface Qt avec PySide6
   - Système de configuration et logs

2. **[Session 2 - Installation Unity](docs/session_2_unity_installation/)** ✅
   - Installation Unity 2022.3 LTS
   - Création projet URP
   - Configuration de base

3. **[Session 3 - Installation UniVRM](docs/session_3_univrm_installation/)** ✅
   - Installation du package UniVRM
   - Support des modèles VRM
   - Configuration des shaders

4. **[Session 4 - Connexion Python ↔ Unity](docs/session_4_python_unity_connection/)** ✅
   - Communication IPC via socket TCP
   - PythonBridge.cs (serveur Unity)
   - unity_bridge.py (client Python)
   - Résolution des problèmes de connexion

5. **[Session 5 - Chargement VRM](docs/session_5_vrm_loading/)** ✅
   - VRMLoader.cs avec thread-safety
   - Chargement dynamique des modèles VRM
   - Affichage de l'avatar 3D
   - **Application fonctionnelle !** 🎉

### Guides spécifiques

- [Configuration Git Unity](docs/session_0_git_configuration/GIT_UNITY_FIX.md)
- [Architecture technique](docs/session_1_setup/architecture.md)
- [Debug connexion Unity](docs/session_4_python_unity_connection/DEBUG_CONNECTION.md)
- [Fix script Unity](docs/session_4_python_unity_connection/FIX_SCRIPT_NOT_RUNNING.md)
- [Récapitulatif Session 5](docs/session_5_vrm_loading/SESSION_VRM_LOADING_SUCCESS.md)

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
- �️ **Conversation intelligente** : L'avatar pourra discuter naturellement grâce à un LLM (chatbot IA)
- 😊 **Émotions réactives** : Analyse du sentiment et expressions faciales adaptées
- 🚶 **Mobilité libre** : Déplacement autonome sur le bureau, interactions avec l'environnement
- 🎤 **Voix naturelle** : Reconnaissance vocale + synthèse vocale synchronisée
- 🧠 **Comportements intelligents** : Décisions autonomes basées sur le contexte

**L'avatar deviendra un véritable compagnon numérique interactif et intelligent !**

## �👤 Auteur

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

**🎊 Status actuel : MVP fonctionnel ! L'avatar s'affiche et répond aux commandes ! 🎊**

⭐ **N'oubliez pas de mettre une étoile si ce projet vous plaît !** ⭐
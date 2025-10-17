# Desktop-Mate

🎭 **Interactive VRM Desktop Companion** - Une application hybride Unity + Python qui donne vie à votre avatar VRM sur votre bureau !

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Unity 2022.3+](https://img.shields.io/badge/unity-2022.3+-black.svg)](https://unity.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Description

Desktop-Mate est une application qui permet d'afficher un avatar VRM interactif sur votre bureau Windows. L'avatar peut :
- 🎤 Synchroniser ses lèvres avec votre microphone (lip-sync)
- 😊 Afficher des expressions et émotions
- 👁️ Suivre votre visage via webcam
- 🎮 Réagir à des commandes et interactions

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
│   │   └── app.py        # Application principale
│   ├── ipc/              # Communication Unity ↔ Python
│   │   └── unity_bridge.py
│   ├── audio/            # Capture et traitement audio
│   ├── avatar/           # Gestion avatar et VRM
│   └── utils/            # Utilitaires (config, logs)
│       ├── config.py
│       └── logger.py
│
├── unity/                 # Projet Unity
│   └── (À créer avec Unity Hub)
│
├── assets/               # Assets partagés
│   └── Mura Mura - Model.vrm
│
├── tests/                # Tests unitaires
├── docs/                 # Documentation
└── .github/              # CI/CD et workflows
    └── workflows/
```

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
2. Créer un nouveau projet **3D (URP)** dans le dossier `unity/`
3. Installer les packages nécessaires :
   - **VRM** : [UniVRM](https://github.com/vrm-c/UniVRM)
   - **Netcode** (optionnel pour IPC avancé)

### Étape 4 : Lancer l'application

```powershell
# Activer le venv si ce n'est pas déjà fait
.\venv\Scripts\Activate.ps1

# Lancer l'application Python
python main.py
```

## 🎯 Roadmap

### Phase 1 : MVP (En cours) ✨
- [x] Structure du projet
- [x] Interface Qt de base
- [x] Communication IPC Unity ↔ Python (socket)
- [ ] Lancement Unity depuis Python
- [ ] Chargement d'un modèle VRM dans Unity
- [ ] Affichage basique du modèle

### Phase 2 : Audio & Lip-Sync 🎤
- [ ] Capture audio microphone
- [ ] Détection d'amplitude vocale
- [ ] Lip-sync basique (ouverture bouche)
- [ ] VU-meter dans l'UI

### Phase 3 : Expressions & Animations 😊
- [ ] Contrôle des blendshapes VRM
- [ ] Système d'émotions prédéfinies
- [ ] Animations idle et gestuelles
- [ ] Timeline d'animations

### Phase 4 : Tracking & Avancé 👁️
- [ ] Face tracking via webcam (MediaPipe)
- [ ] Eye tracking basique
- [ ] TTS (Text-to-Speech)
- [ ] Système de plugins

### Phase 5 : Polish & Release 🚀
- [ ] Packaging .exe
- [ ] Installeur Windows
- [ ] Documentation complète
- [ ] Tutoriels vidéo

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
- **Sockets TCP** : IPC Python ↔ Unity
- (Futur : OSC ou gRPC pour plus de robustesse)

## 📖 Documentation

- [Guide d'installation détaillé](docs/installation.md) *(à venir)*
- [Architecture technique](docs/architecture.md) *(à venir)*
- [API Documentation](docs/api.md) *(à venir)*
- [Guide de contribution](CONTRIBUTING.md) *(à venir)*

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

## 👤 Auteur

**Xyon15**
- GitHub: [@Xyon15](https://github.com/Xyon15)

## 🙏 Remerciements

- [UniVRM](https://github.com/vrm-c/UniVRM) pour le support VRM
- [Model VRM](https://acidicdollz.booth.pm/) AcidicDoll pour le modèle VRM

## 📞 Support

Si vous rencontrez des problèmes ou avez des questions :
- Ouvrez une [issue](https://github.com/Xyon15/desktop-mate/issues)
- Consultez la [documentation](docs/)

---

⭐ **N'oubliez pas de mettre une étoile si ce projet vous plaît !** ⭐
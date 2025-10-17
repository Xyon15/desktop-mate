# Unity Project Setup Guide

Ce dossier contiendra le projet Unity pour le rendu VRM de Desktop-Mate.

## Création du projet Unity

### Étape 1 : Créer le projet

1. Ouvrir **Unity Hub**
2. Cliquer sur **"New Project"**
3. Sélectionner le template **"3D (URP)"** (Universal Render Pipeline)
4. Paramètres :
   - **Project Name** : `DesktopMateUnity`
   - **Location** : Sélectionner ce dossier (`desktop-mate/unity/`)
   - **Unity Version** : 2022.3 LTS ou plus récent
5. Cliquer sur **"Create Project"**

### Étape 2 : Installer UniVRM

UniVRM est la bibliothèque officielle pour charger des modèles VRM dans Unity.

**Option A : Via Unity Package Manager (Recommandé)**
1. Ouvrir **Window > Package Manager**
2. Cliquer sur **"+" > Add package from git URL**
3. Entrer : `https://github.com/vrm-c/UniVRM.git?path=/Assets/VRMShaders`
4. Répéter avec : `https://github.com/vrm-c/UniVRM.git?path=/Assets/UniGLTF`
5. Répéter avec : `https://github.com/vrm-c/UniVRM.git?path=/Assets/VRM`

**Option B : Via unitypackage**
1. Télécharger depuis : https://github.com/vrm-c/UniVRM/releases
2. Importer le package dans Unity : **Assets > Import Package > Custom Package**

### Étape 3 : Créer la scène principale

1. Créer une nouvelle scène : **File > New Scene**
2. Sauvegarder sous `Assets/Scenes/MainScene.unity`
3. Configurer la caméra :
   - Position : (0, 1.5, -3)
   - Rotation : (0, 0, 0)
4. Ajouter un éclairage directionnel si nécessaire

### Étape 4 : Scripts de communication IPC

Les scripts C# pour communiquer avec Python seront ajoutés dans `Assets/Scripts/`.

Structure à créer :
```
Assets/
├── Scenes/
│   └── MainScene.unity
├── Scripts/
│   ├── IPC/
│   │   ├── PythonBridge.cs      # Communication socket avec Python
│   │   └── CommandHandler.cs    # Gestionnaire de commandes
│   ├── VRM/
│   │   ├── VRMLoader.cs         # Chargement de modèles VRM
│   │   └── VRMController.cs     # Contrôle animations/blendshapes
│   └── Core/
│       └── GameManager.cs       # Gestionnaire principal
└── Models/
    └── (Modèles VRM importés)
```

## Prochaines étapes

1. **Créer le projet Unity** selon les instructions ci-dessus
2. **Implémenter PythonBridge.cs** pour la communication socket
3. **Implémenter VRMLoader.cs** pour charger les modèles
4. **Tester la connexion** avec l'application Python

## Références

- [UniVRM Documentation](https://vrm.dev/en/univrm/)
- [Unity Scripting Reference](https://docs.unity3d.com/ScriptReference/)
- [VRM Specification](https://github.com/vrm-c/vrm-specification)

# 📚 Documentation Desktop-Mate

Organisation de la documentation par sessions de développement.

---

## 📁 Structure des dossiers

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

### 📂 Unity_docs/ (legacy)
Ancienne documentation Unity - À réorganiser ou supprimer

### 📂 1st/ (legacy)
Ancien dossier - À vérifier et réorganiser si nécessaire

---

## 🎯 État actuel du projet

### ✅ Fonctionnel
- Application Python avec interface Qt
- Communication Python ↔ Unity via socket TCP
- Chargement de modèles VRM depuis Python
- Affichage 3D de l'avatar dans Unity

### 🚧 En cours / À venir
- Contrôle des expressions faciales (blendshapes)
- Animation de l'avatar
- Lip-sync avec microphone
- TTS (Text-to-Speech)
- Face tracking (optionnel)

---

## 📖 Comment utiliser cette documentation

1. **Débutant :** Lis les sessions dans l'ordre (1 → 5)
2. **Problème spécifique :** Consulte la session correspondante
3. **Référence rapide :** Utilise les fichiers de la session concernée
4. **Code propre :** Les scripts finaux sont dans les dossiers `scripts/`

---

## 🔗 Liens utiles

- [Repository GitHub](https://github.com/Xyon15/desktop-mate)
- [Documentation UniVRM](https://github.com/vrm-c/UniVRM)
- [Documentation Unity](https://docs.unity3d.com/)
- [Documentation PySide6](https://doc.qt.io/qtforpython/)

---

**Dernière mise à jour :** 18 octobre 2025  
**Version du projet :** 0.1.0-alpha  
**Status :** ✅ Chargement VRM fonctionnel

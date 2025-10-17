---
mode: agent
---
Je veux démarrer pour la première fois le projet.

Je vais te donner un prompt généré par chatgpt pour t'expliquer le contexte du projet et ce que j'attends de toi.
Comme je te l'ai dit, je ne suis pas un expert en développement, donc si tu vois la moindre erreur, moindre problème ou question n'hésite pas à me le dire.

Voici le prompt :

Objectif : Créer une application desktop "Desktop-Mate" en Python inspirée de Desktop Mate (VRM avatar interactif). L'application doit charger un modèle VRM (ou glTF/VRM), afficher et animer l'avatar en temps réel, gérer l'audio (microphone & TTS), proposer du lip-sync, des émotions/expressions, du suivi visage/caméra basique (via webcam), et une UI de configuration. Le projet doit être modulaire, cross-platform (Windows + Linux), documenté et prêt pour CI.

Contraintes & priorités :
1. Prototype minimum viable (MVP) d'abord : chargement VRM + rendu OpenGL + animation basique + UI pour importer un modèle.
2. Qualité ensuite : lip-sync via audio input, expressions blendshapes, commandes clavier, persistance des prefs.
3. Architecture modulaire : séparation nette entre rendu (renderer), logique d'avatar (avatar_engine), entrées (audio, webcam, hotkeys), UI, et backend (IPC / socket pour extensions).

Choix d'architecture recommandés (deux options) :
A) **Stack Python pur (recommandé si tu veux rester 100% Python)**  
   - GUI : PySide6 (Qt) ou PyQt6  
   - Rendu GPU : moderngl (OpenGL moderne) ou pyglet (si plus simple)  
   - Parsing VRM/glTF : `pygltflib` (lecture/accès aux nodes, blendshapes) ou loader custom minimal  
   - Webcam / tracking : OpenCV (face landmarks via dlib ou mediapipe)  
   - Audio input / VAD : sounddevice + numpy ; lip-sync par extraction d'énergie/phonemes (p. ex. via vosk ou Whisper pour phonèmes si disponible)  
   - TTS : pyttsx3 (offline) ou possibilité d'appels à services externes  
   - Packager : PyInstaller / brief instructions pour creation d’exe / AppImage

B) **Stack Hybride (recommandé si priorité rendu VRM avancé)**  
   - Rendu & VRM natif : Unity (ou Godot) pour charger VRM facilement  
   - Logique & UI : Python app (PySide6) qui communique avec Unity via sockets / OSC / HTTP local  
   - Avantage : rendu et mécaniques VRM complètes ; Inconvénient : plus d’outillage et multi-langage.

Fonctionnalités MVP détaillées :
- Chargement d'un fichier VRM/glTF via UI (drag & drop) et affichage 3D.  
- Caméra orbitale & zoom.  
- Play/Pause animation, contrôles d'expression (slider pour blendshapes).  
- Microphone input → amplitude → animation bouche (lip-sync simple).  
- Sauvegarde & chargement des préférences utilisateur (fichier JSON local).  
- Fenêtre "Studio" pour tester expressions / poses / audio.  
- Logs basiques et écran Debug.

Fonctionnalités avancées (phase 2) :
- Reconnaissance phonèmes (amélioration lip-sync) via Whisper/Vosk si dispo.  
- Face tracking via Mediapipe → mapping tête/yeux/expressions.  
- Text-to-speech avec réglage voix & timing pour animation.  
- Plugins (architecture simple pour extensions externes).  
- Hotkeys personnalisables, overlay toujours au-dessus (optionnel).

Livrables attendus dans le repo GitHub :
- `README.md` clair (but, installation, how to run, roadmap).  
- Structure de projet initiale : `src/` avec `gui/`, `renderer/`, `avatar/`, `io/`, `utils/`.  
- Exemple minimal `main.py` qui lance l'app et charge un modèle d'exemple (placeholder).  
- `requirements.txt` (ou `pyproject.toml`) et instructions packaging.  
- Tests unitaires de base pour utilitaires (pytest).  
- Workflow GitHub Actions : lint (flake8/black), tests, build artefact (optional).  
- Licence (MIT par défaut) + CONTRIBUTING.md + issue/template.

Tâches Copilot / issues automatiques à générer :
1. Initialiser repo + venv + requirements.  
2. Implémenter UI principal (PySide6) : barre menu, panneau 3D, panneau paramètres.  
3. Implementer renderer minimal avec moderngl : fenêtre OpenGL embarquée dans Qt.  
4. Parser VRM/glTF minimal pour obtenir mesh + blendshapes.  
5. Intégrer microphone input et afficher niveau audio (VU meter).  
6. Mapper amplitude → ouverture bouche (lip sync basique).  
7. Sauvegarder/charger prefs JSON.  
8. Écrire README & CI.

Exemples de messages que Copilot doit générer pour les commits :
- feat(gui): add main window + 3D viewport placeholder  
- feat(renderer): add moderngl context + basic render loop  
- feat(avatar): add VRM loader skeleton + blendshape controller  
- feat(audio): add microphone capture + VU meter + simple lip sync

Tests & QA :
- Unit tests pour parsing VRM (structure de base).  
- Integration test: lancer app en mode headless (renderer mock) et charger un modèle test.  
- Checklist QA pour release.

Fichiers d'exemple à générer automatiquement (boilerplate) :
- `README.md` (avec badges ci, instructions)  
- `src/main.py` (entrypoint)  
- `src/gui/app.py` (Qt App bootstrap)  
- `src/renderer/gl_view.py` (OpenGL widget)  
- `src/avatar/loader.py` (VRM/glTF parsing utils)  
- `src/audio/mic.py` (capture audio)  
- `requirements.txt` (PySide6, moderngl, pygltflib, sounddevice, numpy, opencv-python, mediapipe optional, pytest)

Critères de réussite (MVP) :
- Lancement de l'application sous Windows.  
- Chargement visuel d'un modèle VRM simple (au moins le mesh visible).  
- Lip-sync basique à partir du micro (bouche s'ouvre quand on parle).  
- UI pour charger/sauvegarder prefs.

Documenter :
- Roadmap (MVP → 2 mois features → 6 mois features).  
- Liste des bibliothèques alternatives et justification.  
- Guides d'intégration Unity/Python si opté pour le mode hybride.

Ton attendu pour les messages de commit et issues : clair, en anglais pour la visibilité open source (mais documentation principale en FR et EN).

Génère maintenant le squelette du repo (README + structure de dossiers + fichier `main.py`) en tant que prochaine étape.



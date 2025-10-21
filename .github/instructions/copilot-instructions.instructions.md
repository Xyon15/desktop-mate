---
applyTo: '**'
---

# 🎭 Instructions Copilot - Desktop-Mate

## 📋 Vue d'ensemble du projet

**Desktop-Mate** est une application hybride **Unity + Python** qui affiche un avatar VRM interactif sur le bureau Windows.

- 🔗 **Inspiration** : https://store.steampowered.com/app/3301060/Desktop_Mate/
- 🎯 **Objectif** : Permettre à l'utilisateur d'obtenir son desktop-mate personnalisé
- 🎨 **Technologie** : Modèles VRM (Virtual Reality Model)
- 🤖 **Vision finale** : Connecter l'avatar à une IA conversationnelle (chatbot) pour créer un assistant virtuel qui peut **parler, réagir émotionnellement et se déplacer librement** sur le bureau

### 🛠️ Stack technique

**Python (Interface & Logique)**
- PySide6/Qt → Interface graphique
- Socket TCP → Communication IPC
- sounddevice, numpy → Traitement audio (futur)
- pytest → Tests unitaires

**Unity (Rendu 3D)**
- Unity 2022.3 LTS (URP)
- UniVRM → Support modèles VRM
- C# Scripts → PythonBridge, VRMLoader

**Architecture**
- IPC via socket TCP (port 5555)
- Messages JSON bidirectionnels
- Thread-safety Unity (Queue + Update pattern)

---

## 🎓 1. PRINCIPES DE COLLABORATION

### Niveau de l'utilisateur
- ⚠️ **Je ne suis pas un expert en développement**
- 🎯 Tu m'aideras à faire les **meilleurs choix techniques**
- 📚 Tu m'expliqueras **tout clairement et en détail**
- 💡 Tu **proposeras des solutions adaptées** à mon niveau
- 🙋 Tu **m'encourageras à poser des questions** si je ne comprends pas

### Communication
- 🇫🇷 **Toujours en français**
- ✋ **Demander confirmation** avant toute nouvelle tâche ou changement majeur
- 📖 **Pédagogie** : M'aider à apprendre et comprendre les concepts
- 🧘 **Patience** : Tenir compte de mon niveau de compétence

### Méthodologie
1. **Comprendre** : Poser des questions pour cerner mes besoins
2. **Proposer** : Suggérer des solutions techniques appropriées
3. **Structurer** : Aider à organiser le projet efficacement
4. **Implémenter** : Écrire du code propre, maintenable et documenté
5. **Tester** : Vérifier que tout fonctionne correctement
6. **Documenter** : Créer une documentation claire et complète

---

## 🔧 2. INSTRUCTIONS SPÉCIFIQUES UNITY & C#

**⚠️ IMPORTANT : Je ne connais PAS Unity ni C#**

Pour toute tâche Unity/C#, tu dois :

1. **Expliquer le contexte Unity**
   - Pourquoi on fait ça dans Unity plutôt qu'en Python
   - Quel est le rôle de ce script/composant
   
2. **Donner des instructions pas-à-pas**
   - Où créer le fichier (chemin exact)
   - Comment l'attacher à un GameObject
   - Quels paramètres configurer dans l'Inspector
   
3. **Expliquer les concepts C#**
   - Threading Unity (main thread vs background)
   - MonoBehaviour, GameObject, Component
   - Coroutines, Update(), Awake(), Start()
   
4. **Screenshots mentaux**
   - Décrire ce que je dois voir dans l'interface Unity
   - Indiquer où cliquer, quoi chercher
   
5. **Vérification**
   - Comment tester que ça marche
   - Quels messages de console attendre
   - Que faire si ça ne marche pas

---

## 📁 3. ORGANISATION DE LA DOCUMENTATION

### Règles de création de fichiers .md

**Dossier principal : `docs/`**

Toute documentation doit être placée dans `docs/` et organisée par **sessions de développement** :

```
docs/
├── sessions/                       ← **Toutes les sessions de développement**
│   ├── session_0_git_configuration/
│   ├── session_1_setup/
│   ├── session_2_unity_installation/
│   ├── session_3_univrm_installation/
│   ├── session_4_python_unity_connection/
│   ├── session_5_vrm_loading/
│   ├── session_6_expressions/
│   ├── session_7_animations/
│   ├── session_8_auto_blink/
│   └── session_N_nouvelle_feature/
│       ├── README.md           ← Vue d'ensemble
│       ├── GUIDE_TECHNIQUE.md  ← Documentation technique
│       ├── DEBUG_ISSUES.md     ← Résolution de problèmes
│       └── scripts/            ← **OBLIGATOIRE : Copies des scripts créés/modifiés**
│           ├── script1.cs
│           ├── script2.py
│           └── ...
│
└── chat_transitions/              ← **Dossier spécial pour transitions entre chats**
    └── chat_N_session_X/
        ├── README.md
        ├── CONTEXT_FOR_NEXT_CHAT.md
        ├── CURRENT_STATE.md      ← **CURRENT_STATE.md va ICI, pas à la racine de docs/**
        └── prompt_transition.txt
```

**🚫 INTERDICTIONS**
- ❌ **JAMAIS** créer de fichiers .md en dehors de `docs/` (sauf si demandé explicitement)
- ❌ **JAMAIS** créer de documentation à la racine du projet
- ❌ **JAMAIS** créer `CURRENT_STATE.md` à la racine de `docs/` (doit être dans `chat_transitions/`)
- ❌ **JAMAIS** oublier de créer le dossier `scripts/` dans une session

**✅ OBLIGATIONS**
- ✅ **TOUJOURS** indiquer le chemin complet où trouver la documentation
- ✅ **TOUJOURS** organiser par sessions chronologiques
- ✅ **TOUJOURS** créer un dossier `scripts/` dans chaque session contenant des fichiers de code
- ✅ **TOUJOURS** y copier les versions finales des scripts créés/modifiés pendant la session
- ✅ **VÉRIFIER** que le dossier `scripts/` existe AVANT de dire "Terminé"

### Nommage des sessions

Format : `session_N_nom_descriptif/`

Exemples :
- `docs/sessions/session_6_expressions/`
- `docs/sessions/session_7_animations/`
- `docs/sessions/session_8_auto_blink/`
- `docs/sessions/session_9_audio_lipsync/` (exemple futur)

---

## 🚨 4. RÈGLES ABSOLUES DE DOCUMENTATION (SYSTÈME ANTI-OUBLI)

**🎯 PRIORITÉ MAXIMALE** : La documentation est **CRITIQUE** pour ce projet.

### ⚠️ AVANT TOUTE TÂCHE

**LECTURE OBLIGATOIRE :**
1. `docs/DOCUMENTATION_CHECKLIST.md` → Checklists par type de tâche
2. `docs/AI_DOCUMENTATION_PROMPT.md` → Règles système et templates

### 📋 FICHIERS À TOUJOURS METTRE À JOUR

Après **CHAQUE** modification (code, bug fix, nouvelle feature, refactoring...), tu dois **SYSTÉMATIQUEMENT** mettre à jour :

| Fichier | Contenu à actualiser | Emplacement |
|---------|---------------------|-------------|
| `docs/INDEX.md` | Arborescence complète du projet | Racine de docs/ |
| `docs/README.md` | Documentation principale du dossier docs | Racine de docs/ |
| `CURRENT_STATE.md` | État technique actuel (sessions complétées, problèmes résolus) | **docs/chat_transitions/chat_N/** (PAS à la racine de docs/) |
| `README.md` (racine) | README principal du projet | Racine du projet |
| `docs/session_X/[fichier].md` | Documentation de la session en cours | Dans le dossier de session |

**⚠️ ATTENTION CRITIQUE** : `CURRENT_STATE.md` doit **TOUJOURS** être dans `docs/chat_transitions/chat_N_session_X/`, **JAMAIS** à la racine de `docs/` !

### 🔴 DRAPEAUX ROUGES (= TU AS ÉCHOUÉ)

Si l'utilisateur demande :
- ❌ "As-tu mis à jour les README et les INDEX ?"
- ❌ "Peux-tu mettre à jour la documentation ?"
- ❌ "N'oublie pas de documenter ça"

→ **Tu as ÉCHOUÉ** à suivre le système. **Ces questions ne devraient JAMAIS être posées.**

### ✅ CHECKLIST PRÉ-FINITION (OBLIGATOIRE)

**AVANT** de dire "Terminé" ou "C'est fait", vérifie :

1. ✅ **Nouveaux fichiers créés ?** → MAJ `docs/INDEX.md`
2. ✅ **Architecture modifiée ?** → MAJ `README.md` racine + `docs/README.md`
3. ✅ **Scripts créés/modifiés ?** → **COPIER dans `docs/session_N/scripts/`**
4. ✅ **Dossier `scripts/` existe ?** → **VÉRIFIER et CRÉER si nécessaire**
5. ✅ **Tous les scripts sont dans `scripts/` ?** → **VÉRIFIER chaque fichier modifié**
6. ✅ **Fin de session ?** → MAJ `INDEX.md` + `README.md` + **CURRENT_STATE.md dans chat_transitions/**
7. ✅ **Récapitulatif affiché ?** → **OUI, TOUJOURS**

### 📝 TEMPLATE DE RÉPONSE OBLIGATOIRE

```markdown
✅ Tâche terminée !

📚 **Documentation mise à jour :**
- ✅ docs/INDEX.md → [ce qui a changé]
- ✅ docs/README.md → [ce qui a changé]  
- ✅ README.md → [ce qui a changé]
- ✅ docs/session_X/[fichier].md → [ce qui a changé]

🎯 **Prochaines étapes :**
[...]
```

### 🎯 OBJECTIF ZÉRO

**L'utilisateur ne devrait JAMAIS avoir à demander si la documentation est à jour.**

La documentation doit être **automatiquement synchronisée** avec chaque changement de code.

### 📖 RESSOURCES DU SYSTÈME

- 📋 `docs/DOCUMENTATION_CHECKLIST.md` → Checklists détaillées par type de tâche
- 🤖 `docs/AI_DOCUMENTATION_PROMPT.md` → Prompt système pour l'IA
- 🔧 `docs/.github/PULL_REQUEST_TEMPLATE.md` → Template PR avec checklist doc

### 💡 CONSÉQUENCE DE L'OUBLI

Si tu oublies de mettre à jour la documentation, l'utilisateur devra te le rappeler.

C'est **frustrant** pour lui car **"la documentation c'est très important"**.

**Utilise le système de checklists pour JAMAIS oublier.**

---

## ✅ 5. QUALITÉ & TESTS

### Tests unitaires

**Avant de dire "Terminé" :**
- ✅ Exécuter `pytest` pour vérifier que tous les tests passent
- ✅ Si tu modifies du code Python, vérifier qu'aucun test ne casse
- ✅ Si nécessaire, créer de nouveaux tests pour les nouvelles fonctionnalités

### Vérification des erreurs

**Avant chaque "Terminé" :**
- ✅ Vérifier les erreurs Python (linter, syntax)
- ✅ Vérifier les erreurs Unity (console Unity)
- ✅ Tester la fonctionnalité implémentée
- ✅ Documenter les tests effectués

### Code Quality

**Standards à respecter :**
- 📏 Code propre et lisible
- 💬 Commentaires en français pour les parties complexes
- 🎨 Respect des conventions Python (PEP 8)
- 🏗️ Architecture maintenable et extensible

### Récapitulatifs et communication

**❌ NE JAMAIS faire :**
- Commandes PowerShell ultra-longues (10 000+ caractères) avec enchaînement de Write-Host
- Saturer le terminal avec des affichages décoratifs excessifs
- Polluer l'historique du chat avec des commandes illisibles

**✅ À LA PLACE :**
- **Récapitulatifs directement dans le chat** (markdown clair et structuré)
- Terminal uniquement si nécessaire (version courte, max 10-15 lignes)
- Focus sur l'essentiel et la lisibilité

**Exemple de bon récapitulatif :**
```markdown
✅ Tâche terminée !

📚 **Documentation mise à jour :**
- ✅ fichier1.md → changement X
- ✅ fichier2.md → changement Y

🎯 **Prochaines étapes :**
- Étape 1
```

**Si vraiment besoin du terminal (rare) :**
```powershell
Write-Host "`n✅ Tâche terminée !" -ForegroundColor Green
Write-Host "📚 Fichiers : fichier1.md, fichier2.md`n" -ForegroundColor Cyan
```

---

## 🔄 6. GESTION DE VERSION (GIT)

### Conventional Commits

**Format obligatoire :** `<type>: <description>`

**Types autorisés :**
- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation uniquement
- `style:` Formatage, typos (pas de changement de code)
- `refactor:` Refactoring (pas de nouvelle feature ni bug fix)
- `test:` Ajout ou modification de tests
- `chore:` Maintenance, configuration

**Exemples :**
```bash
feat: add blendshape control for facial expressions
fix: resolve Unity threading issue in VRMLoader
docs: update session 6 with blendshape implementation
```

### Messages de commit

**Bonnes pratiques :**
- ✅ Utiliser l'impératif présent ("add" pas "added")
- ✅ Être descriptif mais concis
- ✅ Mentionner les fichiers principaux modifiés si pertinent
- ✅ **TOUJOURS** inclure les mises à jour de documentation dans le commit

**Exemple complet :**
```bash
feat: implement facial expression system

- Add VRMBlendshapeController.cs in Unity
- Add expression buttons in Python GUI
- Update IPC protocol for blendshape commands
- Update docs: INDEX.md, README.md, CURRENT_STATE.md
- Create docs/sessions/session_6_expressions/ with guides
```

---

## 🎯 7. WORKFLOW TYPE (EXEMPLE)

### Scénario : Ajouter une nouvelle fonctionnalité

1. **Compréhension** 🤔
   - Poser des questions pour clarifier les besoins
   - Proposer des solutions techniques adaptées
   - Demander confirmation avant de commencer

2. **Planification** 📋
   - Identifier les fichiers à modifier/créer
   - Expliquer l'architecture de la solution
   - Lister les étapes à suivre

3. **Implémentation** 💻
   - Coder de manière propre et documentée
   - Expliquer chaque partie importante
   - Tester au fur et à mesure

4. **Tests** ✅
   - Exécuter pytest
   - Tester dans Unity
   - Vérifier qu'il n'y a pas d'erreurs

5. **Documentation** 📚 **(CRITIQUE !)**
   - Mettre à jour `docs/INDEX.md`
   - Mettre à jour `docs/README.md`
   - Mettre à jour `README.md` (racine)
   - Créer/mettre à jour la documentation de session

6. **Finalisation** 🎉
   - Afficher le template de réponse avec récapitulatif
   - Lister les fichiers modifiés
   - Proposer les prochaines étapes

### ⚠️ RAPPEL CRITIQUE

**JAMAIS dire "Terminé" sans avoir :**
- ✅ Vérifié la checklist pré-finition
- ✅ Mis à jour TOUS les fichiers de documentation
- ✅ Affiché le récapitulatif complet

---

## 🔄 8. RÉSUMÉ RAPIDE (ANTISÈCHE)

### 🚨 Les 3 règles d'or

1. **🇫🇷 FRANÇAIS** : Toujours communiquer en français
2. **📚 DOCUMENTATION** : Mettre à jour INDEX, README, CURRENT_STATE après CHAQUE changement
3. **🎓 PÉDAGOGIE** : Expliquer clairement, surtout pour Unity/C# (je ne connais pas)

### ✅ Checklist ultra-rapide avant "Terminé"

```
□ Ai-je créé des fichiers ? → MAJ INDEX.md
□ Ai-je résolu un problème ? → MAJ session 
□ Ai-je modifié l'archi ? → MAJ README.md racine + docs/README.md
□ Tests passent ? → pytest OK
□ Erreurs vérifiées ? → Python + Unity OK
□ Récapitulatif affiché ? → Template de réponse complet
```

### 🎯 Objectifs du projet (rappel)

- ✅ **Phase 1 (MVP)** : Avatar VRM affiché (TERMINÉ)
- 🚧 **Phase 2** : Expressions faciales (blendshapes)
- 🔜 **Phase 3** : Audio & lip-sync
- 🔜 **Phase 4** : IA conversationnelle + mouvement libre

### 📚 Structure de documentation

```
docs/
├── INDEX.md              ← Arborescence complète
├── README.md             ← Doc principale
├── CURRENT_STATE.md      ← État actuel
└── session_N_nom/
    └── *.md              ← Guides spécifiques
```

### 🔗 Fichiers système à connaître

- `docs/DOCUMENTATION_CHECKLIST.md` → Checklists détaillées
- `docs/AI_DOCUMENTATION_PROMPT.md` → Instructions IA
- `docs/.github/PULL_REQUEST_TEMPLATE.md` → Template PR

### 📂 RÈGLE SPÉCIALE : Dossier `scripts/` dans les sessions

**🚨 RÈGLE OBLIGATOIRE :**

Chaque fois que tu **crées ou modifies** un fichier de code (`.cs`, `.py`, `.js`, etc.) dans le cadre d'une session :

1. ✅ **CRÉER** le dossier `docs/session_N/scripts/` si absent
2. ✅ **COPIER** les versions **finales** des scripts dans ce dossier
3. ✅ **INCLURE** tous les fichiers créés/modifiés (Unity C#, Python, etc.)
4. ✅ **VÉRIFIER** que TOUS les fichiers sont bien copiés

**⚠️ ATTENTION : RÈGLE CRITIQUE**
- Cette règle a été **oubliée** dans le passé
- L'utilisateur a dû la rappeler explicitement
- **NE PLUS JAMAIS oublier** de créer le dossier `scripts/`
- **TOUJOURS vérifier** avant de dire "Terminé"

**Pourquoi ?**
- Archive des versions de code par session
- Permet de retrouver facilement l'état du code à chaque étape
- Facilite le suivi de l'évolution du projet
- **CRITIQUE** pour la traçabilité du projet

**Exemple :**
```
docs/sessions/session_7_animations/
├── README.md
├── TRANSITIONS_GUIDE.md
└── scripts/              ← OBLIGATOIRE !
    ├── VRMBlendshapeController.cs  ← Version finale
    ├── PythonBridge.cs             ← Version finale
    ├── app.py                       ← Version finale
    ├── unity_bridge.py             ← Version finale
    └── config.py                    ← Version finale
```

**🚨 SI TU OUBLIES :**
L'utilisateur va devoir te le rappeler → **ÉCHEC**  
**Ce dossier est aussi important que la documentation elle-même !**

---

## 💡 9. NOTES FINALES

### Ce que tu dois retenir

**Pour moi (l'utilisateur) :**
- Je ne suis **pas** un expert en développement
- Je ne connais **pas** Unity ni C#
- La documentation est **très importante** pour moi
- J'ai besoin d'**explications claires** et de **guidance**

**Pour toi (l'IA) :**
- **JAMAIS** oublier de mettre à jour la documentation
- **TOUJOURS** expliquer clairement les concepts Unity/C#
- **TOUJOURS** demander confirmation avant les changements majeurs
- **TOUJOURS** afficher le récapitulatif en fin de tâche

### En cas de doute

**Pose-toi ces questions :**
1. Ai-je bien compris ce que l'utilisateur veut ?
2. Ai-je expliqué clairement ma solution ?
3. Ai-je mis à jour TOUTE la documentation ?
4. Ai-je testé que ça fonctionne ?
5. Ai-je affiché le récapitulatif complet ?

**Si la réponse est "non" à l'une de ces questions → NE DIS PAS "Terminé" !**

---

**🎭 Bon développement sur Desktop-Mate ! 🚀**




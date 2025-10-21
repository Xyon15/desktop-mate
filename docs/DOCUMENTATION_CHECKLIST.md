# 📋 CHECKLIST DOCUMENTATION - À SUIVRE SYSTÉMATIQUEMENT

**⚠️ RÈGLE D'OR : Toujours mettre à jour la documentation AVANT de terminer une session !**

---

## ✅ Checklist Obligatoire pour CHAQUE Modification

### 1️⃣ **Après Création de Fichiers/Dossiers**

- [ ] Mettre à jour `docs/INDEX.md` avec la nouvelle arborescence
- [ ] Mettre à jour `docs/README.md` avec la nouvelle section
- [ ] Mettre à jour le README du dossier parent si applicable
- [ ] Vérifier que `docs/START_HERE.md` pointe vers les nouveaux contenus

### 2️⃣ **Après Modification de Code Important**

- [ ] Créer/Mettre à jour le fichier de session correspondant
- [ ] Documenter dans `docs/session_X/README.md`
- [ ] Mettre à jour `docs/CURRENT_STATE.md` avec le nouvel état
- [ ] Mettre à jour `README.md` principal si architecture changée

### 3️⃣ **Après Résolution de Problème**

- [ ] Créer fichier `DEBUG_*.md` ou `FIX_*.md` dans session
- [ ] Ajouter dans `docs/INDEX.md` section "Par problème"
- [ ] Référencer dans README de la session
- [ ] Mettre à jour les "Leçons apprises" dans CURRENT_STATE.md

### 4️⃣ **Après Complétion de Session**

- [ ] Créer `SUCCESS_*.md` ou récapitulatif session
- [ ] Mettre à jour tableau de progression dans `docs/INDEX.md`
- [ ] Mettre à jour `docs/README.md` section "État actuel"
- [ ] Mettre à jour `docs/CURRENT_STATE.md` complètement
- [ ] Mettre à jour `README.md` principal (roadmap, changelog)

### 5️⃣ **Avant Transition de Chat**

- [ ] Créer dossier `chat_X_nom_sessions_Y_to_Z/`
- [ ] Copier/Créer `CURRENT_STATE.md` dans le dossier
- [ ] Créer `prompt_chatX_vers_chatY.txt`
- [ ] Créer `CHAT_SUMMARY.md` avec résumé complet
- [ ] Mettre à jour `docs/chat_transitions/README.md`
- [ ] Mettre à jour `docs/README.md` (section chat_transitions)
- [ ] Mettre à jour `docs/INDEX.md` (arborescence + progression)
- [ ] Vérifier que tous les liens fonctionnent

---

## 🎯 Fichiers à TOUJOURS Vérifier

### Documentation Principale (Mise à jour quasi-systématique)

1. **`docs/INDEX.md`** 📑
   - Arborescence complète
   - Tableaux de progression
   - Liens de navigation rapide

2. **`docs/README.md`** 📖
   - Structure des dossiers
   - État actuel du projet
   - Guide d'utilisation

3. **`docs/CURRENT_STATE.md`** 📍
   - Ce qui est terminé
   - État technique
   - Prochaines étapes
   - Problèmes résolus

4. **`README.md` (racine)** 📄
   - Vue d'ensemble projet
   - Installation
   - Roadmap
   - Documentation (liens)
   - Changelog

### Documentation Spécifique (Selon contexte)

5. **`docs/START_HERE.md`** 🚪
   - Point d'entrée cohérent

6. **`docs/session_X/README.md`** 📁
   - Vue d'ensemble de la session

7. **`docs/chat_transitions/README.md`** 🔄
   - Historique des chats

---

## 🤖 Prompt d'Auto-Vérification (Pour l'IA)

**Avant de dire "Terminé", l'IA DOIT se poser ces questions :**

```
✓ Ai-je créé de nouveaux fichiers/dossiers ?
  → OUI : Mettre à jour INDEX.md et README.md

✓ Ai-je résolu un problème ?
  → OUI : Créer fichier DEBUG/FIX + mettre à jour INDEX

✓ Ai-je complété une session ?
  → OUI : Mettre à jour tableau progression + CURRENT_STATE

✓ Sommes-nous en fin de chat ?
  → OUI : Créer dossier transition + mettre à jour 3 fichiers principaux

✓ Ai-je modifié l'architecture ?
  → OUI : Mettre à jour README.md principal + architecture.md

✓ Ai-je ajouté une fonctionnalité ?
  → OUI : Mettre à jour roadmap + changelog
```

---

## 📝 Template de Commit (Inclut documentation)

```bash
# Mauvais commit (oublie la doc)
git commit -m "feat: Add blendshapes controller"

# Bon commit (inclut la doc)
git commit -m "feat: Add blendshapes controller + Update docs (INDEX, README, CURRENT_STATE)"
```

**Règle :** Si commit de code → commit de doc dans le même commit !

---

## 🚨 Indicateurs d'Oubli (Red Flags)

**Si l'utilisateur dit :**
- "as tu mis a jour les readme ?" ❌
- "n'oublie pas la documentation" ❌
- "vérifie que tout est à jour" ❌

**→ C'est que l'IA a RATÉ sa mise à jour automatique !**

**Objectif :** L'utilisateur ne devrait JAMAIS avoir à demander !

---

## ✅ Ordre de Mise à Jour Recommandé

```
1. Faire la modification (code, fichier, etc.)
2. Documenter dans la session (session_X/...)
3. ⬇️ PUIS IMMÉDIATEMENT :
   a. Mettre à jour docs/INDEX.md
   b. Mettre à jour docs/README.md
   c. Mettre à jour docs/CURRENT_STATE.md
   d. Mettre à jour README.md principal si nécessaire
4. Vérifier les liens entre fichiers
5. Créer récapitulatif visuel pour l'utilisateur
```

---

## 🎓 Exemple Parfait de Session Documentée

### Scénario : Création de VRMBlendshapeController.cs

**Étape 1 - Code :** Créer le fichier C#

**Étape 2 - Session :** Créer `docs/sessions/session_6_expressions/`
- `README.md`
- `BLENDSHAPES_GUIDE.md`
- `scripts/VRMBlendshapeController_CLEAN.cs`

**Étape 3 - Mise à jour INDEX.md :**
```markdown
├── 📁 docs/sessions/session_6_expressions/  ← Session 6 : Expressions ✅
│   ├── README.md
│   ├── BLENDSHAPES_GUIDE.md
│   └── scripts/VRMBlendshapeController_CLEAN.cs
```

**Étape 4 - Mise à jour README.md (docs) :**
```markdown
### 📂 docs/sessions/session_6_expressions/
**Contrôle des expressions faciales VRM**
- Réalisations :
  - ✅ VRMBlendshapeController.cs créé
  - ✅ Commande IPC set_blendshape
  - ✅ Boutons émotions GUI Python
```

**Étape 5 - Mise à jour CURRENT_STATE.md :**
```markdown
6. **Session 6 - Expressions Faciales** ✅
   - `VRMBlendshapeController.cs` avec contrôle blendshapes
   - Documentation : `docs/sessions/session_6_expressions/`
```

**Étape 6 - Mise à jour README.md principal :**
```markdown
### Phase 2 : Interactions Avancées 😊 (En cours)
- [x] **Session 6** : Expressions faciales (blendshapes) ✅
```

**Étape 7 - Confirmation visuelle :**
```
✅ VRMBlendshapeController.cs créé
✅ Documentation session 6 créée
✅ INDEX.md mis à jour
✅ README.md (docs) mis à jour
✅ CURRENT_STATE.md mis à jour
✅ README.md (racine) mis à jour
```

---

## 💡 Solutions pour Ne Plus Oublier

### Solution 1 : Checklist Systématique dans Chaque Réponse

L'IA doit mentionner :
```
📝 Documentation mise à jour :
✅ docs/INDEX.md
✅ docs/README.md
✅ docs/CURRENT_STATE.md
✅ README.md (racine)
```

### Solution 2 : Créer un Script de Vérification

```powershell
# verify-docs.ps1
# À exécuter avant chaque commit

Write-Host "Vérification documentation..." -ForegroundColor Yellow

$files = @(
    "docs/INDEX.md",
    "docs/README.md", 
    "docs/CURRENT_STATE.md",
    "README.md"
)

foreach ($file in $files) {
    $lastModified = (Get-Item $file).LastWriteTime
    if ($lastModified -lt (Get-Date).AddHours(-1)) {
        Write-Host "⚠️ $file pas modifié récemment !" -ForegroundColor Red
    } else {
        Write-Host "✅ $file à jour" -ForegroundColor Green
    }
}
```

### Solution 3 : Template de Réponse IA

Chaque réponse de l'IA doit terminer par :
```
🎯 Tâche terminée
📝 Documentation :
   [x] INDEX.md
   [x] README.md
   [x] CURRENT_STATE.md
   [x] README.md principal
   [x] README session
```

---

## 🎯 Engagement de l'IA

**L'IA s'engage à :**

1. ✅ **TOUJOURS** vérifier ces 4 fichiers avant de dire "Terminé"
2. ✅ **TOUJOURS** montrer explicitement quels fichiers ont été mis à jour
3. ✅ **TOUJOURS** créer un récapitulatif visuel des mises à jour
4. ✅ **JAMAIS** attendre que l'utilisateur demande la mise à jour
5. ✅ **TOUJOURS** inclure la doc dans le même flux de travail que le code

---

## 📊 Métriques de Qualité

**Session parfaitement documentée :**
- ✅ 0 question de l'utilisateur sur la doc
- ✅ Tous les README à jour
- ✅ INDEX.md reflète la structure réelle
- ✅ CURRENT_STATE.md synchronisé avec le code
- ✅ Liens fonctionnels entre tous les fichiers

**Session mal documentée :**
- ❌ Utilisateur demande "as tu mis à jour..."
- ❌ INDEX.md incomplet
- ❌ README.md obsolète
- ❌ CURRENT_STATE.md pas synchronisé

---

## 🔄 Cycle de Documentation Parfait

```
Création/Modification
         ↓
   Documentation Session
         ↓
   Mise à jour INDEX.md ──────┐
         ↓                     │
   Mise à jour README.md ──────┤
         ↓                     │ AUTOMATIQUE
   Mise à jour CURRENT_STATE ─┤ IMMÉDIAT
         ↓                     │ SYSTÉMATIQUE
   Mise à jour README racine ─┘
         ↓
   Récapitulatif visuel
         ↓
   Commit (code + doc ensemble)
```

---

**📌 CE FICHIER DOIT ÊTRE CONSULTÉ AVANT CHAQUE FIN DE TÂCHE !**

**🎯 Objectif : L'utilisateur ne doit JAMAIS avoir à demander si la doc est à jour !**

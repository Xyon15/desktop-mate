# 🤖 PROMPT SYSTÈME POUR L'IA - DOCUMENTATION

**À inclure dans CHAQUE nouveau chat pour garantir la documentation !**

---

## 📋 Instructions Système Documentation

```
RÈGLE ABSOLUE DE DOCUMENTATION :

Chaque fois que tu crées, modifies ou termines quelque chose, tu DOIS :

1. ✅ Documenter dans la session appropriée (docs/session_X/)
2. ✅ Mettre à jour docs/INDEX.md (arborescence + tableaux)
3. ✅ Mettre à jour docs/README.md (sections + état)
4. ✅ Mettre à jour docs/CURRENT_STATE.md (état technique)
5. ✅ Mettre à jour README.md racine si nécessaire
6. ✅ Afficher un récapitulatif visuel des mises à jour

AVANT de dire "Terminé" ou "C'est fait", vérifie :
- [ ] Ai-je créé de nouveaux fichiers ? → MAJ INDEX.md + README.md
- [ ] Ai-je résolu un problème ? → Créer DEBUG/FIX.md
- [ ] Ai-je complété une session ? → MAJ progression + CURRENT_STATE
- [ ] Est-ce une fin de chat ? → Créer transition complète
- [ ] Ai-je modifié l'architecture ? → MAJ README.md principal

NE JAMAIS attendre que l'utilisateur demande "as tu mis à jour...?"

La documentation est AUSSI importante que le code !
```

---

## 🎯 Template de Fin de Tâche

À TOUJOURS inclure à la fin de chaque réponse :

```markdown
## 📝 Documentation Mise à Jour

✅ Fichiers mis à jour :
- [ ] `docs/INDEX.md` - [Description du changement]
- [ ] `docs/README.md` - [Description du changement]
- [ ] `docs/CURRENT_STATE.md` - [Description du changement]
- [ ] `README.md` (racine) - [Description du changement]
- [ ] `docs/session_X/README.md` - [Si applicable]

🎯 Navigation :
- Arborescence à jour dans INDEX.md
- État actuel synchronisé dans CURRENT_STATE.md
- Guides d'utilisation à jour
```

---

## ⚠️ Red Flags à Éviter

Si l'utilisateur dit :
- ❌ "as tu mis a jour les readme ?"
- ❌ "n'oublie pas la documentation"
- ❌ "vérifie l'INDEX"

→ **L'IA a ÉCHOUÉ dans sa mission de documentation !**

---

## ✅ Checklist Rapide par Type de Tâche

### Création de Fichier/Dossier
```
✓ Documenter dans session_X/
✓ MAJ docs/INDEX.md (arborescence)
✓ MAJ docs/README.md (nouvelle section)
✓ Afficher récapitulatif
```

### Résolution de Problème
```
✓ Créer DEBUG_*.md ou FIX_*.md
✓ MAJ docs/INDEX.md (section problèmes)
✓ MAJ docs/CURRENT_STATE.md (problèmes résolus)
✓ Référencer dans session README
```

### Complétion de Session
```
✓ Créer SUCCESS_*.md
✓ MAJ docs/INDEX.md (tableau progression ✅)
✓ MAJ docs/README.md (état actuel)
✓ MAJ docs/CURRENT_STATE.md (session complète)
✓ MAJ README.md racine (roadmap)
```

### Transition de Chat
```
✓ Créer dossier chat_X_nom_sessions_Y_to_Z/
✓ Copier CURRENT_STATE.md
✓ Créer prompt_chatX_vers_chatY.txt
✓ Créer CHAT_SUMMARY.md
✓ MAJ docs/chat_transitions/README.md
✓ MAJ docs/README.md (section transitions)
✓ MAJ docs/INDEX.md (arborescence + progression)
✓ Vérifier tous les liens
```

---

**📌 Ce prompt doit être lu au début de chaque nouveau chat !**

**🎯 Objectif : 0 question de l'utilisateur sur l'état de la documentation**

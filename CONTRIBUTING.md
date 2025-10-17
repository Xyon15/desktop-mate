# Guide de Contribution

Merci de votre intérêt pour contribuer à Desktop-Mate ! 🎉

## Comment Contribuer

### 1. Fork & Clone

```powershell
# Fork le repo sur GitHub, puis :
git clone https://github.com/VOTRE_USERNAME/desktop-mate.git
cd desktop-mate
```

### 2. Configurer l'environnement

```powershell
# Créer et activer le venv
python -m venv venv
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Créer une branche

```powershell
git checkout -b feature/ma-super-fonctionnalite
# ou
git checkout -b fix/correction-bug
```

### 4. Développer

- Écrivez du code propre et bien documenté
- Ajoutez des tests pour vos nouvelles fonctionnalités
- Suivez les conventions de code (PEP 8)
- Utilisez les docstrings pour documenter vos fonctions

### 5. Tester

```powershell
# Lancer les tests
pytest tests/ -v

# Vérifier le formatage
black src/ tests/

# Vérifier le linting
flake8 src/ tests/
```

### 6. Commit

Utilisez les [Conventional Commits](https://www.conventionalcommits.org/) :

```
feat: ajout du support des blendshapes custom
fix: correction crash au chargement VRM
docs: mise à jour du README
style: formatage du code
refactor: restructuration du module audio
test: ajout tests pour unity_bridge
chore: mise à jour des dépendances
```

### 7. Push & Pull Request

```powershell
git push origin feature/ma-super-fonctionnalite
```

Puis ouvrez une Pull Request sur GitHub avec :
- Une description claire des changements
- Des captures d'écran si pertinent
- La référence aux issues résolues (#123)

## Standards de Code

### Python
- **PEP 8** pour le style
- **Type hints** pour les fonctions publiques
- **Docstrings** au format Google ou NumPy
- **Tests** avec pytest

### Unity (C#)
- Conventions Unity/C# standards
- Commentaires XML pour les API publiques
- Noms explicites pour variables et méthodes

## Structure des Commits

Exemple de bon commit :

```
feat(audio): add microphone input capture

- Implement sounddevice integration
- Add VU meter widget
- Add audio device selection
- Add tests for audio module

Closes #12
```

## Questions ?

N'hésitez pas à :
- Ouvrir une [issue](https://github.com/Xyon15/desktop-mate/issues)
- Poser vos questions dans les discussions
- Contacter les mainteneurs

Merci ! 🙏

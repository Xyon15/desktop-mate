# Session 9 : Mouvements de Tête Subtils 🎭

**Date :** 21 octobre 2025  
**Status :** 🚧 **EN COURS DE PLANIFICATION**  
**Difficulté :** 🔴 Faible  
**Impact :** 🎯🎯 Moyen  
**Durée estimée :** 1/2 session  

---

## 📋 Vue d'ensemble

Ajouter des **mouvements de tête subtils** à l'avatar pour le rendre plus vivant et réaliste, même au repos. Cette session se concentre sur des animations procédurales simples mais efficaces qui donneront l'impression que l'avatar "respire" et "pense".

### 🎯 Objectifs

1. **Head Bobbing** : Mouvement léger gauche/droite
2. **Head Tilt** : Inclinaison subtile
3. **Respiration** : Mouvement du torse (bonus si facile)
4. **Paramètres configurables** : Amplitude, fréquence, activation

---

## 🎭 Pourquoi cette session maintenant ?

### ✅ Avantages

- **Facile à implémenter** : Similaire au système de clignement (Session 8)
- **Gros impact visuel** : Ajoute beaucoup de réalisme avec peu d'effort
- **Avatar vivant** : Rend l'avatar dynamique même au repos
- **Réutilisation de code** : Pattern coroutines + SmoothStep déjà maîtrisé
- **Complémentaire** : Fonctionne parfaitement avec le clignement automatique

### 📊 Priorisation

**Option B choisie** plutôt que :
- ❌ Option A (Audio & Lip-sync) : Complexe, nécessite analyse FFT
- ❌ Option C (Eye Tracking) : Nécessite MediaPipe/webcam

**Raisons :**
- Session courte (1/2 session) → progression rapide
- Réutilisation architecture Session 8 → moins de risques
- Impact visuel immédiat → satisfaction rapide
- Préparation pour Session 10 (Audio) → avatar déjà "vivant"

---

## 🏗️ Architecture Technique

### Composants à créer

#### 1. **VRMHeadMovementController.cs** (Unity)

**Responsabilités :**
- Gérer les mouvements de tête procéduraux
- Rotation subtile du GameObject Head (pitch/yaw)
- Animation via coroutines + SmoothStep
- Paramètres configurables

**Pattern réutilisé :**
```csharp
// Similaire à VRMAutoBlinkController.cs
public class VRMHeadMovementController : MonoBehaviour
{
    // Paramètres
    public bool autoHeadMovement = true;
    public float minInterval = 3.0f;  // 3-7s entre mouvements
    public float maxInterval = 7.0f;
    public float movementDuration = 2.0f;  // 2s par mouvement
    public float maxRotationAngle = 5.0f;  // ±5° max
    
    // Références
    private GameObject headBone;
    private Quaternion initialRotation;
    
    // Coroutine
    private IEnumerator HeadMovementLoop()
    {
        while (autoHeadMovement)
        {
            yield return new WaitForSeconds(Random.Range(minInterval, maxInterval));
            yield return StartCoroutine(PerformHeadMovement());
        }
    }
    
    private IEnumerator PerformHeadMovement()
    {
        // Choisir direction aléatoire (gauche/droite, haut/bas)
        float targetYaw = Random.Range(-maxRotationAngle, maxRotationAngle);
        float targetPitch = Random.Range(-maxRotationAngle/2, maxRotationAngle/2);
        
        // Animation SmoothStep (similaire au clignement)
        // Phase 1 : Rotation (50% du temps)
        // Phase 2 : Retour (50% du temps)
    }
}
```

#### 2. **PythonBridge.cs** (Unity - Mise à jour)

**Nouvelle commande IPC :**
```json
{
  "command": "set_auto_head_movement",
  "data": {
    "enabled": true,
    "min_interval": 3.0,
    "max_interval": 7.0,
    "max_angle": 5.0
  }
}
```

#### 3. **app.py** (Python - Interface GUI)

**Ajouts dans l'onglet "Options" :**
- ☑️ Checkbox "Auto Head Movement"
- 🎚️ Slider "Movement Frequency" (3-10s)
- 🎚️ Slider "Movement Amplitude" (2-10°)

#### 4. **config.py** (Python - Configuration)

**Nouvelles clés :**
```python
DEFAULT_CONFIG = {
    # ... existing config ...
    "auto_head_movement": True,
    "head_movement_min_interval": 3.0,
    "head_movement_max_interval": 7.0,
    "head_movement_max_angle": 5.0
}
```

---

## 🎯 Fonctionnalités Principales

### 1. **Head Bobbing** (Mouvement gauche/droite)

**Rotation Yaw (axe Y) :**
- Angle : ±5° maximum
- Durée : 2s par mouvement (1s rotation + 1s retour)
- Fréquence : Toutes les 3-7 secondes
- Animation : SmoothStep pour fluidité

**Comportement :**
```
Repos → Gauche 3° → Repos → Droite 4° → Repos → ...
  0s      1s        2s      4s        5s      7s
```

### 2. **Head Tilt** (Inclinaison haut/bas)

**Rotation Pitch (axe X) :**
- Angle : ±2.5° maximum (plus subtil)
- Combiné avec le Yaw (mouvement diagonal)
- Même timing que le bobbing

**Exemple :**
```
Direction aléatoire :
- Gauche-Haut : (Yaw: -3°, Pitch: +2°)
- Droite-Bas : (Yaw: +4°, Pitch: -1.5°)
```

### 3. **Respiration** (Bonus - si temps)

**Scale du torse :**
- Amplitude : ±1% sur l'axe Y
- Cycle : 3-5 secondes (respiration lente)
- Indépendant des mouvements de tête

---

## 🔧 Implémentation Technique

### Étape 1 : Trouver le Head Bone

```csharp
void Start()
{
    // Recherche récursive du bone "Head"
    headBone = FindChildRecursive(transform, "Head");
    if (headBone != null)
    {
        initialRotation = headBone.transform.localRotation;
        StartCoroutine(HeadMovementLoop());
    }
}

GameObject FindChildRecursive(Transform parent, string name)
{
    if (parent.name.Contains(name))
        return parent.gameObject;
    
    foreach (Transform child in parent)
    {
        var result = FindChildRecursive(child, name);
        if (result != null) return result;
    }
    return null;
}
```

### Étape 2 : Animation SmoothStep

```csharp
private IEnumerator PerformHeadMovement()
{
    // Direction aléatoire
    float targetYaw = Random.Range(-maxRotationAngle, maxRotationAngle);
    float targetPitch = Random.Range(-maxRotationAngle/2, maxRotationAngle/2);
    
    Quaternion targetRotation = initialRotation * 
        Quaternion.Euler(targetPitch, targetYaw, 0);
    
    // Phase 1 : Rotation vers la cible (50% du temps)
    float halfDuration = movementDuration / 2f;
    float elapsed = 0f;
    
    while (elapsed < halfDuration)
    {
        elapsed += Time.deltaTime;
        float t = Mathf.Clamp01(elapsed / halfDuration);
        float smoothT = SmoothStep(t);
        
        headBone.transform.localRotation = Quaternion.Slerp(
            initialRotation, 
            targetRotation, 
            smoothT
        );
        
        yield return null;
    }
    
    // Phase 2 : Retour à la position initiale (50% du temps)
    elapsed = 0f;
    while (elapsed < halfDuration)
    {
        elapsed += Time.deltaTime;
        float t = Mathf.Clamp01(elapsed / halfDuration);
        float smoothT = SmoothStep(t);
        
        headBone.transform.localRotation = Quaternion.Slerp(
            targetRotation,
            initialRotation,
            smoothT
        );
        
        yield return null;
    }
    
    // Assurer le retour exact
    headBone.transform.localRotation = initialRotation;
}

// Fonction SmoothStep (réutilisée de Session 8)
float SmoothStep(float t)
{
    return t * t * (3f - 2f * t);
}
```

### Étape 3 : Interface Python

```python
# app.py - Onglet Options
class OptionsTab(QWidget):
    def setup_head_movement_section(self):
        # Checkbox Auto Head Movement
        self.auto_head_checkbox = QCheckBox("Mouvements de Tête Automatiques")
        self.auto_head_checkbox.setChecked(
            self.config.get("auto_head_movement", True)
        )
        self.auto_head_checkbox.stateChanged.connect(
            self.on_auto_head_changed
        )
        
        # Slider Fréquence
        self.head_freq_slider = QSlider(Qt.Horizontal)
        self.head_freq_slider.setRange(30, 100)  # 3.0-10.0s
        self.head_freq_slider.setValue(
            int(self.config.get("head_movement_max_interval", 7.0) * 10)
        )
        
        # Slider Amplitude
        self.head_amp_slider = QSlider(Qt.Horizontal)
        self.head_amp_slider.setRange(20, 100)  # 2.0-10.0°
        self.head_amp_slider.setValue(
            int(self.config.get("head_movement_max_angle", 5.0) * 10)
        )
    
    def on_auto_head_changed(self, state):
        enabled = state == Qt.Checked
        self.config.set("auto_head_movement", enabled)
        
        # Envoyer commande à Unity
        if self.unity_bridge.is_connected():
            self.unity_bridge.send_command("set_auto_head_movement", {
                "enabled": enabled,
                "max_interval": self.head_freq_slider.value() / 10.0,
                "max_angle": self.head_amp_slider.value() / 10.0
            })
```

---

## ✅ Checklist d'Implémentation

### Phase 1 : Unity (1-2h)
- [ ] Créer `VRMHeadMovementController.cs`
- [ ] Implémenter recherche du Head bone
- [ ] Implémenter coroutine `HeadMovementLoop()`
- [ ] Implémenter animation SmoothStep
- [ ] Ajouter paramètres configurables (Inspector)
- [ ] Tester avec différents modèles VRM

### Phase 2 : IPC (30min)
- [ ] Ajouter commande `set_auto_head_movement` dans `PythonBridge.cs`
- [ ] Implémenter handler avec thread-safety (Queue<Action>)
- [ ] Tester communication Python → Unity

### Phase 3 : Interface Python (1h)
- [ ] Ajouter section "Mouvements de Tête" dans onglet Options
- [ ] Créer checkbox "Auto Head Movement"
- [ ] Créer sliders Fréquence et Amplitude
- [ ] Connecter signaux Qt
- [ ] Implémenter sauvegarde configuration

### Phase 4 : Tests & Debug (30min)
- [ ] Tester activation/désactivation
- [ ] Tester réglages fréquence
- [ ] Tester réglages amplitude
- [ ] Vérifier thread-safety Unity
- [ ] Tester avec clignement automatique activé (interaction)

### Phase 5 : Documentation (1h)
- [ ] Créer `HEAD_MOVEMENT_GUIDE.md`
- [ ] Documenter architecture
- [ ] Documenter problèmes rencontrés
- [ ] Mettre à jour `README.md`
- [ ] Mettre à jour `INDEX.md`
- [ ] Copier scripts finaux dans `scripts/`

---

## 🎯 Résultats Attendus

### Visuel
- ✅ Avatar qui bouge légèrement la tête toutes les 3-7 secondes
- ✅ Mouvements fluides et naturels (SmoothStep)
- ✅ Direction aléatoire (gauche/droite, haut/bas)
- ✅ Retour à la position initiale en douceur

### Interface
- ✅ Checkbox "Auto Head Movement" fonctionnelle
- ✅ Sliders de configuration réactifs
- ✅ Configuration sauvegardée dans `config.json`

### Technique
- ✅ Thread-safety Unity (Queue<Action> pattern)
- ✅ Performance optimale (coroutines)
- ✅ Code réutilisable et extensible
- ✅ Compatible avec clignement automatique

---

## 🚨 Pièges à Éviter

### 1. **Nom du Head Bone**
**Problème :** Différents modèles VRM utilisent différents noms
**Solution :** Recherche récursive avec `.Contains("Head")` ou `.Contains("head")`

### 2. **Rotation Globale vs Locale**
**Problème :** Utiliser `transform.rotation` au lieu de `localRotation`
**Solution :** Toujours utiliser `localRotation` pour les bones

### 3. **Accumulation de Rotation**
**Problème :** Ne pas revenir exactement à `initialRotation`
**Solution :** Forcer `headBone.transform.localRotation = initialRotation;` à la fin

### 4. **Conflit avec Expressions**
**Problème :** Les expressions peuvent affecter la position de la tête
**Solution :** Vérifier que les blendshapes n'incluent pas de rotation de tête

### 5. **Timing Trop Rapide**
**Problème :** Mouvements trop fréquents = avatar agité
**Solution :** Intervalle minimum 3s, par défaut 5-7s

---

## 📚 Ressources Techniques

### Courbes SmoothStep
```
f(t) = t² × (3 - 2t)

Propriétés :
- f(0) = 0
- f(1) = 1
- f'(0) = 0  (dérivée nulle au début)
- f'(1) = 0  (dérivée nulle à la fin)
→ Accélération/décélération douce
```

### Quaternions Unity
```csharp
// Slerp = Interpolation sphérique (meilleure pour rotations)
Quaternion.Slerp(from, to, t);

// Euler = Créer rotation depuis angles
Quaternion.Euler(pitch, yaw, roll);

// Multiplication = Combiner rotations
initialRotation * Quaternion.Euler(x, y, 0);
```

### Coroutines Unity
```csharp
// Démarrer
StartCoroutine(MyCoroutine());

// Arrêter toutes
StopAllCoroutines();

// Wait
yield return new WaitForSeconds(delay);
yield return null;  // 1 frame
```

---

## 🔄 Évolutions Futures (Post-Session 9)

### Session 10+ (Optionnel)
- **Respiration** : Scale du torse (cycle 3-5s)
- **Eye Dart** : Petits mouvements oculaires rapides
- **Micro-expressions** : Changements subtils de blendshapes
- **Idle Animations** : Combinaisons complexes (tête + yeux + expressions)

### Intégration IA (Session 12+)
- **Head Tracking** : Suivre la conversation (regard vers l'utilisateur)
- **Nod/Shake** : Hochement de tête (oui/non) basé sur IA
- **Emotion-driven** : Mouvements influencés par l'émotion (triste = tête baissée)

---

## 📊 Estimation Temps

| Tâche | Temps estimé |
|-------|--------------|
| VRMHeadMovementController.cs | 1-2h |
| Commande IPC | 30min |
| Interface Python | 1h |
| Tests & Debug | 30min |
| Documentation | 1h |
| **TOTAL** | **4-5h** |

---

## 🎉 Définition de "Terminé"

La Session 9 sera considérée comme **terminée** quand :

1. ✅ Avatar bouge la tête naturellement toutes les 3-7 secondes
2. ✅ Checkbox "Auto Head Movement" fonctionne dans l'interface
3. ✅ Sliders de configuration fonctionnels et sauvegardés
4. ✅ Aucun conflit avec le clignement automatique
5. ✅ Code thread-safe et performant
6. ✅ Documentation complète créée (`HEAD_MOVEMENT_GUIDE.md`)
7. ✅ Scripts copiés dans `docs/sessions/session_9_head_movements/scripts/`
8. ✅ `README.md`, `INDEX.md`, `docs/README.md` mis à jour

---

**🚀 Prêt pour l'implémentation ! Session courte et efficace !** ✨🎭

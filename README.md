# Projet : Traitement d'Images avec Python

Ce projet permet de manipuler des images avec différentes transformations telles que la conversion en noir et blanc, l'application d'un flou, l'ajout de texte, la rotation, et le redimensionnement.
Il utilise les bibliothèques **Pillow**, **OpenCV**, et **NumPy**.

## Fonctionnalités

1. **Conversion en Noir et Blanc**  
   Convertit une image en niveaux de gris et la sauvegarde dans un dossier de sortie.

2. **Application d'un Flou Gaussien**  
   Ajoute un effet de flou gaussien à une image.

3. **Rotation d'Images**  
   Pivote une image d'un angle donné et la sauvegarde.

4. **Ajout de Texte**  
   Ajoute un texte noir à une image à une position spécifiée.

5. **Redimensionnement d'Image**  
   Redimensionne une image selon un facteur de mise à l’échelle.

6. **Application de Dilatation**  
   Applique une opération de dilatation à une image pour épaissir les contours.

## Prérequis

- Python 3.10 ou version ultérieure

### Bibliothèques nécessaires
Les bibliothèques suivantes doivent être installées :
- **Pillow** : Manipulation d'images
- **OpenCV** : Traitement avancé d'images
- **NumPy** : Calculs matriciels

## Utilisation

Les scripts sont conçus pour être appelés directement en Python. Voici comment utiliser les principales fonctions :

### Exemple : Conversion en Noir et Blanc
```python
from script import convertirNoirBlanc

chemin_image = "chemin/vers/votre/image.jpg"
convertirNoirBlanc(chemin_image)
```

### Exemple : Ajout de Texte
```python
from script import ajouter_texte

chemin_image = "chemin/vers/votre/image.jpg"
ajouter_texte(chemin_image, texte="Bonjour", position=(50, 50))
```

### Exemple : Redimensionnement
```python
from script import redimensionner_image_scaling

chemin_image = "chemin/vers/votre/image.jpg"
redimensionner_image_scaling(chemin_image, facteur_scaling=0.5)
```

## Organisation des Fichiers

- **`requirements.txt`** : Liste des dépendances Python.
- **`logger.log`** : Fichier généré pour enregistrer les logs des opérations effectuées.
- **`output/`** : Dossier généré automatiquement pour sauvegarder les résultats des traitements.

## Contributeurs
Ahmet Emre, Yanis, Mattéo


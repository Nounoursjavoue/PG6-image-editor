import os
from log import log
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime

# Vérifier et créer le répertoire de sortie
def verifier_repertoire_sortie():
    """
    Vérifie l'existence du répertoire de sortie et le crée si nécessaire.

    Returns:
        str: Le chemin absolu du répertoire de sortie.
    """
    output_dir = os.path.join(os.getcwd(), "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

# Image processing functions
def convertirNoirBlanc(chemin_image):
    """
    Convertit une image en niveaux de gris et la sauvegarde dans un sous-dossier.

    Args:
        chemin_image (str): Le chemin de l'image source.
    """
    try:
        # Obtenir le chemin de sortie pour l'image modifiée
        output_dir = verifier_repertoire_sortie()
        chemin_sortie = os.path.join(output_dir, os.path.basename(chemin_image))

        # Charger et convertir l'image
        image = Image.open(chemin_image)
        image_noir_blanc = image.convert("L")

        # Sauvegarder l'image convertie
        image_noir_blanc.save(chemin_sortie)
        log(f"Image convertie en noir et blanc : {chemin_sortie}")
        print(f"Image convertie en noir et blanc et sauvegardée sous : {chemin_sortie}")
    except Exception as e:
        # Gérer et enregistrer toute erreur rencontrée
        log(f"Erreur lors de la conversion en noir et blanc de {chemin_image} : {e}")
        print(f"Une erreur s'est produite : {e}")

def appliquerFlouPillow(chemin_image):
    """
    Applique un flou gaussien à une image et sauvegarde le résultat.

    Args:
        chemin_image (str): Le chemin de l'image source.
    """
    try:
        output_dir = verifier_repertoire_sortie()
        chemin_sortie = os.path.join(output_dir, os.path.basename(chemin_image))

        # Charger l'image et appliquer un flou gaussien
        image = Image.open(chemin_image).convert("RGB")
        image_floue = image.filter(ImageFilter.GaussianBlur(radius=5))

        # Sauvegarder l'image floutée
        image_floue.save(chemin_sortie)
        log(f"Flou appliqué à l'image : {chemin_sortie}")
        print(f"Flou appliqué et sauvegardé sous : {chemin_sortie}")
    except Exception as e:
        log(f"Erreur lors de l'application du flou à {chemin_image} : {e}")
        print(f"Une erreur s'est produite : {e}")

def pivoteImage(angle:int, chemin_image):
    """
    Pivote une image selon un angle donné et sauvegarde le résultat.

    Args:
        angle (float): L'angle en degrés pour pivoter l'image.
        chemin_image (str): Le chemin de l'image source.
    """
    try:
        output_dir = verifier_repertoire_sortie()
        chemin_sortie = os.path.join(output_dir, os.path.basename(chemin_image))

        # Charger l'image et la pivoter
        image = Image.open(chemin_image)
        image_pivotee = image.rotate(angle, expand=True)

        # Sauvegarder l'image pivotée
        image_pivotee.save(chemin_sortie)
        log(f"Image pivotée de {angle}° : {chemin_sortie}")
        print(f"Image pivotée de {angle}° et sauvegardée sous : {chemin_sortie}")
    except Exception as e:
        log(f"Erreur lors de la rotation de {chemin_image} : {e}")
        print(f"Une erreur s'est produite : {e}")

def appliquerDilatation(chemin_image, taille_kernel=(5, 5), iterations=1):
    """
    Applique une opération de dilatation sur une image.

    Args:
        chemin_image (str): Le chemin de l'image source.
        taille_kernel (tuple, optional): La taille du noyau pour la dilatation.
        iterations (int, optional): Le nombre d'itérations de la dilatation.
    """
    try:
        output_dir = verifier_repertoire_sortie()
        chemin_sortie = os.path.join(output_dir, os.path.basename(chemin_image))

        # Charger l'image en niveaux de gris et appliquer la dilatation
        image = cv2.imread(chemin_image, 0)
        kernel = np.ones(taille_kernel, np.uint8)
        image_dilatee = cv2.dilate(image, kernel, iterations=iterations)

        # Sauvegarder l'image dilatée
        cv2.imwrite(chemin_sortie, image_dilatee)
        log(f"Dilatation appliquée : {chemin_sortie}")
        print(f"Dilatation appliquée et sauvegardée sous : {chemin_sortie}")
    except Exception as e:
        log(f"Erreur lors de la dilatation de {chemin_image} : {e}")
        print(f"Une erreur s'est produite : {e}")
        
def redimensionnerImage(chemin_image, facteur):
    """
    Redimensionne une image selon un facteur de scaling donné.

    Args:
        chemin_image (str): Le chemin de l'image source.
        facteur_scaling (float): Le facteur de redimensionnement (>0).
            - Un facteur >1 agrandit l'image.
            - Un facteur <1 réduit l'image.
    """
    # si le facteur est negatif
    
    if facteur < 0:
        log(f"Erreur lors du redimensionnement de {chemin_image} car facteur negatif")
        print("Erreur lors du redimensionnement, facteur negatif")
        return
    
    try:
        output_dir = verifier_repertoire_sortie()
        chemin_sortie = os.path.join(output_dir, os.path.basename(chemin_image))

        # Charger l'image
        image = cv2.imread(chemin_image)
        if image is None:
            raise ValueError(f"Impossible de charger l'image depuis {chemin_image}")

        # Calculer les nouvelles dimensions
        hauteur, largeur = image.shape[:2]
        nouvelle_largeur = int(largeur * facteur)
        nouvelle_hauteur = int(hauteur * facteur)

        # Redimensionner l'image
        image_redimensionnee = cv2.resize(image, (nouvelle_largeur, nouvelle_hauteur))

        # Sauvegarder l'image redimensionnée
        cv2.imwrite(chemin_sortie, image_redimensionnee)
        log(f"Image redimensionnée avec un facteur de scaling {facteur} : {chemin_sortie}")
        print(f"Image redimensionnée et sauvegardée sous : {chemin_sortie}")
    except Exception as e:
        log(f"Erreur lors du redimensionnement de {chemin_image} avec facteur {facteur} : {e}")
        print(f"Une erreur s'est produite : {e}")


def ajouterTexte(chemin_image, texte, taille_police=1, epaisseur=1, couleur=(0, 0, 0)):
    """
    Ajoute un texte centré à une image et sauvegarde le résultat. Si le texte est trop long, lève une exception ValueError.

    Args:
        chemin_image (str): Le chemin de l'image source.
        texte (str): Le texte à ajouter sur l'image.
        taille_police (int, optional): La taille de la police du texte (OpenCV). 
        epaisseur (int, optional): L'épaisseur des lettres du texte. 
        couleur (tuple, optional): La couleur du texte en format RGB (par défaut noir). 
    """
    try:
        output_dir = verifier_repertoire_sortie()
        chemin_sortie = os.path.join(output_dir, os.path.basename(chemin_image))

        # Charger l'image
        image = cv2.imread(chemin_image)
        if image is None:
            raise ValueError(f"Impossible de charger l'image depuis {chemin_image}")

        # Récupérer les dimensions de l'image
        hauteur_image, largeur_image = image.shape[:2]

        # Calculer la taille du texte pour vérifier s'il ne dépasse pas la largeur de l'image
        (largeur_texte, hauteur_texte), _ = cv2.getTextSize(texte, cv2.FONT_HERSHEY_SIMPLEX, taille_police, epaisseur)
        
        # Vérifier si le texte est trop large pour l'image
        if largeur_texte > largeur_image:
            # Log l'erreur que le texte est trop large
            log(f"Erreur : Le texte '{texte}' est trop large pour l'image (largeur de texte : {largeur_texte}, largeur de l'image : {largeur_image}). Essayez de réduire la taille du texte.")
            raise ValueError(f"Le texte '{texte}' est trop large pour l'image. Essayez de réduire la taille du texte.")

        # Calculer la position pour centrer le texte
        position_x = (largeur_image - largeur_texte) // 2
        position_y = (hauteur_image + hauteur_texte) // 2
        
        # Ajouter le texte centré
        cv2.putText(image, texte, (position_x, position_y), cv2.FONT_HERSHEY_SIMPLEX, taille_police, couleur, epaisseur, lineType=cv2.LINE_AA)

        # Sauvegarder l'image avec texte
        cv2.imwrite(chemin_sortie, image)
        log(f"Texte ajouté et centré à l'image : {chemin_sortie}")
        print(f"Texte ajouté et centré, sauvegardé sous : {chemin_sortie}")
    
    except Exception as e:
        log(f"Erreur lors de l'ajout de texte à {chemin_image} : {e}")
        print(f"Une erreur s'est produite : {e}")

        

# Pour appliquer un filtre a plusieurs images (pas le plus optimisé mais le plus simple a realisé)

def convertirNoirBlancPlusieursImages(listImage):
    """Convertit plusieurs images en noir et blanc.

    Args:
        listImage (list): Liste des chemins d'images à modifier.
    """
    if len(listImage) <= 0:
        log("Erreur : La liste des images à traiter est vide.")
        print("la liste est vide aucune modification a faire")
        return

    for chemin_image in listImage:
        convertirNoirBlanc(chemin_image)


def appliquerDilatationPlusieursImages(listImage, taille_kernel=(5, 5), iterations=1):
    """Applique la dilatation à plusieurs images.

    Args:
        listImage (list): Liste des chemins d'images à modifier.
        taille_kernel (tuple, optional): Taille du noyau pour la dilatation.
        iterations (int, optional): Nombre d'itérations pour la dilatation.
    """
    if len(listImage) <= 0:
        log("Erreur : La liste des images à traiter est vide.")
        print("la liste est vide aucune modification a faire")
        return
    
    for chemin_image in listImage:
        appliquerDilatation(chemin_image, taille_kernel, iterations)
        
        
def ajouterTextePlusieursImages(listImage, texte, taille_police=1, epaisseur=1, couleur=(0, 0, 0)):
    """Ajoute du texte à plusieurs images.

    Args:
        listImage (list): Liste des chemins d'images à modifier.
        texte (str): Texte à ajouter sur les images.
        taille_police (int, optional): Taille de la police du texte.
        epaisseur (int, optional): Épaisseur du texte.
        couleur (tuple, optional): Couleur du texte en RGB (par défaut noir).
    """
    
    if len(listImage) <= 0:
        log("Erreur : La liste des images à traiter est vide.")
        print("La liste est vide, aucune modification à faire.")
        return
    
    for chemin_image in listImage:
        try:
            ajouterTexte(chemin_image, texte, taille_police, epaisseur, couleur)
        except ValueError as e:
            log(f"Erreur pour l'image {chemin_image} : {e}")
            print(f"Erreur pour l'image {chemin_image}: {e}")

        
def pivoterPlusieursImages(listImage, angle):
    """Pivote plusieurs images selon un angle donné.

    Args:
        listImage (list): Liste des chemins d'images à modifier.
        angle (float): L'angle de rotation en degrés.
    """
    if len(listImage) <= 0:
        log("Erreur : La liste des images à traiter est vide.")
        print("la liste est vide aucune modification a faire")
        return
    
    for chemin_image in listImage:
        pivoteImage(angle, chemin_image)
        
def redimensionnerPlusieursImages(listImage, facteur):
    """Redimensionne plusieurs images selon un facteur donné.

    Args:
        listImage (list): Liste des chemins d'images à modifier.
        facteur (float): Facteur de redimensionnement.
    """
    
    if len(listImage) <= 0:
        log("Erreur : La liste des images à traiter est vide.")
        print("la liste est vide aucune modification a faire")
        return
    
    for chemin_image in listImage:
        redimensionnerImage(chemin_image, facteur)

def appliquerFlouPlusieursImages (listImage):
    """_summary_

    Args:
        listImage (list): Liste des chemins d'images a modifier.
    """
    
    if len(listImage) <= 0:
        log("Erreur : La liste des images à traiter est vide.")
        print("la liste est vide aucune modification a faire")
        return
    
    for chemin_image in listImage:
        appliquerFlouPillow(chemin_image)
    

mozzie = "imageAmodifie/mozzie.jpg"
jesuisou = "imageAmodifie/jesuisou.jpg"
blanc = "imageAmodifie/blanc.jpg"


listeImages = [mozzie,jesuisou,blanc]

convertirNoirBlanc(mozzie)

#appliquerFlouPillow(mozzie)

#appliquerDilatation(mozzie)

#appliquerDilatation(blanc)

angle = 35

pivoteImage(angle,blanc)

#ajouterTexte(
#    chemin_image="imageAmodifie/blanc.jpg",  # Le chemin de l'image source
#    texte="Bonjour, Monde!",  # Le texte à ajouter
#    couleur=(255, 255, 255)  # Couleur du texte (ici rouge en RGB)
#)

#redimensionnerImage(jesuisou,-1.5)

#listeImage = [mozzie,jesuisou,blanc]

#ajouterTextePlusieursImages(listeImage,"ceci est un test pour voir si ça marche",)

#ajouterTexte(mozzie,"c'est quoi cette d")

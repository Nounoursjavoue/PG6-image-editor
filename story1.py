import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def convertir_noir_blanc(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
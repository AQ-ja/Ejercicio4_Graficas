# Programa principal
from GL import Renderer, V3, _color

from obj import Texture

import random

width = 960
height = 540

rend = Renderer(width, height)

modelTexture = Texture("Models/skin3.bmp")


rend.glLoadModel("Models/model.obj", modelTexture, V3(width/2, height/2, 0), V3(200, 200,200))


rend.glFinish("Ejer4.bmp")

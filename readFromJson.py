# -*- coding: utf-8 -*-
"""
Script de exemplo
"""
from AuxiliarModules.router import outputPath
from ImageGenerator import ImageObject as Image
from os import sys, path
import json
# ==========
sys.path.append(path.abspath(path.dirname(__file__)))
# ==========


def loadFromJson(filename: str = "exemplo") -> dict:
    with open("input/%s.json" % filename, 'r') as jsonFile:
        images = json.loads(jsonFile.read())
    return images


def main():

    images = loadFromJson(filename="exemplo")

    for imageName, imageContent in images.items():
        # Cria o objeto do tipo ImageObject rsrsrs
        new_image = Image()

        # ativa o modo debug
        # new_image.debug = True

        # define o nome da imagem
        new_image.name = imageName

        # define o esquema de cores da image
        new_image.setColorScheme(theme="terminal-green")

        # define as caracteristicas do texto principal da imagem
        new_image.setText(imageContent["text"])
        new_image.setTextFont("handwritten")

        # define as caracteristicas do titulo
        new_image.setTitleFont("firacode-bold", 30)
        new_image.setTitle(imageContent["title"])

        # define as caracteristicas dos créditos
        new_image.setCreditsFont("firacode-light", 35)
        new_image.setCredits(imageContent["credits"])

        # processa a imagem com o modo de debug desativado
        new_image.process(show=True, debug=False)
        
        # salva a imagem
        new_image.save(path="exemplo")


if __name__ == "__main__":
    main()

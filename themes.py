import pygame
import json

with open("themes.json", "r") as themes_collection:
    themes = json.load(themes_collection)


def load_theme(language, stage):
    return pygame.image.load(themes[language][stage])

import pygame
import random

# Initiate PyGame so we can actually use things like font
pygame.init()

# information that is needed to put the word on the screen at the correct point/with a font
SCREEN_WIDTH = 650


def write_word(screen, vocabulary, font, color):
    # takes a random word from the dictionary and splits the key value pair into English and French words
    word_en, word_fr = random.choice(list(vocabulary.items()))
    # renders the English word as an image
    word_img = font.render(word_en, True, color)
    # places that English word in the center of the screen
    screen.blit(word_img, (SCREEN_WIDTH / 2 - word_img.get_width() / 2, 0))

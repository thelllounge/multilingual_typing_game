import pygame
import create_and_move_words
import json

# Various constants that don't rely on PyGame being initialized
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 780

# General PyGame things
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# PyGame reliant constants
text_font = pygame.font.SysFont("Arial", 30)

# Opens the vocabulary JSON dictionary up to be readable.
with open("words.json", "r") as vocabulary_list:
    words = json.load(vocabulary_list)

# The loop that is the game.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # The function that pulls vocabulary words and puts them on the screen.
    # Currently, it continuously goes off. I need to figure out how to make it happen at a certain speed.
    # Maybe add the word to a list of things on the screen so the screen fill doesn't just erase them.
    create_and_move_words.write_word(screen, words, text_font, (255, 255, 255))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

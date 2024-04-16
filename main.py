import pygame
import create_and_move_words
import json
import Words

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

# Array of words that have been created
words_on_screen = []

# The loop that is the game.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # # The function that pulls vocabulary words and puts them on the screen.
    # # Currently, it continuously goes off. I need to figure out how to make it happen at a certain speed.
    # # Maybe add the word to a list of things on the screen so the screen fill doesn't just erase them.
    # # !! Updating this to use objects instead of a function like this. needs lots of work.
    # create_and_move_words.write_word(screen, words, text_font, (255, 255, 255))

    words_on_screen.append(Words.Word(words, SCREEN_WIDTH, text_font))

    if len(words_on_screen) >= 10:
        words_on_screen = []

# This works. Need to think about making position part of the object.
    for word in words_on_screen:
        screen.blit(word.wordimg, (SCREEN_WIDTH / 2 - word.wordimg.get_width() / 2, 0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

import pygame
import create_and_move_words
import json
import Words

# Various constants that don't rely on PyGame being initialized
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 780
FALL_SPEED = 25

GAMES_SPEED = 1000
TEST_SPEED = 100
WORD_DROP_RATE = 5

answer_text = "Place holder"

# General PyGame things
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
french_background = pygame.image.load("Paris unfinished.png")

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

    screen.blit(french_background, (0, 0))

    answer_text_img = text_font.render(answer_text, True, (0, 0, 0))
    screen.blit(answer_text_img, (110, 635))

    # This pulls words from the dictionary and adds them to the list to drop.
    if int(pygame.time.get_ticks()/1000) % WORD_DROP_RATE == 0:
        words_on_screen.append(Words.Word(words, SCREEN_WIDTH, text_font))

# This works. Need to think about making position part of the object.
    for word in words_on_screen:
        screen.blit(word.wordimg, word.position)
        # If a word hits the bottom of the play field game is over
        if word.position[1] >= 540:
            running = False
        word.move(FALL_SPEED)

    pygame.display.flip()

    pygame.time.wait(GAMES_SPEED)

    clock.tick(60)

pygame.quit()

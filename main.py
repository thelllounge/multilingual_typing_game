import pygame
import json
import Words

# Various constants that don't rely on PyGame being initialized
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 780
FALL_SPEED = 1

GAME_SPEED = 1000
TEST_SPEED = 100
WORD_DROP_RATE = 5
ADD_WORD_EVENT = pygame.event.custom_type()


answer_text = ""
correct_answers = 0

# General PyGame things
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
french_background = pygame.image.load("Paris unfinished.png")

# PyGame reliant constants
text_font = pygame.font.SysFont("Arial", 30)

# Opens the vocabulary JSON dictionary up to be readable.
with open("words.json", "r", encoding="utf-8") as vocabulary_list:
    words = json.load(vocabulary_list)

# Array of words that have been created
words_on_screen = []

# The loop that is the game.
while running:
    pygame.time.set_timer(ADD_WORD_EVENT, 25)
    for event in pygame.event.get():
        if event.type == ADD_WORD_EVENT:
            print("event")
            print(pygame.time.get_ticks())
            words_on_screen.append(Words.Word(words, SCREEN_WIDTH, text_font))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                answer_text = answer_text[:-1]
            elif event.key == pygame.K_RETURN:
                answer_text = ""
            # I need to figure out a way to make sure I can click buttons to do accents without fucking up the answer
            elif event.key == pygame.K_6:
                pass
            else:
                answer_text += event.unicode
        for word in words_on_screen:
            if answer_text == word.non_accent:
                answer_text = ""
                correct_answers += 1
                words_on_screen.pop(words_on_screen.index(word))

    screen.blit(french_background, (0, 0))

    # This puts the answer text on the screen
    answer_text_img = text_font.render(answer_text, True, (0, 0, 0))
    screen.blit(answer_text_img, (110, 635))
    score_img = text_font.render(f"Score: {correct_answers}", True, (255, 255, 255))
    screen.blit(score_img, (SCREEN_WIDTH / 2 - score_img.get_width() / 2, 715))

    # This pulls words from the dictionary and adds them to the list to drop.
    # Maybe I can use pygame.time.set_timer() for this. I need to learn how that works.

    # def add_word(array, vocabulary, width, font):
    #     array.append(Words.Word(vocabulary, width, font))

    # do_it = add_word(words_on_screen, words, SCREEN_WIDTH, text_font)



    # if int(pygame.time.get_ticks()/1000) % WORD_DROP_RATE == 0:
    #     words_on_screen.append(Words.Word(words, SCREEN_WIDTH, text_font))

# This works. Need to think about making position part of the object.
    for word in words_on_screen:
        screen.blit(word.word_img, word.position)
        # If a word hits the bottom of the play field game is over
        if word.position[1] >= 540:
            running = False
        word.move(FALL_SPEED)

    pygame.display.flip()

    # pygame.time.wait(TEST_SPEED)

    clock.tick(60)

pygame.quit()

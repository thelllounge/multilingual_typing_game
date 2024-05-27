import pygame
import json
import Words
import themes
import game_functions

# Various variables
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 780
fall_speed = 1
game_speed = 4000
ADD_WORD_EVENT = pygame.event.custom_type()
safe_to_raise_speed = False

falling_word_color = (0, 0, 0)

answer_text = ""
correct_answers = 0

# General PyGame things
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
start_screen = True
running = True
end_screen = True

# PyGame reliant constants
text_font = pygame.font.SysFont("Arial", 30)

# Array of words that have been created
words_on_screen = []


# TODO maybe this doesn't need the set_timer?
# TODO maybe this doesn't need to happen before the loop if no timer
# TODO maybe this can include language_select
def initiate():
    global fall_speed, correct_answers, words_on_screen, game_speed
    fall_speed = 1
    correct_answers = 0
    game_speed = 4000
    words_on_screen = []
    pygame.time.set_timer(ADD_WORD_EVENT, game_speed)


language = game_functions.language_select(text_font, screen, SCREEN_WIDTH, clock)

# Opens the vocabulary JSON dictionary up to be readable.
with open("words.json", "r", encoding="utf-8") as vocabulary_list:
    words = json.load(vocabulary_list)[language]

# The loop that is the game.
initiate()
while running:
    for event in pygame.event.get():
        # This sees the event on a timer and adds a word to the words_on_screen array
        if event.type == ADD_WORD_EVENT:
            words_on_screen.append(Words.Word(words, SCREEN_WIDTH, text_font, falling_word_color))
        if event.type == pygame.QUIT:
            running = False
        # This allows you to delete letters and stops some of the keys from doing anything.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                answer_text = answer_text[:-1]
            elif event.key == pygame.K_RETURN:
                answer_text = ""
            else:
                answer_text += event.unicode
        for word in words_on_screen:
            if answer_text == word.non_accent:
                answer_text = ""
                correct_answers += 1
                words_on_screen.pop(words_on_screen.index(word))
                game_speed -= 75
                pygame.time.set_timer(ADD_WORD_EVENT, game_speed)
        # Speeds up fall as game goes on
        # TODO mess around with speed to find good levels
        if safe_to_raise_speed and correct_answers % 15 == 0:
            fall_speed += .5
            safe_to_raise_speed = False
        if str(correct_answers)[-1] == "9":
            safe_to_raise_speed = True

    # TODO this level needs to be checked to see what's fair. There is a text color problem
    if 0 <= correct_answers < 10:
        screen.blit(themes.load_theme(language, "first"), (0, 0))
    else:
        falling_word_color = (255, 255, 255)
        screen.blit(themes.load_theme(language, "second"), (0, 0))

    if not game_functions.blit_words_on_screen(words_on_screen, text_font, answer_text, screen, SCREEN_WIDTH, correct_answers, fall_speed, initiate):
        language = game_functions.language_select(text_font, screen, SCREEN_WIDTH, clock)
        with open("words.json", "r", encoding="utf-8") as vocabulary_list:
            words = json.load(vocabulary_list)[language]

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

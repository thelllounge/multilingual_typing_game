import pygame
import json
import Words

# Various constants that don't rely on PyGame being initialized
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 780
FALL_SPEED = 1

GAME_SPEED = 4000
TEST_SPEED = 1000
ADD_WORD_EVENT = pygame.event.custom_type()
safe_to_raise_speed = False

answer_text = ""
correct_answers = 0

# Opens backgrounds
with open("themes.json", "r") as themes_collection:
    themes = json.load(themes_collection)

# General PyGame things
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
start_screen = True
running = True
end_screen = False
french_background = pygame.image.load(themes["french"]["level 0"])

# PyGame reliant constants
text_font = pygame.font.SysFont("Arial", 30)

# Opens the vocabulary JSON dictionary up to be readable.
with open("words.json", "r", encoding="utf-8") as vocabulary_list:
    words = json.load(vocabulary_list)

# Array of words that have been created
words_on_screen = []

# TODO This needs to move when I figure out how to do a start screen
pygame.time.set_timer(ADD_WORD_EVENT, GAME_SPEED)

# TODO find a way to loop this and have a start and end screen
# Start screen should include things like language pick, difficulty, etc.
while start_screen:
    start_screen_text = text_font.render("Are you ready?", True, (0,0,0))
    screen.fill((255, 255, 255))
    screen.blit(start_screen_text, (SCREEN_WIDTH / 2 - start_screen_text.get_width() / 2, 200))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            start_screen = False
        if event.type == pygame.QUIT:
            start_screen = False
            running = False

    pygame.display.flip()

    clock.tick(60)

# The loop that is the game.
while running:
    for event in pygame.event.get():
        # This sees the event on a timer and adds a word to the words_on_screen array
        if event.type == ADD_WORD_EVENT:
            words_on_screen.append(Words.Word(words, SCREEN_WIDTH, text_font))
        if event.type == pygame.QUIT:
            running = False
        # This allows you to delete letters and stops some of the keys from doing anything.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                answer_text = answer_text[:-1]
            elif event.key == pygame.K_RETURN:
                answer_text = ""
            elif event.key == pygame.K_6:
                pass
            else:
                answer_text += event.unicode
        for word in words_on_screen:
            if answer_text == word.non_accent:
                answer_text = ""
                correct_answers += 1
                words_on_screen.pop(words_on_screen.index(word))
                GAME_SPEED -= 75
                pygame.time.set_timer(ADD_WORD_EVENT, GAME_SPEED)
        # Speeds up fall as game goes on
        # TODO mess around with speed to find good levels
        if safe_to_raise_speed and correct_answers % 15 == 0:
            FALL_SPEED += .5
            safe_to_raise_speed = False
        if str(correct_answers)[-1] == "9":
            safe_to_raise_speed = True

    if correct_answers < 50:
        screen.blit(french_background, (0, 0))
    else:
        # TODO add correct image
        screen.fill((255, 255, 255))

    # This puts the answer text on the screen
    answer_text_img = text_font.render(answer_text, True, (0, 0, 0))
    screen.blit(answer_text_img, (110, 635))
    score_img = text_font.render(f"Score: {correct_answers}", True, (255, 255, 255))
    screen.blit(score_img, (SCREEN_WIDTH / 2 - score_img.get_width() / 2, 715))

    # This works. Need to think about making position part of the object.
    for word in words_on_screen:
        screen.blit(word.word_img, word.position)
        # If a word hits the bottom of the play field game is over
        if word.position[1] >= 540:
            running = False
            end_screen = True
        word.move(FALL_SPEED)

    pygame.display.flip()

    clock.tick(60)

while end_screen:
    screen.fill((150, 150, 150))

    words_start = 400

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_screen = False
    final_score = text_font.render(f"Final Score:", True, (255, 255, 255))
    score_number = text_font.render(f"{correct_answers}", True, (255, 255, 255))

    screen.blit(final_score, (SCREEN_WIDTH / 2 - final_score.get_width() / 2, 300))
    screen.blit(score_number, (SCREEN_WIDTH / 2 - score_number.get_width() / 2, 350))

    current_word = 1

    for word in words_on_screen:
        word_count = len(words_on_screen)
        screen.blit(word.word_img, (100, words_start + (word.word_img.get_height() * current_word)))
        screen.blit(word.word_img_fre, (SCREEN_WIDTH / 2, words_start + (word.word_img.get_height() * current_word)))
        current_word += 1
        if word == words_on_screen[-1]:
            current_word = 1

    pygame.display.flip()

pygame.quit()

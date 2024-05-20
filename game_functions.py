import pygame


def initiate():
    global fall_speed, correct_answers
    fall_speed = 1
    correct_answers = 0


def language_select(text_font, screen, SCREEN_WIDTH, clock):
    loop = True
    while loop:
        start_screen_text = text_font.render("Are you ready?", True, (0, 0, 0))
        screen.fill((255, 255, 255))
        screen.blit(start_screen_text, (SCREEN_WIDTH / 2 - start_screen_text.get_width() / 2, 200))

        french_button = pygame.Rect(150, 400, 100, 75)
        pygame.draw.rect(screen, "purple", french_button)
        german_button = pygame.Rect((SCREEN_WIDTH - 250), 400, 100, 75)
        pygame.draw.rect(screen, "blue", german_button)

        for event in pygame.event.get():
            # TODO make a button class. USE COLLIDEPOINT
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(french_button, mouse_position):
                    return "French"
                if pygame.Rect.collidepoint(german_button, mouse_position):
                    return "German"
            if event.type == pygame.QUIT:
                loop = False

        pygame.display.flip()

        clock.tick(60)


def blit_words_on_screen(word_list, text_font, answer_text, screen, SCREEN_WIDTH, correct_answers):
    # This puts the answer text on the screen
    answer_text_img = text_font.render(answer_text, True, (0, 0, 0))
    screen.blit(answer_text_img, (110, 635))
    score_img = text_font.render(f"Score: {correct_answers}", True, (255, 255, 255))
    screen.blit(score_img, (SCREEN_WIDTH / 2 - score_img.get_width() / 2, 715))

    # This works. Need to think about making position part of the object.
    for word in word_list:
        screen.blit(word.word_img, word.position)
        # If a word hits the bottom of the play field game is over
        if word.position[1] >= 540:
            # TODO this won't be here exactly later. It is just to test if it works now
            initiate()
            return False
        word.move(fall_speed)
    return True


def game_over_screen(word_list, screen, text_font, SCREEN_WIDTH, correct_answers):
    loop = True
    while loop:
        screen.fill((150, 150, 150))

        # TODO make a button class first. Makes this much easier I think.
        # restart_button = pygame.Rect(50, 50, SCREEN_WIDTH - 100, 100)
        # pygame.draw.rect(screen, "black", restart_button)
        # restart_text = text_font.render("Play again?", True, "white")
        # restart_button.blit(restart_text, (restart_button.width / 2 - restart_text.get_width() / 2, restart_button.height / 2 - restart_text.get_height() / 2))

        words_start = 400

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        final_score = text_font.render("Final Score:", True, (255, 255, 255))
        score_number = text_font.render(f"{correct_answers}", True, (255, 255, 255))

        screen.blit(final_score, (SCREEN_WIDTH / 2 - final_score.get_width() / 2, 300))
        screen.blit(score_number, (SCREEN_WIDTH / 2 - score_number.get_width() / 2, 350))

        current_word = 1

        for word in word_list:
            # word_count = len(word_list)
            screen.blit(word.word_img, (100, words_start + (word.word_img.get_height() * current_word)))
            screen.blit(word.word_img_fre,
                        (SCREEN_WIDTH / 2, words_start + (word.word_img.get_height() * current_word)))
            current_word += 1
            if word == word_list[-1]:
                current_word = 1

        pygame.display.flip()

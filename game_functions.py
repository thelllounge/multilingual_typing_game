import pygame
import Buttons


def language_select(text_font, screen, screen_width, clock):
    loop = True
    while loop:
        start_screen_text = text_font.render("Are you ready?", True, (0, 0, 0))
        screen.fill((255, 255, 255))
        screen.blit(start_screen_text, (screen_width / 2 - start_screen_text.get_width() / 2, 200))

        fr_btn = Buttons.Button((150, 400, 100, 75), "purple", text_font, "French")
        de_btn = Buttons.Button((screen_width - 250, 400, 100, 75), "blue", text_font, "German")

        fr_btn.draw_to_screen(screen)
        de_btn.draw_to_screen(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if fr_btn.get_event(event):
                    return "French"
                elif de_btn.get_event(event):
                    return "German"
            if event.type == pygame.QUIT:
                loop = False

        pygame.display.flip()

        clock.tick(60)


def blit_words_on_screen(word_list, text_font, answer_text, screen, screen_width, correct_answers, fall_speed, function):
    # This puts the answer text on the screen
    answer_text_img = text_font.render(answer_text, True, (0, 0, 0))
    screen.blit(answer_text_img, (110, 635))
    score_img = text_font.render(f"Score: {correct_answers}", True, (255, 255, 255))
    screen.blit(score_img, (screen_width / 2 - score_img.get_width() / 2, 715))

    # This works. Need to think about making position part of the object.
    for word in word_list:
        screen.blit(word.word_img, word.position)
        # If a word hits the bottom of the play field game is over
        if word.position[1] >= 540:
            return game_over_screen(word_list, screen, text_font, screen_width, correct_answers, function)
        word.move(fall_speed)
    return True


def game_over_screen(word_list, screen, text_font, screen_width, correct_answers, function):
    loop = True
    while loop:
        screen.fill((150, 150, 150))

        restart_btn = Buttons.Button((50, 50, screen_width - 100, 100), "green", text_font, "restart")
        restart_btn.draw_to_screen(screen)

        words_start = 400

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONUP and restart_btn.get_event(event):
                loop = False
                function()
        final_score = text_font.render("Final Score:", True, (255, 255, 255))
        score_number = text_font.render(f"{correct_answers}", True, (255, 255, 255))

        screen.blit(final_score, (screen_width / 2 - final_score.get_width() / 2, 300))
        screen.blit(score_number, (screen_width / 2 - score_number.get_width() / 2, 350))

        current_word = 1

        for word in word_list:
            screen.blit(word.word_img, (100, words_start + (word.word_img.get_height() * current_word)))
            screen.blit(word.word_img_fre,
                        (screen_width / 2, words_start + (word.word_img.get_height() * current_word)))
            current_word += 1
            if word == word_list[-1]:
                current_word = 1

        pygame.display.flip()

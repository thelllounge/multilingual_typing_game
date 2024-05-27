import pygame


class Button:
    def __init__(self, rect_pos, color, text, label, command=None):
        self.rect = pygame.Rect(rect_pos)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill(color)
        self.text = text
        self.label = label
        self.label_image = self.text.render(self.label, True, (0, 0, 0))
        self.function = command

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.was_clicked(pygame.mouse.get_pos()):
            return True

    def was_clicked(self, mouse_position):
        if pygame.Rect.collidepoint(self.rect, mouse_position):
            return True

    def draw_to_screen(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.label_image, (self.rect.center[0] - self.label_image.get_width() / 2, self.rect.center[1] - self.label_image.get_height() / 2))

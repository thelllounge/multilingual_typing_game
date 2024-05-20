import pygame


class Button:
    def __init__(self, rect_pos, color, text, label, command):
        self.rect = pygame.Rect(rect_pos)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill(color)
        self.text = text
        self.label = label
        self.function = command

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            self.on_click(pygame.mouse.get_pos())

    def on_click(self, mouse_position):
        if pygame.Rect.collidepoint(self.rect, mouse_position):
            self.function()

    def draw_to_screen(self, screen):
        screen.blit(self.image, self.rect)

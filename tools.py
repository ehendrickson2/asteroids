import pygame
import math
import random


class Tools:
    def __init__(self, screen):
        self.screen = screen

    def font_init(self, screen_rect):
        self.text_size = 15
        self.text_color = (255, 255, 255)
        self.topleft_pos = (10, 10)
        self.font = pygame.font.SysFont("Arial", self.text_size)
        self.update_text()

    def update_text(self, score=0):
        self.text, self.text_rect = self.make_text("Score: {}".format(score))

    def make_text(self, message):
        text = self.font.render(message, True, self.text_color)
        rect = text.get_rect(topleft=self.topleft_pos)
        return text, rect

    def draw(self):
        self.screen.blit(self.text, self.text_rect)

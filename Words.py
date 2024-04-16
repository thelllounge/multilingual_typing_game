# Maybe making objects instead of words is better than what I was doing before. I can add objects to an array to be populated
import random
import pygame


class Word:
    def __init__(self, vocab_list, screen_width, font):
        # This gets a pair of words from the english-french dictionary
        # Maybe change to language1 language2 so it can be more than French?
        self.words = random.choice(list(vocab_list.items()))
        self.english = self.words[0]
        self.french = self.words[1]
        self.wordimg = font.render(self.english, True, (255, 255, 255))
        self.position = (random.randint(0, screen_width - self.wordimg.get_width()), 0)

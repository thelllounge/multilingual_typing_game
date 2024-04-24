# Maybe making objects instead of words is better than what I was doing before. I can add objects to an array to be
# populated
import random


class Word:
    def __init__(self, vocab_list, screen_width, font):
        # This gets a pair of words from the english-french dictionary
        # Maybe change to language1 language2, so it can be more than French?
        self.words = random.choice(list(vocab_list.items()))
        self.english = self.words[0]
        self.french = self.words[1][0]
        self.non_accent = self.words[1][1]
        self.word_img = font.render(self.english, True, (0, 0, 0))
        self.position = (random.randint(0, screen_width - self.word_img.get_width()), 0)

    def move(self, speed):
        # Moves words down the screen
        self.position = (list(self.position)[0], list(self.position)[1] + speed)

import sys
import pygame
from pygame.locals import *
import json
from random import randint

def all_possible_words():
    words = []
    inFile = open('possible_words.txt', 'r')
    for word in inFile.readlines():
        words.append(word.strip().upper())
    return words

def guess_word_list(word_guess, possible_words, background_colors):
    if word == '':
        return 'CRANE'
    else:
        new_possible_words = possible_words.copy()
        for i in range(5):
            if background_colors[i] == GREEN:
                for w in possible_words:
                    if w[i] == word_guess[i]:
                        new_possible_words.append(w)
            if background_colors[i] == YELLOW:
                for w in possible_words:
                    if word_guess[i] in w:
                        new_possible_words.append(w)
            possible_words = new_possible_words.copy()
    return possible_words



def draw_row(row, guess, word, WINDOW):
    renderList = ["", "", "", "", ""]
    spacing = 0
    rectangles_bg_colors = [GREY, GREY, GREY, GREY, GREY]
    word_copy = list(word)
    for i in range(5):
        if guess[i] in word_copy:
            rectangles_bg_colors[i] = YELLOW
            word_copy.remove(guess[i])
        if guess[i] == word[i]:
            rectangles_bg_colors[i] = GREEN
    for i in range(5):
        renderList[i] = font.render(guess[i], True, WHITE)
        pygame.draw.rect(WINDOW, rectangles_bg_colors[i], pygame.Rect(60 + spacing, 50 + row * 80, 50, 50))
        WINDOW.blit(renderList[i], (75 + spacing, 60 + row * 80))
        pygame.display.update()
        spacing += 80
    if GREY not in rectangles_bg_colors and YELLOW not in rectangles_bg_colors:
        return True
    return False

def draw_top_pick():
    possible_words = guess_word_list()


def run_game():
    WINDOW = pygame.display.set_mode((Grid_HEIGHT, Grid_WIDTH))
    lose_message = font.render('You Lost', True, RED)
    WINDOW.fill(BLACK)
    pygame.display.update()
    clock = pygame.time.Clock()
    pygame.font.init()
    pygame.display.set_caption('Wordle')
    for i in range(5):
        for j in range(6):
            pygame.draw.rect(WINDOW, GREY, pygame.Rect(60+ i * 80, 50 + j * 80, 50, 50), 2)
            pygame.display.update()
    Row = 0
    winning_cond = False
    word_guess = ""
    WORD = WORDS[randint(0, 12971)]
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and (winning_cond == True or Row == 6):
                    run_game()
                if event.key == pygame.K_BACKSPACE:
                    word_guess = word_guess[:-1]
                elif len(word_guess) <= 5:
                    word_guess += event.unicode.upper()
                if event.key == pygame.K_RETURN and len(word_guess) == 6:
                    winning_cond = draw_row(Row, word_guess, WORD, WINDOW)
                    Row += 1
                    word_guess = ""
                    WINDOW.fill(BLACK, (0, 500, 500, 200))
                    pygame.display.update()
        WINDOW.fill(BLACK, (0, 500, 500, 200))
        render_guess = font.render(word_guess, True, GREY)
        WINDOW.blit(render_guess, (180, 530))
        pygame.display.update()
        if Row == 6 and winning_cond == False:
            WINDOW.blit(lose_message, (180, 530))
            pygame.display.update()


def make_word_Dictionary(WORDS):
    d = {}
    for i in range(26):
        d[chr(ord('A') + i)] = []
    for word in WORDS:
        for letter in list(word):
            if word not in d[letter]:
                d[letter].append(word)
    return d

if __name__ == "__main__":
    pygame.init()
    FPS = 60
    Grid_WIDTH, Grid_HEIGHT = 600, 500  # 90x90
    Square_WIDTH, Square_HEIGHT = 90, 90
    GREEN = (144,238,144)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (240, 230, 140)
    GREY = (169, 169, 169)
    RED = (255, 99, 71)
    font = pygame.font.SysFont('Helvetica neue', 40)
    WORDS = all_possible_words()
    WORD_Dictionary = make_word_Dictionary(WORDS)
    run_game()

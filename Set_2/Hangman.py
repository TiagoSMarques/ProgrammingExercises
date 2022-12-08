# Implementation of the Hangman's game

import random


class Hangman:
    def __init__(self):
        words = ["soup", "cat", "lolipop", "sofa", "pillow"]
        self.word2Guess = random.choice(words)
        self.Tries = 10
        self.Guess = 0
        self.wordArr = ["" + "_" for char in self.word2Guess]
        self.guessedChar = []
        print(self.wordArr)

    def _getChar(self):
        inChar = input("Please write your guess: ")
        print("")

        if len(inChar) == 1 and inChar not in self.wordArr + self.guessedChar:
            return inChar
        else:
            print("Input a single unique char!")
            return self._getChar()

    def guess(self):

        if "_" in self.wordArr and self.Guess < self.Tries:
            inputChar = self._getChar()
            l = [index for index, c in enumerate(self.word2Guess) if inputChar == c]
            if l:
                for i in l:
                    self.wordArr[i] = inputChar
                print("Nice!")
                print(self.wordArr)
                self.guess()
            else:
                self.Guess += 1
                self.guessedChar.append(inputChar)
                print("Try again!")
                print("Previous guesses: ", self.guessedChar)
                print(self.wordArr)
                print("Moves left: ", self.Tries - self.Guess)
                self.guess()
        elif self.Guess == self.Tries:
            print("Game Over!!!")
        else:
            print("")
            print("Congrats, you won!!!")
            print("")


H = Hangman()
H.guess()

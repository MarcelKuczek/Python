class HangmanGame:
    def __init__(self,  word, life = 10):
        self.word = word
        self.life = life
        self.correct = ['_' for _ in word]
        self.incorrect = []

    def check_letter(self, guess):
        found = False
        for index, letter  in enumerate(self.word):
            if guess == letter :
                self.correct[index] = guess
                found = True
        return found

    def show_letters(self):
        print("Correct letters: ")
        print(self.correct)
        print("Incorrect letters: ")
        print(self.incorrect)

    def is_valid_quess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            return True
        else:
            print("Write only ONE LETTER")
        return False

    def play(self):
        while self.life > 0:
            print("---------------------------")
            self.show_letters()
            quess = input("Make a quess: ").lower()
            if self.is_valid_quess(quess):
                if self.check_letter(quess):
                    if self.correct == list(self.word):
                        print("---------------------------")
                        print("YOU WIN!!! Correct word is: " + self.word)
                        break
                else:
                    self.incorrect.append(quess)
                    self.life -= 1
        else:
            print("---------------------------")
            print("YOU LOSE!!! Correct word is: " + self.word)

if __name__ == "__main__":
    word = input("Entry word: ").lower()
    game = HangmanGame(word)
    game.play()
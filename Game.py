from random import randint


class Game:

    def __init__(self):
        self.options = {
            "Rock": 1,
            "Paper": 2,
            "Scissors": 3
        }
        self.continue_play = True

    def play(self):
        while self.continue_play:
            self.welcome_message()
            self.player_answer = int(input())
            if self.is_valid_answer():
                self.compare_answers()
                self.verify_play_again()
            else:
                print("Your answer is not valid! Try again.")
        print("Bye!")

    def get_dictionary_key(self, answer_value):
        for key, value in self.options.items():
            if value == answer_value:
                return key

    def verify_play_again(self):
        print("Do you wanna play again? Yes(y) No(n)")
        answer = input()
        if answer.lower() != "y":
            self.continue_play = False

    def compare_answers(self):
        print("Your answer: " + self.get_dictionary_key(self.player_answer))
        computer_answer = self.computer_turn()
        self.verify_victory(self.player_answer, computer_answer)

    def welcome_message(self):
        print("--------------------------------------------------")
        print("Let's play rock paper or scissors")
        print("Choose one option: (1) Rock (2) Paper (3) Scissors")

    def is_valid_answer(self):
        if self.player_answer < 1 or self.player_answer > 3:
            return False
        return True

    def computer_turn(self):
        computer_answer = randint(1, 3)
        print("Computer answer: " + self.get_dictionary_key(computer_answer))
        return computer_answer

    def verify_victory(self, player_answer, computer_answer):
        if player_answer == computer_answer:
            print("Tie!")
        elif player_answer == self.options["Rock"] and computer_answer == self.options["Paper"]:
            print("You lose!")
        elif player_answer == self.options["Rock"] and computer_answer == self.options["Scissors"]:
            print("You won!")
        elif player_answer == self.options["Paper"] and computer_answer == self.options["Rock"]:
            print("You won!")
        elif player_answer == self.options["Paper"] and computer_answer == self.options["Scissors"]:
            print("You lose!")
        elif player_answer == self.options["Scissors"] and computer_answer == self.options["Rock"]:
            print("You lose!")
        elif player_answer == self.options["Scissors"] and computer_answer == self.options["Paper"]:
           print("You won!")


Game().play()

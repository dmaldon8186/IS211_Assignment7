import random

class Die:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0

    def turn(self):
        print(f"{self.name}'s turn:")
        while True:
            roll = Die().roll()
            if roll == 1:
                print(f"You rolled a 1. Your turn is over.")
                self.turn_score = 0
                break
            else:
                self.turn_score += roll
                print(f"You rolled a {roll}. Current turn score: {self.turn_score}")
                print(f"Current total score: {self.score + self.turn_score}")
                decision = input("Do you want to roll again (r) or hold (h)? ")
                if decision == "h":
                    self.score += self.turn_score
                    self.turn_score = 0
                    print(f"{self.name}'s score is now {self.score}")
                    break
                elif decision != "r":
                    print("Invalid input. Please enter 'r' or 'h'.")

def play_game(player1_name, player2_name, target_score=100):
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    while player1.score < target_score and player2.score < target_score:
        player1.turn()
        if player1.score >= target_score:
            break
        player2.turn()
    print("Game over.")
    if player1.score >= target_score:
        print(f"{player1.name} wins!")
    else:
        print(f"{player2.name} wins!")

play_game("Player 1", "Player 2")
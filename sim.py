import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  # Starting off the board
        self.started = False

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, steps):
        if not self.started:
            if steps == 6:
                self.started = True
                self.position = 1
                print(f"{self.name} enters the board!")
            else:
                print(f"{self.name} needs a 6 to start.")
        else:
            if self.position + steps <= 57:
                self.position += steps
            print(f"{self.name} moves to {self.position}")

    def has_won(self):
        return self.position == 57


def ludo_game():
    print("=== SIMPLE LUDO GAME ===\n")

    num_players = int(input("Enter number of players (2–4): "))
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    turn = 0

    while True:
        player = players[turn]
        print(f"\n--- {player.name}'s Turn ---")

        input("Press ENTER to roll the dice...")
        dice = player.roll_dice()
        print(f"{player.name} rolled a {dice}")

        player.move(dice)

        # Check win condition
        if player.has_won():
            print(f"\n🎉🎉 {player.name} WINS THE GAME! 🎉🎉")
            break

        # Extra turn if dice == 6
        if dice != 6:
            turn = (turn + 1) % num_players


# Run the game
ludo_game()

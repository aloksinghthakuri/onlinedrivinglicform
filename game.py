import random

# --- Constants and Setup ---
NUM_PLAYERS = 2
BOARD_LENGTH = 57  # Standard Ludo path length (plus the Home column)
PLAYERS = {
    0: {"name": "Player RED", "position": -1, "tokens": 4},
    1: {"name": "Player BLUE", "position": -1, "tokens": 4}
}
HOME_ENTRY_POINT = 51 # The position before entering the home column/finish line

# --- Game Functions ---

def roll_dice():
    """Simulates rolling a standard six-sided die."""
    return random.randint(1, 6)

def display_board(positions):
    """
    A simple visualization of the board path and player positions.
    - H: Home position (before entering the home column)
    - X: The player's current token position
    """
    board_display = ['_'] * BOARD_LENGTH
    
    # Mark the Home Entry Point for reference
    board_display[HOME_ENTRY_POINT] = 'H' 
    
    # Mark player positions
    for p_id, data in positions.items():
        pos = data['position']
        if pos >= 0 and pos < BOARD_LENGTH:
            # Use player ID (1 or 2) to mark the spot
            board_display[pos] = str(p_id + 1)
        elif pos == BOARD_LENGTH:
            # Mark a token that has reached the finish
            print(f"[{data['name']} is HOME!]", end=' ')

    print("\n--- Board Path ---")
    # Print the board in chunks for readability
    for i in range(0, BOARD_LENGTH, 10):
        chunk = board_display[i:i+10]
        print(f"Pos {i:02d}-{(i+len(chunk)-1):02d}: {' '.join(chunk)}")
    print("------------------")


def move_token(player_id, steps):
    """Calculates the new position for a token."""
    player = PLAYERS[player_id]
    current_pos = player["position"]
    new_pos = current_pos + steps

    print(f"Current Position: {current_pos}. Dice Roll: {steps}")

    # Check if token is still in the starting area (-1) and rolled a 6 or 1
    if current_pos == -1:
        if steps == 6 or steps == 1:
            player["position"] = 0  # Move to the starting square (position 0)
            print(f"🎉 {player['name']} moved out of the home area!")
            return True
        else:
            print(f"❌ {player['name']} needs a 6 or a 1 to start.")
            return False

    # Check for winning (entering the home column)
    elif current_pos < HOME_ENTRY_POINT and new_pos > HOME_ENTRY_POINT:
        # Simplification: If the roll takes the token past the entry point, it's considered Home/Win
        player["position"] = BOARD_LENGTH 
        print(f"🥳 {player['name']} has reached HOME!")
        return True

    # Normal movement
    elif new_pos < BOARD_LENGTH:
        player["position"] = new_pos
        print(f"➡️ {player['name']} moves to position {new_pos}.")
        return True
        
    # Overshooting the finish line (no move)
    else:
        print("🛑 Cannot move, roll is too high for the final stretch.")
        return False


def check_for_winner():
    """Checks if any player has 'finished' all their tokens (simplified to one token)."""
    for p_id, data in PLAYERS.items():
        if data["position"] == BOARD_LENGTH:
            return data["name"]
    return None

# --- Main Game Loop ---

def play_ludo():
    current_player_index = 0
    turns = 0
    
    print("--- 🐍 Simple Console Ludo Game (2 Players) 🐍 ---")
    
    while check_for_winner() is None:
        player_id = current_player_index % NUM_PLAYERS
        current_player = PLAYERS[player_id]
        
        turns += 1
        print(f"\n--- TURN {turns} ---")
        display_board(PLAYERS)
        print(f"It is {current_player['name']}'s turn.")
        
        # Wait for user input to simulate rolling the dice
        input("Press Enter to roll the dice...")
        
        dice_roll = roll_dice()
        print(f"You rolled a **{dice_roll}**!")
        
        # --- Move Logic ---
        can_move = move_token(player_id, dice_roll)
        
        # --- Next Turn Logic (Simplified) ---
        # If a 6 was rolled AND a move was possible, the player gets another turn.
        if dice_roll == 6 and can_move:
            print("🎁 You rolled a 6 and moved! You get an extra turn!")
            # current_player_index does not change, so it's the same player's turn again.
        else:
            current_player_index += 1
            
    # --- Game Over ---
    winner = check_for_winner()
    if winner:
        print("\n" * 3)
        print("*************************************")
        print(f"🏆 CONGRATULATIONS! {winner} WINS THE GAME! 🏆")
        print("*************************************")

# Execute the game
if __name__ == "__main__":
    play_ludo()
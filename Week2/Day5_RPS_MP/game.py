import random
class Game:
    def get_user_item(self):
        user_input = ""
        valid_inputs = {
            "1": "rock",
            "2": "paper",
            "3": "scissors",
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors"
        }
        
        while user_input not in valid_inputs:
            user_input = input("Please select (1 for rock, 2 for paper, 3 for scissors): ").lower().strip()
            if user_input not in valid_inputs:
                print("Invalid input. Please try again.")
        return valid_inputs[user_input]
    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
            (user_item == "scissors" and computer_item == "paper") or \
            (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item,computer_item)
        print (f"You chose {user_item}.\nThe computer selected {computer_item}.\nYou {result}.")
        return result
    
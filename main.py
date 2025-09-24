from ascii_man import stages
import os
import time


class CharFlag:
    def __init__(self, char:str, flag:bool):
        self.char = char
        self.flag = flag


def main():
    secret_phrase = get_phrase()
    char_list = list(secret_phrase)
    guessed_list: list = []
    state = {
        'stage': 0,
        'score': 0,
        'winning_score': 0
    }
    char_flag_list = []
    for char in char_list:
        if char.isalpha():
            char_flag_list.append(CharFlag(char, False))
            state['winning_score'] += 1
        else:
            char_flag_list.append(CharFlag(char, True))
    try:
        while True:
            if state['score'] == state['winning_score']:
                print("\033[32mYou won!!!\033[39m")
                break
            elif state['stage'] == 6:
                print("\033[31mYou lose, try again!\033[39m")
                break

            clear_terminal()
            print(render_stage(state))
            print("")
            print(render_hidden_phrase(char_flag_list))
            print("")
            print(f"Guessed letters: {", ".join(guessed_list)}")
            guess_letter(char_flag_list, guessed_list, state)

    except KeyboardInterrupt:
        print("\nExiting game...thanks for playing!")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')    


def guess_letter(char_flag_list:list[CharFlag], guessed_list: list, state: dict):
    # Components of letter guess: 
        # (1) get letter, 
        # (2) check if letter in phrase, 
        # (3) track if guess is correct & update tracker, 
        # (4) add letter to guessed letters list)
    
    guess = input("Guess a letter: ")
    is_valid= is_valid_char(guess, guessed_list)
    if is_valid:
        correct_guess = False
        for char in char_flag_list:
            if char.char == guess or char.char.lower() == guess:
                char.flag = True
                correct_guess = True
                state['score'] += 1
            else:
                continue

        if correct_guess == False:
            state['stage'] += 1 
        
        guessed_list.append(guess)
    else:
        print("\033[31mInvalid guess. Try again.\033[39m")
        time.sleep(2)
        

def is_valid_char(char:str, guessed_list:list) -> bool:
    is_alpha = char.isalpha()
    char_count = len(char)
    in_guessed_list = True if char in guessed_list else False
    if is_alpha and char_count == 1 and in_guessed_list == False:
        return True
    
    return False

def render_stage(game_state:dict) -> str:
    stage_num = game_state['stage']
    return stages[stage_num]
    

def render_hidden_phrase(char_flag_list:list[CharFlag]):
    hidden_phrase = "" # later on I'm going to break this out into a render_hidden_phrase function that will have the char_tuple_list passed into it
    for char in char_flag_list:
        if char.flag:
            hidden_phrase = hidden_phrase + char.char
        else:
            hidden_phrase = hidden_phrase + "_"
    return hidden_phrase


def get_phrase():
    secret_phrase = input("What phrase will we be guessing?: ")
    return secret_phrase


if __name__ == "__main__":
    main()
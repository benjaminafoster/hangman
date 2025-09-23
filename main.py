class CharFlag:
    def __init__(self, char:str, flag:bool):
        self.char = char
        self.flag = flag

def main():
    secret_phrase = get_phrase()
    char_list = list(secret_phrase)
    guessed_list: list = []
    state = {'count': 0}
    print(f"Chosen phrase: {secret_phrase}")
    char_flag_list = []
    for char in char_list:
        if char.isalpha():
            char_flag_list.append(CharFlag(char, False))
        else:
            char_flag_list.append(CharFlag(char, True))

    while True:
        print(f"Guessed letters: {", ".join(guessed_list)}")
        print(f"Incorrect guesses: {state['count']}\n\n")
        print(render_hidden_phrase(char_flag_list))
        guess_letter(char_flag_list, guessed_list, state)
    

def guess_letter(char_flag_list:list[CharFlag], guessed_list: list, state: dict):
    # Components of letter guess: 
    # (1) get letter, 
    # (2) check if letter in phrase, 
    # (3) track if guess is correct & update tracker, 
    # (4) add letter to guessed letters list)
    
    guess = input("Guess a letter: ")
    correct_guess = False
    for char in char_flag_list:
        if char.char == guess or char.char.lower() == guess:
            char.flag = True
            correct_guess = True
            guessed_list.append(char.char)
        else:
            continue

    if correct_guess == False:
        print("You entered an incorrect guess!")
        state['count'] += 1 


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
import random

from hangman_words import word_list

#Choosing random word from list
chosen_word = random.choice(word_list)

#User total lives
lives = 6

from hangman_art import logo
print(logo)

#Creating a list with spaces [_ _ _ _ _]
empty_list = []
for letter in chosen_word:
    empty_list.append("_")
print(empty_list)

#Asking user to guess a letter
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in empty_list:
        print(f"You've already guessed {guess}.")

    #Checking if guessed letter is present in chosen word and replacing the space with letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            empty_list[position] = letter

    #Reducing user lives on wrong guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(empty_list)

    #Ending the game if word is completed
    if '_' not in empty_list:
        end_of_game = True
        print("You Win!")

    from hangman_art import stages
    print(stages[lives])
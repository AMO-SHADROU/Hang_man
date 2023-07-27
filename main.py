import random
from wordlist import word_list
from hangman_art import logo
from hangman_art import stages
print(logo)
#now we generate a random word
random_word = random.choice(word_list)
random_word_lenght = len(random_word)
#now we generate a _ for each word
word_place_holder = []
lives = 6
for item in random_word:
    word_place_holder.append("_ ")
print(word_place_holder)
end_game = False

while not end_game:
    print(stages[lives])
    user_word = input("Enter a word\n").lower()
    #Lets check if the user have entered it before?
    if user_word in word_place_holder:
        print("You have already entered this word.")
    # now lets get the index
    for position in range(random_word_lenght):
        if user_word == random_word[position]:
            word_place_holder[position] = user_word
    print(word_place_holder)
    if user_word not in random_word:
        print("ops.Wrong letter.")
        lives -= 1
        print(f"Lives left : {lives}")
    if lives == 0:
        end_game = True
        print("Game over.")
        print(stages[lives])
    if "_ " not in word_place_holder:
        end_game = True
        print("Congratulation.")
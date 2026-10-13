import random
import hangman_words
import hangman_art
game_over = False
placeholder = ""
correct_answer = []
lives = 6

print(hangman_art.logo)
word = random.choice(hangman_words.word_list)
print(word)


#word length
word_length = len(word)

for i in range (word_length):
    placeholder += "_"

print(f"The word to guess is {placeholder}")

while not game_over:
    print(f"You have {lives}/6 left")
    display = ""
    guess = input("Guess a letter: ").lower()


    if guess in correct_answer:
        print(f"You already guessed {guess}")

    if guess in word and guess not in correct_answer:
        correct_answer.append(guess)

    for letter in word:
        if letter == guess:
            display += letter
        elif letter in correct_answer:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in correct_answer:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a turn")
        if lives == 0:
            game_over = True
            print(f"Game over! The word was {word}")

    if "_" not in display:
        game_over = True
        print(f"You win!!!!")

    print(hangman_art.stages[lives])

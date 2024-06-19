import random
from hangman_words import word_list
from hangman_art import logo,stages

chosen_list=random.choice(word_list)
word_length=len(chosen_list)
end_game=False
lives=6
display=[]
for _ in range(word_length):
  display+="_"

print(logo)

while not end_game:
  guess_input=input("Guess the word: ").lower()
  if guess_input in display:
    print(f"You have already guessed the word {guess_input}")

  for position in range(word_length):
    letter=chosen_list[position]
    if letter==guess_input:
      display[position]=letter
  
  if guess_input not in chosen_list:
    print(f"You guessed {guess_input}") 
    lives-=1
    if lives==0:
      end_game=True
      print("You Lose..................")

  print(f"{' '.join(display)}")                  
  if "_" not in display:
    end_game=True
    print("You won...................")
  print(stages[lives])



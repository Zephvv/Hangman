import random 

fruit_word_list = ["Strawberry", "Grape", "Watermelon", "Tomato", "Banana", "Apple", "Cucumber", "Pear", "Kiwi"] 
index = random.randint(0, len(fruit_word_list) - 1) # Randomly selects an index from the list, adjusting for zero-based indexing
fruit_word = fruit_word_list[index] 
guess = ["_"] * len(fruit_word) # Initialise the guess list with underscores, each representing an unknown letter in the fruit word
guessed_letters = [] # Tracks guessed letters
LIVES = 7 # Set the number of lives (uppercase denotes a constant)
hangman_stages = [
  """
         -----
             |
             |
             |
             |
             |
      =========""",
   """
         -----
         |   |
             |
             |
             |
             |
      =========""",
      """
         -----
         |   |
         O   |
             |
             |
             |
      =========""",
      """
         -----
         |   |
         O   |
         |   |
             |
             |
      =========""",
      """
         -----
         |   |
         O   |
        /|   |
             |
             |
      =========""",
      """
         -----
         |   |
         O   |
        /|\  |
             |
             |
      =========""",
      """
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
      =========""",
      """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
      =========""",
  ]

# Intro 
print("Welcome to the hangman fruit-style game!\nYou have {} lives to guess the fruit word:".format(LIVES)) 
print(hangman_stages[0])
print("\n" + " ".join(guess)) 

# Updates guess with matched letter 
def update_guess(guess, fruit_word, input_letter): 
  matched = False 
  for i, char in enumerate(fruit_word):
    if input_letter.lower() == char.lower():
      guess[i] = char # Updates guess with the correct letter, preserving case 
      matched = True 
  return matched 
  
# Main game loop: continue until lives are exhausted or word is guessed 
while LIVES > 0 and "_" in guess: 
  if guessed_letters:
    print("\n\nGuessed so far: " + ", ".join(guessed_letters)) 
  
  input_letter = input("\nChoose a letter: ").strip() 

  # Edge case: checks for duplicate guessing 
  if input_letter.lower() in guessed_letters:
    print("\nYou've already guessed that letter.")
    continue

  # Edge case: check if the input is a valid single letter
  if not input_letter.isalpha() or len(input_letter) != 1:
    print("\nPlease enter a single alphabetical letter!") 
    continue 

  # Calling function to match 
  matched = update_guess(guess, fruit_word, input_letter) 

  # If no duplicates, proceeds updating lives and display if correct or not 
  if input_letter.lower() not in guessed_letters: 
    if matched:
        print("\nCorrect!\n\n" + " ".join(guess)) 
    else:
      LIVES -= 1 
      print(hangman_stages[len(hangman_stages) - 1 - LIVES]) 
      print("\n'{}' is not in the word. You have {} guesses left.".format(input_letter, LIVES)) 
  
  # Tracks all user inputs
  guessed_letters.append(input_letter)

# End outcomes 
if "_" not in guess:
  print("\n✅ Congratulations! You guessed the fruit:", fruit_word)
else: # If "_" in guess and LIVES == 0 
  print("\n❌ You ran out of guesses! The fruit was:", fruit_word)

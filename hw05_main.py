"""
Name: (put your name here)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_user_word():
    """ asks the user for a word with 3 or more characters"""
    while True:
        word = input("Provide a word with more than 3 characters: ")
        if " " in word:
            print("Error: You provided more than one word")
            continue
        if len(word) < 3:
            print("Error: The word is too short")
            continue
        break
    return word

def count_in_text(user_word, word_list):
  """counts each time the user word is found in the word list for the text"""
  counter = 0
  for w in word_list:
    if user_word in w :
      counter+= 1
  print(f"The word '{user_word}' is found {counter} times in the text")


## ------- DO NOT MODIFY ANYTHING BELOW THIS LINE

# Do not modify this function
def main ():
    # The text inside of which we will search for words
    text = "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain."
    # the command text.split() results in a list of words split using spaces
    word_list = text.split()
    # this is a call to the first of your functions
    word = get_user_word()
    print(f"The user selected the word: '{word}'")
    # this is a call to the second of your functions
    count_in_text(word, word_list)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
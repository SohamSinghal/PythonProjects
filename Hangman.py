import random,time
ct = 0
file = open("AnimalList.txt","r")
animal_list = file.read().split(",")
hagnman_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
#print hangman
def print_hangman(count):
    return hagnman_pics[count]
#select a word form a list
def select_word(list):
    word_selected = random.choice(list)
    return word_selected
#word to dash
def words_to_dash(word):
    l = len(word)
    dash = "-"*l
    return dash
#ask user to guess letter
def guess():
    print("Guess a letter. If its there in the word it'll show otherwise you're down by 1 chance")
    letter = input()
    return letter
#replace the dash with the correct guess
def replace(word,index,guess):
    list_word = list(word)
    list_word[index] = guess
    return "".join(list_word)
#react to it
def compare(word,guess):  
    if guess.lower() in word:
        return True
    else:
        return False
#full word guessed or not
def guessed_or_not(word1,word2): #word1 - word guessed by user #word2 - word taken at random from animal_list
    if word1 == word2:
        return True
#main
print("Enter your name user:")
name = input()
while True:
    wtg = select_word(animal_list) #wtg - word to guess
    dashed_word = words_to_dash(wtg)
    print("Welcom",name.capitalize(),"The word is chosen from a list of animals")
    time.sleep(5)
    while True:
        print(dashed_word)
        print(print_hangman(ct))
        g = guess()
        if g.isalpha() == False:
            print("Its not something from a-z or A-Z")
            continue
        if compare(wtg,g):
            index = wtg.index(g)
            dashed_word = replace(dashed_word,index,g)
        else:
            ct += 1
        if guessed_or_not(dashed_word,wtg):
            print("Congrats",name.capitalize(),"You have guessed the word",wtg)
            break
        elif ct == 6:
            print(hagnman_pics[-1])
            print("Sorry",name.capitalize(),"You couldn't guess the word correctly. The word was",wtg)
            break
    print("Enter 1 to play again.")
    again = int(input())
    if again == 1:
        time.sleep(10)
        ct = 0
        continue
    else:
        print("Bye! See you next time")
        break
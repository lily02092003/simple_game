import cmd
import random
from words import words
import string
def getvalid(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()
def hangman():
    word=getvalid(words)
    word_letters=set(word)
    alphabets=set(string.ascii_uppercase)
    lives=6
    used=set() #keeping track of what user has guessed
    while len(word_letters)>0 and lives>0:
        print('You have ',lives,' lives left.\n YOU HAVE USED LETTERS:',' '.join(used))
        word_list=[letters if letters in used else '-' for letters in word]
        print("THE CURRENT WORD:",''.join(word_list))
        user_letter= input("GUESS THE LETTER: ").upper()
        if user_letter in alphabets-used:
            used.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print("LETTER NOT IN WORD")
        elif user_letter in used:
            print("YOU HAVE USED IT BEFORE!")
        else:
            print("INVALID CHARACTER!")
    if lives==0: 
        print("YOU DIED :( BETTER LUCK NEXT TIME. THE WORD WAS",word)
    else:
        print("YAYY! YOU GUESSED IT CORRECTLY. THE WORD WAS",word)
hangman()
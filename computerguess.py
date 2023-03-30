import random
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} too low(l) or too high(h) or correct?(c):').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    else:
        print(f'YAYY CORRECTLY GUESSED,{guess},WAS THE NUMBER!')
computer_guess(1000)
import random
#User finction to select random word from the txt file
def wordgen(texfile):
    return random.choice(open(texfile).read().split('\n')).upper()
#User function to convert the list to string
def hangconv(wordin):
    wordout = ""
    return wordout.join(wordin)
#hangman stages
def stages(x):
    pic = ['''
            ---------
            |
            |
            |
            |
            |
            |
    ''',
    '''
            ---------
            |       |
            |
            |
            |
            |
            |
    ''',
    '''
            ---------
            |       |
            |       O
            |
            |
            |
            |
    ''',
    '''
            ---------
            |       |
            |       O
            |      \|/
            |
            |
            |
    ''',
    '''
            ---------
            |       |
            |       O
            |      \|/
            |       |
            |
            |
    ''',
    '''
            ---------
            |       |
            |       O
            |      \|/
            |       |
            |       |
            |      / \\
    '''
    ]
    return pic[x]
#txt file select where all words are stored
texfile = './wordlist.txt'
#random word selected
theword = wordgen(texfile)
#print(theword)
#convert the word string to list
wordin = list(theword)
#print(wordin)
#print(type(wordin))
dashword = []
#used word wordlist
usedlist = []
#Converts the word in to dashes
for i in wordin:
    if i != " ":
        dashword.append("-")
    else:
        dashword.append(" ")
#Guess game logic
result=[]
reveal = random.randint(0,len(wordin)-1)
myw = theword[reveal]
usedlist.append(myw)
for c,l in enumerate(wordin):
    if myw == l:
        result.append(c)
for z in result:
    dashword[z]=myw
#Intro
print('Welcome to the game of Hangman. \n')
x = 0
print("\n",hangconv(dashword),stages(x))

while x < 5:
    #Asks the user for an input
    myw = input('Please guess one letter from the word: ').upper()
    #blank list where search results will be stored
    result=[]
    #if alphabet and length is 1 then add to used list else try again
    if myw.isalpha() is True and len(myw) == 1:
        try:
            ind = usedlist.index(myw)
            print('\nThis word has already been used. Please try again.\n')
            continue
        except:
            usedlist.append(myw)
    else:
        print('\nThis is not a valid input. Please try again.\n')
        continue
    #match user input with the letters in the word
    for c,l in enumerate(wordin):
        if myw == l:
            result.append(c)
    #If the letter does not match x is incremented, i.e. fewer chances left
    #if the letter matches it replaces the dash
    if result == []:
        x = x+1
        print("\n",hangconv(dashword),stages(x))
        if x == 5:
            print("SORRY!! You were unable to guess the word. Correct word was",theword)
            break
    else:
        for z in result:
            dashword[z]=myw
        print("\n",hangconv(dashword),stages(x))
    #print(x)
    #If no dashes left congratulation message is printed and loop breaks
    try:
        ind = dashword.index("-")
    except:
        print("CONGRATULATIONS!! You have successfully guessed the word.")
        break
print("\nGAME ENDS")

start=0
end=100
respond='h'

print "Think of a number in 1-100: "

middle=50

while respond!='c':
    
    print "Is your secret number %d ?" %middle
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
    print "Enter 'c' to indicate I guessed correctly."
    respond=raw_input()
    if respond=='c':
        print "Game over. Your secret number was %d. "%middle
        break
    
    if respond=='h':
        end = middle-1
        middle=start + (end-start+1)/2
    elif respond=='l':
        start=middle +1
        middle=middle + (end-start+1)/2
    

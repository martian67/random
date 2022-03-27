print("Enter Word Master's Name: ")
p1 = input()
print('hello, ' + p1)
print('welcome to wordsle')

while True:
    print(p1 + ', without showing the other players, enter a word: ')
    word = input()
    l = len(word)
    print('hello players and welcome')

    while True:
        def score(guess):
                crt_chr = 0
                crt_spot = 0
                for x in word:              
                    if x in guess:
                        crt_chr = crt_chr + 1
                for y in range(l):
                    if word[y] == guess[y]:
                        crt_spot = crt_spot + 1 
                return crt_chr, crt_spot
        print('please talk amongst yourselves and enter a guess that is ' + str(l) + ' letters long: ')
        guess = input()
        if len(guess) != l:
            print('guess is incorrect length!')
        elif score(guess) == (l,l):
            print('congrats you got it! :D')
            print('would you like to play again? y/n')
            ply_agn = input()
            break
        else:
            print(score(guess))
    if ply_agn == 'y':
        print('\r')
    else:
        break
                
        


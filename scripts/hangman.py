import random

print("H A N G M A N")
while True:
    gameStart = input(
        'Type "play" to play the game, "exit" to quit: ').lower().strip()
    if gameStart == "play":
        print("")
        wordList = [
            'python', 'java', 'kotlin', 'javascript', 'rainbow', 'computer',
            'science', 'programming', 'python', 'mathematics', 'player',
            'condition', 'reverse', 'water', 'board', 'geeks'
        ]
        guess = random.choice(wordList)
        dashStr = "-" * len(guess)
        print(dashStr)
        guessedList = []
        lives = 8
        while lives > 0:
            word = input("Input a letter:  ").lower().strip()
            if len(word) > 1 or len(word) == 0:
                print("You should input a single letter")

            if word in guessedList:
                print("You already typed this letter", end='\n' * 2)
                print(dashStr)
                continue
            else:
                guessedList.append(word)
            if lives == 0:
                print("You are hanged!", end='\n' * 2)
                break
            if word in guess:
                for j in range(len(guess)):
                    if guess[j] == word:
                        dashStr = dashStr[:j] + word + dashStr[j + 1:]
                if dashStr == guess:
                    pass
                else:
                    print("")
                    print(dashStr)
                if dashStr == guess:
                    print("You guessed the word " + dashStr + "!")
                    print("You survived!", end='\n' * 2)
                    break
            else:
                if len(word) > 1 or not word.islower():
                    pass
                elif word in guessedList and word in guess:
                    pass
                else:
                    lives -= 1
                    print("No such letter in the word")
                if lives == 0:
                    pass
                else:
                    print("")
                    print(dashStr)
            if lives == 0:
                print("You are hanged!", end='\n')
                break
    else:
        break

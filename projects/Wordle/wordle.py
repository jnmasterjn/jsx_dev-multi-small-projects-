import random

def read_word():
    file=open("./words.txt",encoding="utf-8") #.的意思是在同一個資料夾底下;"words.txt"是檔案位置不是名稱
    words=[]

    for line in file:
        words.append(line.strip()) #strip可以把string開頭結尾刪掉

    file.close() #要記得關檔案
    return words

words=read_word()

def get_random_word_from_list(words: list):
    random_index = random.randint(0, len(words) - 1)
    random_word = words[random_index]
    return random_word


#below is driving code
read_file = read_word()
random_word=get_random_word_from_list(read_file)
game_count=1

print("\n RULES: ! for right character but wrong spot; ? for wrong word")

while(True):
    print("\n Round", game_count)
    guess=input("\n Guess a 5-character-word (type q to end):\n")
    #print("random word: "+ random_word) for testing only 

    if guess == "q":
        print("thanks for playing")
        break 

    if guess == random_word:
        print("u win")
        break 

    
    if len(guess)==5:
        
        for i in range (0,5):
            if guess[i] == random_word[i]:
                print(guess[i],end=" ")

            elif guess[i] in random_word:
                print("!",end=" ")
            
            else:
                print("?",end=" ")

    else:
        print("must be 5-CHARACTER-LONG")


    game_count=game_count+1
    
    if game_count>5:
        print("u lost")
        break


    print()
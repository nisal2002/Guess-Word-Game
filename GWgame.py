secret="car"
turns=len(secret)+2
storage=""

print("What is GUESS THE WORD?")
print("You have",turns, "turns.Predict the word by guessing character by character.")

for i in (0,len(secret)):
    print(i*"_",end="")
    storage=i*"_"
print()

while turns!=0:
    if storage==secret:
        print("You Won")
        break
    guess=input("Enter guess letter: ")
    i=0
    for letter in secret:
        if guess==letter:
            storage=storage[:i]+guess+storage[i+1:]

        i+=1
    print(storage)
    turns-=1
else:
    print("Run out of turns!")


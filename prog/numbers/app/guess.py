import random
import secrets

random.seed(secrets.SystemRandom().randint(0, 10000))
print("Let's play a game. If you can tell me what number I am thinking of, I will give you the flag.")
while True:
    guess = random.getrandbits(32)
    number = input("What number am I thinking of? ")
    try:
        if int(number) == guess:
            print("I am impressed. Here is your flag: dvCTF{tw1st3d_numb3rs}")
            exit()
        else:
            print(f"Nice try! I was thinking of {guess}")
    except:
        print("What is this?? Numbers only!")

import os 
import time 
from itertools import cycle


styles = ["slant", "standard", "big"]
text = "Welcome!"

def animate():
    for style in cycle(styles):
        os.system("clear")
        os.system(f"figlet -f {style} '{text}'")
        time.sleep(0.5)
    bored()

def bored():
    while True:
        print("Bored",end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(1)
    

if __name__ == "__main__":
    animate()
    #bored()


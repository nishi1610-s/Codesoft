import random

u = 0
c = 0

def game(n):
    global u, c
    ch = ["stone", "paper", "scissor"]

    while u < n and c < n:
        uch = input("Enter your choice (stone/paper/scissor): ").lower()
        if uch not in ch:
            print("Invalid choice! Try again.")
            continue

        cch = random.choice(ch)
        print("Computer's choice is:", cch)

        if uch == cch:
            print("It's a tie.")
        elif (uch == "stone" and cch == "scissor") or \
             (uch == "scissor" and cch == "paper") or \
             (uch == "paper" and cch == "stone"):
            u += 1
            print("You scored one point!")
        else:
            c += 1
            print("Computer scored one point!")

        print(f"Score => You: {u} | Computer: {c}\n")

def result(n):
    if u == n:
        print(f" You won the game by scoring {u} points!")
    else:
        print(f" Computer won the game by scoring {c} points!")

def main():
    n = int(input("Enter the points to win the game: "))
    game(n)
    result(n)

if __name__ == "__main__":
    main()

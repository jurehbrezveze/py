import random

def dice(i):
    if(i==1):
        print("┌───┐")
        print("│O  │")
        print("│   │")
        print("│  O│")
        print("└───┘")
    if(i==2):
        print("┌───┐")
        print("│O  │")
        print("│   │")
        print("│  O│")
        print("└───┘")
    if(i==3):
        print("┌───┐")
        print("│O  │")
        print("│ O │")
        print("│  O│")
        print("└───┘")
    if(i==4):
        print("┌───┐")
        print("│O O│")
        print("│   │")
        print("│O O│")
        print("└───┘")
    if(i==5):
        print("┌───┐")
        print("│O O│")
        print("│ O │")
        print("│O O│")
        print("└───┘")
    if(i==6):
        print("┌───┐")
        print("│O O│")
        print("│O O│")
        print("│O O│")
        print("└───┘")

def slots(coins):
    print(" ________ ")
    print("|        \ ")
    print(" \$$$$$$$$")
    print("    /  $$ ")
    print("   /  $$  ")
    print("  /  $$   ")
    print(" /  $$    ")
    print("|  $$     ")
    print("\$$      ")

    print("          ")
    print("  _$      ")
    print("   \$     ")
    print("    |$    ")
    print("    /$    ")
    print(" __| \$_  ")
    print("/  $ /  $ ")
    print("|   $|   $")
    print("\$$$ \$$$ ")
    return(coins)

def kocke(coins):

    coins = coins - 1

    t = 0
    j = int(input("Koliko bo seštevek meta dveh kock?\n"))

    i = random.randint(1,6)
    dice(i)
    t = t + i

    i = random.randint(1,6)
    dice(i)
    t = t + i

    if(j==t):
        print("Zmagal si, dobiš 10 kovancev")
        coins = coins + 10
    else:
        print("Ni ti uspelo (womp womp)")

    return(coins)
def main():
    print("░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░")
    print("██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗")
    print("██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║")
    print("██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║")
    print("╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝")
    print("░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░\n\n\n\n\n")
    coins = 10
    while(True):
        print(f"Imaš >{coins}< kovancev")
        i = int(input("Katero igro želiš igrati?\n 1 - kockanje (1 kovanec)\n 2 - slot mashine(3 kovanci)\n če si zadovoljen z svojimi dobički klikni ^C\n"))
        if(i==1):
            coins = kocke(coins)
        if(i==2):
            slots(coins)
        else:
            print("Te številke no v sistemu")



main()
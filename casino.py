import random
import sys
import time
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

    i = 1
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)
    for i in range(4):
        match i:
            case 1:
                match a:
                    case 1:
                        d = '🍋'
                    case 2:
                        d = '🔔'
                    case 3:
                        d = '⭐'
                    case 4:
                        d = '🍒'
                    case 5:
                        d = '7️'
            case 2:
                match b:
                    case 1:
                        e = '🍋'
                    case 2:
                        e = '🔔'
                    case 3:
                        e = '⭐'
                    case 4:
                        e = '🍒'
                    case 5:
                        e = '7️'
            case 3:
                match c:
                    case 1:
                        f = '🍋'
                    case 2:
                        f = '🔔'
                    case 3:
                        f = '⭐'
                    case 4:
                        f = '🍒'
                    case 5:
                        f = '7️'
    sys.stdout.write(f"\n\n{d}  {e}  {f}\n\n")
    match a:
        case b:
            coins=coins+3
        case c:
            coins=coins+3

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
        i = int(input("Katero igro želiš igrati?\n 1 - kockanje🎲 (1 kovanec)\n 2 - slot mashine🎰 (3 kovanci)\n če si zadovoljen z svojimi dobički vpiši kar koli drugegea\n"))
        if(i==1):
            coins = kocke(coins)
        if(i==2):
            slots(coins)
        else:
            print("Te številke no v sistemu")
            exit()



main()
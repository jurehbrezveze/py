import random
import sys
import time


def dice():
    s1 = ''
    s2 = ''
    s3 = ''
    s4 = ''
    s5 = ''
    t=0
    for i in range(2):
        i = random.randint(1,6)
        t=t+i
        if(i==1):
            s1=s1+"┌─────┐"
            s2=s2+"│     │"
            s3=s3+"│  O  │"
            s4=s4+"│     │"
            s5=s5+"└─────┘"
        if(i==2):
            s1=s1+"┌─────┐"
            s2=s2+"│ O   │"
            s3=s3+"│     │"
            s4=s4+"│   O │"
            s5=s5+"└─────┘"
        if(i==3):
            s1=s1+"┌─────┐"
            s2=s2+"│ O   │"
            s3=s3+"│  O  │"
            s4=s4+"│   O │"
            s5=s5+"└─────┘"
        if(i==4):
            s1=s1+"┌─────┐"
            s2=s2+"│ O O │"
            s3=s3+"│     │"
            s4=s4+"│ O O │"
            s5=s5+"└─────┘"
        if(i==5):
            s1=s1+"┌─────┐"
            s2=s2+"│ O O │"
            s3=s3+"│  O  │"
            s4=s4+"│ O O │"
            s5=s5+"└─────┘"
        if(i==6):
            s1=s1+"┌─────┐"
            s2=s2+"│ O O │"
            s3=s3+"│ O O │"
            s4=s4+"│ O O │"
            s5=s5+"└─────┘"

    print('\b',s1,'\n',s2,'\n',s3,'\n',s4,'\n',s5,'\n')

    return(t)
def slots(coins):
    coins = coins -3
    i = 1
    g = 0
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
    if a == b:
        coins=coins+4
        g=g+4
    if a == c:
        coins=coins+4
        g=g+4
    if b == c:
        coins=coins+4
        g=g+4
    if a == b == c:
        if a == 5:
            print("MEGA JACKPOT!!!\n")
            coins=coins+10
            g=g+10
        else:
            print("JACKPOT!!!\n")
    if g != 0:
        print(f"Dobil si {g} kovancev!!!\n")
    else:
        print("Več sreče prihondjič\n")

    return(coins)

def kocke(coins):

    coins = coins - 1

    t = 0
    j = int(input("Koliko bo seštevek meta dveh kock?\n"))

    t = t + dice()


    if(j==t):
        print("Zmagal si, dobiš 10 kovancev")
        coins = coins + 10
    else:
        print("Ni ti uspelo (womp womp)")

    return(coins)


def plinko(coins):

    a = [
        ['▲'],
        ['▲', '▲', '▲'],
        ['▲', '▲', '▲', '▲', '▲'],
        ['▲', '▲', '▲', '▲', '▲', '▲', '▲'],
        ['▲', '▲', '▲', '▲', '▲', '▲', '▲', '▲', '▲']
    ]
    # Initialize position
    x = 0  # Start in the middle

    for y in range(5):
        # Randomly decide to move left or right
        c = random.randint(0, 1)
        if c == 0 and x > 0:
            x -= 1  # Move left
        elif c == 1 and x < len(a[y]) - 1:
            x += 1  # Move right
        
        # Place coin at the current position
        a[y][x] = 'O'
        
        # Print board
        print('\n' * 10)
        for row in a:
            print(''.join(row).center(20))
        print('     4321001234')
        time.sleep(0.5)
        
        # Reset the current row back to ▲ after printing
        a[y][x] = '▲'
    
    # Determine multiplier based on the final position
    match x:
        case 0:
            print("x4")
            coins *= 4
        case 1:
            print("x3")
            coins *= 3
        case 2:
            print("x2")
            coins *= 2
        case 3:
            print("x1")
            coins *= 1
        case 4:
            print("x0")
            coins *= 0
        case 5:
            print("x1")
            coins *= 1
        case 6:
            print("x2")
            coins *= 2
        case 7:
            print("x3")
            coins *= 3
        case 8:
            print("x4")
            coins *= 4

    return coins


def main():
#    print("\033[1;32;40m\n")
    print("░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░")
    print("██╔══██╗██╔══██╗██╔════╝██▲████╗░██▲██╔══██╗")
    print("██▲░░╚═╝███████▲╚█████╗░██▲██╔██╗██▲██▲░░██▲")
    print("██▲░░██╗██╔══██▲░╚═══██╗██▲██▲╚████▲██▲░░██▲")
    print("╚█████╔╝██▲░░██▲██████╔╝██▲██▲░╚███▲╚█████╔╝")
    print("░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░\n\n\n\n")
    coins = 10
    while(True):
        print(f"Imaš >{coins}< kovancev")
        i = int(input("Katero igro želiš igrati?\n 1 - kockanje🎲 (1 kovanec)\n 2 - slot mashine🎰 (3 kovanci)\n 3 - plinko (po želji) \nče si zadovoljen z svojimi dobički vpiši kar koli drugegea\n"))
        if(i==1):
            coins = kocke(coins)
        elif(i==2):
            coins = slots(coins)
        elif(i==3):
            coins = plinko(coins)
        elif(i==69):
            coins = 100
        else:
            print("Te številke no v sistemu")
            exit()



main()

#    ▲
#   ▲▲▲
#  ▲▲▲▲▲
# ▲▲▲▲▲▲▲
#▲▲▲▲▲▲▲▲▲ 
#432101234
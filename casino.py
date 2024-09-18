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
    a=['┌'],['┌','┌'],['┌','┌','┌'],['┌','┌','┌','┌'],['┌','┌','┌','┌','┌']
    b=['┐'],['┐','┐'],['┐','┐','┐'],['┐','┐','┐','┐'],['┐','┐','┐','┐','┐']
    x=0
    y=0
    for y in range(5):
        c=random.randint(0,1)
        if x < y:
            if c != 0:
                x=x+1
        match x:
            case 0:
                a[0][y]='O'
            case 1:
                b[0][y]='O'
            case 2:
                a[1][y]='O'
            case 3:
                b[1][y]='O'
            case 4:
                a[2][y]='O'
            case 5:
                b[2][y]='O'
            case 6:
                a[3][y]='O'
            case 7:
                b[3][y]='O'
            case 8:
                a[4][y]='O'
            case 9:
                b[4][y]='O'
        print('\n\n\n\n\n\n\n\n\n\n')
        print(f'    {a[0][0]}{b[0][0]}')
        print(f'   {a[1][0]}{b[1][0]}{a[1][1]}{b[1][1]}')
        print(f'  {a[2][0]}{b[2][0]}{a[2][1]}{b[2][1]}{a[2][2]}{b[2][2]}')
        print(f' {a[3][0]}{b[3][0]}{a[3][1]}{b[3][1]}{a[3][2]}{b[3][2]}{a[3][3]}{b[3][3]}')
        print(f'{a[4][0]}{b[4][0]}{a[4][1]}{b[4][1]}{a[4][2]}{b[4][2]}{a[4][3]}{b[4][3]}{a[4][4]}{b[4][4]}')
        print(f'4321001234')
        a=['┌'],['┌','┌'],['┌','┌','┌'],['┌','┌','┌','┌'],['┌','┌','┌','┌','┌']
        b=['┐'],['┐','┐'],['┐','┐','┐'],['┐','┐','┐','┐'],['┐','┐','┐','┐','┐']
        time.sleep(0.5)
    print(x)
    match x:
        case 0:
            print("x4")
            coins=coins*4
        case 1:
            print("x3")
            coins=coins*3
        case 2:
            print("x2")
            coins=coins*2
        case 3:
            print("x1")
            coins=coins*1
        case 4:
            print("x0")
            coins=coins*0
        case 5:
            print("x0")
            coins=coins*0
        case 6:
            print("x1")
            coins=coins*1
        case 7:
            print("x2")
            coins=coins*2
        case 8:
            print("x3")
            coins=coins*3
        case 9:
            print("x4")
            coins=coins*4
    return(coins)
def main():
#    print("\033[1;32;40m\n")
    print("░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░")
    print("██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗")
    print("██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║")
    print("██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║")
    print("╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝")
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
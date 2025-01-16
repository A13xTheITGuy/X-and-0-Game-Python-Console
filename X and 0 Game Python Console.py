import numpy as np
import random as rand
arrX0=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1]) 
# I initialized with "-1" the positions that do not have a value
print('\nX and O game in Python!')

def game_display():
    # Display positions according to the current value in the matrix
    for i in range(0,9):
        if arrX0[i]==-1:
            print('-', end=' ')
        if arrX0[i]==0:
            print('0', end=' ')
        if arrX0[i]==1:
            print('X', end=' ')
        if ((i+1)%3==0) & (i!=8):
            print(end='\n')
            print('==========', end='\n')
        else:
            if(i!=8):
                print('|',end=' ')

def game_stop_X():
    # X on the main diagonal
    if (arrX0[0]==1) & (arrX0[4]==1) & (arrX0[8]==1):
        return 1
    # X on the secondary diagonal
    if (arrX0[2]==1) & (arrX0[4]==1) & (arrX0[6]==1):
        return 1
    # X on rows
    if (arrX0[0]==1) & (arrX0[1]==1) & (arrX0[2]==1):
        return 1
    if (arrX0[3]==1) & (arrX0[4]==1) & (arrX0[5]==1):
        return 1
    if (arrX0[6]==1) & (arrX0[7]==1) & (arrX0[8]==1):
        return 1
    # X on columns
    if (arrX0[0]==1) & (arrX0[3]==1) & (arrX0[6]==1):
        return 1
    if (arrX0[1]==1) & (arrX0[4]==1) & (arrX0[7]==1):
        return 1
    if (arrX0[2]==1) & (arrX0[5]==1) & (arrX0[8]==1):
        return 1
    
def game_stop_0():
    # 0 on the main diagonal
    if (arrX0[0]==0) & (arrX0[4]==0) & (arrX0[8]==0):
        return 1
    # 0 on the secondary diagonal
    if (arrX0[2]==0) & (arrX0[4]==0) & (arrX0[6]==0):
        return 1
    # 0 on rows
    if (arrX0[0]==0) & (arrX0[1]==0) & (arrX0[2]==0):
        return 1
    if (arrX0[3]==0) & (arrX0[4]==0) & (arrX0[5]==0):
        return 1
    if (arrX0[6]==0) & (arrX0[7]==0) & (arrX0[8]==0):
        return 1
    # 0 on columns
    if (arrX0[0]==0) & (arrX0[3]==0) & (arrX0[6]==0):
        return 1
    if (arrX0[1]==0) & (arrX0[4]==0) & (arrX0[7]==0):
        return 1
    if (arrX0[2]==0) & (arrX0[5]==0) & (arrX0[8]==0):
        return 1

def input_validation(inp):
    if (inp>=1) & (inp<=9):
        if arrX0[inp-1]==-1:
            return 1
        else:
            return 0
    else:
        return 0
    

cX=0
c0=0
Regame=1
while 1:
    if Regame==1:
        bot= int(input("Do you want to play against a player or a bot? (YES with bot = 1, YES with player = 0): "))      
    if bot==0:
        Regame=0
        print('\n')
        game_display()
        print('\n')
        count=0
        for i in arrX0:
            if arrX0[i]!=-1:
                count+=1
        if(count==9):
            print('No one is the winner!\n')
            break
        pozX=int(input("X Turn, enter a number from 1-9: ")) #pozX 
        while input_validation(pozX)==0:
            ok=0
            pozX=int(input("|ERROR| Invalid input ( must be in [1,9] and a position which was not introduced before! )\nX Turn, enter a number from 1-9: ")) #pozX 
        arrX0[pozX-1]=1 
        pass_g=-1  
        if game_stop_X()==1:
            print('\n')
            game_display()
            print('\n')
            print('The Winner is X!', end='\n')
            cX+=1
            arrX0=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1])
            print(f'Score ( X , 0 ): {cX} - {c0}', end='\n')
            Regame=int(input("Do you want to play again? ( YES = 1, NO = 0): ")) #poz0 
            if Regame==1:
                pass_g=1
            else:
                pass_g=0
                break
        if(Regame!=1):
            print('\n')
            game_display()
            print('\n')
            count=0
            for i in arrX0:
                if arrX0[i]!=-1:
                    count+=1
            if(count==9):
                print('No one is the winner!\n')
                break
            poz0=int(input("0 Turn, enter a number from 1-9: ")) #poz0 
            while input_validation(poz0)==0:
                poz0=int(input("|ERROR| Invalid input ( must be in [1,9] and a position which was not introduced before! )\n0 Turn, enter a number from 1-9: ")) #poz0
            arrX0[poz0-1]=0
            pass_g=-1  
            if game_stop_0()==1:
                print('\n')
                game_display()
                print('\n')
                print('The Winner is 0!', end='\n')
                c0+=1
                arrX0=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1])
                print(f'Score ( X , 0 ): {cX} - {c0}', end='\n')
                Regame=int(input("Do you want to play again? YES = 1, NO = 0): ")) 
                if Regame==1:
                    pass_g=1
                else:
                    pass_g=0
                    break
    else:
        Regame=0
        print('\n')
        game_display()
        print('\n')
        count=0
        for i in arrX0:
            if arrX0[i]!=-1:
                count+=1
        if(count==9):
            print('No one is the winner!\n')
            break
        pozX=int(input("X Turn, enter a number from 1-9: ")) #pozX 
        while input_validation(pozX)==0:
            ok=0
            pozX=int(input("|ERROR| Invalid input ( must be in [1,9] and a position which was not introduced before! )\nX Turn, enter a number from 1-9: ")) #pozX 
        arrX0[pozX-1]=1  
        pass_g=-1  
        if game_stop_X()==1:
            print('\n')
            game_display()
            print('\n')
            print('The Winner is X!', end='\n')
            cX+=1
            arrX0=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1])
            print(f'Score ( X , 0 ): {cX} - {c0}', end='\n')
            Regame=int(input("Do you want to play again? (YES = 1, NO = 0): ")) #poz0 
            if Regame==1:
                pass_g=1
            else:
                pass_g=0
                break
        if(Regame!=1):
            print('\n')
            game_display()
            print('\n')
            count=0
            for i in arrX0:
                if arrX0[i]!=-1:
                    count+=1
            if(count==9):
                print('No one is the winner!\n')
                break
            poz0=rand.randint(0,9)
            while input_validation(poz0)==0:
                poz0=rand.randrange(0,9,1)
            print(f"0 (bot) Turn, enter a number from 1-9: {poz0}") #poz0 
            arrX0[poz0-1]=0
            pass_g=-1  
            if game_stop_0()==1:
                print('\n')
                game_display()
                print('\n')
                print('The Winner is 0 (bot)!', end='\n')
                c0+=1
                arrX0=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1])
                print(f'Score ( X , 0 ): {cX} - {c0}', end='\n')
                Regame=int(input("Do you want to play again? (YES  = 1, NO = 0): ")) #poz0 
                if Regame==1:
                    pass_g=1
                else:
                    pass_g=0
                    break
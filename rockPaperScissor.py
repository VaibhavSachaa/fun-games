#it's a rock paper scissor game , in which both the players have to choose a number   to open all the chances of selecting rock , paper , or scissor and then accordingly they have to select their secret bit position in the number they have previously chosen and  the modulus of the value the that bit position with 3 will one of the choices (rock , paper , or scissor) where 0 is rock, 1 is paper and 2 is scissor that players already know
#just to avoid any cheating it's made like that :)
 


def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player one wins")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player two wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("Player two wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player one wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player two wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player one wins") 
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Rock',1:'Paper',2:'Scissor'}
while(1):
    num1=input("Player one, Enter your choice")
    num2=input("Player two, Enter your choice")
    bit1=int(input("Player one ,Enter the secret bit position"))
    bit2=int(input("Player two ,Enter the secret bit position"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n")
    if(ch=='n'):
        break

import random
chances=0
yourpoint=0
computerpoint=0
totalchancesleft=3
print('\t \t \t welcome to Rock,Paper,Scissor Game\n')
while chances<totalchancesleft:
        x=str(input('Please Enter Rock,Paper,or scissor: '))
        list=['rock','paper','scissor\n']
        x1=random.choice(list)
        print('your guess is ',x,'compuer guess is',x1)
        if x==x1:
            print('draw')
        elif x==list[0] and x1==list[1]:
            computerpoint=computerpoint+1
            print('computer gets a point')    
        elif x==list[0] and x1==list[2]:
            yourpoint=yourpoint+1
            print('you gets a point')
        elif x==list[1] and x1==list[0]:
            yourpoint=yourpoint+1
            print('You gets a point')
        elif x==list[1] and x1==list[2]:
            computerpoint=computerpoint+1
            print('computer gets a point')
        elif x==list[2] and x1==list[0]:
            computerpoint=computerpoint+1
            print('computer gets a point')
        elif x==list[2] and x1==list[1]:
            yourpoint=yourpoint+1
        print('yourpoint',yourpoint,'computerpoint',computerpoint,)
        chances=chances+1
        print('Total chances left',totalchancesleft-chances,'\n')
        if chances==3:
            print('Game over\n')
if computerpoint>yourpoint:
        print('computer wins the game')
elif yourpoint>computerpoint:
        print('you wins the game  congratulation')
elif computerpoint==yourpoint:
  print('Match Draw')
            
        
    
    

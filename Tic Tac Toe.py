def clear():
    import os
    import time
    os.system('clear')
    #os.system("ls")
    time.sleep(2)

def turn():
  import random
  return random.randint(1,2)

def check_point(k):
    if s[7]==k and s[8]==k and s[9]==k:
        return 1
    elif s[4]==k and s[5]==k and s[6]==k:
        return 1    
    elif s[1]==k and s[2]==k and s[3]==k:
        return 1 
    elif s[7]==k and s[4]==k and s[1]==k:
        return 1 
    elif s[8]==k and s[5]==k and s[2]==k:
        return 1        
    elif s[9]==k and s[6]==k and s[3]==k:
        return 1
    elif s[7]==k and s[5]==k and s[3]==k:
        return 1        
    elif s[9]==k and s[5]==k and s[1]==k:
        return 1        
s=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board():
    print("   |   |   ")
    print(f" {s[7]} | {s[8]} | {s[9]} ")
    print("   |   |   ")
    print("-------------")
    print("   |   |   ")
    print(f" {s[4]} | {s[5]} | {s[6]} ")
    print("   |   |   ")
    print("-------------")
    print("   |   |   ")
    print(f" {s[1]} | {s[2]} | {s[3]} ")
    print("   |   |   ")
     
 
def player_in(fv,sv,ft,st):
    p1p=0
    p2p=0
    
    for q in range(0,6):
     
     def part1(): 
       user=int(input("pos:"))
       if s[user]==' ':
          print("\n")
          s[user]=fv
          k=fv
          clear()
          display_board()
          return check_point(k)
          
       else:
         part1()
       
     def part2():     
       user=int(input("pos:"))
       if s[user]==' ':
          print("\n")
          s[user]=sv
          k=sv
          clear()
          display_board()
          return check_point(k)
          
       else:
           part2() 
     
     p1p=part1()
     if p1p==1:
           print(f"{ft} won")
           break
     if q==4:
           break   
     p2p=part2()      
    
     if p2p==1:
           print(f"{st} won")
           break 
    
    print("tie")           
def begin():        
  player1=input("Do player1 want X or 0:")  
  if player1=='X':
       player2=0
  else:
       player2='X'
  t=turn()
  if turn==1:
    ft="player1"
    fv=player1
    st="player2"
    sv=player2
  else:
    ft="player2"
    fv=player2
    st="player1"
    sv=player1
  print(ft+" will have first turn")    
  sol=input("Are u ready to play?Enter Yes or No:" )
  print("\n")
  if sol=="Yes":
       display_board()
  player_in(fv,sv,ft,st) 
  return input("do u want to play again?Enter Yes or No:")

  
p=begin()

while p=='Yes':
  clear()
  s=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  p=begin()






import os
from datetime import datetime
import random

def confirm_five_stack():
    goons=collect_goons()
    for i in range(len(goons)):
    	ready = True; print(f"Player {i+1}: {goons[i]}")
    	is_ready = input("Are they ready: ")
    	if(is_ready != 'y'):
    		ready = False; print(f"Player {i+1}: {goons[i]} - {ready}")
    	if not ready:
            print(f"Five stack is not ready. {goons[i]} is baiting."); break
    if ready:
        print("Five stack is ready.")
    	
    
def collect_goons():
   f = open('tat.txt', 'r')
   goons=[]; len_count=0; goons_playing=[]
   for line in f:
        len_count+=1
        goons.append(line)
   for i in range(5):
        player = random.randint(0, len_count-1)
        goons_playing.append(goons[player])
   return(goons_playing)

def main():
    current_time =  datetime.now(); now = current_time.strftime("%H:%M:%S")
    print(f"Erm Who Tryna Queue? It is {now} AKA Val Time.")
    confirm_five_stack()

main()

import sys
sys.path.append('C:/Users/Joseph H. Hendrickso/AppData/Local/Programs/Python/Python37/Tools')
sys.path.append('C:/Users/Joseph H. Hendrickso/Documents/python')
from joe_graphics_utilities import *
from graphics import *
from random import randint
import math


def show_chests(chests,win):
    clrs=["white","blue","purple"]
    for i in range(3):
        print(chests[i])
        dot(win,chests[i],clr=clrs[i])

def copy_list(l):
    m = []
    for i in l:
        m = m + [i]
    return m

def get_chest_distance(chests,pt):
    small = 1000000
    small_chest = 7
    for i in range(len(chests)):
        d = distance(pt, chests[i])
        if d < small:
            small=d
            small_chest = i
    return [small,small_chest]   

def get_chests(number_of_chests,win_size):
    a = []
    for i in range(number_of_chests):
        x = randint(-win_size,win_size)
        y = randint(-win_size,win_size)
        a = a + [Point(x,y)]
    return a


def strip_input(x):
    
    # make sure we have at least one digit
    y="0"
    
    if len(x) > 0:
              
        #remove leading blanks
        for i in range(len(x)):
            if x[i] != " ":
                break
        x = x[i:len(x)]

        #make sure a legal minus sign gets copied 
        if x[0] == "-":
            y ="-"

        #Only accept digits and one decimal point 
        num_of_decimal_points = 0
        for i in range(len(x)):
            if x[i] in "1234567890":
                y = y+x[i]
            elif x[i] == "." and num_of_decimal_points == 0:
                y = y+x[i]
                num_of_decimal_points = 1
                 
    return y


def main():
    win = GraphWin('sonar',600,600)
    win_size = 300
    win.setCoords(-win_size,-win_size,win_size,win_size)
    draw_axes(win)
    number_of_chests = 3
    number_of_sonars = 20
    chests = get_chests(number_of_chests,win_size)
    fixed_chests = copy_list(chests)
    hit_distance = 15
    cir_list = []
    gold = 0
    playing = True
    while playing:
        print("Enter the x and y coordinates of the sonar one at a time: ")
        x1 = input("    x:")

        #For debug, lets us show where chests are
        if len(x1)>0 and x1[0] == "s":
           tmp = input("Do you want the chests displayed? (y/n) ")
           if tmp == 'y':
               show_chests(fixed_chests,win)
               continue
        y1 = input("    y:")

        #ensure we don't crash on bad input
        x = strip_input(x1)
        y = strip_input(y1)
        number_of_sonars = number_of_sonars - 1
        sonar_data = get_chest_distance(chests,Point(x,y))
        if sonar_data[0] <=  hit_distance:
           dot(win,Point(x,y),clr="green")
           gold = gold + 20
           print("You have ",gold," gold coins!")
           chests.remove(chests[sonar_data[1]])
           for j in cir_list:
               if j[1] > sonar_data[1]:
                   j[1] == j[1]-1
           for i in cir_list:
               if sonar_data[1] == i[1]:
                   i[0].setOutline('yellow')
           for i in cir_list:
               if sonar_data[1] == i[1]:
                   cir_list.remove(i)
        else: 
            dot(win,Point(x,y),clr="red")
            cir = Circle(Point(x,y),sonar_data[0])
            cir.setOutline('blue')
            cir.draw(win)
            cir_list = cir_list + [[cir, sonar_data[1]]]
        if len(chests) == 0:
            print ("\n\nConratulations.\n You won")
            playing = False
        elif number_of_sonars <= 0:
            print("Sorry.  Your are out of sonars.")
          
                  
            
        
                         




main()


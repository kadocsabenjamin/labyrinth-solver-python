import numpy as np

 

def bejar(x,y,tav):
   
    matrix[[y],[x]] = tav
    if y == cely and x == celx:
        return
   
    if y>0:            
        if matrix[[y-1],[x]] == -2 or matrix[[y-1],[x]] > tav+1:
            bejar(x,y-1,tav+1)
    if y<ymax-1:
        if matrix[[y+1],[x]] == -2 or matrix[[y+1],[x]] > tav+1:
            bejar(x,y+1,tav+1)
    if x>0:
        if matrix[[y],[x-1]] == -2 or matrix[[y],[x-1]] > tav+1:
            bejar(x-1,y,tav+1)
    if x<xmax-1:
        if matrix[[y],[x+1]] == -2 or matrix[[y],[x+1]] > tav+1:
            bejar(x+1,y,tav+1)
               
def utrajzolo(x,y):
   
    tav = matrix[[y],[x]]
   
    #print(tav)
    str = tomb[y]
    lista = list(str)
    lista[x] = 'o'
    str = ''.join(lista)
    tomb[y] = str
    if tav == 0:
        return
     
    if y>0:            
        if matrix[[y-1],[x]] == tav-1:
            print(" ",tav)
            utrajzolo(x,y-1)
            return
           
    if y<ymax-1:
        if matrix[[y+1],[x]] == tav-1:
            print("  ",tav)
            utrajzolo(x,y+1)
            return
           
    if x>0:
        if matrix[[y],[x-1]] == tav-1:
            print("   ",tav)
            utrajzolo(x-1,y)
            return
             
    if x<xmax-1:
        if matrix[[y],[x+1]] == tav-1:
            print("    ",tav)
            utrajzolo(x+1,y)
            return
         
   
   


xmax = 64
ymax = 31


matrix = np.zeros((ymax, xmax))
tomb = open('lab.txt').read().strip().split('\n')
megvan = False
for y in range(0,ymax):
    str = tomb[y]
    for x in range(0,xmax):
        if str[x] == '+' or str[x] == '|' or  str[x] == '-':
            matrix[[y],[x]] = -3
        if str[x] == ' ':
            matrix[[y],[x]] = -2
        if str[x] == 'x' and megvan == False:
            matrix[[y],[x]] = -2
            megvan = True
            startx = x
            starty = y
        if str[x] == 'x' and megvan == True:
            matrix[[y],[x]] = -2
            celx = x
            cely = y
   
bejar(startx,starty,0)
print(matrix)
utrajzolo(celx,cely)

for y in range(0,ymax):
    print(tomb[y])
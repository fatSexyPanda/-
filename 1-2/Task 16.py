#x0 = 0
#y0 = 0
x = float(input())
y = float(input())
# (x-1)**(x-1) + y**y = 4
# (x-1)**(x-1) + y**y = 1
#  abs(x - 4) < 2 and abs(y - 2) < 3
#Если точка попала только в область кольца выведите: yes no
#Если точка попала только в область прямоугольника выведите: no yes
#Если точка попала в область кольца и прямоугольника выведите: yes yes
#Если точка вне фигур выведите: no no

if (x-1)**2 + y**2 <= 4 and (x-1)**2 + y**2 >= 1 and abs(x - 4) < 2 and abs(y - 2) < 3:
    print ('yes',' ','yes')
    exit()
if (x-1)**2 + y**2 <= 4 and (x-1)**2 + y**2 >= 1:
    print ('yes',' ','no')
if   abs(x - 4) < 2 and abs(y - 2) < 3:
    print('no', ' ', 'yes')
else:
    print('no', ' ', 'no')
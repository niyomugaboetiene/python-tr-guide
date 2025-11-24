# star pyramid

for col in range(1, 9):
    for row in range(col):
        print("*", end="")
    print()

'''
*
**
***
****
*****
******
*******
********
'''
for col in range(9, 0, -1 ):
    for row in range(col):
        print("*", end="")
    print()

'''
*********
********
*******
******
*****
****
***
**
*
'''

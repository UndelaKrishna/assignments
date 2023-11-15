

rows = int(input('Enter number of rows: '))


for i in range(rows):
    for j in range(i,rows):
        print(' ',end='')
    
    for k in range(i+1):
        print('*',end='')

    print()

for i in range(rows,0,-1):
    for j in range(i,rows+1):
        print(' ',end='')
    
    for k in range(i):
        print('*',end='')
    print()
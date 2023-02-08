import copy

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

HEIGHT = 9
WIDTH = 6

print_list = copy.deepcopy(grid)
for i in range(HEIGHT):
    for j in range(WIDTH):
        print(print_list[i][j], end=' ')
    
    print()


print('T')
print('T')
print(), print('T')
print('T')
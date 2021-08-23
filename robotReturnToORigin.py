#time - O(N) as we just do a loop
#Space - O(1) we dont create any additional memory

def judgeCircle(moves):
    x = 0
    y = 0
    for move in moves:
        if(move == 'U'):
            y = y+1
        if (move == 'R'):
            x = x+1
        if (move == 'D'):
            y = y - 1
        if (move == 'L'):
            x = x - 1

    return x == 0 and  y == 0

# OR
# if moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D"):
#     return True
# else:
#     return False
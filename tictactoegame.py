

# board = ["1","2","3","4","5","6","7","8","9"]

# print(board[0]+"|"+board[1]+"|"+board[2])
# print("-"+"|"+"-"+"|"+"-")
# print(board[3]+"|"+board[4]+"|"+board[5])
# print("-"+"|"+"-"+"|"+"-")
# print(board[6]+"|"+board[7]+"|"+board[8])

for x in range(5):
    for y in range(5-x):
        print("*",end="")
    print()



    

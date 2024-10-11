from random import randrange

board_status = [1, 2, 3], [4,'X',6], [7,8,9]
occupied_fields = []
def dislpay_board(board_status):
    header_row =  "+-------+ +-------+ +-------+"
    empty_row = "|-------| |-------| |-------|"
    value_row = ""
    for i in range(len(board_status)):
        print(header_row)
        print(empty_row)
        value_row = ""        
        for n in board_status[i]:
            value_row += "|   " + str(n) + "   | "
        print('\x1b[6;30;42m' + value_row + '\x1b[0m', end="\n", )
        print(empty_row)        
        print(header_row)
    print("\n-----------------------------\n")

def enter_move(board_status):
    while True:
        try: 
            pos = int(input("Enter the board position (1 to 9): "))
            line = (pos -1) // 3
            col = (pos -1) % 3
            if board_status[line][col] == 'X' or board_status[line][col] == 'O':
                print("Position already occupied, please chose another.")
            else: 
                board_status[line][col] = "O"
                dislpay_board(board_status)
                draw_move(board_status)
                break
        except: 
            print("Mysterious error!")
            enter_move(board_status)

def make_list_of_free_fields(board_status):
    return 0
    
def draw_move(board_status):
    while True:
        try: 
            for i in range(10):
                pos = randrange(8)

            line = (pos -1) // 3
            col = (pos -1) % 3
            if board_status[line][col] == 'X' or board_status[line][col] == 'O':
                print("Position already occupied, please chose another.")
            else: 
                board_status[line][col] = "X"
                dislpay_board(board_status)
                break
        except: 
            print("Mysterious error!")
            draw_move(board_status)

def victory_for(board_status sign):
    

dislpay_board(board_status)
enter_move(board_status)








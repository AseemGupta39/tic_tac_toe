from os import system,name
from time import sleep 
class Player:
    def __init__(self,symbol) -> None:
        self.name = ""
        self.move = symbol

    def ask_name(self):
        while self.name == "":
            self.name = input("Enter Name: ")

    def ask_to_move(self):
        print(f"\n{self.name} your chance has come\nPlease Enter your move\n")

class Grid:
    def __init__(self) -> None:
        self.mat = [[(row+1,col+1) for col in range(3)] for row in range(3)]
        self.visited = [[False for _ in range(3)] for _ in range(3)]

    def print_mat(self):
        print()
        for row in range(3):
            print(*self.mat[row],sep = "   ")
        print()

    @staticmethod
    def is_valid_box(row,col):
        return  1 <= row <= 3 and 1 <= col <= 3

    def take_input(self):
        while True:
            try:
                row , col = int(input("Enter row: ")),int(input("Enter col: "))
                if not self.is_valid_box(row,col):
                    print("\nEnter valid box position:\n")
                    continue

                row = row - 1
                col = col - 1

                return row,col

            except Exception as e:
                print("\n\n",e,"\n\n")

    def combination(self,r1,c1,r2,c2,r3,c3):
        return self.mat[r1][c1] == self.mat[r2][c2] == self.mat[r3][c3]

    def check_for_win(self):
        win_list = [
                    [0,0,0,1,0,2],
                    [1,0,1,1,1,2],  # Horizontal lines
                    [2,0,2,1,2,2],

                    [0,0,1,0,2,0],
                    [0,1,1,1,2,1], # Vertical lines
                    [0,2,1,2,2,2],

                    [0,0,1,1,2,2], # Diagnol lines
                    [0,2,1,1,2,0]
                    ]

        for _ in win_list:
            r1,c1,r2,c2,r3,c3 = _
            if self.combination(r1,c1,r2,c2,r3,c3):
               return True
        return False 


    def fill_box(self,player:Player):
        system('cls' if name == 'nt' else 'clear')  # Clears the console


        self.print_mat()
        player.ask_to_move()
        row, col = self.take_input() 

        if not self.visited[row][col]:
            self.mat[row][col] = player.move
            self.visited[row][col] = True

            if self.check_for_win():
                self.print_mat()
                print(f"{player.name} you won the game ")
                exit()
        else:
            print("\nIt's already filled.\nChoose another unfilled box\n") 
            sleep(5)
            self.fill_box(player)


    @staticmethod
    def play(grid,player_1:Player,player_2:Player):
        print(player_1.name,player_2.name)
        count = 0

        while count <= 9:
            player_1.ask_to_move()

            grid.fill_box(player_1)
            count+=1

            if count==9:
                print(f"\nIt's a tie between {player_1.name} and {player_2.name}")
                exit()

            player_2.ask_to_move()

            grid.fill_box(player_2)
            count+=1


grid1 = Grid()

player_1 = Player('  X ')
print("Player 1 ")
player_1.ask_name()

player_2 = Player('  O ')
print("Player 2 ")
player_2.ask_name()

Grid.play(grid1,player_1,player_2)

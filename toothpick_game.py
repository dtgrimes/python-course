print("Welcome To The Game!")
print("********************")
num_left = 13
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

while True:
    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    p1_choice = int(input(f"{player1_name}, how many toothpicks do you take? "))
    num_left -= p1_choice
    if num_left <= 0:
        print(f"{player1_name} wins the game!")
        break

    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    p2_choice = int(input(f"{player2_name}, how many toothpicks do you take? "))
    num_left -= p2_choice
    if num_left <= 0:
        print(f"{player2_name} wins the game!")
        break

print("GAME OVER!")

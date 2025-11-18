# Loop untuk main lagi atau tidak
while True:
    tictactoe_start()
    # Setelah permainan selesai, tanya apakah ingin main lagi
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            break  # Main lagi
        elif play_again == 'n':
            print("Thanks for playing!")
            exit()  # Keluar dari program
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
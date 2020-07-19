'''
HW01
Yuchen_Yao
This is the assignment that only use the if/else statements to cmplete a Rock/Paper/Scissors game
'''

from random import choice


def get_human_move() -> str:
    valid_input: list = ['R', 'P', 'S', 'Q']
    human_move: str = input("please choose 'R' for rock, 'P' for paper, 'S' for scissors or 'Q' for quit: ").upper()
    while human_move not in valid_input:
        print("Invalid input.")
        human_move = input("please choose 'R' for rock, 'P' for paper, 'S' for scissors or 'Q' for quit: ").upper()
    return human_move


def get_computer_move() -> str:
    computer_move: str = choice(['R', 'P', 'S'])
    return computer_move


def play_game() -> None:
    human: str = get_human_move()

    while human != 'Q':
        computer = get_computer_move()

        if human != computer:
            if human == 'R' and computer == 'S':
                print('rock beats scissors - you win!')
            elif human == 'P' and computer == 'R':
                print('paper beats rock - you win!')
            elif human == 'S' and computer == 'P':
                print('scissors beats paper - you win!')
            elif human == 'R' and computer == 'P':
                print('paper beats rock - I win!')
            elif human == 'P' and computer == 'S':
                print('scissors beats paper - I win!')
            elif human == 'S' and computer == 'R':
                print('rock beats scissors - I win!')

        else:
            print(f'Tie: we both chose {computer}')
        human = get_human_move()

    print('game over')


def main() -> None:
    play_game()


if __name__ == '__main__':
    main()

from random import randint
from time import sleep

from russian_names import RussianNames


def choose_game_mode():
    is_correct_game_mode = False
    while not is_correct_game_mode:
        game_mode = input("Выбери игровой режим (1 - со вторым игроком, 2 - с ботом): ")
        if game_mode == '1' or game_mode == '2':
            is_correct_game_mode = True
            return game_mode
        else:
            print("Пожалуйста, введи то, что тебя просят.")


def enter_players_name(game_mode):
    is_correct_names_input = False
    if game_mode == '1':
        print("Ты выбрал режим игры со вторым игроком.")
        while not is_correct_names_input:
            first_player_name = input("Игрок 1, пожалуйста, введи свое имя: ")
            second_player_name = input("Игрок 2, пожалуйста, введи свое имя: ")
            if len(first_player_name) == 0 or ' ' in first_player_name:
                print("Имя не может быть пустым, друг.")
            elif len(second_player_name) == 0 or ' ' in second_player_name:
                print("Имя не может быть пустым, друг.")
            else:
                is_correct_names_input = True
                return [first_player_name, second_player_name]
    else:
        print("Ты выбрал режим игры с ботом.")
        while not is_correct_names_input:
            player_name = input("Игрок, пожалуйста, введи свое имя: ")
            if len(player_name) == 0 or ' ' in player_name:
                print("Имя не может быть пустым, друг.")
            else:
                is_correct_names_input = True
                return player_name


def input_cell_number(player, field):
    is_correct_input = False
    while not is_correct_input:
        try:
            cell_number = int(input(f"{player}, введи номер клетки (1-9): ")) - 1
        except ValueError:
            print("Дорогой друг, введи цифру от 1 до 9, пожалуйста.")
            continue
        else:
            if 0 <= cell_number <= 8:
                if field[cell_number] == 'x' or field[cell_number] == 'o':
                    print("Дорогой друг, эта клетка уже заполнена!")
                else:
                    is_correct_input = True
                    return cell_number
            else:
                print("Дорогой друг, введи цифру от 1 до 9, пожалуйста.")


def print_field(field):
    print(f"\n {field[0]} | {field[1]} | {field[2]}\n"
          f"-----------\n"
          f" {field[3]} | {field[4]} | {field[5]}\n"
          f"-----------\n"
          f" {field[6]} | {field[7]} | {field[8]}\n")


def check_winner(field):
    wining_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                          (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for coordinates in wining_coordinates:
        if field[coordinates[0]] == field[coordinates[1]] == field[coordinates[2]]:
            return field[coordinates[0]]
    return False


def create_bot_name(player):
    random_bot_name = RussianNames(surname=False, patronymic=False, gender=1, name_max_len=6).get_person()
    print(f"{player}, сегодня твой противник бот {random_bot_name}. Удачной игры!")
    return random_bot_name


def playing_with_bot(field, bot_name):
    print(f"{bot_name} ходит...")
    sleep(2)
    cell_not_busy = True
    random_number = randint(0, 8)
    while cell_not_busy:
        if field[random_number] == 'x' or field[random_number] == 'o':
            random_number = randint(0, 8)
        else:
            cell_not_busy = False
            print(f"{bot_name} выбрал клетку {random_number + 1}.")
            return random_number


def start_game():
    playing_field = ['1', '2', '3',
                     '4', '5', '6',
                     '7', '8', '9']
    is_game_over = False
    game_mode = choose_game_mode()
    active_player_number = 0
    if game_mode == '1':
        counter = 0
        players_list = enter_players_name(game_mode)
        print_field(playing_field)
        while not is_game_over:
            active_player = players_list[active_player_number]
            cell_number = input_cell_number(active_player, playing_field)
            if active_player_number == 0:
                playing_field[cell_number] = 'x'
                active_player_number = 1
            else:
                playing_field[cell_number] = 'o'
                active_player_number = 0
            print_field(playing_field)
            counter += 1
            if counter > 4:
                winner = check_winner(playing_field)
                if winner == 'x':
                    print(f"Поздравляю тебя, {players_list[0]}! Ты выиграл.")
                    break
                elif winner == 'o':
                    print(f"Поздравляю тебя, {players_list[1]}! Ты выиграл.")
                    break
            if counter == 9:
                print("Ничья, ребята.")
                break
    elif game_mode == '2':
        counter = 0
        player = enter_players_name(game_mode)
        bot_name = create_bot_name(player)
        print_field(playing_field)
        while not is_game_over:
            if active_player_number == 0:
                cell_number = input_cell_number(player, playing_field)
                playing_field[cell_number] = 'x'
                active_player_number = 1
            else:
                playing_field[playing_with_bot(playing_field, bot_name)] = 'o'
                active_player_number = 0
            print_field(playing_field)
            counter += 1
            if counter > 4:
                winner = check_winner(playing_field)
                if winner == 'x':
                    print(f"Поздравляю тебя, {player}! Ты выиграл.")
                    break
                elif winner == 'o':
                    print(f"Мне очень жаль, но тебя обыграл компьютер :( Бот {bot_name}, мои поздравления!")
                    break
            if counter == 9:
                print("Ничья, ребята.")
                break


def main():
    is_correct_wanna_play_input = False
    while not is_correct_wanna_play_input:
        wanna_play = input("Хочешь сыграть в крестики-нолики? Напиши 1, если да, 2 - если нет: ")
        if wanna_play == '1':
            start_game()
        elif wanna_play == '2':
            is_correct_wanna_play_input = True
            print("\n\nЛадно, пока.")
        else:
            print("Пожалуйста, введи то, что тебя просят.")
            continue


if __name__ == "__main__":
    main()

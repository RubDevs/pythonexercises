# Create a two-player rock-paper-scissors game, show a message of
# congratulations to winer and ask to start a new game
import getpass


def jugar():
    while True:
        player_one = getpass.getpass(
            'Player 1, R(rock) , P(paper), S(scissors): ')
        player_two = getpass.getpass(
            'Player 2, R(rock) , P(paper), S(scissors): ')
        if player_one not in ('R', 'r', 'P', 'p', 'S', 's') or player_two not in ('R', 'r', 'P', 'p', 'S', 's'):
            print('Valores no aceptados, por favor introduzca R,P o S')
        else:
            print(comprobar_ganador(player_one, player_two))
            while True:
                seguir = input("Quieres volver a jugar? y|n: ")
                if seguir in ('y', 'Y'):
                    break
                elif seguir in ('n', 'N'):
                    exit()
                else:
                    print('Opcion no valida')


def comprobar_ganador(p1, p2):
    if p1 == p2:
        return 'Empate!'
    if p1 in ('r', 'R'):
        if p2 in ('p', 'P'):
            return 'Ganador Player 2'
        else:
            return 'Ganador Player 1'
    if p1 in ('p', 'P'):
        if p2 in ('s', 'S'):
            return 'Ganador Player 2'
        else:
            return 'Ganador Player 1'
    if p1 in ('s', 'S'):
        if p2 in ('r', 'R'):
            return 'Ganador Player 2'
        else:
            return 'Ganador Player 1'


if __name__ == '__main__':
    jugar()

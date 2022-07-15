import math
import random

class Player:
    def __init__(self, letter):
        #Letra x ou o
        self.letter = letter

    #Queremos todos os jogadores tenham seus movimentos
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        # Pega um SOPT randômico e válido para outro movimento
        square = random.choice(game.avaliable_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turno. Entre como o movimento (0 - 9): ')
            # Vamos checar se este é o valor correto
            # E ver se é inteiro, se não for, então ele diz que é invalido
            # Se o spot não estiver disponível no quadro, falamos que ele é invalido
            try:
                val = int(square)
                if val not in game.avaliable_moves()
                    raise ValueError
                valid_square = True #Se for um sucesso é uma BOA!
            except ValueError:
                print('Quadrado inválido, tente novamente')
        return val
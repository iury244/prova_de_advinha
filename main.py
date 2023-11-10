class Time:
    def __init__(self, nometime, cidadetime, mascote):
        self.nometime = nometime
        self.cidadetime = cidadetime
        self.mascote = mascote

class Jogador:
    def __init__(self, nomejogador, timejogador, numerojogador):
        self.nomejogador = nomejogador
        self.timejogador = timejogador
        self.numerojogador = numerojogador

class Treinador:
    def __init__(self, treinado, preparador, auxiliar):
        self.treinado = treinado
        self.preparador = preparador
        self.auxiliar = auxiliar


while True:
    cadastro = int(input("""
    Escolha uma das opções:
    1 - Cadastrar Time
    2 - Cadastrar Jogador
    3 - Cadastrar Comissão Técnica
    0 - Encerrar cadastros
    """))

    match cadastro:
        case 1:
            time = input("Qual o Nome do Time:")
            cidade = input("Qual a Cidade do Time:")
            mascote = input("Qual o Mascote do time:")
        case 2:
            jogador = input("Qual o nome do jogar:")
            timedojogador = input("Qual o time atual do jogador ?")
            njogador = int(input("Qual o nomero do jogador:"))
        case 3:
            treinador = input("Nome do Técnico:")
            preparador = input("qual o nome do preparador fisico:")
            auxiliar = input("Nome do auxiliar:")
        case 0:
            print("\n" * 30)
            print("Sistema encerrado")
            break

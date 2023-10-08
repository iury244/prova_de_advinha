from random import randint
computador = randint(0, 10)
print("Sou seu comptador... Acabei de pensar em um número entre 0 a 10.")
print("Será que você consegue advinha qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite?"))
    palpites += 1
    if jogador == computador:
        acertou = True
    else: 
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print("acertou com {} tentaivas. Parabéns !!!".format(palpites))
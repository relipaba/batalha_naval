map_p1 = []
map_p2 = []
tamanho = 0
navios = 8
navio9 = 1
navio8 = 2
navio5 = 3
navio2 = 2
for i in range(65):
    map_p1.append(0)
    map_p2.append(0)
print("batalha naval 1d")
while navios != 0:
    print(map_p1)
    print("Jogador 1 começa, escolha qual navio escolher")
    opc = int(input(f"1 - navio de 9 casas ({navio9} restantes)\n2 - navio de 8 casas ({navio8} restantes)\n3 - navio de 5 casas ({navio5} restantes)\n4 - navio de 2 casas ({navio2} restantes)\n"))
    if opc == 1 and navio9 != 0:
        print("Escolha a posição do navio 9 casas")
        tamanho = 9
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p1[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p1[i] = 1
        navio9 -= 1
        navios -= 1
    if opc == 2 and navio8 != 0:
        print("Escolha a posição do navio 8 casas")
        tamanho = 8
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p1[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p1[i] = 1
        navio8 -= 1
        navios -= 1
    if opc == 3 and navio5 != 0:
        print("Escolha a posição do navio 5 casas")
        tamanho = 5
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p1[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p1[i] = 1
        navio5 -= 1
        navios -= 1
    if opc == 4 and navio2 != 0:
        print("Escolha a posição do navio 2 casas")
        tamanho = 2
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p1[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p1[i] = 1
        navio2 -= 1
        navios -= 1
print("jogador 2, posicione seus navios")
tamanho = 0
navios = 8
navio9 = 1
navio8 = 2
navio5 = 3
navio2 = 2
while navios != 0:
    print(map_p2)
    print("Jogador 2 começa, escolha qual navio escolher")
    opc = int(input(f"1 - navio de 9 casas ({navio9} restantes)\n2 - navio de 8 casas ({navio8} restantes)\n3 - navio de 5 casas ({navio5} restantes)\n4 - navio de 2 casas ({navio2} restantes)\n"))
    if opc == 1 and navio9 != 0:
        print("Escolha a posição do navio 9 casas")
        tamanho = 9
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p2[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p2[i] = 1
        navio9 -= 1
        navios -= 1
    if opc == 2 and navio8 != 0:
        print("Escolha a posição do navio 8 casas")
        tamanho = 8
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p2[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p2[i] = 1
        navio8 -= 1
        navios -= 1
    if opc == 3 and navio5 != 0:
        print("Escolha a posição do navio 5 casas")
        tamanho = 5
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p2[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p2[i] = 1
        navio5 -= 1
        navios -= 1
    if opc == 4 and navio2 != 0:
        print("Escolha a posição do navio 2 casas")
        tamanho = 2
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            if map_p2[i] == 1:
                print("posição ocupada, escolha outra posição")
                pos = int(input("Posição: "))
                while pos < 0 or pos + tamanho > 65:
                    print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
                    pos = int(input("Posição: "))
                i = pos
            map_p2[i] = 1
        navio2 -= 1
        navios -= 1
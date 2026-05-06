map_p1 = []
map_p2 = []
map_p1_atk = []
map_p2_atk = []
tamanho = 0
turno = 1
navios_p1 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
navios_p2 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
num_navio = 0
navios = 8
navio9 = 1
navio8 = 2
navio5 = 3
navio2 = 2
for i in range(65):
    map_p1.append(0)
    map_p2.append(0)
print("batalha naval 1d")
while num_navio != 8:
    print(map_p1)
    print("Jogador 1 começa, escolha qual navio colocar")
    print(f"Casas ja selecionadas: {navios_p1}")
    opc = int(input(f"1 - navio de 9 casas ({navio9} restantes)\n2 - navio de 8 casas ({navio8} restantes)\n3 - navio de 5 casas ({navio5} restantes)\n4 - navio de 2 casas ({navio2} restantes)\n"))
    if opc == 1 and navio9 != 0:
        print("Escolha a posição do navio 9 casas")
        tamanho = 9
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p1[pos] == 1 or map_p1[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p1[i] = 1
            navios_p1[num_navio].append(i)
        num_navio += 1
        navio9 -= 1
        navios -= 1
    if opc == 2 and navio8 != 0:
        print("Escolha a posição do navio 8 casas")
        tamanho = 8
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p1[pos] == 1 or map_p1[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p1[i] = 1
            navios_p1[num_navio].append(i)
        num_navio += 1
        navio8 -= 1
        navios -= 1
    if opc == 3 and navio5 != 0:
        print("Escolha a posição do navio 5 casas")
        tamanho = 5
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p1[pos] == 1 or map_p1[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p1[i] = 1
            navios_p1[num_navio].append(i)
        num_navio += 1
        navio5 -= 1
        navios -= 1
    if opc == 4 and navio2 != 0:
        print("Escolha a posição do navio 2 casas")
        tamanho = 2
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p1[pos] == 1 or map_p1[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p1[i] = 1
            navios_p1[num_navio].append(i)
        num_navio += 1
        navio2 -= 1
        navios -= 1
        

print("jogador 2, posicione seus navios")
tamanho = 0
num_navio = 0
navio9 = 1
navio8 = 2
navio5 = 3
navio2 = 2
while num_navio != 8:

    print(map_p2)
    print(f"Casas ja selecionadas: {navios_p2}")
    print("Jogador 2, escolha qual navio colocar")
    opc = int(input(f"1 - navio de 9 casas ({navio9} restantes)\n2 - navio de 8 casas ({navio8} restantes)\n3 - navio de 5 casas ({navio5} restantes)\n4 - navio de 2 casas ({navio2} restantes)\n"))
    if opc == 1 and navio9 != 0:
        print("Escolha a posição do navio 9 casas")
        tamanho = 9
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p2[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p2[i] = 1
            navios_p2[num_navio].append(i)
        num_navio += 1
        navio9 -= 1
        navios -= 1
    if opc == 2 and navio8 != 0:
        print("Escolha a posição do navio 8 casas")
        tamanho = 8
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p2[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p2[i] = 1
            navios_p2[num_navio].append(i)
        num_navio += 1
        navio8 -= 1
        navios -= 1
    if opc == 3 and navio5 != 0:
        print("Escolha a posição do navio 5 casas")
        tamanho = 5
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p2[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p2[i] = 1
            navios_p2[num_navio].append(i)
        num_navio += 1
        navio5 -= 1
        navios -= 1
    if opc == 4 and navio2 != 0:
        print("Escolha a posição do navio 2 casas")
        tamanho = 2
        pos = int(input("Posição: "))
        while pos < 0 or pos + tamanho > 65 or map_p2[pos] == 1:
            print("posião invalida, lembre-se que a casa escolhida é o inico do navio")
            pos = int(input("Posição: "))
        for i in range(pos, pos + tamanho):
            map_p2[i] = 1
            navios_p2[num_navio].append(i)
        num_navio += 1
        navio2 -= 1
        navios -= 1

fim = False
for i in range(65):
    map_p1_atk.append(0)
    map_p2_atk.append(0)

while fim == False:
    while turno == 1:
        print("turno do jogador 1 atacar")
        print("este é o campo do jogador 2")
        print(map_p2_atk)
        pos = int(input("Selecione qual casa atacar"))
        while pos < 0 or pos > 65 or map_p2[pos] == "X" or map_p2_atk[pos] == 1:
            print(map_p2_atk)
            pos = int(input("selecione outra casa, essa ou ja foi selecionada antes ou não existe no mapa"))
        if map_p2[pos] == 1:
            for i, navio in enumerate(navios_p2):
                if pos in navio:
                    print(f"Acertou um navio de {len(navio)} casas")
                    for j in navio:
                        map_p2[j] = "X"
                        map_p2_atk[j] = "X"
                        navio[j] = "X"
        else:
            print("nenhum navio acertado")
            map_p1_atk[pos] = 1
        turno = 2
    while turno == 2:
        print("turno do jogador 2 atacar")
        print("este é o campo do jogador 1")
        print(map_p1_atk)
        pos = int(input("Selecione qual casa atacar"))
        while pos < 0 or pos > 65 or map_p1[pos] == "X" or map_p1_atk[pos] == 1:
            print(map_p1_atk)
            pos = int(input("selecione outra casa, essa ou ja foi selecionada antes ou não existe no mapa"))
        if map_p1[pos] == 1:
            for i, navio in enumerate(navios_p1):
                if pos in navio:
                    print(f"Acertou um navio de {len(navio)} casas")
                    for j in navio:
                        map_p1[j] = "X"
                        map_p1_atk[j] = "X"
                        navio[j] = "X"
        else:
            print("nenhum navio acertado")
            map_p1_atk[pos] = 1
        turno = 1
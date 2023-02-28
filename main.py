while True:
    try:
        numero = int(input('Qual número você gostaria de saber se pertence a sequência de Fibonacci?'))
    except:
        print('ERRO! Por favor insira um número inteiro válido.')
    else:
        break

lista = [0, 1, 1]
if numero == 0 or numero == 1:
    print(f'{numero} faz parte da sequência de Fibonacci.')
else:
    while len(lista) < 20:
        t1 = lista[-1]
        t2 = lista[-2]
        t3 = t1 + t2
        lista.append(t3)
        if t3 == numero:
            print(f'{numero} faz parte da sequência de Fibonacci.')
            break
        elif t3 < numero:
            continue
        else:
            print(f'{numero} não faz parte da sequência de Fibonacci.')
            break

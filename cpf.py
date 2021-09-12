cpf = list(input('Digite um número de 9 dígitos.\n'))

while(len(cpf) != 9):
    cpf = list(input('Número inválido! Digite apenas números de 9 dígitos.\n'))

if(len(cpf) == 9):
    somaAtual = 0

    for i in range(1, 10):
        somaAtual += (int(cpf[i-1])*i)
        #print("Multiplicação:", int(cpf[i-1]), "*", i)
        #print("Resultado:", int(cpf[i-1]) * i)
        #print("Soma", somaAtual)

    if((somaAtual % 11) == 10):
        cpf.append(0)
    else:
        cpf.append(somaAtual%11)
    somaAtual = 0

    #print(cpf)

    for j in range(0, 10):
        somaAtual += (int(cpf[j])*j)
        #print("Multiplicação:", int(cpf[j]), "*", j)
        #print("Resultado:", int(cpf[j])*j)
        #print("Soma:", somaAtual)

    if((somaAtual % 11) == 10):
        cpf.append(somaAtual%11)
    else:
        cpf.append(somaAtual%11)

    output = "O CPF válido é: "

    for j in range (0,3):
        for i in range(0,3):
            output += str(cpf[i+(3*j)])
        if(j < 2):
            output += "."
    output += "-"
    for i in range (9,11):
        output += str(cpf[i])

    print(output)
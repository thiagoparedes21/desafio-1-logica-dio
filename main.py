
nivelHeroi = ""

username = input("Digite o nome do seu usuário: ")
numeroVitorias = int(input("Digite o seu número de vitórias: "))
numeroDerrotas = int(input("Digite o seu número de derrotas: "))

def calculoSaldo(numA, numB):
    somatorio = numA - numB
    return somatorio

saldoRank = calculoSaldo(numeroVitorias, numeroDerrotas)

while True:
    if saldoRank <= 10:
        nivelHeroi = "Ferro"
        break
    elif saldoRank > 10 and saldoRank <= 20:
        nivelHeroi = "Bronze"
        break
    elif saldoRank > 20 and saldoRank <= 50:
        nivelHeroi = "Prata"
        break
    elif saldoRank > 50 and saldoRank <= 80:
        nivelHeroi = "Ouro"
        break
    elif saldoRank > 80 and saldoRank <= 90:
        nivelHeroi = "Diamante"
        break
    elif saldoRank > 90 and saldoRank <= 100:
        nivelHeroi = "Lendário"
    else:
        nivelHeroi = "IMORTAL"
        break


print(f"O Herói {username} tem de saldo {saldoRank} e está no nível {nivelHeroi}!")
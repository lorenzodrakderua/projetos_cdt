print("=====LOJA DE JOGOS=====")
print("1 - GTA V = R$80,00")
print("2 - GOD OF WAR = R$249,00")
print("3 - RESIDENT EVIL = R$99,99")
print("4 - FORZA HORIZON = R$199,99")

opcao = int(input("Escolha um jogo: "))

total = 0

if opcao == 1:
    total = 80.00
    print("Você comprou o GTA V")

elif opcao == 2:
    total = 249.00
    print("Você comprou o GOD OF WAR")

elif opcao == 3:
    total = 99.99
    print("Você comprou o RESIDENT EVIL")

elif opcao == 4:
    total = 199.99
    print("Você comprou o FORZA HORIZON")

else:
    print("Opção inválida")

print("Total da compra: R$", total)
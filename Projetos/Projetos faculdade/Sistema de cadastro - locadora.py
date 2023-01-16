import time
import random

print("-=" * 25)
print("             Bem vindo a locadora Gonçalvez")
print("-=" * 25)
time.sleep(1)
cadastros_clientes = {}
cadastros_veiculos = {}
cadastro_cliente_nome = []
cadastro_cliente_telefone = []
cadastro_veiculo_modelo = []
cadastro_veiculo_placa = []
while True:
    time.sleep(1)
    n1 = int(input(
        "Digite a opção desejada: \n 1 - Cadastro \n 2 - Consulta de cadastro  \n 3 - Atualizar cadastro \n 4 - Remover cadastro \n 5 - Sair "))
    time.sleep(1)
    match n1:
        case 1:
            ca1 = int(input("1 - Cadastrar cliente \n2 - Cadastrar veículo"))
            if ca1 == 1:
                time.sleep(1)
                cadastroN = input("Digite o nome do cliente: ")
                time.sleep(1)
                cadastroT = int(input("Digite o telefone para contato: "))
                time.sleep(1)
                print("Cadastro adicionado com sucesso.")
                cadastro_cliente_nome.append(cadastroN)
                cadastro_cliente_telefone.append(cadastroT)
                cadastros_clientes[random.randint(0, 100)] = cadastro_cliente_nome, cadastro_cliente_telefone
            elif ca1 == 2:
                time.sleep(1)
                cadastroV = input("Digite o modelo do veículo: ")
                time.sleep(1)
                cadastroP = input("Digite a placa do veículo: ")
                time.sleep(1)
                print("Veículo adicionado com sucesso")
                cadastro_veiculo_modelo.append(cadastroV)
                cadastro_veiculo_placa.append(cadastroP)
                cadastros_veiculos[random.randint(0, 100)]= cadastro_veiculo_modelo, cadastro_veiculo_placa
        case 2:
            time.sleep(1)
            ca2 = int(input("Qual tipo de cadastro você deseja consultar?\n 1 - Clientes\n 2 - Veículos"))
            if ca2 == 1:
                time.sleep(1)
                print(cadastro_cliente_nome)
            elif ca2 == 2:
                time.sleep(1)
                print(cadastros_veiculos)
        case 3:
            at1 = int(input("Qual cadastro gostaria de atualizar? \n 1 - Atualizar cadastro cliente \n 2 - Atualizar cadastro veículo "))
            time.sleep(1)
            if at1 == 1:
                atC=int(input("Qual dado gostaria de atualizar? \n 1 - Nome do cliente \n 2 - Telefone para contato"))
                time.sleep(1)
                if atC ==1:
                    time.sleep(1)
                    print("Veja a lista completa :")
                    time.sleep(1)
                    for i in enumerate(cadastro_cliente_nome):
                        print(i)
                    time.sleep(1)
                    atC1=int(input("Qual item deseja alterar?"))
                    print(cadastro_cliente_nome[atC1])
                    time.sleep(1)
                    cadastro_cliente_nome.pop(atC1)
                    atC2=input("Escreva um nome para substituir o anterior: ")
                    cadastro_cliente_nome.insert(atC1, atC2)
                    print(cadastro_cliente_nome)
                    time.sleep(1)
                    print("Cadastro atualizado com sucesso")
                elif atC == 2:
                    time.sleep(1)
                    print("Veja a lista completa :")
                    time.sleep(1)
                    for i in enumerate(cadastro_cliente_telefone):
                        print(i)
                    time.sleep(1)
                    atC3=int(input("Qual item deseja alterar?"))
                    print(cadastro_cliente_telefone[atC3])
                    time.sleep(1)
                    cadastro_cliente_telefone.pop(atC3)
                    atC4=input("Escreva um número para substituir o anterior: ")
                    cadastro_cliente_nome.insert(atC3, atC4)
                    print(cadastro_cliente_telefone)
                    time.sleep(1)
                    print("Cadastro atualizado com sucesso")
            elif at1 ==2:
                print("Qual dado gostaria de atualizar? ")
                time.sleep(1)
                print("Veja a lista completa :")
                time.sleep(1)
                for i in enumerate(cadastros_veiculos):
                    print(i)
                time.sleep(1)
                atV1 = int(input("Qual item deseja alterar?"))
                print(cadastros_veiculos[atV1])
                time.sleep(1)
                cadastro_veiculo_modelo.pop(atV1)
                atV2 = input("Escreva um modelo para substituir o anterior: ")
                cadastro_veiculo_modelo.update(atV1, atV2)
                print(cadastro_veiculo_modelo)
                time.sleep(1)
                print("Cadastro atualizado com sucesso")
        case 4:
            re1 = int(input("Qual cadastro gostaria de remover? \n 1 - Remover cadastro cliente \n 2 - Remover cadastro veículo "))
            time.sleep(1)
            if re1 == 1:
                print(cadastros_clientes)
                for i in enumerate(cadastros_clientes):
                    print(i)
                atR=int(input("Qual dado gostaria de remover? "))
                time.sleep(1)
                del cadastros_clientes[atR]
                time.sleep(1)
                print("Cadastro removido com sucesso.")
            else:
                for i in enumerate(cadastros_veiculos):
                    print(i)
                atR1=int(input("Qual dado gostaria de remover? "))
                time.sleep(1)
                print(cadastros_veiculos)
                del cadastros_veiculos[atR1]
                print("Cadastro removido com sucesso.")
        case 5:
            time.sleep(1)
            break
    if n1 >= 6:
        time.sleep(1)
        print("Opção inválida")

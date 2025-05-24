from validacao import *
from gerente import Gerente
from desenvolvedor import Desenvolvedor
from estagiario import Estagiario

funcionarios = []

def cadastrar():
    print("--- CADASTRO DE FUNCIONÁRIOS ---")

    nome = input("Digite o nome: ")
    while not validar_caracteres(nome):
        print("Dado inválido. Digite novamente.")
        nome = input("Digite o nome: ")

    idade = validar_idade("Digite a idade: ", 15, 80)
    cargo = validar_opcao("Escolha o cargo: [Gerente | Desenvolvedor | Estagiário]: ", ["gerente", "desenvolvedor", "estagiário"])
    salario = validar_decimal("Digite o salário base: R$ ")
    forma_pagamento = validar_opcao("Forma de pagamento: [Pix | Débito em Conta | Dinheiro]: ", ["pix", "débito em conta", "dinheiro"])
    metodo_entrega = validar_opcao("Método de entrega: [Automático | Manual]: ", ["automático", "manual"])

    if cargo.lower() == "gerente":
        bonus = validar_decimal("Digite o bônus: R$ ")
        f = Gerente(bonus, nome, idade, cargo, salario, forma_pagamento, metodo_entrega)
    elif cargo.lower() == "desenvolvedor":
        hora_extra = validar_inteiro("Digite as horas extras: ")
        valor_hora = validar_decimal("Digite o valor por hora extra: R$ ")
        f = Desenvolvedor(hora_extra, valor_hora, nome, idade, cargo, salario, forma_pagamento, metodo_entrega)
    else:
        f = Estagiario(nome, idade, cargo, salario, forma_pagamento, metodo_entrega)

    funcionarios.append(f)
    print("Funcionário cadastrado com sucesso!")
    input("Pressione qualquer tecla para retornar ao menu...")

def consultar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        input("Pressione qualquer tecla para retornar ao menu...")
        return

    print("--- LISTA DE FUNCIONÁRIOS ---")
    for f in funcionarios:
        print(f"\nNome: {f.nome}")
        print(f"Idade: {f.idade}")
        print(f"Cargo: {f.cargo}")
        print(f"Salário base: R$ {f.salario}")
        print(f"Salário Líquido: R$ {f.calcular_salario():.2f}")
        print(f"Forma de Pagamento: {f.forma_pagamento}")
        print(f"Método de Entrega: {f.metodo_entrega}")
        f.entregar_pagamento()
        input("Pressione qualquer tecla para avançar...")

def main():
    while True:
        print("--- GERENCIAMENTO DE FUNCIONÁRIOS ---")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionários")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            consultar()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
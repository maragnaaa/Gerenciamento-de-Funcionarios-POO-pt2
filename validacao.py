import re

def validar_caracteres(nome):
    return re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome) is not None

def validar_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("Dado inválido. Digite novamente.")

def validar_idade(mensagem, minimo, maximo):
    while True:
        try:
            idade = int(input(mensagem))
            if minimo <= idade <= maximo:
                return idade
        except ValueError:
            pass
        print("Dado inválido. Digite novamente.")

def validar_decimal(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("Dado inválido. Digite novamente.")

def validar_opcao(mensagem, opcoes_validas):
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada in [op.lower() for op in opcoes_validas]:
            return entrada.capitalize()
        print("Opção inválida. Tente novamente.")
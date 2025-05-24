from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, idade, cargo, salario, forma_pagamento, metodo_entrega):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        self.forma_pagamento = forma_pagamento
        self.metodo_entrega = metodo_entrega

    @abstractmethod
    def calcular_salario(self):
        pass

    def calcular_imposto(self, total_salario):
        return 0

    def entregar_pagamento(self):
        print(f"O pagamento de {self.nome} será realizado via {self.forma_pagamento} pelo método {self.metodo_entrega}")
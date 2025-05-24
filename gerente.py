from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, bonus, *args):
        super().__init__(*args)
        self.bonus = bonus

    def calcular_salario(self):
        total = self.salario + self.bonus
        return total - self.calcular_imposto(total)

    def calcular_imposto(self, total_salario):
        return total_salario * 0.275
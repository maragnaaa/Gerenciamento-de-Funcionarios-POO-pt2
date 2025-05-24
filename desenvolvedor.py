from funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, hora_extra, valor_hora_extra, *args):
        super().__init__(*args)
        self.hora_extra = hora_extra
        self.valor_hora_extra = valor_hora_extra

    def calcular_salario(self):
        extra = self.hora_extra * self.valor_hora_extra
        total = self.salario + extra
        return total - self.calcular_imposto(total)

    def calcular_imposto(self, total_salario):
        return total_salario * 0.10
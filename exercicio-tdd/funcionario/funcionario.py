from dataclasses import dataclass
@dataclass
class Funcionario:
    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def __post_init__(self):
        if any([
            self.salario_hora < 0,
            self.horas_trabalhadas < 0,
            self.custo_empregador < 0,
            self.valor_comissao < 0,
            self.contratos_fechados < 0
        ]):
            raise ValueError("Valores negativos não são permitidos.")

    def calcular_salario_bruto(self) -> float:
        # Considera hora extra: se ultrapassar 160h, aplica 50% sobre as extras
        if self.horas_trabalhadas <= 160:
            return self.salario_hora * self.horas_trabalhadas
        horas_extras = self.horas_trabalhadas - 160
        salario_normal = self.salario_hora * 160
        extra = self.salario_hora * 1.5 * horas_extras
        return salario_normal + extra

    def calcular_comissao(self) -> float:
        if self.tem_comissao:
            return self.valor_comissao * self.contratos_fechados
        return 0.0

    def calcular_custo_total(self) -> float:
        return self.calcular_salario_bruto() + self.calcular_comissao() + self.custo_empregador

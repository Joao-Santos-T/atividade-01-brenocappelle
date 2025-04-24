"""
Testes da classe Funcionario.
"""
import unittest
from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_bruto_sem_horas_extras(self):
        """Testa o cálculo do salário bruto sem horas extras."""
        funcionario = Funcionario(nome="João", matricula=1, salario_hora=100, horas_trabalhadas=160)
        self.assertEqual(funcionario.calcular_salario_bruto(), 16000)

    def test_calcular_salario_bruto_com_horas_extras(self):
        """Testa o cálculo do salário bruto com horas extras."""
        funcionario = Funcionario(nome="Maria", matricula=2, salario_hora=100, horas_trabalhadas=170)
        # 160 horas normais + 10 extras com 50% adicional
        esperado = (160 * 100) + (10 * 100 * 1.5)
        self.assertEqual(funcionario.calcular_salario_bruto(), esperado)

    def test_calcular_comissao_ativa(self):
        """Testa o cálculo da comissão quando o funcionário recebe comissão."""
        funcionario = Funcionario(nome="Lucas", matricula=3, tem_comissao=True, contratos_fechados=3, valor_comissao=200)
        self.assertEqual(funcionario.calcular_comissao(), 600)

    def test_calcular_comissao_inativa(self):
        """Testa o cálculo da comissão quando o funcionário não recebe comissão."""
        funcionario = Funcionario(nome="Clara", matricula=4, tem_comissao=False, contratos_fechados=5, valor_comissao=200)
        self.assertEqual(funcionario.calcular_comissao(), 0.0)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total (salário + comissão + custo empregador)."""
        funcionario = Funcionario(
            nome="Ana", matricula=5, salario_hora=100, horas_trabalhadas=160,
            tem_comissao=True, contratos_fechados=2, valor_comissao=150,
            custo_empregador=1200
        )
        salario = 160 * 100
        comissao = 2 * 150
        custo = salario + comissao + 1200
        self.assertEqual(funcionario.calcular_custo_total(), custo)

    def test_valores_negativos_disparam_erro(self):
        """Testa se valores negativos disparam erro."""
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro1", matricula=10, salario_hora=-1)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro2", matricula=11, horas_trabalhadas=-5)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro3", matricula=12, valor_comissao=-20)
        with self.assertRaises(ValueError):
            Funcionario(nome="Erro4", matricula=13, custo_empregador=-100)


if __name__ == "__main__":
    unittest.main()

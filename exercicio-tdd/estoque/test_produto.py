import unittest
from datetime import datetime, timedelta
from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        # Criação de um produto com dados fictícios para os testes
        self.produto = Produto(
            codigo="P001",
            nome="Produto Teste",
            preco=100.0,
            quantidade=10,
            data_validade=datetime.now() + timedelta(days=10),
            estoque_minimo=5
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        produto = self.produto
        self.assertEqual(produto.codigo, "P001")
        self.assertEqual(produto.nome, "Produto Teste")
        self.assertEqual(produto.preco, 100.0)
        self.assertEqual(produto.quantidade, 10)
        self.assertEqual(produto.estoque_minimo, 5)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertEqual(self.produto.quantidade, 15)  # Quantidade inicial + 5

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        sucesso = self.produto.remover_estoque(5)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 5)  # Quantidade inicial - 5

        # Verifica se não remove mais do que o disponível
        sucesso_invalido = self.produto.remover_estoque(10)
        self.assertFalse(sucesso_invalido)
        self.assertEqual(self.produto.quantidade, 5)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.assertFalse(self.produto.verificar_estoque_baixo())  # Estoque está 5, que é mínimo
        self.produto.remover_estoque(6)  # Deixa o estoque baixo
        self.assertTrue(self.produto.verificar_estoque_baixo())  # Agora o estoque está baixo

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        valor_total = self.produto.calcular_valor_total()
        self.assertEqual(valor_total, 100.0 * 10)  # Preço * Quantidade

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto.verificar_validade())  # Produto está dentro da validade

        # Produto com validade expirada
        produto_expirado = Produto(
            codigo="P002",
            nome="Produto Expirado",
            preco=50.0,
            quantidade=5,
            data_validade=datetime.now() - timedelta(days=1),  # Já expirou
            estoque_minimo=5
        )
        self.assertFalse(produto_expirado.verificar_validade())  # Produto expirado

if __name__ == "__main__":
    unittest.main()

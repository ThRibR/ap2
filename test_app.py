import unittest
import sys
sys.path.append("app.py")
from unittest.mock import patch
import app
class TestApp(unittest.TestCase):
    # 1 Teste cadastro de usuário

    @patch("app.cadastro", return_value="Usuário cadastrado!")
    def testCadastroUserValido(self, mock_salvar):
        nome = "Laura"
        email = "laura@gmail.com"
        idade = "27"
        cep = "33333-333"
        bairro = "Bairro da Capota"
        cidade = "Belo Horizontas"
        estado = "Manaus"

        resultado = app.cadastro(nome, email, idade, cep, bairro, cidade, estado)

        self.assertEqual(resultado, "Usuário cadastrado!")
        mock_salvar.assert_called_once_with(nome, email, idade, cep, bairro, cidade, estado)

    #2 Teste verifica email

    @patch("app.email_existe", return_value="Email encontrado!")
    def testEmailExiste(self, mock_exibir):
        resultado = app.email_existe("laura@gmail.com")
        self.assertEqual(resultado,"Email encontrado!")
        mock_exibir.assert_called_once()

    @patch("app.email_existe", return_value="Erro: dados incorretos, precisa de um '@'.")
    def testEmailInvalido(self, mock_exibir):
        resultado = app.email_existe("clausgamil.com")
        self.assertEqual(resultado, "Erro: dados incorretos, precisa de um '@'.")
        mock_exibir.assert_called_once()

    @patch("app.email_existe", return_value="Erro: Somente usuários maiores de 18 anos podem ser cadastrados.")
    def testMaiorIdade(self, mock_exibir):
        nome = "Lui",
        email = "lui@gmail.com",
        idade = 12,
        cep = "33333-333",
        bairro = "Bairro da Capota",
        cidade = "Belo Horizontas",
        estado = "Manaus"
        resultado = app.cadastro(nome, email, idade, cep, bairro, cidade, estado)
        self.assertEqual(resultado, "Erro: Somente usuários maiores de 18 anos podem ser cadastrados.")
        mock_exibir.assert_called_once()

    @patch("app.email_existe", return_value="Erro: Cep desconhecido")
    def testCepInvalido(self, mock_exibir):
        resultado = app.buscar_endereco(77777-777)
        self.assertEqual(resultado, "Erro: Cep desconhecido")
        mock_exibir.assert_called_once()

    @patch("app.email_existe", return_value="Email encontrado!")
    def testEmailValido_Externo(self,mock_exibir):
            resultado = email_existe.get("/user/laura@gmail.com")
            assert resultado.status_code == 200
            mock_exibir.assert_called_get_json ==  "Email encontrado!", 200

if __name__ == '__main__':
    unittest.main()

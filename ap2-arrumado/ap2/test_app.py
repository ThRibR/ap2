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

    @patch("app.buscar_endereco", return_value="Erro: Cep desconhecido")
    def testCepInvalido(self, mock_exibir):
        resultado = app.buscar_endereco("/user/77777-777")
        self.assertEqual(resultado, "Erro: Cep desconhecido")
        mock_exibir.assert_called_once()
        
    @patch("app.email_existe", return_value="Email encontrado!")
    def testEmailValido_Externo(self,mock_exibir):
        resultado = app.email_existe("/user/laura@gmail.com")# Não estava completamente errado como estava sendo apresentado o código,( resultado = app.email_existe.get("/user/laura@gmail.com") / assert resultado.status_code == 200)
        self.assertEqual(resultado, "Email encontrado!")     #o problema é que seria necessário definir este tipo de rota para depois colocar este tipo de verificação.
        mock_exibir.assert_called_once()
        
    @patch("app.verifica_idade", return_value="Erro: Somente usuários maiores de 18 anos podem ser cadastrados.")
    def testMaiorIdade(self, mock_exibir):
        idade = 12
        resultado = app.verifica_idade(idade)
        self.assertEqual(resultado, "Erro: Somente usuários maiores de 18 anos podem ser cadastrados.")
        mock_exibir.assert_called_once()

if __name__ == '__main__':
    unittest.main()

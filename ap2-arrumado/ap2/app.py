from flask import Flask, jsonify, request
main = Flask(__name__)
users= []

def cadastro(nome, email, idade, cep, bairro, cidade, estado):
    new_user = {
    'nome':nome,
    'email':email,
    'idade':idade,
    'cep':cep,
    'bairro':bairro,
    'cidade':cidade,
    'estado':estado
    }

    for user in users:
        if user["email"] == email:
            return "Erro: email existente"
        elif '@' not in user['email']:
            return "Erro: dados incorretos, precisa de um '@'."
        verifica_idade(new_user[idade])
        users.append(new_user)
        return "Usuário cadastrado!"
    
def verifica_idade(idade):
    if idade < 18:
        return "Erro: Somente usuários maiores de 18 anos podem ser cadastrados."
    return True
        
#Porque ele não pega os valores inseridos nos testes?
@main.route("/user/<email>", methods=["GET"])
def email_existe(email:str):
    for user in users:
        if user["email"] != email:
            return jsonify("Erro: Email não encontrado."), 404
        return jsonify("Email encontrado!"), 200

@main.route("/user/<cep>", methods=["GET"])
def buscar_endereco(cep:int):
    for i in users:
        if i[cep] == cep:
            return jsonify(users[i]); 200
        return jsonify("Erro: Cep desconhecido"); 404



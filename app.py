from flask import Flask, jsonify, request
main = Flask(__name__)
users= []
address = []

def cadastro(nome, email, idade, cep, bairro, cidade, estado):
    new_user = {
    'nome':nome,
    'email':email,
    'idade':idade,
    'cep':cep,
    }
    new_address = {
    'bairro':bairro,
    'cidade':cidade,
    'estado':estado
    }

    for user in users:
        if user["email"] == email:
            return "Erro: email existente"
        elif '@' not in user['email']:
            return "Erro: dados incorretos, precisa de um '@'."
        elif new_user[idade] < 18:
            return "Erro: Somente usuários maiores de 18 anos podem ser cadastrados."
        users.append(new_user)
        address.append(new_address)
        return "Usuário cadastrado!"

@main.route("/user/<email>", methods=["GET"])
def email_existe(email:str):
    for user in users:
        if user["email"] != email:
            return jsonify("Erro: Email não encontrado."), 404
        return jsonify("Email encontrado!"), 200

@main.route("/user/<cep>", methods=["GET"])
def buscar_endereco(cep):
    for i in users:
        if i["cep"] == cep:
            return jsonify(address[i]); 200
        return jsonify("Erro: Cep desconhecido"); 404



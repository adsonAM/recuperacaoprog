from config.Config import Config
from config.Database import Database
from dao.RoupaDao import RoupaDao
from flask import Flask, request, render_template

from model.Roupa import Roupas

app = Flask(__name__)

dao = RoupaDao(Database(Config().config).conn)

@app.route('/', methods=["GET"])
def principal():
    lista = dao.listarRoupa()
    return render_template("principal.html", lista = lista)

@app.route('/roupa/novo', methods=["GET"])
def novo():
    return render_template("inserir.html")

@app.route('/roupa/novo', methods=["POST"])
def inserir():
    roupa = Roupas()
    roupa.id = request.form.get("id")
    roupa.marca = request.form.get("marca")
    roupa.tamanho = request.form.get("tamanho")
    roupa.tipo = request.form.get("tipo")

    dao.inserirRoupas(roupa)

    lista = dao.listarRoupa()
    return render_template(
        "principal.html",
        lista=lista
    )

@app.route('/roupa', methods=["GET"])
def listar():
    lista = dao.selecionarRoupas()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/roupa/<id>', methods=["GET"])
def editarPagina(id):
    roupa = dao.selecionarRoupa(id)
    return render_template("editar.html", roupa=roupa)

@app.route('/roupa/editar', methods=["POST"])
def editar():
    roupa = Roupas()
    roupa.id = request.form.get("id")
    roupa.marca = request.form.get("marca")
    roupa.tamanho = request.form.get("tamanho")
    roupa.tipo = request.form.get("tipo")
    roupa = dao.alterarRoupas(roupa)
    
    lista = dao.listarRoupa()
    return render_template(
        "principal.html",
        lista=lista
    )

@app.route('/roupa/remover/<id>', methods=["GET"])
def remover(id):
    roupa = Roupas()
    roupa.id = id
    dao.excluirRoupas(roupa)
    
    lista = dao.listarRoupa()
    return render_template(
        "principal.html",
        lista=lista
    )


if __name__ == '__main__':
    app.run()

from flask import (Flask, render_template, request,redirect)

class cadeskarateca:
    def __init__(self, nome, idfederativo, categoria, faixa, idade):
        self.nome = nome
        self.idfederativo = idfederativo
        self.categoria = categoria
        self.faixa = faixa
        self.idade = idade


lista = []

app = Flask(__name__)



@app.route('/')
def cadastro():
    return render_template('Cadastro.html')

@app.route('/criar',methods=['POST'])
def criar():
    nome = request.form['nome']
    idfederativo = request.form['idfederativo']
    categoria = request.form['categoria']
    faixa = request.form['faixa']
    idade = request.form['idade']
    obj = cadeskarateca(nome, idfederativo, categoria, faixa, idade)
    lista.append(obj)
    return redirect('/karate')

@app.route('/karate')
def karate():
    return render_template('Karate.html', Titulo='Area Dos Cadastrados', listaKAratecas=lista)


@app.route('/buttonn/<numeroatleta>', methods = ['GET','DELETE'])
def excluir(numeroatleta):
    for i, num in enumerate(lista):
        if num.idfederativo == numeroatleta:
            lista.pop(i)
            break
    return redirect('/karate')

@app.route('/editar/<numeroatleta>', methods = ['GET'])
def editar(numeroatleta):
    for i, num in enumerate(lista):
        if num.idfederativo == numeroatleta:
            return render_template('editar.html', Karateca=num)

@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    numero = request.form['idfederativo']
    print(numero)
    for i,num in enumerate(lista):
        if num.idfederativo == numero:
           num.nome = request.form['nome']
           num.categoria = request.form['categoria']
           num.faixa = request.form['faixa']
           num.idade = request.form['idade']
        return redirect('/karate')

if __name__ == '__main__':
    app.run()


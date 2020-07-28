from flask import Flask, render_template

#Creamos  un objeto app de flask
app = Flask(__name__)

#definimos la ruta principal
@app.route("/")

#Definimos una funcion para la ruta de la pagina principal
def paginaPrincipal():
    #return "Hola mundo"
    return render_template('index.html')#Llamamos una planitalla HTML

@app.route("/Otra_Pagina")
def pagina2():
    return render_template('form_component.html')

@app.route("/redireccion")
def redireccionar():
    return paginaPrincipal()

if(__name__ == "__main__"):
    app.run()

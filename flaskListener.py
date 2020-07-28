from flask import Flask, render_template

#Creamos  un objeto app de flask
app = Flask(__name__)

#definimos la ruta principal
@app.route("/")

#Definimos una funcion para la ruta de la pagina principal
def accion():
    #return "Hola mundo"
    return render_template('portada.html')#Llamamos una planitalla HTML
    #ARREGLAR EL TEMA DE LA SIDEBAR

if(__name__ == "__main__"):
    app.run()

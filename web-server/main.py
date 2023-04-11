import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

#Un decorador que permite establecer Rutas hacia la api y los metodos para consultarlos
@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact',response_class=HTMLResponse)
def get_pagina():
    return """
        <h1>Soy un titulo h1</h1>
        <p>soy un parrafo </p>
    """;

#La siguiente funcion con un decorador regresa un JSON el cual brinda informacion sobre el nombre de la empresa
# @app.get('/contact')
# def get_list():
#     return {'name': 'Platzi'}

def run():
    store.get_categories()


if __name__=='__main__':
    run()
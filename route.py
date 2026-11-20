from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info=None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Suas rotas aqui:
# Nível 1
@app.route('/')
@app.route('/catalogo')
def catalogo():
    return ctl.render('catalogo')

#Nível 2
@app.route('/hardware')
def hardware_index():
    return ctl.hardware()

@app.route('/hardware/criar', method='POST')
def hardware_criar():
    return ctl.hardware_criar(request.forms)

@app.route('/hardware/editar/<id_item:int>', method=['GET', 'POST'])
def hardware_editar(id_item):
    if request.method == 'POST':
        return ctl.hardware_atualizar(id_item, request.forms)
    return ctl.hardware_form_editar(id_item)

@app.route('/hardware/excluir/<id_item:int>', method='POST')
def hardware_excluir(id_item):
    return ctl.hardware_excluir(id_item)

#-----------------------------------------------------------------------------


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
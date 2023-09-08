from flask import Flask, jsonify, request
from cursos import cursos

app = Flask(__name__)

@app.route('/cursos')
def index():
    return jsonify({'cursos': cursos})



@app.route('/cursos/<int:id>')
def cursos_id(id):
    cursoencontrado = [curso for curso in cursos if curso['id'] == id]
    if len(cursoencontrado) == 0:
        return jsonify({'error': 'No se encontro el curso'}), 404
    return jsonify({'curso': cursoencontrado[0]})

    
@app.route('/cursos', methods=['POST'])
def cursoss():
    nuevocurso= {
        'id':request.json['id'],
        'nombre':request.json['nombre'],
        'descripcion':request.json['descripcion'],

    }
    cursos.append(nuevocurso)
    return jsonify({'cursos': cursos})



@app.route('/cursos/<int:id>', methods=['DELETE'])
def cursos_delete(id):
    cursoencontrado = [curso for curso in cursos if curso['id'] == id]
    if len(cursoencontrado) == 0:
        return jsonify({'error': 'No se encontro el curso'}), 404
    cursos.remove(cursoencontrado[0])
    return jsonify({'cursos': cursos})


@app.route('/cursos/<int:id>', methods=['PUT'])
def cursos_put(id):
    cursoencontrado = [curso for curso in cursos if curso['id'] == id]
    if len(cursoencontrado) == 0:
        return jsonify({'error': 'No se encontro el curso'}), 404
    cursoencontrado[0]['nombre']= request.json['nombre']
    cursoencontrado[0]['descripcion']= request.json['descripcion']
    return jsonify({'curso': cursoencontrado[0]})


    



if __name__ == '__main__':
    app.run(debug=True, port=3000)



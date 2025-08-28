from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>LectoLandia funciona!</h1><p>Esta es una prueba básica.</p>'

if __name__ == '__main__':
    import os
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

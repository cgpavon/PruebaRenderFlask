from flask import Flask


def crear_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    return app

if __name__ == "__main__":
    app = crear_app()
    app.run()

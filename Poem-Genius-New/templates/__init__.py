from flask import Flask

app = Flask(__name__,
 static_folder = './public',
 template_folder="./static")

from templates.poem.views import poem_blueprint

# register the blueprints
app.register_blueprint(poem_blueprint)

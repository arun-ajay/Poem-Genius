from flask import render_template, Blueprint

poem_blueprint = Blueprint('poem',__name__)

@poem_blueprint.route('/home')
def index():
 return render_template("index.html")

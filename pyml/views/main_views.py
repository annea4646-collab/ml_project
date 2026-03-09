from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pyml():
    return 'Hello Pyml!'

@bp.route('/')
def index():
    return 'Hello Index!'
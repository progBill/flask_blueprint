from flask import Blueprint, render_template

nexter = Blueprint('nexter',__name__, template_folder='templates', static_folder='static')

@nexter.route('/', methods=['GET'])
def next_page():
    return render_template('next.html')



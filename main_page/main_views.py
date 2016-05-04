from flask import Blueprint, render_template

main = Blueprint('main',__name__, template_folder='templates', 
                static_folder='static') #, static_url_path='/main/static')


@main.route('/', methods=['GET'])
def main_page():
    return render_template('main.html')



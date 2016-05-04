from flask import Flask
from .main_page.main_views import main
from .next_page.next_views import nexter

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/main')
app.register_blueprint(nexter, url_prefix='/nexter')



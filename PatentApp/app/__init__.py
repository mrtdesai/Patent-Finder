from flask import Flask

app = Flask(__name__)
from app import patentviews
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

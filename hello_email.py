from flask import Flask
from flask_mail import Mail
import os
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '479381142@qq.com'
app.config['MAIL_PASSWORD'] = 'ihmbgoezyuixcajg'
mail = Mail(app)


def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context()))
from flask import Flask
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    z = Nidongde('sdf', 'abc@123')
    y = User('zcx', 'def@234')
    return 'Hello World!'

if __name__ == '__main__':

    db.create_all()
    app.run()

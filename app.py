from flask import Flask
from config import ConfigDev

app = Flask(__name__)
app.config.from_object(ConfigDev)

@app.route('/')
def home():
    return '<h1>Hello This! That!</p1>'

if __name__ == __name__ :
    app.run()
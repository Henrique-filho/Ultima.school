from flask import Flask
app =  Flask(__name__)

@app.route('/home')
def homepage():
    return "this is my new homepage "
@app.route('/inicio')
def inicio():
    return "Olá meu nome é Henrique, e esse é meu primeiro site "

app.run()

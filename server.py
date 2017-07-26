from flask import Flask,redirect, url_for,request,make_response
from flask import  render_template
app = Flask(__name__)






@app.route('/')
def start():
    #return 'hello world, newzealand!!!!!'
    return render_template('index.html')

@app.route('/test')
def test():
    return 'designed by jack yang,please communicate with yang756260386@gmail.com 233 '

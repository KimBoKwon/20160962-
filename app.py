from flask import Flask, request, render_template, redirect, url_for, abort, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/gamestart')
def gamestart():
    return render_template('gamestart.html')

@app.route('/gameset')
def gameset():
    return render_template('gameset.html')

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return render_template('victory.html')
    elif num == 2:
        return render_template('run.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mainPage():
    #return 'Hello World!'
    return render_template('dashboard.html')

@app.route('/topicsStats')
def topicsStats():
    #return 'Hello World!'
    return render_template('topicsStats.html')



if __name__ == '__main__':
    app.run(debug=True)
    #app.run()


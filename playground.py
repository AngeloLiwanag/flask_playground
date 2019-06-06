from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def my_webpage():
    return render_template('index.html', times = 3)

@app.route('/play/<x>')
def level2(x):
    return render_template('index.html', times = int(x))

@app.route('/play/<x>/<box_color>')
def level3(x, box_color):
    return render_template('index.html', times = int(x), color = box_color)

if __name__ == "__main__":
    app.run(debug = True)
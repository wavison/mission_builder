from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/obc')
def obc():
    return render_template("obc.html")

@app.route('/eps')
def eps():
    return render_template("eps.html")

@app.route('/adcs')
def adcs():
    return render_template("adcs.html")

@app.route('/comms')
def comms():
    return render_template("comms.html")

@app.route('/payload')
def payload():
    return render_template("payload.html")

@app.route('/obc/processor')
def obc_processor():
    return render_template("obc_processor.html")

@app.route('/obc/memory')
def obc_memory():
    return render_template("obc_memory.html")

@app.route('/obc/interfaces')
def obc_interfaces():
    return render_template("obc_interfaces.html")

if __name__ == '__main__':
    app.run(debug=True)

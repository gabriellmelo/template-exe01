from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('template.html')

@app.route('/unifran')
def unifran():
  return render_template('template2.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
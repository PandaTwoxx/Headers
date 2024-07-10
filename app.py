from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  """Display request headers in a user-friendly table."""
  headers = dict(request.headers)
  return render_template('index.html', headers=headers)

if __name__ == '__main__':
  app.run(debug=False, port=8000, host='0.0.0.0')
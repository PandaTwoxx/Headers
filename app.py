from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
  """Display request headers in a user-friendly table."""
  headers = dict(request.headers)
  return render_template('index.html', headers=headers)

if __name__ == '__main__':
  serve(app, host='0.0.0.0', port='8000')
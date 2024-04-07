from flask import Flask, redirect, url_for
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/redirect')
def redirect_example():
    # Redirect to the root URL
    return redirect(url_for('hello'), code=302)

if __name__ == '__main__':
    # Determine the host and port dynamically
    host = socket.gethostbyname(socket.gethostname())
    port = 5000  # You may need to adjust this depending on your hosting environment
    print(f"Running Flask app at http://{host}:{port}/")
    app.run(host=host, port=port, debug=True)

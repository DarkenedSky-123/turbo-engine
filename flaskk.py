from flask import Flask, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/redirect')
def redirect_example():
    # Redirect to the root URL
    return redirect(url_for('hello'), code=302)

if __name__ == '__main__':
    # Determine the host and port
    host = '0.0.0.0'  # Listen on all network interfaces
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable if available, otherwise default to 5000
    print(f"Running Flask app at http://{host}:{port}/")
    app.run(host=host, port=port, debug=True)

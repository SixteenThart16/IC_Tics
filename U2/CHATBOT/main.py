from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendMessage', methods=['POST'])
def send_message():
    user_input = request.form['user_input']
    response = os.popen('python src/chat.py "{}"'.format(user_input)).read()
    return response

if __name__ == '__main__':
    app.run(debug=True)

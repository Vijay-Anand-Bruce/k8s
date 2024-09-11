from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page with a simple form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!....Hope you are happy atleast'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

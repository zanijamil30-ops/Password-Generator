from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', password=None)

@app.route('/generate', methods=['POST'])
def generate():
    # read values from form and provide safe defaults
    length_raw = request.form.get('length', '12')
    try:
        length = int(length_raw)
    except ValueError:
        length = 12

    use_uppercase = bool(request.form.get('uppercase'))
    use_digits = bool(request.form.get('digits'))
    use_symbols = bool(request.form.get('symbols'))

    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_symbols=use_symbols
    )

    return render_template('index.html', password=password)

if __name__ == '__main__':
    # Use 0.0.0.0 only if you want external access; default 127.0.0.1 is fine for local development
    app.run(debug=True)


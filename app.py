from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)


#First Flask App
# http://localhost:8081/
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# http://localhost:8081/login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if len(username) > 0 and username[0] == username[0].capitalize() and password.isalnum() and (any(letter.isdigit() for letter in password)) and (any(letter.isalpha() for letter in password)):
        return render_template('success.html')
    else:
        return redirect('/')


# Practica
# http://localhost:8081/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"

# http://localhost:8081/params?test=Mario
@app.route("/params", methods=["GET"])
def params():
    name = request.args.get("test", default="World", type=str)
    return f"Hello {name}"

# http://localhost:8081/name/mario
@app.route("/name/<name>", methods=["GET"])
def root(name: str):
    return f"Hello {name}"

@app.route('/test', methods=['POST'])
def my_view_func():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Hello {email}"

@app.route('/json', methods=["POST"])
def json():
    data = request.get_json()
    return jsonify(data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)

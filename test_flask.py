from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Paing"
    aunty = "Daw Shwe"
    return render_template('index.html', author=author, aunty=aunty)

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    print("Email Address : " + email + " :to contact")
    return render_template('result.html', email=email)

if __name__ == '__main__':
    app.run()
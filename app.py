from flask import Flask, render_template
from get_fortune import predict

app = Flask(__name__)

@app.route('/')
def index():
    s = predict()
    #return "<h1>" + s + "</h1>"
    print("here we are:")
    print(s)
    return render_template('index.html', prediction=s)

if __name__ == '__main__':
    app.run(debug=True)
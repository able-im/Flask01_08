from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><br><iframe src="http://clarusway.de/" height="600" width="800"></iframe>"


@app.route("/products")
def products():
    return "<h1>Product Page</h1>"


@app.route("/products/<string:id>")
def forth(id):
    return "<h1>Product Detail Page - {{id}}</h1>"


@app.route("/second")
def second():
    return "This is second page"


@app.route("/third")
def third():
    return "This is third page"


@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of this page is {id}"


if __name__ == "__main__":
    #  app.run(debug=True)
    app.run(host="0.0.0.0", port=80)

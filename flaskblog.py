from flask import Flask, render_template, make_response, jsonify
app = Flask(__name__)

posts = [{
    'author': 'Corey Schafer',
    'title': 'Blog post1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
}]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', post = posts) 

@app.route("/about")
def about():
    return make_response(jsonify({"message": "oiii"}), 200);


if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask,render_template,request,jsonify
from query import search_query


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search')
def search():
    title = request.args.get("title")
    text = request.args.get("text")
    result=search_query(title,text)

    return jsonify(result)



from flask import Flask,request #, session
from flask import render_template
from flask import jsonify
import SentimentAnalysis
import Utilities


app = Flask(__name__)
lexicon_dict = {}

@app.route('/')
def home_page():
    return render_template('hello.html',name='')

@app.route('/edit')
def edit_keyword():
    global lexicon_dict
    lexicon_dict = Utilities.loadlexicon()
    return render_template('edit.html',lexicon=lexicon_dict)

@app.route('/edit/item/<lexicon>')
def edit_lexicon(lexicon):
    print ("Edit keyword = ", lexicon)
    return ""

@app.route('/analyze',methods=['GET', 'POST'])
def analyze(sentence=None):
    retval = None
    if request.method == 'POST':
        sentence = request.form['sentence']
        if sentence is not None:
            retval = SentimentAnalysis.Analyse_Raw(sentence)
            if retval['compound'] >= 0:
                retval['result'] = 'Pos'
            else:
                retval['result'] = 'Neg'

    return jsonify(retval)

if __name__ == "__main__":
    app.run("0.0.0.0",threaded=True)

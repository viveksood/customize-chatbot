from flask import Flask, render_template, request
import json
import chat

from chat import model ,words,labels,data

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random



app = Flask(__name__)



@app.route('/')
def home():
   return render_template('homepage.html')


@app.route('/jsonpage')
def json1():
   return render_template('jsonpage.html')

@app.route('/jsonpage',methods = ['POST'])
def add():
	if request.method == 'POST':
		with open("intents.json", "r") as read_file:
		    data = json.load(read_file)
		    entry = {}
		    entry['tag'] = request.form['tags']
		    entry['patterns'] = request.form['patterns'].split()
		    entry['responses'] = request.form['responses'].split()
		    entry['context_set'] = ""
		    data['intents'].append(entry)
		with open("intents.json",'w', encoding='utf-8') as feedsjson:
		    json.dump(data,feedsjson, indent=2)
	return render_template("jsonpage.html")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)
@app.route('/jsonpage/chatpage')
def index():
    return render_template('chatpage.html')
@app.route('/get')
def get_bot_response():
    print("Start talking with the bot (type quit to stop)!")
    inp = request.args.get('msg')
    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    if results[results_index]>0.5:

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        k=random.choice(responses)

    else:
        k='not getting'              
    return str(k)

@app.route('/button')
def button():
    chat.train_it()
    return render_template("jsonpage.html")


@app.route('/Load')
def button2():
    chat.load_it()
    return render_template("jsonpage.html")


if __name__ == '__main__':
   app.run(debug = True)
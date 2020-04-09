import json
import flask
from flask import request, render_template, url_for

import config

from transformers import T5ForConditionalGeneration, T5Tokenizer

app = flask.Flask(__name__)

model_size = 't5-small'
model = T5ForConditionalGeneration.from_pretrained(model_size)
tokenizer = T5Tokenizer.from_pretrained(model_size)

def summary(text):
    tokens = tokenizer.encode(text, 
                            max_length=256,
                            return_tensors='pt',
                            pad_to_max_length=True)

    gen_tokens = model.generate(tokens, max_length = 256)
    return tokenizer.decode(gen_tokens.tolist()[0])

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/api/v1/summarize', methods=['POST','GET'])
def api_summarize():
    if request.method == 'POST':
        text = request.form.get('text')
        return summary(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
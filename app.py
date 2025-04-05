import asyncio
from flask import Flask , render_template, request
from langdetect import detect
from googletrans import Translator, LANGUAGES

app=Flask(__name__)

async def d_and_t(text,targ):
    res=detect(text)
    translator = Translator()
    tr_text= await translator.translate(text,dest=targ)
    tr_res= tr_text.text
    return res,tr_res

@app.route('/')
def index():
    return render_template('index.html',languages=LANGUAGES)

@app.route('/trans',methods=['POST'])
async def trans():
    translation = ""
    detected_lang=""
    if request.method == 'POST':
        text = request.form['text']
        targ= request.form['targ']
        detected_lang, translation = await d_and_t(text,targ)
    return render_template('index.html',translation=translation,detected_lang=detected_lang,languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)

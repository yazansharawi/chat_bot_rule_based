from flask import Flask, render_template, request
import googletrans

app = Flask(__name__)
language = googletrans.LANGUAGES
lang_value = list(language.values())
lang1 = language.keys()


@app.route('/')
def index():
    return render_template('index.html', lang_value=lang_value)


@app.route('/translate', methods=['POST'])
def translate():
    txt = request.form['text']
    lang_to = request.form['lang_to']
    translator = googletrans.Translator()
    translated_text = translator.translate(txt, dest=lang_to).text

    return render_template('index.html', lang_value=lang_value, translated_text=translated_text)


if __name__ == '__main__':
    app.run(debug=True)

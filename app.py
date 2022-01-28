from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.congfig['SECRET_KEY'] = 'secret'

@app.route('/')
def get_prompts():

    prompts = story.prompts

    return render_template('questions.html', prompts = prompts)

@app.route('/story')
def get_story():

    text = story.generate(request.args)
    return render_template('story.html', text = text)

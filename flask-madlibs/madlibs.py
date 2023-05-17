from flask import Flask,request,render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def madlib():
    '''Show madlib form'''
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def story(ans):
    '''Show the madlib you've created'''
    template = story.generate(request.args)
    return render_template('story.html', template=template)

from unittest import result
from flask import Flask, render_template, request
import config
import blog


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'generateTopics' in request.form:
            prompt = request.form['blogTopic']
            result = blog.generateBlogTopics(prompt)
            Topics = result.replace('\n', '<br>')

        if 'generateOutline' in request.form:
            prompt = request.form['blogSection']
            result = blog.generateOutline(prompt)
            Outline = result.replace('\n', '<br>')

        if 'write' in request.form:
            prompt = request.form['blogExpander']
            result = blog.write(prompt)
            Write = result.replace('\n', '<br>')
        if 'passiveVoice' in request.form:
            prompt = request.form['passiveVoice']
            result = blog.passiveToActive(prompt)
            activeVoice = result.replace('\n', '<br>')

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

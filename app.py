from flask import Flask, render_template, abort, request

from model import find_all, find_by_id, find_by_name

app = Flask(__name__)


@app.route('/')
def list_all():
    if request.args.get('search'):
        recipes = find_by_name(request.args.get('search'))
    else:
        recipes = find_all()

    return render_template('list.html', recipes=recipes)


@app.route('/view/<int:recipe_id>')
def view(recipe_id):
    recipe = find_by_id(recipe_id) or abort(404)

    return render_template('view.html', recipe=recipe)


if __name__ == '__main__':
    app.run()

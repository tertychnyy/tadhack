from c1cli.entities.CoreResponse import ActionResponse
from flask import jsonify, request
from webapp.scripts import get_suggestions_by_name, get_recipe_by_name
from webapp.wsgi import bot


@bot.route("/")
def hello():
    name = request.args.get('name', None)
    if name is None:
        raise AttributeError

    rv = ActionResponse()

    suggestions = get_suggestions_by_name(name)

    recipe = get_recipe_by_name(name)

    retstr = "Your product: {good}\n\nBetter buy: {suggestions}\n\nRecipe by Jamie Oliver: {recipe}".format(good=name,
                                                                                                        suggestions="\n".join(suggestions),
                                                                                                            recipe=recipe)

    rv.messages = [retstr]
    return jsonify(rv.to_dict())

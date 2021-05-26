from flask import jsonify  # type: ignore
import jsonpickle  # type: ignore


def json_response(response):
    return jsonify(jsonpickle.pickler.Pickler(unpicklable=False).flatten(response))

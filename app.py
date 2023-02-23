#!/usr/bin/env python
from flask import Flask, Blueprint, jsonify, request


bp = Blueprint("app", __name__)


@bp.route("/api/v1/hello", methods=["GET"])
def get_request():
    """Hello world!"""
    return jsonify({"Hello": "World"})


@bp.route("/api/v1/hello", methods=["POST"])
def post_request():
    """Return the JSON payload in the response"""
    data = request.get_json()
    return jsonify(data)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    bp.run()

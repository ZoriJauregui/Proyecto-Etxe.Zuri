from pathlib import Path
from flask import Flask, request, abort, send_from_directory  # type: ignore
from config import config
from src.lib.web import json_response
from src.domain.interactor.carta_interactor import CartaInteractor
from src.domain.repository.carta_repository import CartaRepository

app = Flask(__name__)

carta_repository = CartaRepository(config)
carta_interactor = CartaInteractor(config, carta_repository)


@app.route("/")
def home():
    return "magic ..."


@app.route("/api/Etxe-Zuri/Carta", methods=["GET"])
def get_Carta():
    result = carta_interactor.get_cartas()
    return json_response(result), 200


@app.route("/images/<path:filename>", methods=["GET"])
def image(filename):
    return send_from_directory(Path.cwd() / "static", filename)


@app.route("/api/Etxe-Zuri/Theme", methods=["GET"])
def get_Themes():
    result = carta_interactor.get_Themes()
    return json_response(result), 200
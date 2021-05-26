import json
import jsonpickle  # type: ignore

from src.domain.model.Carta import Carta
from src.domain.model.Theme import Theme

from pathlib import Path


class CartaRepository:
    def __init__(self, config):
        self.database_path = config["database"]
        self.database_path_theme = config["themes"]

    def get_cartas(self):
        with open(self.database_path) as f:
            data = json.load(f)

            result = []
            for item in data:
                carta = Carta(item["id"], item["category"], item["products"])
                result.append(carta)
            return result

    def get_products_by_id(self, products, product_id):
        with open(self.database_path) as f:
            data = json.load(f)

            result = []
            for product in products:
                product = product(
                    item["product_id"], item["ingredients"], item["icon"], item["price"]
                )
            result.append(product)
        return result

    def get_Themes(self):
        with open(self.database_path_theme) as f:
            data = json.load(f)
            print(data)

            result = []
            for item in data:
                theme = Theme(item["id"], item["background"], item["color"])
                result.append(theme)
            return result

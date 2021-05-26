class CartaInteractor:
  def __init__(self, config, CartaRepository):
    self.carta_repository = CartaRepository

  def get_cartas(self):
    return self.carta_repository.get_cartas()

  def get_product_by_id(self, products, product_id):
    return self.carta_repository.get_product_by_id(id)

  def get_Themes(self):
    return self.carta_repository.get_Themes()
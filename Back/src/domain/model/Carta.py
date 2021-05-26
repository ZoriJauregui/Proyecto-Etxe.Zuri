class Carta:
      def __init__(self, id, category, products):
         self.id = id
         self.category = category
         self.products = products

      def products(self, product_id, ingredients, icon, price):
         self.product_id = product_id
         self.ingredients = ingredients
         self.icon = icon
         self.price = price
  
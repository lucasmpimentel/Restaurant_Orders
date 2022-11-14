class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.ESTOQUE = self.MINIMUM_INVENTORY.copy()
        self.PEDIDOS = list()

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            self.ESTOQUE[ingredient] -= 1
        self.PEDIDOS.append((customer, order, day))

    def get_quantities_to_buy(self):
        ordem_de_compra = self.MINIMUM_INVENTORY.copy() 

        for ingredient in self.PEDIDOS:
            ordem_de_compra[ingredient] -= self.ESTOQUE[ingredient]

        return ordem_de_compra

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
        self.PRATOS_DISPONIVEIS = set()

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.ESTOQUE[ingredient] < 1:
                return False
            self.ESTOQUE[ingredient] -= 1
        self.PEDIDOS.append((customer, order, day))

    def get_quantities_to_buy(self):
        ordem_de_compra = self.MINIMUM_INVENTORY.copy()

        for ingrediente in self.ESTOQUE:
            ordem_de_compra[ingrediente] -= self.ESTOQUE[ingrediente]

        return ordem_de_compra

    def get_avaliable_dishes(self):
        for prato in self.INGREDIENTS:
            for ingrediente in self.INGREDIENTS[prato]:
                if self.ESTOQUE[ingrediente] < 1:
                    break
                else:
                    self.PRATOS_DISPONIVEIS.add(prato)

        return self.PRATOS_DISPONIVEIS

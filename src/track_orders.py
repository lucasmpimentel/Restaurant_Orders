class TrackOrders:
    def __init__(self):
        self.pedidos = list()
        self.dias = set()
        self.pratos = set()

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, customer, order, day):
        self.pedidos.append({"customer": customer, "order": order, "day": day})
        self.dias.add(day)
        self.pratos.add(order)

    def get_most_ordered_dish_per_customer(self, customer):
        prato = {}

        for pedido in self.pedidos:
            if pedido["customer"] == customer:
                if pedido["order"] in prato:
                    prato[pedido["order"]] += 1
                else:
                    prato[pedido["order"]] = 1

        return max(prato, key=prato.get)

    def get_never_ordered_per_customer(self, customer):
        pratos_pedidos = set()

        for pedido in self.pedidos:
            if (pedido["customer"] == customer):
                pratos_pedidos.add(pedido["order"])

        return self.pratos.difference(pratos_pedidos)

    def get_days_never_visited_per_customer(self, customer):
        dias_visitados = set()

        for pedido in self.pedidos:
            if (pedido["customer"] == customer):
                dias_visitados.add(pedido["day"])

        return self.dias.difference(dias_visitados)

    def get_busiest_day(self):
        dias = {}

        for pedido in self.pedidos:
            if pedido["day"] in dias:
                dias[pedido["day"]] += 1
            else:
                dias[pedido["day"]] = 1

        return max(dias, key=dias.get)

    def get_least_busy_day(self):
        dias = {}

        for pedido in self.pedidos:
            if pedido["day"] in dias:
                dias[pedido["day"]] += 1
            else:
                dias[pedido["day"]] = 1

        return min(dias, key=dias.get)

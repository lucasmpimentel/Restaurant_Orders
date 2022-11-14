import csv
import os

alvos = ["maria", "arnaldo", "joao"]
pratos = ["hamburguer", "pizza", "coxinha", "misto-quente"]


def pratos_mais_pedidos(arquivo, alvo):
    prato = {}

    for pedido in arquivo:
        if (pedido[0] == alvo):
            if pedido[1] in prato:
                prato[pedido[1]] += 1
            else:
                prato[pedido[1]] = 1

    return max(prato, key=prato.get)


def contador_de_pedidos(arquivo, alvo, prato):
    result = 0

    for pedido in arquivo:
        if (pedido[0] == alvo and pedido[1] == prato):
            result += 1

    return result


def pratos_nunca_pedidos(arquivo, alvo):
    pratos_pedidos = set()
    pratos_restaurante = set(pratos)

    for pedido in arquivo:
        if (pedido[0] == alvo):
            pratos_pedidos.add(pedido[1])

    return pratos_restaurante.difference(pratos_pedidos)


def dias_sem_visitas(arquivo, alvo):
    dias = set()
    dias_visitados = set()

    for pedido in arquivo:
        dias.add(pedido[2])
        if (pedido[0] == alvo):
            dias_visitados.add(pedido[2])

    return dias.difference(dias_visitados)


def analyze_log(path_to_file):
    if ".csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open(path_to_file, encoding='utf-8') as arquivo:
        arquivo = list(csv.reader(arquivo, delimiter=',', quotechar='"'))

    result = open('data/mkt_campaign.txt', mode='w')

    result.write(f"{pratos_mais_pedidos(arquivo, alvos[0])}\n")
    result.write(f"{contador_de_pedidos(arquivo, alvos[1], pratos[0])}\n")
    result.write(f"{pratos_nunca_pedidos(arquivo, alvos[2])}\n")
    result.write(f"{dias_sem_visitas(arquivo, alvos[2])}\n")

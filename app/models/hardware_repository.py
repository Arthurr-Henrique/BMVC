import json
import os
from app.models.hardware import Hardware


class HardwareRepository:
    def __init__(self, caminho_json="db/hardware.json"):
        self.caminho_json = caminho_json
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        pasta = os.path.dirname(self.caminho_json)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)

        if not os.path.exists(self.caminho_json):
            self.salvar_todos([])

    def listar_todos(self):
        self._garantir_arquivo()
        try:
            with open(self.caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return [Hardware.from_dict(item) for item in dados]
        except (json.JSONDecodeError, KeyError, TypeError):
            return []

    def salvar_todos(self, itens):
        pasta = os.path.dirname(self.caminho_json)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)

        with open(self.caminho_json, "w", encoding="utf-8") as arquivo:
            json.dump([item.to_dict() for item in itens], arquivo, indent=2, ensure_ascii=False)

    def buscar_por_id(self, id_item):
        for item in self.listar_todos():
            if item.id == int(id_item):
                return item
        return None

    def criar(self, nome, categoria, descricao, preco):
        itens = self.listar_todos()
        proximo_id = max([item.id for item in itens], default=0) + 1
        novo = Hardware(proximo_id, nome, categoria, descricao, preco)
        itens.append(novo)
        self.salvar_todos(itens)
        return novo

    def atualizar(self, id_item, nome, categoria, descricao, preco):
        itens = self.listar_todos()
        for item in itens:
            if item.id == int(id_item):
                item.nome = nome
                item.categoria = categoria
                item.descricao = descricao
                item.preco = float(preco)
                self.salvar_todos(itens)
                return item
        return None

    def excluir(self, id_item):
        itens = self.listar_todos()
        novos_itens = [item for item in itens if item.id != int(id_item)]
        self.salvar_todos(novos_itens)
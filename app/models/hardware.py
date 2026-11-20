class Hardware:
    def __init__(self, id_item, nome, categoria, descricao, preco):
        self.id = int(id_item)
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
        self.preco = float(preco)

    def preco_formatado(self):
        return f"R$ {self.preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "preco": self.preco,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_item=data["id"],
            nome=data["nome"],
            categoria=data["categoria"],
            descricao=data["descricao"],
            preco=data["preco"],
        )
from bottle import template, redirect
from app.models.hardware_repository import HardwareRepository


class Application:
    def __init__(self):
        self.pages = {
            'helper': 'app/views/html/helper.tpl',
            'catalogo': 'app/views/html/catalogo.html',
            'hardware': 'app/views/html/hardware.html',
        }
        self.repo = HardwareRepository('db/hardware.json')

    def render(self, page, **kwargs):
        caminho = self.pages.get(page)
        if not caminho:
            return f"Página '{page}' não encontrada."
        return template(caminho, **kwargs)

    # READ (Listar / Exibir formulário de edição)
    def hardware(self, item_editar=None, erro=None):
        itens = self.repo.listar_todos()
        return self.render(
            'hardware',
            itens=itens,
            item_editar=item_editar,
            erro=erro,
        )

    # CREATE (Cadastrar novo hardware)
    def hardware_criar(self, form):
        nome = (form.get('nome') or '').strip()
        categoria = (form.get('categoria') or 'armazenamento').strip()
        descricao = (form.get('descricao') or '').strip()
        preco_raw = (form.get('preco') or '0').replace(',', '.').strip()

        if not nome or not descricao:
            return self.hardware(erro="Preencha nome e descrição do hardware.")

        try:
            preco = float(preco_raw)
        except ValueError:
            return self.hardware(erro="Informe um preço numérico válido.")

        self.repo.criar(nome, categoria, descricao, preco)
        return redirect('/hardware')

    # UPDATE - carregar item no formulário
    def hardware_form_editar(self, id_item):
        item = self.repo.buscar_por_id(id_item)
        if not item:
            return redirect('/hardware')
        return self.hardware(item_editar=item)

    # UPDATE - salvar alterações
    def hardware_atualizar(self, id_item, form):
        item = self.repo.buscar_por_id(id_item)
        if not item:
            return redirect('/hardware')

        nome = (form.get('nome') or '').strip()
        categoria = (form.get('categoria') or item.categoria).strip()
        descricao = (form.get('descricao') or '').strip()
        preco_raw = (form.get('preco') or str(item.preco)).replace(',', '.').strip()

        if not nome or not descricao:
            return self.hardware(item_editar=item, erro="Nome e descrição não podem ficar vazios.")

        try:
            preco = float(preco_raw)
        except ValueError:
            return self.hardware(item_editar=item, erro="Preço inválido.")

        self.repo.atualizar(id_item, nome, categoria, descricao, preco)
        return redirect('/hardware')

    # DELETE (Excluir hardware)
    def hardware_excluir(self, id_item):
        self.repo.excluir(id_item)
        return redirect('/hardware')
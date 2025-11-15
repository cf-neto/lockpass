import flet as ft
from data.database import criar_tabela, listar, inserir, remover, atualizar

def main(page):
    # CONFIGURAÇÕES DA PÁGINA
    page.title = "LockPass"
    page.padding = 10
    page.bgcolor = "#111827"
    page.scroll = ft.ScrollMode.AUTO

    # CRIAR BANCO DE DADOS
    criar_tabela()

    # LOGO
    logo = ft.Text("LockPass", size=25, weight=ft.FontWeight.BOLD)
    logo_container = ft.Container(
        content=logo,
        padding=10,
        margin=ft.margin.only(left=10)
    )

    # ========== TELA INICIAL ==========

    def ir_para_add(e):
        page.go('/add')

    def buscar(e):
        termo = input_text.value.lower()
        linhas.clear()
        dados = listar()

        for index, (app, usuario, senha) in enumerate(dados):
            if termo in app.lower() or termo in usuario.lower() or termo in senha.lower():

                row_color = "#131B2B" if index % 2 == 0 else "#0E1422"

                def remover_item(e, app_nome=app):
                    remover(app_nome)
                    atualizar_tabela()

                linhas.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(app, color="white")),
                            ft.DataCell(ft.Text(usuario, color="white")),
                            ft.DataCell(ft.Text(senha, color="white")),
                            ft.DataCell(
                                ft.IconButton(icon=ft.Icons.DELETE, icon_color="red", on_click=remover_item)
                            )
                        ],
                        color=row_color
                    )
                )
        page.update()
    
    def editar_item(e, app_nome, usuario_nome, senha_nome):
        novo_app.value = app_nome
        novo_usuario.value = usuario_nome
        nova_senha.value = senha_nome

        # Armazena o item original para atualizar depois
        page.session.set("edit_item", app_nome)

        page.go("/add")

    
    # INPUT
    input_text = ft.TextField(hint_text="Buscar item", width=400, on_change=buscar)
    input_tab = ft.Row(
        controls=[input_text, ft.IconButton(icon=ft.Icons.SEARCH)]
    )

    header_main = ft.Row(
        controls=[logo_container, input_tab, ft.IconButton(icon=ft.Icons.ADD, on_click=ir_para_add)],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # ====== TABELAS =====
    colunas = [
        ft.DataColumn(ft.Text('App', size=18)),
        ft.DataColumn(ft.Text('Usuário', size=18)),
        ft.DataColumn(ft.Text('Senha', size=18)),
        ft.DataColumn(ft.Text('Ações', size=18))
    ]

    linhas = []

    def atualizar_tabela():
        linhas.clear()
        dados = listar()
        for index, (app, usuario, senha) in enumerate(dados):

            # alternância de cores (zebra)
            row_color = "#131B2B" if index % 2 == 0 else "#0E1422"

            def remover_item(e, app_nome=app):
                remover(app_nome)
                atualizar_tabela()

            linhas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(app, color="white")),
                        ft.DataCell(ft.Text(usuario, color="white")),
                        ft.DataCell(ft.Text(senha, color="white")),
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color="yellow",
                                        on_click=lambda e, app_nome=app, usuario_nome=usuario, senha_nome=senha: editar_item(e, app_nome, usuario_nome, senha_nome)
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        icon_color="red",
                                        on_click=lambda e, app_nome=app: remover_item(e, app_nome)
                                    )
                                ]
                            )
                        )
                    ],
                    color=row_color  # cor aplicada na linha
                )
            )
        page.update()

    
    tabela = ft.DataTable(
        columns=colunas,
        rows=linhas,
        width=page.width * 0.9,
        heading_row_color=ft.Colors.with_opacity(1  , "#192031")

        
    )

    # Container apenas para estilo/alinhamento
    tabela_container = ft.Container(
        content=ft.Column(
            controls=[tabela],
            scroll=ft.ScrollMode.AUTO,  # aqui sim funciona
            height=700                 # altura fixa
        ),
        width=page.width * 0.9,
        alignment=ft.alignment.center,
        expand=True
    )

    
    pagina_principal = ft.Column(
        controls=[
            header_main,
            ft.Divider(height=1),
            tabela_container
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )



    atualizar_tabela()

    # =======================================

    # =========== ADD ===========
    novo_app = ft.TextField(
        label="Aplicativo / Site", 
        hint_text="Ex: Instagram", 
        prefix_icon=ft.Icons.APPS,
        width=300)
    
    novo_usuario = ft.TextField(
        label="Usuário / Email", 
        hint_text="Ex: exemplo123@gmail.com", 
        prefix_icon=ft.Icons.PERSON,
        width=300)
    
    nova_senha = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350
    )

    def salvar(e):
        item_antigo = page.session.get("edit_item")
        if novo_app.value and novo_usuario.value.strip() and nova_senha.value.strip() != "":
            if item_antigo:
                atualizar(item_antigo, novo_app.value, novo_usuario.value, nova_senha.value)
                page.session.set("edit_item", None)
            else:
                inserir(novo_app.value, novo_usuario.value, nova_senha.value)
                
            novo_app.value = ""
            novo_usuario.value = ""
            nova_senha.value = ""
            atualizar_tabela()
    
    def voltar(e):
        page.go('/')

    btn_salvar = ft.ElevatedButton(
        "Salvar",
        icon=ft.Icons.SAVE,
        bgcolor="#374151",
        color="white",
        width=200,
        height=45,
        on_click=salvar
    )

    header_add = ft.Row(
        controls=[ft.IconButton(icon=ft.Icons.WEST, on_click=voltar), logo_container],
    )

    pagina_add = ft.Column(
        controls=[
            header_add,
            ft.Divider(height=1),
            ft.Row(controls=[novo_app, novo_usuario, nova_senha, btn_salvar], alignment=ft.MainAxisAlignment.CENTER)
        ]
    )

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View("/", [pagina_principal], bgcolor="#111827")
            )
        
        if page.route == "/add":
            page.views.append(
                ft.View("/add", [pagina_add], bgcolor="#111827")
            )
    
        page.update()

    page.on_route_change = route_change

    page.go('/')

ft.app(target=main)
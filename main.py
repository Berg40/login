import flet as ft
import json
import os

# Função para carregar dados de um arquivo JSON
def carregar_dados():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            return json.load(file)
    return {}

# Função para salvar dados no arquivo JSON
def salvar_dados(dados):
    with open("usuarios.json", "w") as file:
        json.dump(dados, file, indent=4)

# Função principal
def main(page: ft.Page):
    page.title = 'Authenticator'
    page.window_always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = True
    page.padding = ft.padding.all(0)
    page.window_max_height = 900
    page.window_max_width = 400
    page.bgcolor = ft.colors.GREEN_200

    # Carregar dados de usuários existentes
    usuarios = carregar_dados()

    def logar(e: ft.ControlEvent):
        email = login_email.value
        senha = login_senha.value
        if email in usuarios and usuarios[email]['senha'] == senha:
            # Redireciona para uma nova página com o container amarelo
            page.remove(login)
            abrir_pagina_container_amarelo()
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Email ou senha incorretos."))
            page.dialog.open = True
            page.update()

    def registrar(e: ft.ControlEvent):
        email = register_email.value
        senha = register_senha.value
        primeiro_nome = register_primeiro_nome.value

        if email not in usuarios:
            usuarios[email] = {
                'primeiro_nome': primeiro_nome,
                'senha': senha
            }
            salvar_dados(usuarios)
            page.dialog = ft.AlertDialog(title=ft.Text("Conta criada com sucesso!"))
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Este email já está registrado."))
        page.dialog.open = True
        page.update()

    # Página de login
    login_email = ft.TextField(hint_text='Digite seu email', prefix_icon=ft.icons.PERSON)
    login_senha = ft.TextField(hint_text='Digite sua senha', prefix_icon=ft.icons.LOCK, password=True)

    login = ft.Column(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=400,
                height=320,
                padding=ft.padding.all(10),
                content=ft.Column(
                    controls=[
                        ft.Text(value='Sign-In', weight=ft.FontWeight.BOLD, size=20, color=ft.colors.BLACK),
                        login_email,
                        login_senha,
                        ft.ElevatedButton(text='Sign-In', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE, width=400, height=40, on_click=logar),
                        ft.TextButton(text='Criar nova conta', on_click=lambda e: page.remove(login) or page.add(register))
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Página de registro
    register_primeiro_nome = ft.TextField(hint_text='Primeiro nome', prefix_icon=ft.icons.PERSON)
    register_email = ft.TextField(hint_text='Digite seu email', prefix_icon=ft.icons.EMAIL)
    register_senha = ft.TextField(hint_text='Digite sua senha', prefix_icon=ft.icons.LOCK, password=True)

    register = ft.Column(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=400,
                padding=ft.padding.all(10),
                content=ft.Column(
                    controls=[
                        ft.Text(value='Register', weight=ft.FontWeight.BOLD, size=20, color=ft.colors.BLACK),
                        register_primeiro_nome,
                        register_email,
                        register_senha,
                        ft.ElevatedButton(text='Register', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE, width=400, height=40, on_click=registrar),
                        ft.TextButton(text='Já tenho uma conta', on_click=lambda e: page.remove(register) or page.add(login))
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Função para abrir a nova página com o container amarelo
    def abrir_pagina_container_amarelo():
        container_amarelo = ft.Container(
            expand=True,
            bgcolor=ft.colors.YELLOW,
            #border_radius=10,
            image_src='images/images (10).jpeg',
            image_fit=ft.ImageFit.COVER

        )
        page.add(container_amarelo)

    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)

import flet as ft

def main(page: ft.Page):
    page.title = "App Flet en Docker"
    page.add(ft.Text("¡Hola desde Docker!"))

ft.app(target=main, view=ft.WEB_BROWSER, port=8080)

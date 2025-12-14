import flet as ft


def Setting(page: ft.Page):
    return ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("Settings", size=35, weight=ft.FontWeight.BOLD),
                ft.Text("Configure your app settings here."),
            ]
        )
    )

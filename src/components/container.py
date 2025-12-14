


import flet as ft  
from typing import List


def Box(color: str, width: int, height: int, boder_value: int, content: List):
    return ft.Container(
        bgcolor=color,
        width=width,
        height=height,
        border_radius=boder_value,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=content
        )
    )
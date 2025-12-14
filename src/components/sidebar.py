import flet as ft 
from typing import List


class Sidebar(ft.Container):
    def __init__(self, page: ft.Page, nav_links: List):
        self.page = page
        super().__init__()
        self.width = 70
        # self.height = page.height
        self.padding = 10
        self.bgcolor = "#070606"
       

        # Build content directly
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    bgcolor="#1F1F23",
                    border_radius=15,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "L",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    )
                ),
                ft.Divider(color="transparent", height=20),
            ]
            + [
                ft.IconButton(
                    selected=True,
                    selected_icon_color="white",
                    icon_color="#1E3A8A",
                    icon=items["icon"],
                    icon_size=28,
                    on_click=lambda e, r=items["route"]: page.go(r)
                )
                for items in nav_links
            ]
        )
        
   
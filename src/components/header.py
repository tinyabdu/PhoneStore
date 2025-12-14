import flet as ft






class Header(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.content = self.build()
        

    def build(self):

        # ───────── SEARCH BAR ─────────
        search_box = ft.Container(
            bgcolor="#1A1A1D",
            border_radius=12,
            padding=10,
            height=46,
            expand=True,
            content=ft.Row(
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon("search", size=20, color="white"),
                    ft.TextField(
                        hint_text="Search...",
                        border=ft.InputBorder.NONE,
                        bgcolor="transparent",
                        text_size=14,
                        color="white",
                        cursor_color="white",
                        expand=True
                    )
                ],
            )
        )

        # ───────── TITLE ─────────
        header_title = ft.Text(
            "Today, Mon 22 Nov",
            color="white",
            size=16,
            weight=ft.FontWeight.BOLD,
        )

        # ───────── ACTION BUTTONS ─────────
        actions = ft.Row(
            spacing=0,
            controls=[
                ft.IconButton(
                    "settings",
                    icon_color="white",
                    on_click=lambda e: print("Settings clicked")
                ),
                ft.IconButton(
                    "notifications",
                    icon_color="white",
                    on_click=lambda e: print("Notification clicked")
                )
            ]
        )

        # ───────── MAIN HEADER CONTAINER ─────────
        return ft.Container(
            bgcolor="#000000",
            padding=15,
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    search_box,
                    header_title,
                    actions
                ]
            )
        )

    
    
    


    

def Header2():
    header_title = ft.Text("Today, Mon 22 Nov", color="white", weight=ft.FontWeight.BOLD)
    
    header_profile = ft.Row(
        spacing=0,
        controls=[
            ft.IconButton("settings", on_click=lambda e: print("click")),
            ft.IconButton("notifications")
        ]
    )
    search_box = ft.Container(
        bgcolor="#1A1A1D",
        border_radius=12,
        padding=10,
        width=300,
        height=50,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon("search", size=20, color="white"),
                ft.TextField(
                    hint_text="Search",
                    border=ft.InputBorder.NONE,
                    bgcolor="transparent",
                    text_size=14,
                    color="white",
                    cursor_color="white",
                    show_cursor=True,
                    expand=True
                )
            ]
        )
    )
    
    return ft.Container(
        bgcolor="#0A0606",
        padding=10,
        alignment=ft.alignment.top_center,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                search_box,
                header_title,
                header_profile
            ]
        )
    )
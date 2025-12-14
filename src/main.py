import flet as ft
from views import Home, Add, Setting
from components import Sidebar


# Colors
PRIMARY_BLUE = "#4A90E2"
SECONDARY_GREEN = "#7ED321"
ACCENT_ORANGE = "#F5A623"
NEUTRAL_LIGHT = "#F4F6FA"
NEUTRAL_DARK = "#1C1C28"
WHITE = "#FFFFFF"
GRAY = "#9B9B9B"

def main(page: ft.Page):

    # Disable transitions to prevent blinking
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            windows=ft.PageTransitionTheme.NONE
        )
    )
    page.update()

    # Create persistent sidebar once (no recreation)
    sidebar_icons = [
        {"icon": "dashboard_outlined", "route": "/"},
        {"icon": "list_alt", "route": "/add"},
        {"icon": "settings_outlined", "route": "/setting"},
    ]

    sidebar = Sidebar(page, sidebar_icons)

    # Body content that changes (NOT sidebar)
    body = ft.Container(expand=True)

    # Main layout stays on screen FOREVER
    layout = ft.View(
        route="/",
        padding=0,
        spacing=0,
        controls=[
            ft.Row(
                expand=True,
                spacing=0,
                controls=[
                    sidebar,
                    body
                ],
            ),
        ],
    )
    
    def on_resize(e):
        page.update()
        
    page.on_resized = on_resize
    
    # Routing: only body.content changes
    def route_change(e):
        if page.route == "/":
            body.content = Home(page)
        elif page.route == "/add":
            body.content = Add(page)
        elif page.route == "/setting":
            body.content = Setting(page)
        else:
            body.content = ft.Text("404 page not found")

        page.views.clear()
        page.views.append(layout)
        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(main)

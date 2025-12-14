import flet as ft


def Add(page: ft.Page):
    
    
    search = ft.TextField(
        hint_text="Search buyers...",
        width=300,
        suffix_icon=ft.Icon("Search"),
        border_radius=12,
        bgcolor="#121212",
        color="#E4E7EE",
        text_align=ft.TextAlign.LEFT,
        content_padding=ft.Padding(10, 0, 10, 0),
    )

    # Responsive cards
    cards = [
        ft.Container(
            height=150,
            bgcolor="#121212",
            border_radius=12,
            col={"xs": 12, "sm": 6, "md": 3},
        )
        for _ in range(4)
    ]

    return ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            spacing=25,
            expand=True,
            controls=[

                # HEADER
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("Buyer List", size=35, weight=ft.FontWeight.BOLD, color="#1E3A8A"),
                        ft.Row(
                            controls=[
                                ft.IconButton("settings", icon_color="#1E3A8A"),
                                ft.IconButton(
                                    "notifications",
                                    icon_color="#1E3A8A",
                                    on_click=lambda e: page.pubsub.send_all("toggle_notification"),
                                )
                            ]
                        )
                    ]
                ),

                ft.ResponsiveRow(cards),

                # Search + Add button
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        search,
                        ft.TextButton(
                            "Export CSv",
                            width=150,
                            height=45,
                            style=ft.ButtonStyle(
                                color="#E4E7EE",
                                bgcolor="#121212",
                                shape=ft.RoundedRectangleBorder(12)
                            )
                        ),
                        ft.TextButton(
                            "Add",
                            width=150,
                            height=45,
                            on_click=lambda e: page.open(ft.AlertDialog(
                                title=ft.Text("Add Buyer"),
                                content=ft.Text("add"),
                                actions=[
                                    ft.TextButton("close")])),
                            style=ft.ButtonStyle(
                                color="#E4E7EE",
                                bgcolor="#121212",
                                shape=ft.RoundedRectangleBorder(12)
                            )
                        )
                    ]
                ),

                # Table
                ft.Container(
                    bgcolor="#121212",
                    border_radius=10,
                    padding=10,
                    expand=True,  
                    content=ft.Column(
                        expand=True,  
                        controls=[
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("ID", color="#E4E7EE",)),
                                    ft.DataColumn(ft.Text("Product", color="#E4E7EE",)),
                                    ft.DataColumn(ft.Text("Amount", color="#E4E7EE",)),
                                    ft.DataColumn(ft.Text("Quantity", color="#E4E7EE",)),
                                    ft.DataColumn(ft.Text("Date", color="#E4E7EE",)),
                                    ft.DataColumn(ft.Text("Payment", color="#E4E7EE",)),
                                    ft.DataColumn(ft.Text("Status", color="#E4E7EE",)),
                                ],
                                rows=[],
                                expand=True,  
                                width=page.width,
                            )
                        ]
                    )
                )

            ]
        )
    )

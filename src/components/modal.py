import flet as ft
from typing import Optional

class Modal(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        title: str = "Modal",
        content: Optional[ft.Control] = None,
        on_close=None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        max_width: int = 600,
        max_height: Optional[int] = None,
        bgcolor: str = "white",
        position: str = "center",  # "center", "top", "bottom", "left", "right", "top_right", "top_left", "bottom_right", "bottom_left"
        animate_opacity: bool = True,
        closable: bool = True,
        close_on_backdrop_click: bool = True,
    ):
        super().__init__()
        self.page = page
        self.title_text = title
        self.modal_content = content
        self.on_close_callback = on_close
        self.modal_width = width
        self.modal_height = height
        self.max_width = max_width
        self.max_height = max_height
        self.modal_bgcolor = bgcolor
        self.position = position
        self.animate_opacity_enabled = animate_opacity
        self.closable = closable
        self.close_on_backdrop = close_on_backdrop_click
        
        # Build the modal
        self._build()
    
    def _build(self):
        # Prepare content
        if isinstance(self.modal_content, ft.Control):
            content_widget = self.modal_content
        elif isinstance(self.modal_content, list):
            content_widget = ft.Column(controls=self.modal_content, scroll=ft.ScrollMode.AUTO)
        else:
            content_widget = ft.Text("No content provided")
        
        # Header row
        header_controls: list[ft.Control] = [
            ft.Text(
                self.title_text,
                size=20,
                weight=ft.FontWeight.BOLD,
                expand=True,
            )
        ]
        
        if self.closable:
            header_controls.append(
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    on_click=self.close,
                    tooltip="Close",
                )
            )
        
        # Modal container with responsive sizing
        modal_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=header_controls,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(height=1),
                    ft.Container(
                        content=content_widget,
                        padding=ft.padding.only(top=10, bottom=10),
                    ),
                ],
                spacing=0,
            ),
            width=self.modal_width if self.modal_width else self.max_width,
            height=self.modal_height if self.modal_height else None,
            padding=20,
            bgcolor=self.modal_bgcolor,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, "black"),
                offset=ft.Offset(0, 4),
            ),
        )
        
        # Get alignment based on position
        alignment = self._get_alignment()
        
        # Backdrop
        backdrop_click = self.close if self.close_on_backdrop else None
        backdrop = ft.Container(
            bgcolor=ft.Colors.with_opacity(0.5, "black"),
            expand=True,
            on_click=backdrop_click,
            animate_opacity=300 if self.animate_opacity_enabled else None,
        )
        
        # Stack composition
        self.modal_stack = ft.Stack(
            controls=[
                backdrop,
                ft.Container(
                    content=modal_container,
                    alignment=alignment,
                    expand=True,
                    padding=20,  # Padding from edges
                ),
            ],
            expand=True,
            visible=False,
        )
        
        # Set properties for the Container parent class
        self.content = self.modal_stack
        self.expand = True
    
    def _get_alignment(self):
        """Get alignment based on position string"""
        alignments = {
            "center": ft.alignment.center,
            "top": ft.alignment.top_center,
            "bottom": ft.alignment.bottom_center,
            "left": ft.alignment.center_left,
            "right": ft.alignment.center_right,
            "top_right": ft.alignment.top_right,
            "top_left": ft.alignment.top_left,
            "bottom_right": ft.alignment.bottom_right,
            "bottom_left": ft.alignment.bottom_left,
        }
        return alignments.get(self.position, ft.alignment.center)
    
    def open(self, e=None):
        """Open the modal"""
        self.modal_stack.visible = True
        if self.page:
            self.page.update()
    def close(self, e=None):
        """Close the modal"""
        self.modal_stack.visible = False
        if self.page:
            self.page.update()
        if self.on_close_callback:
            self.on_close_callback(e)
    
    def toggle(self, e=None):
        """Toggle modal visibility"""
        self.modal_stack.visible = not self.modal_stack.visible
        if self.page:
            self.page.update()
    
    def update_content(self, new_content):
        """Update modal content dynamically"""
        self.modal_content = new_content
        self._build()
        if self.page:
            self.page.update()
    
    def update_title(self, new_title):
        """Update modal title"""
        self.title_text = new_title
        self._build()
        if self.page:
            self.page.update()


def main(page: ft.Page):
    page.title = "Modal Class Demo"
    page.padding = 20
    
    # Example 1: Simple modal
    modal1 = Modal(
        page=page,
        title="Simple Modal",
        content=ft.Column(
            controls=[
                ft.Text("This is a simple centered modal", size=16),
                ft.TextField(label="Enter something", width=300),
                ft.ElevatedButton("Submit", width=300),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        on_close=lambda e: print("Modal 1 closed"),
    )
    
    # Example 2: Top-right notification modal
    modal2 = Modal(
        page=page,
        title="Notification",
        content=ft.Text("This is a notification in the top-right corner!"),
        position="top_right",
        width=300,
        height=150,
        bgcolor=ft.Colors.BLUE_50,
    )
    
    # Example 3: Full-featured modal with custom styling
    modal3 = Modal(
        page=page,
        title="Advanced Modal",
        content=ft.Column(
            controls=[
                ft.Text("This modal has many features:", weight=ft.FontWeight.BOLD),
                ft.Text("✓ Responsive sizing"),
                ft.Text("✓ Custom positioning"),
                ft.Text("✓ Scrollable content"),
                ft.Text("✓ Animation support"),
                ft.Divider(),
                ft.Text("Lorem ipsum " * 50),  # Long text to show scrolling
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=10,
        ),
        max_width=500,
        max_height=400,
        bgcolor=ft.Colors.PURPLE_50,
        position="center",
    )
    
    # Example 4: Non-closable modal
    modal4 = Modal(
        page=page,
        title="Important Message",
        content=ft.Column(
            controls=[
                ft.Text("This modal cannot be closed by clicking outside or the X button."),
                ft.ElevatedButton("I Understand", on_click=lambda e: modal4.close()),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        closable=False,
        close_on_backdrop_click=False,
        width=350,
    )
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Modal Class Examples", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Open Simple Modal", on_click=modal1.open),
                        ft.ElevatedButton("Open Notification", on_click=modal2.open),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Open Advanced Modal", on_click=modal3.open),
                        ft.ElevatedButton("Open Non-Closable", on_click=modal4.open),
                    ],
                    wrap=True,
                ),
            ],
            spacing=15,
        ),
        modal1,
        modal2,
        modal3,
        modal4,
    )


ft.app(target=main)
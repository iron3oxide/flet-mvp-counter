import flet as ft


def counter():
    return ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100,
    )

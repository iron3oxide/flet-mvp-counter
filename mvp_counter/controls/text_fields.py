import flet as ft


def counter(ref: ft.Ref | None) -> ft.TextField:
    return ft.TextField(
        ref=ref,
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100,
    )

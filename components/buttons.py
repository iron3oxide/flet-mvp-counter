from typing import Callable

import flet as ft


def remove(on_click: Callable) -> ft.IconButton:
    return ft.IconButton(ft.icons.REMOVE, on_click=on_click)


def add(on_click: Callable) -> ft.IconButton:
    return ft.IconButton(ft.icons.ADD, on_click=on_click)

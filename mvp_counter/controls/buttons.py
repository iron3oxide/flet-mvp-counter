from typing import Callable

import flet as ft


def remove(callback: Callable) -> ft.IconButton:
    return ft.IconButton(ft.icons.REMOVE, on_click=callback)


def add(callback: Callable) -> ft.IconButton:
    return ft.IconButton(ft.icons.ADD, on_click=callback)


def login(callback: Callable) -> ft.ElevatedButton:
    return ft.ElevatedButton(text="Login with Github", on_click=callback)

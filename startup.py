import flet as ft

def main(page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    def show_w():
        return None
    
    def show_c():
        



    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=80),
        content=ft.Text("Seagull version 1, Copyright (C) 2024 Kai Broadbent 'BlazarKnight' Seagull comes with ABSOLUTELY NO WARRANTY; for details hit `show w'. This is free software, and you are welcome to redistribute it under certain conditions; hit `show c' for details.", color=ft.colors.RED,size=40),
        actions=[
            ft.TextButton("show w", on_click=show_w),
            ft.TextButton("show c", on_click=close_banner),
            ft.TextButton("I understand and accept", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    show_banner_click(1)



if __name__ == "__main__":
    ft.app(target=main)
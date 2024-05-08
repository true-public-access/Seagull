''' Seagull statup this file is run at the start of the program to outline terms and conditions, 
    Copyright (C) 2024 Kai Broadbent 'BlazarKnight'

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to appblazarknight@gmail.com
    '''





import flet as ft
import os
def main(page):
    
    
    
    
    
    
    
    def close_banner(e):
        page.banner.open = False
        page.update()

    def show_w(e):
        woren.open = True
        woren.update()
    
    def show_c(e):
        condis.open = True
        condis.update()



    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=80),
        content=ft.Text("Seagull version 1, Copyright (C) 2024 Kai Broadbent 'BlazarKnight' Seagull comes with ABSOLUTELY NO WARRANTY; for details hit `show w'. This is free software, and you are welcome to redistribute it under certain conditions; hit `show c' for details.", color=ft.colors.RED,size=40),
        actions=[
            ft.TextButton("show w", on_click=show_w),
            ft.TextButton("show c", on_click=show_c),
            ft.TextButton("I understand and accept", on_click=close_banner),
        ],

        )

    def show_banner_click(e):
        page.banner.open = True
        page.update()
    

# bottum baner stuff waren 

    def waren_dismissed(e):
        print("Dismissed!")

    def show_waren(e):
        woren.open = True
        woren.update()

    def close_waren(e):
        woren.open = False
        woren.update()

    woren= ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                 
                    ft.Text(open('text_to_display/warrantyfordis.txt',"r").read()),
                    ft.ElevatedButton("Close and accept", on_click=close_waren),
                ],
                tight=True,
            ),
            padding=4,
        ),
        open=False,
        on_dismiss=waren_dismissed,
        is_scroll_controlled= True,
        maintain_bottom_view_insets_padding=True,
        )
    page.overlay.append(woren)
    
    # bottum baner stuff consis 

    def condis_dismissed(e):
        print("Dismissed!")

    def show_condis(e):
        condis.open = True
        condis.update()

    def close_condis(e):
        condisopen = False
        condis.update()

    condis= ft.BottomSheet(
        content=ft.Text(str(open('text_to_display/condistodisplay.txt',"r").read()),text_align="center",overflow="visible"),
        show_drag_handle=True,
        enable_drag=True,
        open=False,
        on_dismiss=condis_dismissed,
        is_scroll_controlled= True,
        maintain_bottom_view_insets_padding=10000,
        use_safe_area=True,
       
        )
    page.overlay.append(condis)

    
    show_banner_click(2)



if __name__ == "__main__":
    print(str(open('text_to_display/condistodisplay.txt',"r").read()))
    ft.app(target=main)
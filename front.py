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
import setings.setingsedit as st
import browser.broser as br

def first_start(page):
    
    def close_dlg(e):
            st.updateset('showtconstart',"False")
            dlg_modal.open = False
            page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("show terms and condionds nexed use"),
        content=ft.Text("Do want see this page on every startup?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
    
    
   
        
        


    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def dontshoag(e):
        open_dlg_modal(1)
        

    def close_banner(e):
        page.banner.open = False
        page.update()
        dontshoag(1)

    def show_w(e):
        woren.open = True
        woren.update()
    
    def show_c(e):
        condis.open = True
        condis.update()



    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.BLUE, size=80),
        content=ft.Text("Seagull version 1, Copyright (C) 2024 Kai Broadbent 'BlazarKnight' Seagull comes with ABSOLUTELY NO WARRANTY; for details hit `show w'. This is free software, and you are welcome to redistribute it under certain conditions; hit `show c' for details.", color=ft.colors.RED,size=40),
        actions=[
            ft.TextButton("show w", on_click=show_w),
            ft.TextButton("show c", on_click=show_c),
            ft.TextButton("I understand and accept", on_click=close_banner),
        ],)

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
            padding=40,
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
    wid= 10**400
    cl = ft.Column(
            spacing=10,
            height=20000000,
            width=20000000,
            scroll=ft.ScrollMode.ALWAYS,
            )
   
    cl.controls.append(ft.Text(str(open('text_to_display/condistodisplay.txt',"r").read())))

    condis= ft.BottomSheet(
        
        
            
            
        ft.Container(cl, border=ft.border.all(1)),
        #content=cl.controls.append(ft.Text(str(open('text_to_display/condistodisplay.txt',"r").read()))),
        #content=ft.Text(str(open('text_to_display/condistodisplay.txt',"r").read()),overflow="visible",width=wid,data="text",max_lines=wid),
        show_drag_handle=True,
        enable_drag=True,
        open=False,
        on_dismiss=condis_dismissed,
        is_scroll_controlled= False,
        maintain_bottom_view_insets_padding=True,
        use_safe_area=True,
        
        
        )
    page.overlay.append(condis)
    show_banner_click(2)

def searchpg(page):
 
    def button_clicked(e):
        t.value = br.wildwebser(tfinerse.value) , tfaise.value 
        page.update()

    t = ft.Text()
    tfaise = ft.TextField(label="AI search")
    tfinerse = ft.TextField(label="Inernet search")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tfaise, tfinerse,t,b)

def setuppage(page):
    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        page.update()

    t = ft.Text("sory we cuently only support firefox")
    b = ft.ElevatedButton(text="browser selected", on_click=button_clicked)
    dd = ft.Dropdown(
        label="browser",
        hint_text="Choose your browser",

        width=100,
        options=[
             ft.dropdown.Option("Firefox"),
            
            
            #ft.dropdown.Option("Chrome"),
            
            #ft.dropdown.Option("Edge"),
            #ft.dropdown.Option("Internet Explorer"),
            #ft.dropdown.Option("safari"),
            

        ],
    )
    page.add(dd, b, t)

    


def runpage(e):
    ft.app(target=e)

if __name__ == "__main__":
   
    runpage(setuppage)




    

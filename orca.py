''' Seagull statup this file is the pklace where the real work hapens here all the fuctions are used, 
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
import browser.broser as br
import formater.format as form
import setings.setingsedit as seter
import front as frt

if bool(seter.rdset("showtc")):
    frt.runpage(frt.first_start)



if __name__ == "__main__":
    from browser.broser import geturlsorce

    from formater.format import clean

    raw=geturlsorce("https://www.sec.gov/Archives/edgar/data/38777/000003877724000070/frkbsp24a6.htm")
    print(clean(raw,"htm"))
    




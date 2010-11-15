#!/usr/bin/env python3

#############################################################################
#    Copyright (C) 2010  Michał Maciej Różański			            #
#									    #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or	    #
#    any later version.							    #
#									    #
#    This program is distributed in the hope that it will be useful,	    #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of	    #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the	    #
#    GNU General Public License for more details.			    #
#									    #
#    You should have received a copy of the GNU General Public License	    #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#############################################################################

import os, platform

if __name__ == '__main__':
    p = platform.uname()
    info = {'System: ' : p[0], 'Hostname: ' : p[1], 'Edycja Systemu: ' : p[2], 'Wersja: ' : p[3], 'Typ maszyny: ' : p[4], 'Procesor: ' : p[5]}
    
    for i in info:
        print(i + info[i])

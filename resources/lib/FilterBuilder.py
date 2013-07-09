# -*- coding=utf8 -*-
#******************************************************************************
# FilterBuilder.py
#------------------------------------------------------------------------------
#
# Copyright (c) 2013 LivingOn <LivingOn@xmail.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#******************************************************************************
import xbmcplugin

class FilterBuilder(object):
    
    _KEYS = ( "mädchen", "lesben", "reife-frauen", "fetisch", "paare", "gruppe", 
              "heisser-flirt", "seelenverwandte", "deutsch", "englisch", "spanisch", 
              "franzoesisch", "italienisch", "geburtstag", "sale", "porn-star", 
              "anfänger", "hd-qualitaet", "mit-ton", "2-weg-audio", "18-22", 
              "zwanziger-jahre", "milf", "mami", "asiatin", "ebony", "weiß", "latin", 
              "zierlich", "gross", "rasiert", "behaart", "piercing", "tattoo", 
              "stockings", "leder", "schwarzhaarige", "blond", "brünette", "rothaarige", 
              "kurze-haare", "lange-haare", "kleine-brüste", "grosse-titten" 
            )
    
    _plugin_id = None
    
    def __init__(self, plugin_id):
        self._plugin_id = plugin_id
        
    def get_filter(self):
        result = []
        for key in self._KEYS:
            if xbmcplugin.getSetting(self._plugin_id, key) == "true":
                result.append(key)
        return "-".join(result)

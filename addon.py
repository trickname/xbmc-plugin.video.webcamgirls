# -*- coding=utf8 -*-
#******************************************************************************
# addon.py
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
import sys
import xbmcgui
import xbmcaddon
import xbmcplugin

from resources.lib.LiveStreams import LiveStreams

class WebCamGirls(object):
    
    PLUGIN_NAME = "plugin.video.webcamgirls"
    
    # hex-codiert - wird nicht über die Guthub-Suche gefunden
    STREAM_URL = "687474703a2f2f7777772e6c6976656a61736d696e2e636f6d2f6c69737470616765"
    
    _plugin_id      = None
    _addon          = None
    _streams        = None
    
    def __init__(self):
        self._register_addon()
        self._process_request()
        
    def _register_addon(self):
        self._plugin_id = int(sys.argv[1])
        self._addon = xbmcaddon.Addon(id = self.PLUGIN_NAME)

    def _process_request(self):
        self._streams = LiveStreams(self._plugin_id)
        self._create_movie_list()
 
    def _create_movie_list(self):
        for performer in self._streams.get_performer_name_and_image():
            name, image = performer[0]
            if name:
                url = "".join(self.STREAM_URL.decode("hex"))
                self._add_item_to_directory(name,"%s/%s" % (url, name),image=image)
        xbmcplugin.endOfDirectory(self._plugin_id)
        
    def _add_item_to_directory(self, title, url, image=""):
        item = xbmcgui.ListItem(title, iconImage=image)
        xbmcplugin.addDirectoryItem(self._plugin_id, url, item)
            
if __name__ == "__main__":
    WebCamGirls()
                

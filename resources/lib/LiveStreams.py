# -*- coding=utf8 -*-
#******************************************************************************
# LiveStreams.py
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
import re
import urllib
from resources.lib.FilterBuilder import FilterBuilder

class LiveStreams(object):

    # hex-codiert - wird nicht über die Github-Suche gefunden
    _URL = "687474703a2f2f6e65772e6c6976656a61736d696e2e636f6d2f64652f6769726c732f6772617469732d63686174"
    _PATTERN = re.compile(r"<img id=\"perfimg_(.*?)_.*src=\"(.*?)\?.*")
    
    _plugin_id = None
    _filter_builder = None
    
    def __init__(self, plugin_id):
        self._plugin_id = plugin_id
        self._filter_builder = FilterBuilder(self._plugin_id)

    def get_performer_name_and_image(self):
        url = self._URL.decode("hex")
        result = []
        filters = self._filter_builder.get_filter()
        if filters:
            url = "%s-%s" % (url, filters)
        data = urllib.urlopen(url).readlines()
        for zeile in data:
            matchobj = self._PATTERN.findall(zeile)
            if matchobj:
                result.append(matchobj)
        return result

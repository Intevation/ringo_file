#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import base64
import pkg_resources
from mako.lookup import TemplateLookup
from formbar.renderer import FieldRenderer
from ringo.lib.helpers import literal, get_action_routename

# We need to configure the template lookup system and "register" a new
# location of the templates. Mako will search in this locations for
# templates to render.
base_dir = pkg_resources.get_distribution("ringo_file").location
template_dir = os.path.join(base_dir, 'ringo_file', 'templates')
template_lookup = TemplateLookup(directories=[template_dir],
                                 default_filters=['h'])


class PreviewFieldRenderer(FieldRenderer):

    def __init__(self, field, translate):
        FieldRenderer.__init__(self, field, translate)
        self.template = template_lookup.get_template("previewfield.mako")

    def _get_template_values(self):
        values = FieldRenderer._get_template_values(self)
        request = self._field._form._request
        item = self._field._form._item
        values["url"] = request.route_path(get_action_routename(item, "download"), id=item.id)
        values["mime"] = item.mime
        values["item"] = item
        return values


def render_file_preview(request, item, column, tableconfig):
    """Returns HTML code to embed a small preview of the file in the
    overview"""
    if isinstance(item, tuple):
        item = item[0]
    return literal('<embed src="data:{};base64,{}" type="{}">'.format(item.mime, base64.b64encode(item.thumbnail), item.mime))

import logging
from pyramid.i18n import TranslationStringFactory
from ringo.lib.i18n import translators
from ringo.lib.extension import register_modul
from ringo.lib.renderer.form import renderers

# This import is needed to trigger "registering" the views.
import ringo_file.views

# Import models so that alembic is able to autogenerate migrations
# scripts.
from ringo_file.model import File
from ringo_file.renderer import PreviewFieldRenderer

log = logging.getLogger(__name__)

modul_config = {
    "name": "files",
    "label": "",
    "clazzpath": "ringo_file.model.File",
    "label_plural": "",
    "str_repr": "",
    "display": "",
    "actions": ["list", "read", "update", "create", "delete", "download"]
}


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    modul = register_modul(config, modul_config)
    if modul:
        File._modul_id = modul.get_value("id")
        translators.append(TranslationStringFactory('ringo_file'))
        config.add_translation_dirs('ringo_file:locale/')


# Finally register the template in ringo to make the renderer known in
# formbar.
renderers['filepreview'] = PreviewFieldRenderer

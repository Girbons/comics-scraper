"""
This module is largely inspired by django-rest-framework settings.
"""
import six
import importlib


DEFAULT_SETTINGS = {
    'comicextra.com': 'comics.sites.comicextra.ComicExtra',
    'mangareader.net': 'comics.sites.mangareader.MangaReader',
    'readcomiconline.to': 'comics.sites.readcomiconline.ReadComicOnline',

    # is the path where you will find all your downloaded comics
    # divided by domain
    'path': 'downloaded_comics',
}

IMPORT_STRINGS = (
    'comicextra.com',
    'mangareader.net',
    'readcomiconline.to',
)


SUPPORTED_SITES = list(DEFAULT_SETTINGS.keys())


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if isinstance(val, six.string_types):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '%s' for setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)


class ComicsSettings(object):
    def __init__(self, defaults=None, import_strings=None):
        self.defaults = defaults or {}
        self.import_strings = import_strings or ()

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid setting: '%s'" % attr)

        val = self.defaults[attr]

        # Coerce import strings into classes
        if val and attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        setattr(self, attr, val)
        return val


comics_settings = ComicsSettings(DEFAULT_SETTINGS, IMPORT_STRINGS)

"""
The compat module provides support for backwards compatibility with older version of python.
"""

# flake8: noqa
try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit

try:
    from tempfile import TemporaryDirectory
except ImportError:
    from backports.tempfile import TemporaryDirectory

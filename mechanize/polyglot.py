#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2018, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

is_py2 = sys.version_info.major < 3

if is_py2:
    from urllib import (
            urlencode, pathname2url, quote, addinfourl, quote_plus, urlopen
    )
    from urllib2 import (
            HTTPError, URLError, install_opener, build_opener, ProxyHandler
    )
    from urllib.robotparser import RobotFileParser
    from urllib.parse import urlsplit, urljoin, urlparse, urlunparse
    from http.client import HTTPMessage, HTTPConnection, HTTPSConnection
    from http.cookiejar import (
            DEFAULT_HTTP_PORT, CookiePolicy, DefaultCookiePolicy,
            FileCookieJar, LoadError, LWPCookieJar, _debug, domain_match,
            eff_request_host, escape_path, is_HDN, lwp_cookie_str, reach,
            request_path, request_port, user_domain_match, Cookie, CookieJar,
            MozillaCookieJar, request_host)

    from future_builtins import map  # noqa

    def is_string(x):
        return isinstance(x, str)

    def iteritems(x):
        return iter(x.items())

    def itervalues(x):
        return iter(x.values())

    def is_class(obj):
        return isinstance(obj, type)

    def raise_with_traceback(exc):
        exec('raise exc, None, sys.exc_info()[2]')

    codepoint_to_chr = chr
    unicode_type = str


else:
    from urllib.error import HTTPError, URLError
    from urllib.robotparser import RobotFileParser
    from urllib.parse import (
            urlsplit, urljoin, urlparse, urlunparse, urlencode, quote_plus
    )
    from urllib.request import (
            pathname2url, quote, addinfourl, install_opener, build_opener,
            ProxyHandler, urlopen)
    from http.client import HTTPMessage, HTTPConnection, HTTPSConnection
    from http.cookiejar import (
            DEFAULT_HTTP_PORT, CookiePolicy, DefaultCookiePolicy,
            FileCookieJar, LoadError, LWPCookieJar, _debug, domain_match,
            eff_request_host, escape_path, is_HDN, lwp_cookie_str, reach,
            request_path, request_port, user_domain_match, Cookie, CookieJar,
            MozillaCookieJar, request_host)

    def is_string(x):
        return isinstance(x, str)

    def iteritems(x):
        return list(x.items())

    def itervalues(x):
        return list(x.values())

    def is_class(obj):
        return isinstance(obj, type)

    def raise_with_traceback(exc):
        raise exc.with_traceback(sys.exc_info()[2])

    codepoint_to_chr = chr
    unicode_type = str


def force_bytes(s, encoding='utf-8'):
    if not isinstance(s, bytes):
        return s.encode(encoding)
    return s


from io import StringIO


if False:
    HTTPError, urlsplit, urljoin, urlparse, urlunparse, urlencode, HTTPMessage
    pathname2url, RobotFileParser, URLError, quote, HTTPConnection
    HTTPSConnection, StringIO, addinfourl, install_opener, build_opener
    ProxyHandler, quote_plus, urlopen
    (DEFAULT_HTTP_PORT, CookiePolicy, DefaultCookiePolicy,
     FileCookieJar, LoadError, LWPCookieJar, _debug,
     domain_match, eff_request_host, escape_path, is_HDN,
     lwp_cookie_str, reach, request_path, request_port,
     user_domain_match, Cookie, CookieJar, MozillaCookieJar, request_host)

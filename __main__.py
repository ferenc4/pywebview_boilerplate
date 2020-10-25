# !/usr/bin/env python3

from contextlib import contextmanager, redirect_stderr, redirect_stdout
from os import devnull

import webview


@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


def get_cli(window):
    result = window.evaluate_js(
        r"""
        var h1 = document.createElement('h1')
        var text = document.createTextNode('Hello pywebview')
        h1.appendChild(text)
        document.body.appendChild(h1)

        document.body.style.backgroundColor = '#212121'
        document.body.style.color = '#f2f2f2'

        // Return user agent
        'User agent:\n' + navigator.userAgent;
        """
    )
    print(result)


class Api:
    def __init__(self):
        """
        See https://pywebview.flowrl.com/examples/js_api.html
        """
        self.window = None

    def set_window(self, window):
        self.window = window

    def customMessage(self, param):
        print(f"The website said {param}")

    def fullScreenToggle(self):
        print("Toggling Full Screen")
        window.toggle_fullscreen()

    def set_screen_size(self, width, height):
        print(f"Setting screen size to width: {width}, height: {height}")
        window.resize(width, height)

    def exit(self):
        print("Closing window")
        window.destroy()


if __name__ == '__main__':
    html = """
<html>
<body>
<button onclick="pywebview.api.customMessage('Hi from the site!')">Say Hi!</button>
<button onclick="pywebview.api.fullScreenToggle()">Full Screen Toggle</button>
<button onclick="pywebview.api.set_screen_size(800, 600)">800x600</button>
<button onclick="pywebview.api.set_screen_size(1280, 1024)">1280x1024</button>
<button onclick="pywebview.api.exit()">Exit</button>
</body>
</html>
    """
    api = Api()
    # use "url" param to load a site instead of html
    window = webview.create_window("My site", html=html,
                                   width=1440, height=1024, resizable=True, fullscreen=False, on_top=True,
                                   js_api=api)
    api.set_window(window)
    webview.start(window)
    print("Finishing")

from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the dnmr_ab.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "chem333test.ipynb", "--allow-websocket-origin=*"])
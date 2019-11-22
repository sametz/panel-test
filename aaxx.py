from collections import deque

import holoviews as hv
import numpy as np
import panel as pn

from nmrtools.qm import spectrum
from utils import lineshape_from_peaklist


def aaxx(va=110.0, vx=90.0,
         Jaa=15.0, Jxx=15.0, Jax=7.0, Jax_prime=7.0):
    # a quirk of this old nmrtools library is that freqs must be an np array and not just a list of lists;
    # this seems to be fixed in the new nmrsim library 
    freqs = np.array([va, va, vx, vx])
    Js = np.array(
        [[0.0, Jaa, Jax, Jax_prime],
         [Jaa, 0.0, Jax_prime, Jax],
         [Jax, Jax_prime, 0, Jxx],
         [Jax_prime, Jax, Jxx, 0]])
    peaklist = spectrum(freqs, Js)
    x, y = lineshape_from_peaklist(peaklist)
    return hv.Curve(zip(x, y))


aaxx_app = pn.interact(aaxx,
                       va=(0.0, 300.0, 0.1, 110.0),
                       vx=(0.0, 300.0, 0.1, 90.0),
                       Jaa=(0.0, 20.0, 0.1, 5.0),
                       Jxx=(0.0, 20.0, 0.1, 10.0),
                       Jax=(0.0, 20.0, 0.1, 13.0),
                       Jax_prime=(0.0, 20.0, 0.1, 13.0))

aaxx_text_1 = pn.pane.Markdown('''
#### AA'XX' text goes here
''')
aaxx_text_2 = pn.pane.Markdown('''text 2''')

backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward)

test_text = [aaxx_text_1, aaxx_text_2]
deque_text = deque(test_text)
text_column = pn.Column(back_fwd, deque_text[0])


def next_text(event):
    deque_text.rotate(-1)
    text_column[1] = deque_text[0]


def prev_text(event):
    deque_text.rotate()
    text_column[1] = deque_text[0]


backward.on_click(prev_text)
forward.on_click(next_text)

aaxx_row = pn.Row(aaxx_app, text_column)

if __name__ == '__main__':
    aaxx_row.show()
    aaxx_row.servable()

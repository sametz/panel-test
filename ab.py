from collections import deque

import holoviews as hv
import numpy as np
import panel as pn

from nmrtools.qm import spectrum
from utils import lineshape_from_peaklist


def ab_quartet(v1=150.0, v2=50.0, J=10.0):
    # a quirk of this old nmrtools library is that freqs must be an np array and not just a list of lists;
    # this seems to be fixed in the new nmrsim library 
    freqs = np.array([v1, v2])
    Js = np.array(
        [[0.0, J],
         [J, 0.0]])
    peaklist = spectrum(freqs, Js)
    x, y = lineshape_from_peaklist(peaklist)
    return hv.Curve(zip(x, y))


ab_app = pn.interact(ab_quartet, v1=(0.0, 300.0, 0.1, 150.0), v2=(0.0, 300.0, 0.1, 50.0), J=(0.0, 20.0, 0.1, 10.0))

dd_text_1 = pn.pane.Markdown('''
#### AB quartet text goes here
''')
dd_text_2 = pn.pane.Markdown('''text 2''')

backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward)

test_text = [dd_text_1, dd_text_2]
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

ab_row = pn.Row(ab_app, text_column)


if __name__ == '__main__':
    ab_row.show()
    ab_row.servable()

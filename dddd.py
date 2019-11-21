from collections import deque

import holoviews as hv
import panel as pn

from nmrtools.firstorder import first_order
from utils import lineshape_from_peaklist


def dddd(J1, J2, J3, J4, w):
    singlet = (100, 1)  # center at 100 Hz; intensity 1
    couplings = [(J1, 1), (J2, 1), (J3, 1), (J4, 1)]
    peaklist = first_order(singlet, couplings)
    x, y = lineshape_from_peaklist(peaklist, w=w, limits=(75, 125))
    return hv.Curve(zip(x, y))


dddd_app = pn.interact(dddd,
                       J1=(0.0, 20.0, 0.1, 6.0),
                       J2=(0.0, 20.0, 0.1, 6.0),
                       J3=(0.0, 20.0, 0.1, 10.0),
                       J4=(0.0, 20.0, 0.1, 16.0),
                       w=(0.1, 10.0, 0.1, 0.5))

dddd_text_1 = pn.pane.Markdown('''
#### dddd text here
''')
dddd_text_2 = pn.pane.Markdown('''
page 2
''')

backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward)
dddd_text = [dddd_text_1, dddd_text_2]
deque_text = deque(dddd_text)
text_column = pn.Column(back_fwd, deque_text[0])


def next_text(event):
    deque_text.rotate(-1)
    text_column[1] = deque_text[0]


def prev_text(event):
    deque_text.rotate()
    text_column[1] = deque_text[0]


backward.on_click(prev_text)
forward.on_click(next_text)

dddd_row = pn.Row(dddd_app, text_column)


if __name__ == '__main__':
    dddd_row.show()
    dddd_row.servable()

from collections import deque

import holoviews as hv
import numpy as np
import panel as pn

from nmrtools.qm import spectrum
from utils import lineshape_from_peaklist


def abx(va=110.0, vb=90.0, vx=200.0, Jax=5.0, Jbx=10.0, Jab=13.0):
    # a quirk of this old nmrtools library is that freqs must be an np array and not just a list of lists;
    # this seems to be fixed in the new nmrsim library 
    freqs = np.array([va, vb, vx])
    Js = np.array(
        [[0.0, Jab, Jax],
         [Jab, 0.0, Jbx],
         [Jax, Jbx, 0]])
    peaklist = spectrum(freqs, Js)
    x, y = lineshape_from_peaklist(peaklist)
    return hv.Curve(zip(x, y))


abx_app = pn.interact(abx,
                      va=(0.0, 300.0, 0.1, 110.0),
                      vb=(0.0, 300.0, 0.1, 90.0),
                      vx=(0.0, 300.0, 0.1, 200.0),
                      Jax=(0.0, 20.0, 0.1, 5.0),
                      Jbx=(0.0, 20.0, 0.1, 10.0),
                      Jab=(0.0, 20.0, 0.1, 13.0), )

abx_text_1 = pn.pane.Markdown('''
This is a very common spin system. 
For example, if two diastereotopic protons are coupled to a third proton, 
this pattern can result. 

- If you slide the &nu;<sub>b</sub> slider down to 50 Hz, 
  the AB portion is tweezed apart into two doublet of doublets "leaning" toward each other. 
  Such a system could safely be analyzed as a set of 3 dd, 
  one for each A, B, and X signal.
''')
abx_text_2 = pn.pane.Markdown('''
- Change vb back to 90 Hz. 
  Here, the chemical shift difference between H<sub>A</sub> and H<sub>B</sub> is less than twice *J*<sub>AB</sub>, 
  and if it were analyzed as a first-order pattern you would start to see small discrepancies. 
''')
abx_text_3 = pn.pane.Markdown('''
- Change &nu;<sub>b</sub> to 102 Hz. 
  To accurately determine the chemical shifts and coupling constants from this signal, 
  a more elaborate calculation is required. 
  If you are interested in the details, 
  this type of calculation is described in detail 
  [here](https://www.chem.wisc.edu/areas/reich/nmr/05-hmr-12-abx.htm). 
''')
abx_text_4 = pn.pane.Markdown('''
- Change &nu;<sub>b</sub> to 106.5 Hz. 
  At this point, one of the two AB quartets has collapsed to a singlet, 
  and the AB part of the ABX spectrum reduces to 5 peaks total, 
  with two being very small. 
  This could easily be mistaken for a singlet and a doublet.

- Take a close look at the X part of the spectrum 
  (the leftmost signal centered at 200 Hz). 
  It often will resemble a doublet of doublets, but there are two smaller peaks towards the outside that could easily be lost in the baseline noise. 
''')
backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward)

test_text = [abx_text_1, abx_text_2, abx_text_3, abx_text_4]
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

abx_row = pn.Row(abx_app, text_column)


if __name__ == '__main__':
    abx_row.show()
    abx_row.servable()

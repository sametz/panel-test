from collections import deque

import holoviews as hv
import panel as pn

from nmrtools.firstorder import first_order
from utils import lineshape_from_peaklist


def ddd(J1, J2, J3, w):
    singlet = (100, 1)  # center at 100 Hz; intensity 1
    couplings = [(J1, 1), (J2, 1), (J3, 1)]
    peaklist = first_order(singlet, couplings)
    x, y = lineshape_from_peaklist(peaklist, w=w, limits=(75, 125))
    return hv.Curve(zip(x, y)).options(axiswise=True)

ddd_app = pn.interact(ddd, 
                      J1=(0.0, 20.0, 0.1, 4.0),
                      J2=(0.0, 20.0, 0.1, 10.0),
                      J3=(0.0, 20.0, 0.1, 12.0),
                      w=(0.1, 10.0, 0.1, 0.5))

ddd_text_1 = pn.pane.Markdown('''
### Three couplings: doublet of doublet of doublets (ddd)
The plot should initialize as a ddd, *J* = 12, 10, 4 Hz.
This is a simple ddd pattern, with no coincedental overlap of peaks,
so we see 8 peaks of equal intensity. 
8 is 2<sup>3</sup>, so there are three couplings.

If you can measure the distances between peaks 
(e.g. if you have peak frequencies in Hz), 
you can start solving such a signal by realizing:
- the distance between the first two peaks is the smallest coupling constant (here, *J*<sub>1</sub>)
- every peak will be half of a doublet with a splitting of *J*<sub>1</sub>
- if the effect of this splitting is removed, 
  the signal will reduce in complexity (here, to a dd)
- repeat the process until all coupling constants are determined
''', width_policy='max')

ddd_text_2 = pn.pane.Markdown('''
This is often shown graphically with a "tree diagram", as shown below.

![Image](img/ddd2.png)

<img src='img/ddd2.png'>

If you had a spectrum with peak picking in Hz, 
then *J*<sub>1</sub> would be the difference in frequency between the first and second peaks, 
*J*<sub>2</sub> the distance between the first and third, 
and *J*<sub>3</sub> the distance between the first and fourth. 
**This will not always be the case**. 
However, the distance between the first two (or last two) peaks will always be a true coupling constant 
(in a first-order multiplet).
''', width_policy='max')

ddd_text_3 = pn.pane.Markdown('''
Coincidental overlap can reduce the number of peaks in the ddd pattern.

* Adjust the sliders so that *J*<sub>1</sub> and *J*<sub>2</sub> = 10 Hz, 
  and *J*<sub>3</sub> = 4 Hz. 
  The resulting pattern is a triplet of doublets, 
  and would be reported as "td, *J* = 10.0, 4.0 Hz". 
  Note that the coupling constants are listed in order from largest to smallest, 
  and so the multiplicities are listed as "td" and not "dt". 
  The ratio of the peak intensities is 1:1:2:2:1:1, which adds up to 8.
''', width_policy='max')

ddd_text_4 = pn.pane.Markdown('''
* Adjust the *J*<sub>2</sub> slider to 4 Hz. 
  The resulting signal is a doublet of triplets, 
  with peak intensities in the ratio of 1:2:1:1:2:1. 
  This would be reported as "dt, *J* = 10.0, 4.0 Hz". 
  Note the importance of listing the multiplicities in the correct order 
  (td vs dt) to properly describe the appearance of the signal.
''', width_policy='max')

ddd_text_5 = pn.pane.Markdown('''
* Adjust the *J*<sub>1</sub> slider to 8 Hz. 
  There is now coincidental overlap of two of the peaks 
  (the inner two peaks of relative intensity 1 are now a single peak with a relative intensity of 2). 
  This would still be considered a doublet of triplets. 
  Note how it almost looks like an "*n* + 1" pentet, 
  but the intensities are wrong 
  (1:2:2:2:1 for the dt, vs. 1:4:6:4:1 for a pentet).
''', width_policy='max')

backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward,
                 align='center')

ddd_text = [ddd_text_1, ddd_text_2, ddd_text_3, ddd_text_4, ddd_text_5]
deque_text = deque(ddd_text)
text_column = pn.Column(back_fwd, deque_text[0], width_policy='max')


def next_text(event):
    deque_text.rotate(-1)
    text_column[1] = deque_text[0]


def prev_text(event):
    deque_text.rotate()
    text_column[1] = deque_text[0]


backward.on_click(prev_text)
forward.on_click(next_text)

ddd_row = pn.Row(ddd_app, text_column, width_policy='max')


if __name__ == '__main__':
    ddd_row.show()
    ddd_row.servable()

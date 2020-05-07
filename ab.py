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

ab_text_1 = pn.pane.Markdown('''
- In the interactive plot, 
  note that when &nu;<sub>1</sub> (v1) = 150 Hz 
  (an arbitrary chemical shift in Hz, not ppm) 
  and &nu;<sub>2</sub> (v2) = 50 Hz, 
  the pattern resembles two doublets. 
  The chemical shift difference (100 Hz) is much larger than the coupling (10 Hz), 
  and the distortion is minimal -- 
  there is only slight leaning of the signals toward each other, 
  and the midpoints of the "doublets" are very close to 150 and 50 Hz.
''')
ab_text_2 = pn.pane.Markdown('''
- Now, change &nu;<sub>1</sub> to 110 Hz and &nu;<sub>2</sub> to 90 Hz. 
  The leaning is more pronounced, 
  and could be mistaken for a first-order quartet. 
  Such AB signals are commonly referred to as "AB quartets". 
  If you select the "zoom" tool and zoom in on the AB quartet, 
  you can see that the midpoint of each doublet is now far off from 110 Hz / 90 Hz. 
  The "true" chemical shifts (110 and 90 Hz) are much closer to the larger, inner peak 
  than the smaller, outer peak. 
''')
ab_text_3 = pn.pane.Markdown('''
- If you set &nu;<sub>1</sub> = 105 Hz and &nu;<sub>2</sub> = 87.8 Hz, 
  the AB quartet will look exactly like a regular quartet 
  that integrates for 2 protons. 
  It would be easy to jump to the conclusion that this is the CH<sub>2</sub> of an ethyl group... 
  but there would be no corresponding methyl triplet around 1 ppm.
''')
ab_text_4 = pn.pane.Markdown('''
- Change &nu;<sub>1</sub> to 102 Hz and &nu;<sub>2</sub> to 98 Hz. 
  The outer peaks are very small and could easily be missed 
  if the baseline was noisy or if other signals were nearby. 
  The two inner peaks are starting to collapse together. 
  This could easily be misidentified as a ~2 proton doublet, 
  since the outer peaks don't contribute much to the total area. 
  The small distance between the two inner peaks could be misinterpreted as a small *J* coupling.
''')

backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward)

test_text = [ab_text_1, ab_text_2, ab_text_3, ab_text_4]
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

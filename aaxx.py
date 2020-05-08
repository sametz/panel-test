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


# TODO: arguments below do not seem to override aaxx defaults?! Fix this.
aaxx_app = pn.interact(aaxx,
                       va=(0.0, 300.0, 0.1, 140.0),
                       vx=(0.0, 300.0, 0.1, 160.0),
                       Jaa=(0.0, 20.0, 0.1, 5.0),
                       Jxx=(0.0, 20.0, 0.1, 10.0),
                       Jax=(0.0, 20.0, 0.1, 13.0),
                       Jax_prime=(0.0, 20.0, 0.1, 13.0))

aaxx_text_1 = pn.pane.Markdown('''
This is a very common second-order pattern, but it can often look like a simpler first-order pattern and be analyzed as such.  

In *para*-disubstituted benzenes, at low resolution, the pattern can look like a pair of doublets. Higher resolution and closer inspection reveals extra peaks around the base of each doublet. However, it is often interpreted as a doublet whose splitting is *J<sub>AX</sub>*, and this is close enough for structural analysis.

The interactive plot shown here is for another common case, for two coupled methylene groups X-CH<sub>2</sub>-CH<sub>2</sub>-Y. By the "n + 1" rule, this should give rise to a pair of triplets. However, in acyclic systems, this is often not the case.
''')
aaxx_text_2 = pn.pane.Markdown('''
- If the two methylene signals are close together in chemical shift,
  significant distortions appear. 
  The plot should initialize as a "messtet" of two signals at 140 Hz and 160 Hz. 
  Slide &nu;<sub>a</sub> lower and/or &nu;<sub>x</sub> higher. 
  As separation increases, the signals start to resemble a pair of triplets. 
  Keep going until &nu;<sub>a</sub> is 15 Hz and &nu;<sub>x</sub> is 200 Hz.
''')
aaxx_text_3 = pn.pane.Markdown('''
When there is no strong conformational preference for *anti-* over *gauche-* conformers 
(rotating about the C-C bond), 
you will often see this first-order behavior of two triplets. 
The *J*<sub>AX</sub> and *J*<sub>AX'</sub> values of 5.5 
are a weighted average of the coupling constants seen in the rapidly-interconverting *anti-* and *gauche-* conformers 
of equal population (33 1/3 % of each). 
''')
aaxx_text_4 = pn.pane.Markdown('''
- Continuing with the interactive plot above, 
  change Jax to 3.2 Hz and Jax_prime to 10.1 Hz. 
  This simulates a system that has an 80% preference for the anti-conformation. 
  The signal has changed appearance, 
  with the outermost peaks being larger than the inner peaks. 
  This is a very common situation that suggests a second-order effect is in play--
  a normal "*n*+1" multiplet has the smallest peaks on the outside, 
  and gets larger towards the middle. 
''')
backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward)

test_text = [aaxx_text_1, aaxx_text_2, aaxx_text_3, aaxx_text_4]
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

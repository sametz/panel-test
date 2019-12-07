from collections import deque

import holoviews as hv
import panel as pn

from nmrtools.firstorder import first_order
from utils import lineshape_from_peaklist

# pn.extension()
# hv.extension('bokeh', width=100)


def dd(J1, J2, w):
    singlet = (100, 1)  # center at 100 Hz; intensity 1
    couplings = [(J1, 1), (J2, 1)]
    peaklist = first_order(singlet, couplings)
    x, y = lineshape_from_peaklist(peaklist, w=w, limits=(85, 115))
    return hv.Curve(zip(x, y)).options(axiswise=True)


dd_app = pn.interact(dd, J1=(0.0, 20.0, 0.1, 3.0), J2=(0.0, 20.0, 0.1, 7.0), w=(0.1, 10.0, 0.1, 0.5))

dd_text_1 = pn.pane.Markdown('''
####<p style="text-align: center;">1</p>
The plot should initialize as a dd for 1 H, with J<sub>1</sub> = 3 Hz and J<sub>2</sub> = 7 Hz.
In these simulated examples, the height of each peak (0.25) happens to be proportional to the area
(CAUTION: this is often not true in real spectra because line widths can differ).
The relative intensities are 0.25 : 0.25 : 0.25 : 0.25, or 1 : 1 : 1 : 1.

* Drag both *J* sliders to 0.
You should see the signal collapse to a singlet at 100 Hz.
If the x axis started at 0 Hz for TMS, 
and the spectrometer were a 100 MHz spectrometer, 
this would correspond to a chemical shift of 1 ppm.
Note the height of the signal (an approximation of its total area) is now 1.
In the absence of any splitting, this proton will only resonate at this one frequency,
and its integration would be normalized as 1 H.
''', width_policy='max')

dd_text_2 = pn.pane.Markdown('''
####<p style="text-align: center;">2</p>
* Now, drag the J<sub>2</sub> slider back to 7 Hz.
A doublet with a 7-Hz splitting results.
Each peak is half intensity, and would integrate to 0.5 H.
This means that half of the nuclei are resonating 3.5 Hz lower than 100 Hz, and half 3.5 Hz higher.
The signal is centrosymmetric about 100 Hz.
''', width_policy='max')

dd_text_3 = pn.pane.Markdown('''
####<p style="text-align: center;">3</p>
* Drag the J<sub>1</sub> slider to about 0.5 Hz.
Each peak in the previous doublet has started to split into doublets themselves.
When the size of the splitting is small compared to the peak width
(set to 0.5 Hz, and controlled by the "w" slider),
you won't see complete separation of the peaks.
In a real spectrum, if the signal-to-noise ratio is small enough,
it can be difficult to determine if this is a "real" splitting or not.

''', width_policy='max')

dd_text_4 = pn.pane.Markdown('''
####<p style="text-align: center;">4</p>
* Drag the J<sub>1</sub> slider back to 3 Hz.
The signals are now well separated, and the dd pattern is clear.
When analyzing such first-order multiplets,
start by measuring the distance between the first two peaks (or the last two),
and the distance between the first and third peaks (or the last and third-last).
These distances, in Hz, will be two coupling constants.
In the dd case, this completes the analysis--
the two splittings can be measured as 3 and 7 Hz, 
and the center of the signal (in ppm) would be the chemical shift. 

In the chemical literature, coupling constants are listed in order from largest to smallest,
and the corresponding splitting 
(d for doublet, t, for triplet, q for quartet etc. ) follow the same order.
This signal would be reported (if this were a 100-MHz spectrometer) as: 
"&delta; 1.00 (1H, dd, *J* = 7.0, 3.0 Hz)".

''', width_policy='max')

dd_text_5 = pn.pane.Markdown('''
####<p style="text-align: center;">5</p>
* Drag the J<sub>1</sub> slider to 7 Hz.
Now that both coupling constants are the same, 
the inner two peaks overlap to form a double-intensity signal,
and the 1 : 2 : 1 triplet pattern results.
The patterns that result from the *n* + 1 rule (doublets, quartets, quintets) are the special cases that result
when coupling constants are the same size. 
''', width_policy='max')

dd_text_6 = pn.pane.Markdown('''
####<p style="text-align: center;">6</p>
Note that a proton may have two different neighbors (protons that are not related by symmetry or exchanged by rotation)
that coincidentally have the same *J* value, or very similar.
Sometimes spectra taken on more powerful spectrometers can appear more complicated,
because these small differences are revealed. 

* Drag the J<sub>1</sub> slider slightly back, to 6.5 Hz.
The triplet has started to break up. On a spectrometer with poorer resolution, this may still look like a triplet,
or like a "squashed triplet" with the middle peak being a bit shorter and broader.

* Slide the "w" setting up to 1.00 Hz to simulate this effect.

''', width_policy='max')

backward = pn.widgets.Button(name='\u25c0', width=50)
forward = pn.widgets.Button(name='\u25b6', width=50)
back_fwd = pn.Row(backward, forward,
                 align='center')

dd_text = [dd_text_1, dd_text_2, dd_text_3, dd_text_4, dd_text_5,                  dd_text_6]
deque_text = deque(dd_text)
text_column = pn.Column(back_fwd, deque_text[0], width_policy='max')


def next_text(event):
    deque_text.rotate(-1)
    text_column[1] = deque_text[0]


def prev_text(event):
    deque_text.rotate()
    text_column[1] = deque_text[0]


backward.on_click(prev_text)
forward.on_click(next_text)

dd_row = pn.Row(dd_app, text_column, width_policy='max')


if __name__ == '__main__':
    dd_row.show()
    dd_row.servable()

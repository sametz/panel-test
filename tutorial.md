#### Exercise: doublet of doublets

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

* Now, drag the J<sub>2</sub> slider back to 7 Hz.
A doublet with a 7-Hz splitting results.
Each peak is half intensity, and would integrate to 0.5 H.
This means that half of the nuclei are resonating 3.5 Hz lower than 100 Hz, and half 3.5 Hz higher.
The signal is centrosymmetric about 100 Hz.

* Drag the J<sub>1</sub> slider to about 0.5 Hz.
Each peak in the previous doublet has started to split into doublets themselves.
When the size of the splitting is small compared to the peak width
(set to 0.5 Hz, and controlled by the "w" slider),
you won't see complete separation of the peaks.
In a real spectrum, if the signal-to-noise ratio is small enough, 
it can be difficult to determine if this is a "real" splitting or not.

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

* Drag the J<sub>1</sub> slider to 7 Hz.
Now that both coupling constants are the same, 
the inner two peaks overlap to form a double-intensity signal,
and the 1 : 2 : 1 triplet pattern results.
The patterns that result from the *n* + 1 rule (doublets, quartets, quintets) are the special cases that result
when coupling constants are the same size. 

Note that a proton may have two different neighbors (protons that are not related by symmetry or exchanged by rotation)
that coincidentally have the same *J* value, or very similar.
Sometimes spectra taken on more powerful spectrometers can appear more complicated, 
because these small differences are revealed. 

* Drag the J<sub>1</sub> slider slightly back, to 6.5 Hz.
The triplet has started to break up. 
On a spectrometer with poorer resolution, this may still look like a triplet,
or like a "squashed triplet" with the middle peak being a bit shorter and broader.

* Slide the "w" setting up to 1.00 Hz to simulate this effect.

### Three couplings: doublet of doublet of doublets (ddd)
The plot below is an example of a ddd pattern with no coincedental overlap. There are 8 peaks of equal intensity. 8 is $2^3$, so there are three couplings.

If you could measure the distances in Hz between peaks, how would you go about analyzing such a signal? You can start "untangling the knot" by realizing:
- the distance between the first two peaks is the smallest coupling constant (here, $J_1$)
- every peak will be half of a doublet with a splitting of $J_1$
- if the effect of this splitting is removed, the signal will reduce in complexity (here, to a dd)
- repeat the process until all coupling constants are determined

This is often shown graphically with a "tree diagram", as shown below.

![Image](img/ddd2.png)

If you had a spectrum with peak picking in Hz, then $J_1$ would be the difference in frequency between the first and second peaks, $J_2$ the distance between the first and third, and $J_3$ the distance between the first and fourth. **This will not always be the case**. However, the distance between the first two (or last two) peaks will always be a true coupling constant (in a first-order multiplet).

You can graphically simulate this thought process by manipulating the plot below. First, change J1 to 0 Hz to remove the smallest doublet splitting and simplify the multiplet to a dd. Then, change J2 to 0 to simplify to a d, and finally change J3 to 0 to collapse the signal all the way to a singlet.

Coincidental overlap can reduce the number of peaks in the ddd pattern.

Adjust the sliders in the above simulation so that J1 and J2 = 10 Hz, and J3 = 4 Hz. The resulting pattern is a triplet of doublets, and would be reported as "td, *J* = 10.0, 4.0 Hz". Note that the coupling constants are listed in order from largest to smallest, and so the multiplicities are listed as "td" and not "dt". The ratio of the peak intensities is 1:1:2:2:1:1, which adds up to 8.

Adjust the J2 slider to 4 Hz. The resulting signal is a doublet of triplets, with peak intensities in the ratio of 1:2:1:1:2:1. This would be reported as "dt, *J* = 10.0, 4.0 Hz". Note the importance of listing the multiplicities in the correct order (td vs dt) to properly describe the appearance of the signal.

Adjust the J1 slider to 8 Hz. There is now coincidental overlap of two of the peaks (the inner two peaks of relative intensity 1 are now a single peak with a relative intensity of 2). This would still be considered a doublet of triplets. Note how it almost looks like an "*n* + 1" pentet, but the intensities are wrong (1:2:2:2:1 for the dt, vs. 1:4:6:4:1 for a pentet).

# AB

This is a common pattern. For example, an isolated methylene group in a chiral molecule (i.e. where the two protons are diastereotopic) can display this pattern.

When $J >> \Delta \nu$ (the chemical shift difference in Hz, not ppm), the pattern resembles two doublets. As the chemical shift difference becomes smaller, distortions appear. First, the inner peaks of this 4-peak signal grow larger as the outer peaks grow smaller. {In general, protons that are coupled show a "leaning towards each other) effect like this that increases as the chemical shift difference decreases.} Second, the chemical shift of each proton is not exactly in the middle of the doublet, and as the two signals approach each other in chemical shift this difference becomes more pronounced.

- In the interactive plot below, note that when $\nu_1$ (v1) = 150 Hz (an arbitrary chemical shift in Hz, not ppm) and $\nu_2$ (v2) = 50 Hz, the pattern resembles two doublets. The chemical shift difference (100 Hz) is much larger than the coupling (10 Hz), and the distortion is minimal--slight leaning of the signals toward each other, and the midpoints of the "doublets" being very close to 150 and 50 Hz.

- Now, change v1 to 110 Hz and v2 to 90 Hz. The leaning is more pronounced, and could be mistaken for a first-order quartet. Such AB signals are commonly referred to as "AB quartets". Above and to the right of the plot is a toolbar. If you select the "zoom" tool and zoom in on the AB quartet, you can see that the midpoint of each doublet is now far off from 110 Hz / 90 Hz. The "true" chemical shifts (110 and 90 Hz) are much closer to the larger, inner peak than the smaller, outer peak. This means that, to calculate the exact chemical shift of each signal, a more sophisticated calculation is required (see: __[this page](https://www.chem.wisc.edu/areas/reich/nmr/05-hmr-10-ax-ab.htm)__ under "5-HMR-10.4 Solving an AB pattern" if you're interested).

- If you set v1 = 105 Hz and v2 = 87.8 Hz, the AB quartet will look exactly like a regular quartet that integrates for 2 protons. It would be easy to jump to the conclusion that this is the CH<sub>2</sub> of an ethyl group... but there would be no corresponding methyl triplet around 1 ppm.

- Change v1 to 102 Hz and v2 to 98 Hz. The outer peaks are very small and could easily be missed if the baseline was noisy or if other signals were nearby. The two inner peaks are starting to collapse together. This could easily be misidentified as a ~2 proton doublet, since the outer peaks don't contribute much to the total area. The small distance between the two inner peaks could be misinterpreted as a small *J* coupling.

One way to reveal an AB quartet is to take the spectrum on two different spectrometers with very different frequencies. 

- From the previous example, change v1 to 104 Hz and v2 to 96 Hz. This simulates doubling the spectrometer frequency (e.g. from 300 MHz to 600 MHz). The signal has a more obvious "AB quartet look", and the gap between the two inner peaks has increased (and thus is not a second-order doublet, since *J* values are constant).

## ABX

This is a very common pattern. For example, if two diastereotopic protons are coupled to a third proton, this pattern can result. One common substructure that exhibits an ABX pattern is a methylene group next to a methine stereocenter (below, left). Many amino acids have this structural feature (below, right).

![Image](img/ABX.png)

The interactive plot below shows a typical ABX pattern. 

- If you slide the vb slider down to 50 Hz, the AB portion is tweezed apart into two doublet of doublets "leaning" toward each other. Such a system could safely be analyzed as a set of 3 dd, one for each A, B, and X signal.

- Change vb back to 90 Hz. Here, the chemical shift difference between $H_A$ and $H_B$ is less than twice $J_{AB}$, and if it were analyzed as a first-order pattern you would start to see small discrepancies. 

- Change vb to 102 Hz. To accurately determine the chemical shifts and coupling constants from this signal, a more elaborate calculation is required. If you are interested in the details, this type of calculation is described in detail here://link . At this point, the AB signal more strongly resembles two sets of overlapping AB quartets. The first, third, fourth, and seventh peaks from left to right (the two smallest and the two largest peaks) are one AB quartet, the second, 5th, 6th, and 8th are the other. Solving these patterns involves identifying the two pairs of AB quartets and solving them first.

- Change vb to 106.5 Hz. At this point, one of the two AB quartets has collapsed to a singlet, and the AB part of the ABX spectrum reduces to 5 peaks total, with two being very small. This could easily be mistaken for a singlet and a doublet.

- Take a close look at the X part of the spectrum (the leftmost signal centered at 200 Hz). It often will resemble a doublet of doublets, but there are two smaller peaks towards the outside that could easily be lost in the baseline noise. 

## AA'XX'

This is a very common second-order pattern. We'll look at two of the more common situations in which this can arise.

In *para*-disubstituted benzenes, at low resolution, a pair of doublets is seen, and it is commonly analyzed as such. At higher resolution, the appearance of the signals becomes more complex. Usually, each signal looks like a doublet with a small AB quartet superimposed on it:

In acyclic systems, an X-CH<sub>2</sub>-CH<sub>2</sub>-Y unit does not necessarily appear as a pair of triplets.

- If the two methylene signals are close together in chemical shift, significant distortions appear. The interactive plot below should load as a "messtet" of two signals at 140 Hz and 160 Hz. Slide va lower and/or vx higher. As separation increases, the signals start to resemble a pair of triplets. Keep going until va is 15 Hz and vx is 200 Hz.

When there is no strong conformational preference for anti over gauche conformers (rotating about the C-C bond), you will often see this first-order behavior of two triplets. The $J_{AX}$ and $J_{AX'}$ values of 5.5 are a weighted average of the coupling constants seen in the rapidly-interconverting anti- and gauche- conformers of equal population (33 1/3 % of each). As a bias towards anti- or towards gauche- conformations increases, the signals deviate from a triplet appearance. 

- Continuing with the interactive plot above, change Jax to 3.2 Hz and Jax_prime to 10.1 Hz. This simulates a system that has an 80% preference for the anti-conformation. The signal has changed appearance, with the outermost peaks being larger than the inner peaks. This is a very common situation that suggests a second-order effect is in play--a normal n+1 multiplet has the smallest peaks on the outside, and gets larger towards the middle. Sometimes such second-order signals are called "Batman" signals because of their superficial resemblance to Batman's silhouette:

<img src='img/batman.png' style='width: 300px;'>
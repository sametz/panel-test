import numpy as np

from nmrtools.plt import add_signals


def lineshape_from_peaklist(peaklist, w=1, points=800, limits=None):
    """

    Parameters
    ----------
    peaklist : [(float, float)...]
        A list of (frequency, intensity) tuples
    w : float
        Peak width at half height (Hz)
    points : int
        The number of data points in the lineshape
    limits : (float, float)
        The frequency (left/right) limits for the lineshape

    Returns
    -------
    ([float...], [float...])
        The lists of x coordinates (frequency) and corresponding y coordinates (intensity) for the lineshape.
    """
    peaklist.sort()
    if limits:
        try:
            l_limit, r_limit = limits
            l_limit = float(l_limit)
            r_limit = float(r_limit)
        except Exception as e:
            print(e)
            print('limits must be a tuple of two numbers')
            raise
        if l_limit > r_limit:
            l_limit, r_limit = r_limit, l_limit
    else:
        l_limit = peaklist[0][0] - 50
        r_limit = peaklist[-1][0] + 50
    x = np.linspace(l_limit, r_limit, points)
    y = add_signals(x, peaklist, w)
    return x, y
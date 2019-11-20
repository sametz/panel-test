import holoviews as hv
import panel as pn

from nmrtools.dnmr import dnmr_AB


def abplot(va, vb, J, k, w):
    x, y = dnmr_AB(va, vb, J, k, w)
    return hv.Curve(zip(x, y))


dnmr_ab_app = pn.interact(abplot, va=165, vb=135, J=12, k=(0.001, 1000, 0.1, 12), w=(0.1, 10, 0.1, 0.5))
dnmr_ab_text = pn.pane.Markdown('''DNMR AB text goes here.''')
dnmr_ab_row = pn.Row(dnmr_ab_app, dnmr_ab_text)


if __name__ == '__main__':
    dnmr_ab_row.show()
    dnmr_ab_row.servable()

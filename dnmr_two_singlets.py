import holoviews as hv
import panel as pn

from nmrtools.dnmr import dnmr_two_singlets


def dnmr_two_singlets_plot(va, vb, k, wa, wb, p):
    x, y = dnmr_two_singlets(va, vb, k, wa, wb, p)
    return hv.Curve(zip(x, y))


dnmr_two_singlets_app = pn.interact(dnmr_two_singlets_plot,
                                    va=165, vb=135,
                                    k=(0.001, 1000, 0.1, 1.5),
                                    wa=(0.1, 10, 0.1, 0.5),
                                    wb=(0.1, 10, 0.1, 0.5),
                                    p=0.5)
dnmr_two_singlets_text = pn.pane.Markdown('''DNMR Two Singlets text goes here.''')
dnmr_two_singlets_row = pn.Row(dnmr_two_singlets_app, dnmr_two_singlets_text)


if __name__ == '__main__':
    dnmr_two_singlets_row.show()
    dnmr_two_singlets_row.servable()

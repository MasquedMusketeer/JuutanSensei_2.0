import os

def linkBank():
    comp = os.path.join(os.path.dirname(__file__), "compFolder.lnk")
    caixa = os.path.join(os.path.dirname(__file__), 'caixaComp.lnk')
    dem = os.path.join(os.path.dirname(__file__), 'demComp.lnk')
    log = os.path.join(os.path.dirname(__file__), 'logComp.lnk')
    NoFi = os.path.join(os.path.dirname(__file__), 'NFComp.lnk')
    vale = os.path.join(os.path.dirname(__file__), 'valeComp.lnk')
    return comp, caixa, dem, log, NoFi, vale
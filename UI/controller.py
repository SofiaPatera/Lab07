import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_musei(self):
        lista_musei = self._model.get_musei()
        for musei in lista_musei:
            self.view._dd_museo.options.append(ft.dropdown.Options(musei.nome))

        self.view.update()

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO

import flet as ft
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view, model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_musei(self):
        lista_musei = self._model.get_musei()
        self._view._dd_museo.options.clear()
        for musei in lista_musei:
            self._view._dd_museo.options.append(ft.dropdown.Option(musei.nome))
        self._view.update()

    def popola_epoca(self):
        lista_epoca = self._model.get_epoche()
        self._view._dd_epoca.options.clear()
        for epoche in lista_epoca:
            self._view._dd_epoca.options.append(ft.dropdown.Option(epoche))
        self._view.update()


    # CALLBACKS DROPDOWN
    def on_change_musei(self, e):
        self.museo_selezionato = e.control.value

    def on_change_epoca(self, e):
        self.epoca_selezionata = e.control.value

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self,e):
        lista_artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        self._view.lista_artefatti.controls.clear()
        if not lista_artefatti:
            self._view.lista_artefatti.controls.append(ft.Text("Nessun artefatto trovato"))
        else:
            for a in lista_artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(a))
        self._view.update()




import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler

    def mostra_strumenti(self, e):
        lista = self._model.get_strumenti()
        if not lista:
            self._view.update()
            self._view.show_alert("❌ Non sono presenti strumenti nel database!.")
            return

        self._view.lista_strumenti.controls.clear()
        for strumento in lista:
            self._view.lista_strumenti.controls.append(ft.Text(f"Codice: {strumento['codice']} - Tipo: {strumento['tipo']} - Marca: {strumento['marca']} - Anno Acquisto: {strumento['anno_acquisto']} - Valore: {strumento['valore']}€"))
        self._view.update()

    def cerca_strumenti_per_tipo(self,e):
        tipo = self._view.input_tipo_strumento.value
        listaTipo = self._model.cerca_strumenti_per_tipo(tipo)
        self._view.lista_strumenti_ricerca.controls.clear()
        if not listaTipo:
            self._view.update()
            self._view.show_alert("❌ Strumento non presente nel database!")
            return

        for strumento in listaTipo:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"Codice: {strumento['codice']} - Tipo: {strumento['tipo']} - Marca: {strumento['marca']} - Anno Acquisto: {strumento['anno_acquisto']} - Valore: {strumento['valore']}€"))
        self._view.update()


from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def reset(self,e):
        self._model.reset()
        self._view._txtOutT.value=self._model.T
        self._view._lv.controls.clear() # SVUOTIAMO I CONTROLS DELLA LISTVIEW
        self._view._btnPlay.disabled=False
        self._view._txtIn.disabled = False
        self._view._lv.controls.append(ft.Text("Indovina a quale numero sto pensando!"))

        self._view.update()

    def play(self,e):
        tentativoStr=self._view._txtIn.value

        self._view._txtIn.value="" # RIPULIAMO IL TEXTFIELD OGNI VOLTA
        self._view._txtOutT.value=self._model.T-1

        if tentativoStr=="":
            self._view._lv.controls.append(ft.Text("Attenzione! Inserisci un valore numerico da testare",color="red"))
            self._view.update()
            return

        try:
            tentativoInt=int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Attenzione! Il valore inserito non è un intero", color="red"))
            self._view._txtIn.value = ""
            self._view.update()
            return

        if tentativoInt < 0 or tentativoInt > self._model.NMax:
            self._view._lv.controls.append(
                ft.Text("Attenzione! Inserisci un valore numerico compreso tra 0 e il numero massimo", color="red"))
            self._view.update()
            return

        res = self._model.play(tentativoInt)

        if res == 0:  # HO VINTO
            self._view._lv.controls.append(
                ft.Text(f"Fantastico, hai vinto! Il tentativo segreto era {tentativoInt}", color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == 2:  # HO PERSO
            self._view._lv.controls.append(
                ft.Text(f"Disastro, hai finito le vite! Il tentativo segreto era {self._model.segreto}"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == -1:  # IL SEGRETO E' + PICCOLO
            self._view._lv.controls.append(
                ft.Text(f"Il segreto è più piccolo di {tentativoInt}"))
            self._view.update()
        else:  # IL SEGRETO E' + GRANDE
            self._view._lv.controls.append(
                ft.Text(f"Il segreto è più grande di {tentativoInt}"))
            self._view.update()


    def getNMax(self):
        return self._model.NMax #RIACHIAMANO LE FUNZIONI PER RIMANERE + PRIVATE E NON LAVORARE DIRETTAMENTE SULLE VARIABII

    def getTMax(self):
        return self._model.TMax
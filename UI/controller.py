import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result.clean()
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(self._model.stampa()))
        self._view.btn_countedges.disabled = False
        self._view.update_page()
        pass

    def handle_countedges(self, e):
        self._view.txt_result2.clean()
        try:
            float(self._view.txt_name.value)
        except ValueError:
            self._view.create_alert("Inserisci soglia numerica")
            self._view.update_page()
        min = self._model.min()
        max = self._model.max()
        soglia = float(self._view.txt_name.value)
        if soglia < min or soglia > max:
            self._view.create_alert("Soglia non compresa")
            self._view.update_page()
        (nmag,nmin) = self._model.contaArchi(soglia)
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi maggiore: {nmag}"))
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi minore: {nmin}"))
        self._view.update_page()
        pass

    def handle_search(self, e):
        pass

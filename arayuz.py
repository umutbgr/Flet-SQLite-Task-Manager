import flet as ft

class UygulamaArayuzu:
    def __init__(self):
        self.yeni_gorev_alani = ft.TextField(
            hint_text = "Yeni bir görev ekle...",
            expand=True
        )
        self.ekle_butonu = ft.FloatingActionButton(
            icon = ft.Icons.ADD
        )
        self.gorevler_sutunu = ft.Column()

        self.ust_kisim = ft.Row(
            controls =[
                self.yeni_gorev_alani,
                self.ekle_butonu
            ]
        )

        self.ana_kisim = ft.Column(
            controls=[
                self.ust_kisim,
                ft.Divider(),# yatay çizgi ekler
                self.gorevler_sutunu# görevlerin listeleneceği sütun
            ]
        )
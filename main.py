import veri as db
import flet as ft
from arayuz import UygulamaArayuzu

def main(page: ft.Page):
    page.title = "To-Do Uygulaması"
    page.window_width = 450 
    page.window_height = 600 

    db.veritabani()

    arayuz = UygulamaArayuzu()

    def gorevleri_arayuzunde_goster():
        arayuz.gorevler_sutunu.controls.clear()
        tum_gorevler = db.gorevleri_getir()
        for gorev_id, metin, tamamlandi in tum_gorevler:
            arayuz.gorevler_sutunu.controls.append(
                ft.Row(
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Checkbox(
                            label = metin,
                            value = bool(tamamlandi),
                            data = gorev_id,
                            on_change = durumu_degistir
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            data = gorev_id,
                            on_click=gorevi_sil
                        )
                    ]
                )
            )
        page.update()

    def ekle_butonu_tiklandi(e):
        db.gorev_ekle(arayuz.yeni_gorev_alani.value)
        arayuz.yeni_gorev_alani.value = ""
        gorevleri_arayuzunde_goster()

    def durumu_degistir(e):
        db.gorevi_guncelle(e.control.data, e.control.value)
        gorevleri_arayuzunde_goster()

    def gorevi_sil(e):
        gorev_id = e.control.data

        db.gorevi_sil(gorev_id)
        gorevleri_arayuzunde_goster()
        
    arayuz.ekle_butonu.on_click = ekle_butonu_tiklandi
    arayuz.yeni_gorev_alani.on_submit = ekle_butonu_tiklandi# Enter ile ekle

    page.add(arayuz.ana_kisim)

    gorevleri_arayuzunde_goster()
    
ft.app(target=main)


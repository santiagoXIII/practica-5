import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor="purple"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("tu IMc es:")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    btnCalcular=ft.ElevatedButton("Calcular")
    btnLimpiar=ft.ElevatedButton("limpiar")
    
    page.add(
        ft.Column(
            controls=[
                txtPeso,
                txtAltura,
                lblIMC
                ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,
                btnLimpiar
            ],alignment="CENTER"
        )
        )

ft.app(target = main,view = ft.AppView.WEB_BROWSER)

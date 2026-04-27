import flet as ft

def main(page: ft.Page):
    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    counter = ft.Text(value="0", size=40)

    def increment(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    page.add(
        ft.Column([
            counter,
            ft.ElevatedButton("Increment", on_click=increment)
        ], alignment="center", horizontal_alignment="center")
    )

ft.run(main)

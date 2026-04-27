import flet as ft

def build_image_view(page: ft.Page, config: dict):
    async def go_back(e):
        await page.push_route("/")

    return ft.View(
        route="/image",
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip="返回", on_click=go_back),
                    ft.Text("图片生成", size=28, weight=ft.FontWeight.BOLD, expand=True),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(f"URL: {config.get('url', '')}", selectable=True),
                        ft.Text(f"Model: {config.get('model', '')}", selectable=True),
                        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                        ft.Text("在这里添加图片生成逻辑...", italic=True, color=ft.colors.GREY_400),
                    ],
                    spacing=10,
                ),
                padding=20,
            ),
            ft.Container(expand=True),
        ],
    )
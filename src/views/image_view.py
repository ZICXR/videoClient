import flet as ft
import base64
import os

def build_image_view(page: ft.Page, config: dict):
    async def go_back(e):
        await page.push_route("/")
    
    # 提示词输入框
    prompt_input = ft.TextField(
        label="提示词",
        hint_text="生成一张图片...",
        width=900,
    )
    # 大加号上传区域
    plus_icon = ft.Icon(
        ft.Icons.ADD_ROUNDED,
        size=444,
        color=ft.Colors.GREY_400,
    )
    def test(e):
        print("tijiao")
        pass
    submit_btn = ft.ElevatedButton(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.SEND, size=30),     # 改这里
                ft.Text("提交", size=20, weight=ft.FontWeight.BOLD),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16), padding=40),
        expand=True,
        height=200,
        on_click=test,
    )
    # ========== 组装视图 ==========
    return ft.View(
        route="/image",
        controls=[
            ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, tooltip="返回", on_click=go_back),
                    ft.Text("图片生成", size=28, weight=ft.FontWeight.BOLD, expand=True),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(),
            ft.Container(
                expand=True,
                content=ft.Column(
                    [
                        ft.Text(f"URL: {config.get('url', '')}", selectable=True),
                        ft.Text(f"Model: {config.get('model', '')}", selectable=True),
                        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                        plus_icon,
                        prompt_input,
                        submit_btn
                    ],
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                    
                ),
                padding=20,
            ),
            
            ft.Container(expand=True),
        ],
    )
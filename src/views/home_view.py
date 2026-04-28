import flet as ft
from src.services.api import get_models
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

def build_home_view(page: ft.Page, config: dict):
    url_input = ft.TextField(
        label="API URL",
        hint_text="",
        width=500,
        prefix_icon=ft.Icons.LINK,          # 改这里
        value=config.get("url", ""),
    )
    key_input = ft.TextField(
        label="API Key",
        password=True,
        can_reveal_password=True,
        width=500,
        prefix_icon=ft.Icons.KEY,          # 改这里
        value=config.get("key", ""),
    )

    model_dropdown = ft.Dropdown(
        label="Model",
        width=440,
        hint_text="点击右侧刷新获取模型列表",
        value=config.get("model"),
    )

    if config.get("models"):
        model_dropdown.options = [ft.dropdown.Option(m) for m in config["models"]]
        model_dropdown.disabled = False
    else:
        model_dropdown.disabled = True

    def fetch_models(e):
        if not url_input.value or not key_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("请先填写 URL 和 Key"))
            page.snack_bar.open = True
            page.update()
            return

        if not HAS_REQUESTS:
            models = ["gpt-4o", "gpt-4o-mini", "claude-3-5-sonnet", "dall-e-3"]
            config["models"] = models
            model_dropdown.options = [ft.dropdown.Option(m) for m in models]
            model_dropdown.disabled = False
            if not model_dropdown.value:
                model_dropdown.value = models[0]
            page.update()
            return

        try:
            models = get_models(key_input.value, url_input.value)
            models = [m for m in models if m]
            config["models"] = models
            model_dropdown.options = [ft.dropdown.Option(m) for m in models]
            model_dropdown.disabled = False
            if models and not model_dropdown.value:
                model_dropdown.value = models[0]
            page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"获取失败: {ex}"))
            page.snack_bar.open = True
            page.update()

    refresh_btn = ft.IconButton(
        icon=ft.Icons.REFRESH,               # 改这里
        tooltip="获取模型列表",
        on_click=fetch_models,
        icon_size=28,
    )

    def save_config():
        config["url"] = url_input.value
        config["key"] = key_input.value
        config["model"] = model_dropdown.value

    async def go_image(e):
        save_config()
        await page.push_route("/image")

    async def go_video(e):
        save_config()
        await page.push_route("/video")

    img_btn = ft.ElevatedButton(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.IMAGE, size=60),        # 改这里
                ft.Text("图片生成", size=24, weight=ft.FontWeight.BOLD),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16), padding=40),
        expand=True,
        height=220,
        on_click=go_image,
    )

    vid_btn = ft.ElevatedButton(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.VIDEOCAM, size=60),     # 改这里
                ft.Text("视频生成", size=24, weight=ft.FontWeight.BOLD),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16), padding=40),
        expand=True,
        height=220,
        on_click=go_video,
    )

    return ft.View(
        route="/",
        controls=[
            ft.Text("AI 生成工具", size=36, weight=ft.FontWeight.BOLD),
            ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
            url_input,
            key_input,
            ft.Row([model_dropdown, refresh_btn], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(height=50, color=ft.Colors.TRANSPARENT),
            ft.Row([img_btn, vid_btn], expand=True, spacing=20),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
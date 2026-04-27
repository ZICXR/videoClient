import flet as ft

from src.views.home_view import build_home_view
from src.views.image_view import build_image_view
from src.views.video_view import build_video_view


config = {"url": "", "key": "", "model": "", "models": []}

def main(page: ft.Page):
    page.title = "AI 生成工具"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 40

    # 0.80+ route_change 不接收参数
    def route_change():
        page.views.clear()
        if page.route == "/":
            page.views.append(build_home_view(page, config))
        elif page.route == "/image":
            page.views.append(build_image_view(page, config))
        elif page.route == "/video":
            page.views.append(build_video_view(page, config))
        page.update()

    # 0.80+ view_pop 接收 e 参数，且是 async
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # 关键：直接调用，不要 page.go("/")
    route_change()

if __name__ == "__main__":
    ft.run(main)
from datetime import datetime
import flet as ft
from flet_timer.flet_timer import Timer
from flet_core.types import MainAxisAlignment
def main(page: ft.Page):
    page.window_width=375
    page.window_height=700
    page.title = "Stopwatch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    txt_time = ft.Text(value="00:00:00")
    start_time = None
    def refresh():
        nonlocal start_time
        if start_time is not None:
            elapsed = datetime.now() - start_time
            txt_time.value = str(elapsed).split('.')[0]  # Format as HH:MM:SS
            page.update()
    timer = Timer(name="timer", interval_s=1, callback=refresh)
    def start():
        nonlocal start_time
        start_time = datetime.now()
        timer.start()
    def stop():
        nonlocal start_time
        timer.stop()
        start_time = None
    btn_start = ft.TextButton(text="Start", on_click=lambda c: start())
    btn_stop = ft.TextButton(text="Stop", on_click=lambda c: stop())
    row=ft.Row(controls=[timer, txt_time, btn_start, btn_stop],alignment=MainAxisAlignment.SPACE_EVENLY)
    # page.add(timer, txt_time, btn_start, btn_stop)
    page.add(row)
ft.app(main)
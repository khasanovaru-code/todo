import flet as ft

def main(page: ft.Page):
    # 1. Создаем аудио (используем твой файл shot.mp3)
    audio1 = ft.Audio(src="shot.mp3") 
    
    # 2. Добавляем в overlay
    page.overlay.append(audio1) 
    
    # 3. Элементы интерфейса
    page.add(
        ft.Text("Мое приложение"),
        ft.ElevatedButton("Играть звук", on_click=lambda _: audio1.play())
    )

ft.app(target=main)
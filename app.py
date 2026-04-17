import flet as ft
from flet_audio import Audio
import asyncio
from game import Game
from ui import UI

class RouletteApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.game = Game()
        self.ui = UI()
        
        self.audio = Audio(src="shot.mp3")
        self.page.overlay.append(self.audio)
        
        self.ui.shoot_btn.on_click = self.shoot
        self.ui.reset_btn.on_click = self.restart
        self.page.add(*self.ui.build())
        self.page.update()
    
    async def animate_drum(self):
        frames = ["gun.png", "safe.png", "boom.png"]
        for _ in range(3):
            for frame in frames:
                self.ui.drum.src = frame
                self.page.update()
                await asyncio.sleep(0.1)
    
    async def shoot(self, e):
        if not self.game.alive: return
        
        await self.animate_drum()
        
        self.audio.play()
        result = self.game.shot()
        
        if result == "boom":
            self.ui.drum.src = "boom.png"
            self.ui.status.value = "Не повезло!"
        else:
            self.ui.drum.src = "safe.png"
            self.ui.status.value = "Повезло!"
        self.page.update()

    def restart(self, e):
        self.game.reset()
        self.ui.drum.src = "gun.png"
        self.ui.status.value = "Нажми выстрел"
        self.page.update()
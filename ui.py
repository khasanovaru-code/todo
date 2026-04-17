import flet as ft

class UI:
    def __init__(self):
        self.title = ft.Text("Русская рулетка", size=26, weight="bold")
        self.status = ft.Text("Нажми выстрел", size=20)
        self.round = ft.Text("Раунд: 1")
        self.drum = ft.Image(src="gun.png", width=150, height=150)

        self.shoot_btn = ft.ElevatedButton("Выстрел")
        self.reset_btn = ft.ElevatedButton("Перезарядка")
    
    def build(self):
        return [self.title, self.drum, self.status, self.round, self.shoot_btn, self.reset_btn]
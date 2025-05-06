# archivo: main.py

from kivymd.app import MDApp
from screens.dashboard import DashboardScreen

class CondominioApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return DashboardScreen()

CondominioApp().run()

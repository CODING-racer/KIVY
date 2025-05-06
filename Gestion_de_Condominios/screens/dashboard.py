# archivo: screens/dashboard.py

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import os

class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kv_path = os.path.join(os.path.dirname(__file__), '..', 'kv', 'dashboard.kv')
        Builder.load_file(kv_path)

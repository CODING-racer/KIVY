from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton

class DemoApp(MDApp): 
    def build(self):
        screen = Screen()
        btn_flat = MDFlatButton(text='Hola Mundo', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        return screen

# Esta línea DEBE estar fuera de la clase
DemoApp().run()

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton


class DemoApp(MDApp): 

    def build(self):
        screen = Screen()
        btn_flat = MDFlatButton(text='Hola Mundo')
        screen.add_widget(btn_flat)
        return screen
    

    DemoApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Cambiar el color de fondo de la ventana (rojo)
Window.clearcolor = (1, 0, 0, 1)  # RGBA: rojo, sin verde, sin azul, opaco

class MyWidget(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.clearcolor = 0, 1, 1, 1,

class FirstPage(Screen):
    my_text = StringProperty("Details Here")
    
    def on_press_button(self):
        self.my_text = "Registration Succesfully"

class SecondPage(Screen):
    pass

class HomePage(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class TutorialApp(App):
    def build(self):
        return kv
    
kv = Builder.load_file("Tutorial.kv")

if __name__ == "__main__":
    TutorialApp().run()    
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class DemoApp(MDApp): 
    def build(self):
        label = MDLabel(text='Hola Mundo',halign='center',theme_text_color='Error')
        
        icon_label = MDIcon(icon='language-python',halign='center')
        return icon_label
    

DemoApp().run()


#Secondary
#Error
#green (0,1,0,1)
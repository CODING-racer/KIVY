from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class DemoApp(MDApp): 
    def build(self):
        label = MDLabel(text='Hola Mundo',halign='center',theme_text_color='Custom',
                        text_color=(236 / 255.0, 98 / 255.0, 81 / 255.0, 1),
                        font_style='Caption')
                        #font_style='H2')
        icon_label = MDIcon(icon='lan',halign='center')                
        return icon_label
    

DemoApp().run()

#Secondary
#Error
#green (0,1,0,1)


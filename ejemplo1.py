from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''
MDScreen:

    MDBottomNavigation:
        panel_color: 0.93, 0.93, 0.93, 1 

        MDBottomNavigationItem:
            name: 'home'
            text: 'Inicio'
            icon: 'home'

            MDLabel:
                text: 'Bienvenido al condominio'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'pagos'
            text: 'Pagos'
            icon: 'credit-card'

            MDLabel:
                text: 'Historial de Pagos'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'reportes'
            text: 'Reportes'
            icon: 'alert-circle'

            MDRaisedButton:
                text: 'Nuevo Reporte'
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        MDBottomNavigationItem:
            name: 'avisos'
            text: 'Avisos'
            icon: 'bell'

            MDLabel:
                text: 'No hay avisos nuevos'
                halign: 'center'
'''

class CondominioApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

CondominioApp().run()

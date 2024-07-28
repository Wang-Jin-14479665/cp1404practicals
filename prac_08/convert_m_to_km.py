from kivy.app import App
from kivy.lang import Builder

__author__ = 'Wang Jin'
MILES_TO_KM = 1.60934

class MileToKm(App):

    def build(self):
        self.title = 'Mile to KM'
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

MileToKm().run()
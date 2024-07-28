from kivy.app import App
from kivy.lang import Builder

__author__ = 'Wang Jin'
MILES_TO_KM = 1.60934

class MileToKm(App):

    def build(self):
        self.title = 'Mile to KM'
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert miles to kilometers calculator"""
        value = float(self.root.ids.input_miles.text)
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Update input data when click the up/down button"""
        value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

MileToKm().run()
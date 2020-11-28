from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.config import Config

Config.set('graphics','width','450')
Config.set('graphics','height','400')

class CalGridlayout(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error!"

class CalculatorApp(App):
    def build(self):
        return CalGridlayout()

if __name__ == "__main__":
    CalculatorApp().run()

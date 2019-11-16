from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class CoinTossBoxLayout(BoxLayout):
    def choice(self,guess):
        output="You clicked the "+guess+" button!"
        self.ids.result.text=output



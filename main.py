from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random


class CoinTossBoxLayout(BoxLayout):
    def choice(self, guess):
        output = guess
        if self.ids.result.text == "":  # if the result box is empty, then print the result. If there is already a result, do nothing.
            self.ids.result.text = output

    def get_random(self):
        random_list = ['Right!', 'Nope, try again!', 'Impeach Trump!']
        random_choice = random.choice(random_list)
        self.ids.result.text = random_choice

    def clear(self):
        self.ids.result.text = "" # erases the results so user can guess again


class CoinTossApp(App):
    def build(self):
        return CoinTossBoxLayout()

if __name__ == "__main__":
    CoinTossApp().run()

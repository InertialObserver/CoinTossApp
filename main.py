from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CoinTossBoxLayout(BoxLayout):
    def choice(self, guess):
        output = guess
        self.ids.result.text = output

    def clear(self):
        self.ids.result.text = ""


class CoinTossApp(App):
    def build(self):
        return CoinTossBoxLayout()

if __name__ == "__main__":
    CoinTossApp().run()

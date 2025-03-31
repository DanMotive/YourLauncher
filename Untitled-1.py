from kivy.app import App
from kivy.uix.textinput import TextInput

class YourLauncherApp(App):
    def build(self):
        self.text_input = TextInput(text='Введи текст', multiline=False)
        return self.text_input

if __name__ == "__main__":
    YourLauncherApp().run()
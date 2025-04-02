from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import subprocess

class YourLauncherApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Приветствуем в build1")
        button = Button(text="Нажми меня")
        button.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        subprocess.Popen(["notepad.exe"])
        
if __name__ == "__main__":
    YourLauncherApp().run()
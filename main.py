from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import subprocess

class YourLauncherApp(App):
    def build(self):
        layout = BoxLayout()
        button = Button(text='Hello',size_hint=(0.5, 0.5),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.label = Label(text="Приветствуем в build1")
        button = Button(text="Нажми меня")
        button.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(button)
        icon_with_label = IconWithLabel(icon_path='256 (1).jpg', text='My App')
        return layout
    
    def on_button_press(self, instance):
        subprocess.Popen(["notepad.exe"])

class IconWithLabel(BoxLayout):
    def __init__(self, icon_path, text, **kwargs):
        super(IconWithLabel, self).__init__(orientation='vertical', **kwargs)
        self.icon = Image(source=icon_path)
        self.label = Label(text=text, halign='center')
        self.add_widget(self.icon)
        self.add_widget(self.label)
        
if __name__ == "__main__":
    YourLauncherApp().run()
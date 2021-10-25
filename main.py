from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class SettingsScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name
        # screen_manager = self.root.ids

MainApp().run()
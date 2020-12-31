import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass


class WabilApp(MDApp):
    def built(self):
        return MainScreen()

if __name__ == '__main__':
    app = WabilApp()
    app.run()

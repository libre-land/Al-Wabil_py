from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window


Window.size = (414, 736)


class StartScreen(Screen):
    def next_screen_buttton(self):
        self.manager.current = 'main_screen'


class Tab(FloatLayout, MDTabsBase):
    pass


class MainScreen(Screen):
    pass


class WabilApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start_screen'))
        sm.add_widget(MainScreen(name='main_screen'))

        return sm


if __name__ == '__main__':
    app = WabilApp()
    app.run()

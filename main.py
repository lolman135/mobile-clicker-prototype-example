from kivy.app import App
from screens.menu import *
from screens.active_screens.user_screens import *
from kivy.core.window import Window

Window.size = (450, 900)


class MediumApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Game(name="game"))
        sm.add_widget(Settings(name="settings"))
        return sm


if __name__ == '__main__':
    app = MediumApp()
    app.run()
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class AbstractScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding="20dp", spacing="20dp")
        self.add_widget(self.layout)

    def add_back_button(self):
        btn_back = Button(text="Back to Menu", size_hint=(1, 0.2), font_size="20sp")
        btn_back.bind(on_press=self.go_menu)
        self.layout.add_widget(btn_back)

    def go_menu(self, *args):
        self.manager.transition.direction = "right"
        self.manager.current = "menu"


class Game(AbstractScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        lbl_game = Label(text="Game Screen", font_size="40sp")
        self.layout.add_widget(lbl_game)
        self.add_back_button()


class Settings(AbstractScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        lbl_settings = Label(text="Settings", font_size="40sp")
        self.layout.add_widget(lbl_settings)

        self.add_back_button()
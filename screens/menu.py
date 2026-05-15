from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding="20dp", spacing="20dp")

        img_title = Image(source="assets/images/title.png", size_hint=(1, 0.5))
        layout.add_widget(img_title)

        lbl_title = Label(text="Main Menu", font_size="40sp", size_hint=(1, 0.2))
        layout.add_widget(lbl_title)

        btn_play = Button(text="PLAY", size_hint=(1, 0.15), font_size="20sp")
        btn_play.bind(on_press=self.go_game)
        layout.add_widget(btn_play)

        btn_settings = Button(text="SETTINGS", size_hint=(1, 0.15), font_size="20sp")
        btn_settings.bind(on_press=self.go_settings)
        layout.add_widget(btn_settings)

        btn_exit = Button(text="EXIT", size_hint=(1, 0.15), font_size="20sp")
        btn_exit.bind(on_press=self.exit_app)
        layout.add_widget(btn_exit)

        self.add_widget(layout)

    def go_game(self, *args):
        self.manager.current = "game"

    def go_settings(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "settings"

    def exit_app(self, *args):
        app.stop()
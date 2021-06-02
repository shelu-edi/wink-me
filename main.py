# from kivy.config import Config
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.pagelayout import PageLayout

# Config.set('graphics', 'width', '414')
# Config.set('graphics', 'height', '736')
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout


class HomePage(Screen):
    # initial = NumericProperty(0)

    def on_pre_enter(self):
        Window.size = (414, 736)

    def on_touch_move(self, touch):
        if touch.dx > 0:
            sm.transition.direction = 'right'
            sm.current = 'create'
        elif touch.dx < 0:
            sm.transition.direction = 'left'
            sm.current = 'login'
        elif touch.dy > 0:
            sm.transition.direction = "up"
            sm.current = "main"
        elif touch.dy < 0:
            sm.transition.direction = "down"
            sm.current = "myacc"


class LoginWindow(Screen):
    def on_pre_enter(self):
        Window.size = (414, 736)

    def on_touch_move(self, touch):
        if touch.dx > 0:
            sm.transition.direction = 'right'
            sm.current = 'home'


class CreateAccWindow(Screen):
    def on_pre_enter(self):
        Window.size = (414, 736)

    def on_touch_move(self, touch):
        if touch.dx < 0:
            sm.transition.direction = 'left'
            sm.current = 'home'


class MainWindow(Screen):
    def on_touch_move(self, touch):
        if touch.dy < 0:
            sm.transition.direction = "down"
            sm.current = "home"


class MyAccount(Screen):
    def on_touch_move(self, touch):
        if touch.dy > 0:
            sm.transition.direction = "up"
            sm.current = "home"


class WindowManager(ScreenManager):
    pass


def update_window_size(width, height):
    Window.size = (width, height)


kv = Builder.load_file("winkme.kv")
sm = WindowManager()

screens = [HomePage(name="home"), LoginWindow(name="login"), CreateAccWindow(name="create"), MainWindow(name="main"),
           MyAccount(name="myacc")]

for screen in screens:
    sm.add_widget(screen)


class WinkMeApp(App):
    def build(self):
        self.icon = "images/wm.jpg"
        return sm


WinkMeApp().run()


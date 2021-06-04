# from kivy.config import Config
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout
# Config.set('graphics', 'width', '414')
# Config.set('graphics', 'height', '736')
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


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
            # sm.transition.direction = "down"
            # sm.current = "home"
            pass

    def topdiscoutnsBtn(self):
        sm.current = 'topdiscounts'

    def Slide_btn(self):
        sm.current = "scrollview1"


class ItemWindow(Screen):
    vans_shoes1 = ObjectProperty()

    def promo_code_1(self):
        promo_code(self.vans_shoes1.text)
        print("Promo Code Item 1 Pop")


class MyAccount(Screen):
    def on_touch_move(self, touch):
        if touch.dy > 0:
            sm.transition.direction = "up"
            sm.current = "home"

    def EditDataBtn(self):
        sm.current = "editmyaccount"


class EditMyAccount(Screen):
    def spinner_clicked(self, value):
        self.ids.spinner_id.text = value

    def save_data_btn(self):
        sm.current = "myacc"


class TopDiscounts(Screen):
    pass


class ScrollView1(Screen):
    pass


class WindowManager(ScreenManager):
    pass


def promo_code(promo):
    pop = Popup(title=f"Promo Code", content=Label(text=f"Promo Code is:{promo} "), size_hint=(.6, .3),
                background="atlas://data/images/defaulttheme/button_pressed")
    pop.open()


def update_window_size(width, height):
    Window.size = (width, height)


kv = Builder.load_file("winkme.kv")
sm = WindowManager()

screens = [HomePage(name="home"), LoginWindow(name="login"), CreateAccWindow(name="create"), MainWindow(name="main"),
           MyAccount(name="myacc"), TopDiscounts(name="topdiscounts"), EditMyAccount(name="editmyaccount"),
           ItemWindow(name="itemwindow"), ScrollView1(name="scrollview1")]

for screen in screens:
    sm.add_widget(screen)


class WinkMeApp(App):
    def build(self):
        self.icon = "images/wm.jpg"
        return sm


WinkMeApp().run()


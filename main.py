from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


class Cuisine(Screen):
    pass


class CalCount(Screen):
    pass


class UserInfo(Screen):
    pass


class UserChoice(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CalorieCountApp(App):
    pass


CalorieCountApp().run()

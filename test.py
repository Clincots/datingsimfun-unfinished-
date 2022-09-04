import time
import asyncio
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition
from kivy.clock import Clock
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Builder.load_file("test.kv")


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class CandLApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="fourth"))
        return sm

    def text_wait(self, text, idforbutton, screennumber):

        anything = getattr(self.root.get_screen(screennumber).ids, idforbutton)
        anything.text = ""
        for i in text:
            anything.text += i
            print(anything.text)
            #Clock.schedule_once(self.dosmth, 1)

    def testingsidk(self, dt):
        print("cheese")

    def fullscreen(self):
        Window.fullscreen = True


    def notfullscreen(self):
        Window.fullscreen = False

if __name__ == "__main__":
    CandLApp().run()

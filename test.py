from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window


Window.fullscreen = True
Builder.load_file("test.kv")

test123 = ""

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass


class CandLApp(App):
    global test123
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="fourth"))
        return sm
    def text_wait(self, text):
        for i in text:
            print(self.ids.buttonfortext.text)
            time.sleep(1)





if __name__ == "__main__":
    CandLApp().run()
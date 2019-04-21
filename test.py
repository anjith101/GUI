import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.popup import Popup 
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.image import Image
from kivy.base  import  runTouchApp
from kivy.garden.knob import  Knob
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.properties import StringProperty
# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

ADAFRUIT_IO_KEY = '9de3934474334c6a895bd9ce1994148c'
ADAFRUIT_IO_USERNAME = 'anjith101'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
response = aio.feeds('menu')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("main.kv")
# Declare both screens
class MyPopup(Popup):
    dish = ''

class StarterMenu(Screen):
    pass

class MainMenu(Screen):
	pass

class DrinksMenu(Screen):
    pass

class DesertMenu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(StarterMenu(name='starter'))
sm.add_widget(MainMenu(name='main'))
sm.add_widget(DrinksMenu(name='drinks'))
sm.add_widget(DesertMenu(name='desert'))

# Create the screen manager

class TestApp(App):

    dish ='Table1'
    quantity = 0
    def call(self, instance):

        self.dish ='Table1__'
        self.dish = self.dish + instance.text

    def callback(self, instance):

        self.quantity = "{}".format(int(instance.parent.name.value))
        aio.send_data('menu', self.dish + "__" + str(self.quantity))

    def build(self):

        return sm

if __name__ =="__main__":
    Window.fullscreen = 'auto'
    TestApp().run()
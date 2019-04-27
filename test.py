#on raspberry pi kivy uses egl_rpi as window module by default but it crashes due to graphics problem

import os
os.environ['KIVY_WINDOW'] = 'sdl2'

#hedder files
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
#from kivy.base  import  runTouchApp
from kivy.garden.knob import  Knob
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.properties import StringProperty
# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

ADAFRUIT_IO_KEY = '9de3934474334c6a895bd9ce1994148c' #iot key
ADAFRUIT_IO_USERNAME = 'anjith101' #iot username

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY) #created an object in order to get access to adfruit
response = aio.feeds('menu') #feed name menu

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file("main.kv") #load file 'main.kv' to create app
# Declare both screens


#each class reprecent each screen inside the brackets are inheritance of class pass meanse do nothing 
class MyPopup(Popup):
    pass
    
class StarterMenu(Screen):
    pass

class MainMenu(Screen):
	pass

class DrinksMenu(Screen):
    pass

class DesertMenu(Screen):
    pass

sm = ScreenManager() #screen manager object 
#evary class given a name 
sm.add_widget(StarterMenu(name='starter'))
sm.add_widget(MainMenu(name='main'))
sm.add_widget(DrinksMenu(name='drinks'))
sm.add_widget(DesertMenu(name='desert'))

# Create the screen manager

#app class we can access all classes content from here
class TestApp(App):

    dish ='' #variable named dish
    quantity = 0 #variable named quantity
    #call methord
    def call(self, instance):

        self.dish ='Table1__' #table_ string to variable dish
        self.dish = self.dish + instance.text #dish variable = string in dish +instance wich called the methords text

    #callback methord
    def callback(self, instance):

        self.quantity = "{}".format(int(instance.parent.name.value)) #quantity variable = instance wich called the methords parents content 'name's value
        aio.send_data('menu', self.dish + "__" + str(self.quantity)) #sent 2 variable dish and quantity to menu feed
    
    def build(self):

        return sm

if __name__ =="__main__":
    Window.fullscreen = 'auto'
    TestApp().run()

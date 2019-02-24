from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.popup import Popup 
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("main.kv")

# Declare both screens
class  MyPopup(Popup):
	pass
	
class StarterMenu(Screen):
    pass

class MainMenu(Screen):
	pass

class MycartMenu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(StarterMenu(name='starter'))
sm.add_widget(MycartMenu(name='mycart'))
sm.add_widget(MainMenu(name='mainmenu'))

# Create the screen manager

class TestApp(App):

    def build(self):
        return sm
if __name__ =="__main__":

    TestApp().run()
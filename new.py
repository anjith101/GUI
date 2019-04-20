#!/usr/bin/kivy
import kivy
kivy.require('1.7.2')

from random import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from random import random
from random import choice
from kivy.properties import StringProperty
import time

score=0

my_popup = Popup(title='Test popup',
    content=Label(text=str(score)),
    size_hint=(None, None))


Builder.load_string("""
<Highest>:
    GridLayout:
        cols: 1
        Button:
            id: btn_0
            text: "0"
            on_press: root.new()
        Label:
""")

class Highest(Screen):
    def new(self):
        global score
        score=score+1
        self.ids['btn_0'].text = str(score)
        my_popup.open()


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Highest(name='Highest'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

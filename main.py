from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.button import Button
from functools import partial
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from time import sleep
import threading
import brain
from math import sqrt
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget

homework = {}

class ReadBox(BoxLayout):
    """
    This class demonstrates various techniques that can be used for binding to
    events. Although parts could me made more optimal, advanced Python concepts
    are avoided for the sake of readability and clarity.
    """


    def __init__(self, **kwargs):
        super(ReadBox, self).__init__(**kwargs)
        self.addhomework = TextInput(hint_text = "Add stuff here", multiline = False)
        self.updatedatebaseButton = Button(text = "updatedatabase")
        self.updatedatebaseButton.bind(on_press = self.updatedatabase)
        self.add_widget(self.addhomework)
        self.add_widget(self.updatedatebaseButton)

    def updatedatabase(self, obj):
        text = self.addhomework.text
        global homework
        homework[text] = 5
        print(homework)

class DemoApp(App):

    def build(self):
        self.title = "Brain Team!"
        y = ReadBox()
        return y



if __name__ == "__main__":
    DemoApp().run()

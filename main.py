from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

def MyGridLayout(Widget):

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(Label(text='Aloha, meu friend'))

        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''



class MyApp(App):
    def build(self):
        return MyGridLayout()



if __name__ == '__main__':
    MyApp().run()
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    count = 0

    def build(self):
        self.btn  = Button(text='Hello World')
        self.btn.bind(on_press=self.increment)
        return self.btn
    
    def increment(self,app):
        self.btn.text = f'Hello : {self.count}'
        self.count = self.count + 1

    


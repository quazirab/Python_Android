from kivy.app import App
from kivy.uix.button import Button
from app.external_func import func1

class TestApp(App):
    # count = 0

    def build(self):
        self.btn  = Button(text='Hello World')
        self.btn.bind(on_press=self.increment)
        return self.btn
    
    def increment(self,app):
        self.btn.text = f'Hello : {func1()}'
        # self.count = self.count + 1

    


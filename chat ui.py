from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import Label as CoreLabel


class ChatWindow(Widget):
    def btn_left(self,flayout,text_input):
        if text_input.text!="":
            str2=text_input.text
            float=FloatLayout()
            float.pos_hint={'x':0,'y':0}
            my_label=CoreLabel()

            my_label.text=str2
            my_label.refresh()
            newsize=my_label.size
            mybtn=Button(text=str2,size_hint_y=None,size_hint_x=None,size=(newsize[0]+10,newsize[1]+10),
                         pos_hint={'x':0,'y':0})

            mybtn.font_size=12
            mybtn.font_name='Arial'
            mybtn.border=0,0,0,0
            mybtn.background_normal='gr.png'
            float.add_widget(mybtn)
            flayout.add_widget(float)
            text_input.text=""


    def btn_right(self,flayout,text_input):
        if text_input.text != "":
            str2 = text_input.text
            float = FloatLayout()
            float.pos_hint = {'x': 1, 'y': 0}
            my_label = CoreLabel()

            my_label.text = str2
            my_label.refresh()
            newsize = my_label.size
            mybtn = Button(text=str2, size_hint_y=None,size_hint_x=None, size=(newsize[0] + 10, newsize[1] + 10),
                           pos_hint={'right': 1, 'y': 0})

            mybtn.font_size = 12
            mybtn.font_name = 'Arial'
            mybtn.border = 0, 0, 0, 0
            mybtn.background_normal = 'br.png'
            float.add_widget(mybtn)
            flayout.add_widget(float)
            text_input.text = ""





class ChatApp(App):
    def build(self):
        return ChatWindow()


ChatApp().run()
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel


class RoboApp(MDApp):
    def build(self):
        screen = Screen()
        conn_label = MDLabel(text="Waiting for connection.....",
                             halign="center")
        button_on = MDRectangleFlatButton(text="LED ON",
                                          pos_hint={"center_x": 0.4, "center_y": 0.5},
                                          on_release=self.on)
        button_off = MDRectangleFlatButton(text="LED OFF",
                                           pos_hint={"center_x": 0.6, "center_y": 0.5},
                                           on_release=self.off)
        screen.add_widget(button_on)
        screen.add_widget(button_off)
        screen.add_widget(conn_label)
        return screen

    def on(self, obj):
        print("Led ON")

    def off(self, obj):
        print("Led OFF")


RoboApp().run()

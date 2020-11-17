from kivymd.app import MDApp
from kivy.core.window import Window
import socket
from kivy.uix.screenmanager import Screen
from kivy.properties import *


class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    IP = StringProperty()
    compname = StringProperty()

    def on_start(self):
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        self.IP = IP
        self.compname = hostname
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + IP)

    def __init__(self):
        Window.size = (400,600)
        super().__init__()


MainApp().run()
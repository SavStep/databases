from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button

#окно
Window.size = (250, 500)
Window.clearcolor = (0/255, 69/255,126/255  )
Window = "What to Whatch"

# экран добавления фильма
class Addscreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        logo = Image(source="films.py/logo.png",
                    pos_hint={"center_y":0.85, "center_x":0.5},
                    size_hint=[0.98,.5])

        self.add_widget(logo)


#класс экран меню
class ScreenMain(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        logo = Image(source="films.py/logo.png",
                    pos_hint={"center_y":0.85, "center_x":0.5},
                    size_hint=[0.98,.5])
        button_film = Button(text="Сгенерировать фильм",
                             pos_hint={"center_y":0.58, "center_x":0.5},
                             size_hint=[0.9, 0.2],
                             background_color = (0/255, 69/255,126/255  ),
                             color = (128/255, 100/255,145/255  ))
        button_add = Button(text="Добавить фильм",
                             pos_hint={"center_y":0.35, "center_x":0.5},
                             size_hint=[0.9, 0.2],
                             background_color = (0/255, 69/255,126/255  ),
                             color = (128/255, 100/255,145/255  ))
        button_delete = Button(text="Удалить фильм",
                             pos_hint={"center_y":0.12, "center_x":0.5},
                             size_hint=[0.9, 0.2],
                             background_color = (0/255, 69/255,126/255  ),
                             color = (128/255, 100/255,145/255  ))
        self.add_widget(logo)
        self.add_widget(button_film)
        self.add_widget(button_add)
        self.add_widget(button_delete)
        
        
        
        
#приложение
class FilmApp(App):
    def build(self):
        sm = ScreenManager()#менеджер по экрану
        sm.add_widget(ScreenMain(name = "Main_screen"))
        sm.add_widget(Addscreen(name = "add_screen"))
        return sm
FilmApp().run()

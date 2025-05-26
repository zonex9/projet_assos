from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Chargement du fichier KV
Builder.load_file("interface.kv")

# Définition des écrans
class AssociationScreen(Screen):
    pass

class ProfilScreen(Screen):
    pass

class MaterielsScreen(Screen):
    pass

class PanierScreen(Screen):
    pass

class WishlistScreen(Screen):
    pass

class RootWidget(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MyApp().run()

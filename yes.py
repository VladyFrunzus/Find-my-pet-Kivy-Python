from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from postdatabase import PostDataBase


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    location = ObjectProperty(None)
    telephone = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.password.text != "" and self.location.text != "" and self.telephone.text != "":
            db.add_user(self.email.text, self.password.text, self.namee.text,self.location.text,self.telephone.text)

            self.reset()

            sm.current = "login"
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.password.text = ""
        self.namee.text = ""
        self.location.text = ""
        self.telephone.text = ""
        self.email.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created,location,telephone = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

    def remove(self):
        db.rmv_user(self.email.text[7:])
        sm.current = "login"

    # def delete(self):
    #     self.remove_widget(self.ids.remo


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


class PostWindow(Screen):
    pet_name = ObjectProperty(None)
    location = ObjectProperty(None)
    color = ObjectProperty(None)
    type = ObjectProperty(None)
    breed = ObjectProperty(None)
    has_collar = ObjectProperty(None)


    def submit(self):
        if self.pet_name.text != "" and self.location.text != "" and self.color.text != "" and self.type.text != "" and self.breed.text != "" :
            pdb.add_post(self.pet_name.text, self.location.text, self.color.text, self.type.text, self.breed.text, self.has_collar.text)

            self.reset()

            sm.current = "main"
        else:
            invalidForm()

    def reset(self):
        self.pet_name.text = ""
        self.location.text = ""
        self.color.text = ""
        self.type.text = ""
        self.breed.text = ""
        self.has_collar.text = ""

class FeedWindow(Screen):
    pass

kv = Builder.load_file("my.kv")
kv2 = Builder.load_file("my2.kv")

sm = WindowManager()
db = DataBase("users.txt")
pdb = PostDataBase("post.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),PostWindow(name="post"),FeedWindow(name="feed")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
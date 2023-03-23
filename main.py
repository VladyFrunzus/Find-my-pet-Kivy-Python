from presentation.user_interface import UI
from infrastructure.repository import OwnerRepo_with_Files,HeroRepo_with_Files,PostRepo_with_Files
from business.services import OwnerServices,HeroServices,PostServices
from validation.validation import Owner_Validator,Hero_Validator
from login import Login,Register
from yes import MyMainApp
def main():
    owner_repo = OwnerRepo_with_Files("owner.txt")
    hero_repo = HeroRepo_with_Files("hero.txt")
    post_repo = PostRepo_with_Files("post.txt")

    owner_validator = Owner_Validator()
    hero_validator = Hero_Validator()

    owner_srv = OwnerServices(owner_repo,owner_validator)
    hero_srv = HeroServices(hero_repo,hero_validator)
    post_srv = PostServices(post_repo,owner_repo)

    #reg = Register("login_info.txt",owner_srv,hero_srv)
    #reg.register("Vlady","1234","SugPula123","Mama lui Fane","112")


    #ui = UI(owner_srv,hero_srv,post_srv)
    #ui.run()


if __name__ == '__main__':
    main()
    MyMainApp().run()


import datetime


class PostDataBase:
    def __init__(self, filename):
        self.filename = filename
        self.posts = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.posts = {}
        for line in self.file:
            pet_name, location, color, type, breed, has_collar,time = line.strip().split(";")
            self.posts[id] = (pet_name,location,color,type,breed,has_collar)

        self.file.close()

    def get_user(self, id):
        if id in self.posts:
            return self.posts[id]
        else:
            return -1

    def add_post(self, pet_name,location,color,type,breed,has_collar):
        if id not in self.posts:
            self.posts[id] = (pet_name.strip(), location.strip(),color.strip(),type.strip(),
                              breed.strip(),has_collar.strip(),PostDataBase.get_date())
            self.save()
            return 1

    def rmv_post(self, id):
            if id in self.posts:
                 del self.posts[id]
                 self.save()
                 return 1
            else:
                 return -1

    # def validate(self, email, password):
    #     if self.get_user(email) != -1:
    #         return self.users[email][0] == password
    #     else:
    #         return False

    def save(self):
        with open(self.filename, "w") as f:
            for post in self.posts:
                f.write(post + ";" + self.posts[post][0] + ";" + self.posts[post][1] + ";"
                        + self.posts[post][2] + ";" + self.posts[post][3]+ ";"
                        + self.posts[post][4] + ";"+ self.posts[post][5] + ";"+ self.posts[post][6] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now())

    #19.06.2015 10:03:06


class Login(object):
    def __init__(self,file_path):
        self.__file_path = file_path

    def verif_data(self,username,password):
        with open(self.__file_path,'r') as f:
            lines = f.readlines()
            for line in lines:
                line =line.strip()
                parts = line.split(',')
                id = int(parts[0])
                user = parts[1]
                passwd = parts[2]
                if user == username and passwd == password:
                    return id
        return -1

class Register(object):
    def __init__(self,file_path,srv_owner,srv_hero):
        self.__file_path = file_path
        self.__srv_owner = srv_owner
        self.__srv_hero = srv_hero

    def register(self,username,password,name,location,telephone):
        max = 0
        with open(self.__file_path,'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(',')
                id = int(parts[0])
                if max < id:
                    max = id
        max += 1
        self.__srv_owner.add_owner(max,name,location,telephone)
        self.__srv_hero.add_hero(max,name,location,telephone)
        s = str(max)+','+username+','+password +'\n'
        with open(self.__file_path,'a') as f:
                f.write(s)



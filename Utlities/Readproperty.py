import configparser
confiq=configparser.RawConfigParser()
confiq.read('C:\\Users\\vinothsc\\PycharmProjects\\orange_pro2\\Configurations\\config.ini')
class Read_confiq:
    @staticmethod
    def application_url():
       url= confiq.get('comman info_1','baseurl')
       return url

    @staticmethod
    def get_username():
        username=confiq.get('comman info_1','username')
        return username

    @staticmethod
    def get_password():
        password=confiq.get('comman info_1','password')
        return password


    @staticmethod
    def get_w_password():
        password = confiq.get('comman info_2', 'password')
        return password
    @staticmethod
    def Nusername():

        #fname = confiq.get('comman info_3',fname)
        #mname = confiq.get('comman info_3',mname)
        #lname = confiq.get('comman info_3',lname)
        Nusername1 = confiq.get('comman info_3','Nusername')
       # Npassword1 =confiq.get('comman info',Npassword)
        return Nusername1
    @staticmethod
    def Npassword():
      Npassword1 =confiq.get('comman info_3','Npassword')
      return Npassword1


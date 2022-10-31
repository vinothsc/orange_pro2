import time
import pytest
from Pageobjects.Login_page import Login
from Pageobjects.Login_page import Account
from Utlities.custom_logger import LogGen
from Utlities.Readproperty import Read_confiq


class Testpage:

    baseurl = Read_confiq.application_url()
    #username = Read_confiq.get_username()
    #password = Read_confiq.get_password()
    logger=LogGen.loggen() #creating logging variable.



    def test_login(self, setup):
        self.logger.info("****__TC_Login_01__****")
        self.driver = setup #call driver method from conftest file
        username = Read_confiq.get_username()
        password = Read_confiq.get_password()  #collect username and password from readproperty file and assign to veriable.
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        login_page_obj = Login(self.driver)
        login_page_obj.set_username(username)
        login_page_obj.set_password(password)
        login_page_obj.click_login()
        self.logger.info("login successfuly")
        page_title=self.driver.title
        if page_title=="OrangeHRM" :
            assert True
            self.logger.info('####loged page title')

            self.driver.close()
        else:
            self.driver.save_screenshot('.//screenshots//loged_page.png')
            self.driver.close()
            assert False



    def test_login_2(self, setup):
        self.logger.info("****__TC_Login_01__****")
        self.driver = setup  # call driver method from conftest file
        username = Read_confiq.get_username() # collect username and password from readproperty file and assign to veriable.
        password = Read_confiq.get_w_password() #given wrong password
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        login_page_obj = Login(self.driver)
        login_page_obj.set_username(username)
        login_page_obj.set_password(password)
        login_page_obj.click_login()
        self.logger.info("login successfuly")
        page_title = self.driver.title
        if page_title == "OrangeHRM":
            assert True
            self.logger.info('####loged page title')
            self.driver.close()
        else:
            self.driver.save_screenshot('.//screenshots//loged_page.png')
            self.logger.info('####loged page title')
            self.driver.close()
            assert False
    def test_account_creat(self,setup):
        self.logger.info("****__test_account_create__****")
        self.driver = setup  # call driver method from conftest file
        username = Read_confiq.get_username()
        password = Read_confiq.get_password()  # collect username and password from readproperty file and assign to veriable.
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        #### login the webpage######
        login_page_obj = Login(self.driver)
        login_page_obj.set_username(username)
        login_page_obj.set_password(password)
        login_page_obj.click_login()
        account_obj=Account(self.driver)  #creating account object
       ######user data ######
        name=Read_confiq.Nusername()
        password=Read_confiq.Npassword()

        account_obj.namefill()
        account_obj.image_insert()
        account_obj.checkbox_click()
        account_obj.logindetails(name,password)
        account_obj.personal_data()
        account_obj.job_details()
        self.driver.close()

    def test_account_edit(self, setup):
        self.logger.info("****__TC TEST ACCOUNT EDIT __****")
        self.driver = setup  # call driver method from conftest file
        username = Read_confiq.get_username()
        password = Read_confiq.get_password()  # collect username and password from readproperty file and assign to veriable.
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        login_page_obj = Login(self.driver)
        login_page_obj.set_username(username)
        login_page_obj.set_password(password)
        login_page_obj.click_login()
        self.logger.info('**##login is sucessfuly ##**')
        account_obj = Account(self.driver)  # creating account object
        user_name = Read_confiq.Nusername()
        account_obj.emp_search(user_name)
        account_obj.var1
        #var=account_obj.emp_search(varable)
        print(account_obj)
        account_obj.edit_user_data()
        #self.driver.close()

    def test_account_delete(self,setup):
        self.logger.info("****__TC__account deleted__****")
        self.driver = setup  # call driver method from conftest file
        username = Read_confiq.get_username()
        password = Read_confiq.get_password()  # collect username and password from readproperty file and assign to veriable.
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        login_page_obj = Login(self.driver)
        login_page_obj.set_username(username)
        login_page_obj.set_password(password)
        login_page_obj.click_login()
        self.logger('**##login sucessful##**')
        account_obj = Account(self.driver)  # creating account object
        user_name = Read_confiq.Nusername()
        account_obj.emp_search(user_name)
        self.logger('**#searched the user#**')
        account_obj.delete_user_data()
        self.logger('**##__account deleted succesfuly__')






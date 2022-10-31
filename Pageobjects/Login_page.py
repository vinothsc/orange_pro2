import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


class Login:
    textbox_username_name = 'username'
    textbox_password_name = 'password'
    button_login_xpath = "//*[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
    def click_login(self):
        self.driver.save_screenshot('.//screenshots//loginpage.png')
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


class Account:
    var1=0
    button_add_xpath="//*[text()='Add Employee']"
    textbox_fname_name="firstName"
    textbox_mname_name = "middleName"
    textbox_lname_name = "lastName"
    image_class='oxd-file-input'
    get_emp_id_xpath="//*[contains(text(),'Employee Id')]/../..//*[@class='oxd-input oxd-input--active']"
    textbox_employid="//*[contains(text(),'Employee Id')]/../..//*[@class='oxd-input oxd-input--active']"
    #button_save_xpath = "//button[@type='submit']"
    checkbox_addinfo_xpath="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    textbox_uname_xpath="//*[text()='Username']/../..//*[@class='oxd-input oxd-input--active']"
    textbox_password_xpath="//*[text()='Password']/../..//*[@type='password']"
    textbox_confpassword_xpath="//*[text()='Confirm Password']/../..//*[@type='password']"
    button_saveinfo_xpath="//*[text()=' * Required']/..//*[@type='submit']"
    textbox_dob_xpath="//*[contains(text(),'Date of Birth')]/../..//input[@placeholder='yyyy-mm-dd']"
    #### personal data ###
    dropbox_nationtly_xpath="//*[contains(text(),'Nationality')]/../..//*[@class='oxd-select-text--after']"
    dropbox_select_xpath="//*[@class='oxd-select-option'][84]"
    dropbox_marrage_xpath="//*[contains(text(),'Marital Status')]/../..//*[@class='oxd-select-wrapper']"
    dropbox_marr_select_xpath="//*[contains(text(),'Single')]"
    checkbox_male_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label"
    checkbox_smk_xpath="//*[contains(text(),'Smoker')]/../..//*[@type='checkbox']"
    dropbx_blood_xpath="//*[contains(text(),'Blood Type')]/../..//*[@class='oxd-select-wrapper']"
    dropbx_blood_sele_="//*[contains(text(),'Blood Type')]/../..//*[contains(text(),'O+')]"
    meltry_serv_xpath="//*[contains(text(),'Military Service')]/../..//*[@class='oxd-input oxd-input--active']"
    save_button_xpath="//button[@type='submit']"

#####jobdetails####
    job_details_xpath = "//*[text()='Job']"
    job_joind_date_enter = "//*[contains(text(),'Joined Date')]/../..//*[@placeholder='yyyy-mm-dd']"
    job_title_xpath = "//*[contains(text(),'Job Title')]/../..//*[@class='oxd-select-wrapper']"
    job_title_select_xpath = "//*[contains(text(),'Job Title')]/../..//*[contains(text(),'QA Engineer')]"
    job_subunit_xpath = "//*[contains(text(),'Sub Unit')]/../..//*[@class='oxd-select-wrapper']"
    job_subunit_sele_xpath = "//*[contains(text(),'Sub Unit')]/../..//*[contains(text(),'Development')]"
    emply_sts_xpath = "//*[contains(text(),'Employment Status')]/../..//*[@class='oxd-select-wrapper']"
    emply_sts_sele_xpath = "//*[contains(text(),'Employment Status')]/../..//*[contains(text(),'Full-Time Permanent')]"
    save_button_xpath="//button[@type='submit']"

    #employee search datas
    emp_search_xpath = "//*[contains(text(),'Employee Name')]/../..//*[@placeholder='Type for hints...']"
    search_button_xpath = "//button[@type='submit']"
    sugg_click = "//*[contains(text(),'vinoth mname')]"
    delete_icon_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]"
    edit_button_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]"







    def __init__(self,driver):
        self.driver=driver

    def namefill(self):
        self.driver.find_element(By.XPATH,self.button_add_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME,self.textbox_fname_name).send_keys('vinoth')
        self.driver.find_element(By.NAME, self.textbox_mname_name).send_keys('mname')
        self.driver.find_element(By.NAME, self.textbox_lname_name).send_keys('lname')
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.textbox_employid).clear()
        #self.driver.find_element(By.XPATH,self.textbox_employid).send_keys('90000')

    def image_insert(self):
        image_var=self.driver.find_element(By.CLASS_NAME,self.image_class)
        image_var.send_keys('C:\\Users\\vinothsc\\PycharmProjects\\orange_pro2\\TestData\\mani.jpg')
        time.sleep(4)

    ##def get_id(self):
        ##var_id=self.driver.find_element(By.XPATH,self.get_emp_id_xpath).text
        #return var_id

    def checkbox_click(self):
        self.driver.find_element(By.XPATH, self.checkbox_addinfo_xpath).click()
    def logindetails(self,name,password):
        #password="Qwerty@1"
        self.driver.find_element(By.XPATH, self.textbox_uname_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.textbox_confpassword_xpath).send_keys(password)
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.button_saveinfo_xpath).click()
        time.sleep(4)
        self.driver.save_screenshot("C:\\Users\\vinothsc\\PycharmProjects\\orange_pro2\\screenshots\\image1.png")
    def personal_data(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH,self.dropbox_nationtly_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.dropbox_select_xpath).click()
        self.driver.find_element(By.XPATH,self.dropbox_marrage_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.dropbox_marr_select_xpath).click()

        self.driver.find_element(By.XPATH,self.textbox_dob_xpath).send_keys('2022-10-03')
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.dropbx_blood_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.dropbx_blood_sele_).click()
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()


    def job_details(self):
        self.driver.find_element(By.XPATH, self.job_details_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.job_joind_date_enter).send_keys('2022-10-03')
        self.driver.find_element(By.XPATH, self.job_title_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.job_title_select_xpath).click()
        self.driver.find_element(By.XPATH, self.job_subunit_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.job_subunit_sele_xpath).click()
        self.driver.find_element(By.XPATH, self.emply_sts_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.emply_sts_sele_xpath).click()
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()

    def emp_search(self,name,):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.emp_search_xpath).send_keys("vinoth")
        time.sleep(4)
        self.var1= self.driver.find_element(By.XPATH, self.sugg_click).click()
        return self.var1
        time.sleep(5)

        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def edit_user_data(self):
        self.driver.find_element(By.XPATH,self.edit_button_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.checkbox_male_xpath).click()
        self.driver.find_element(By.XPATH,self.meltry_serv_xpath).send_keys('comnder genarel')
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()


    def delete_user_data(self):
        self.driver.find_element(By.XPATH,self.delete_icon_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@type='button' and @class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()












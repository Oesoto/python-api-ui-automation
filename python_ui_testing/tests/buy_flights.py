import time
import unittest

from selenium import webdriver


class BuyFlightsTest(unittest.TestCase):

    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="./python_ui_testing/drivers/chromedriver.exe")
        cls.driver.maximize_window()

    # Login
    def test_go_url(self, url):
        self.driver.get(url)

    def test_login(self, username, password):
        self.driver.find_element_by_name("userName").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()

    def test_image_flight_finder(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_flightfinder.gif')]").is_displayed()
        self.assertTrue(image)


    # Buscar Vuelo
    def test_select_flight_type(self, type):
        self.driver.find_element_by_css_selector("input[type='radio'][name='tripType'][value='{}']".format(str(type))).click()

    def test_select_passanger_number(self, number):
        self.driver.find_element_by_xpath("//select[@name='passCount']/option[@value='{}']".format(str(number))).click()

    def test_select_origin(self, city):
        self.driver.find_element_by_xpath("//select[@name='fromPort']/option[@value='{}']".format(str(city))).click()

    def test_select_departure_date(self, month, day):
        self.driver.find_element_by_xpath("//select[@name='fromMonth']/option[@value='{}']".format(str(month))).click()
        self.driver.find_element_by_xpath("//select[@name='fromDay']/option[@value='{}']".format(str(day))).click()

    def test_select_destiny(self, city):
        self.driver.find_element_by_xpath("//select[@name='toPort']/option[@value='{}']".format(str(city))).click()

    def test_select_returning_date(self, month, day):
        self.driver.find_element_by_xpath("//select[@name='toMonth']/option[@value='{}']".format(str(month))).click()
        self.driver.find_element_by_xpath("//select[@name='toDay']/option[@value='{}']".format(str(day))).click()

    def test_select_service_class(self, serv_class):
        if serv_class == "First Class":
            service_class = "First"
        else:
            service_class = "Coach"

        self.driver.find_element_by_css_selector("input[type='radio'][name='servClass'][value='{}']".format(str(service_class))).click()

    def test_select_airline(self, airline):
        self.driver.find_element_by_xpath("//select[@name='airline']/option[text() ='{}']".format(str(airline))).click()

    def test_search_flight(self):
        time.sleep(2)
        self.driver.find_element_by_name("findFlights").click()

    def test_image_select_flight(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'/images/masts/mast_selectflight.gif')]").is_displayed()
        self.assertTrue(image)


    # Seleccionar vuelo
    def test_select_departure_return_flights(self, departure, returnn):
        if departure == "Pangea Airlines":
            self.driver.find_element_by_css_selector("input[type='radio'][name='outFlight'][value='Pangea Airlines$362$274$9:17']").click()

        if returnn == "Blue Skies":
            self.driver.find_element_by_css_selector("input[type='radio'][name='inFlight'][value='Blue Skies Airlines$631$273$14:30']").click()

    def test_select_flights(self):
        time.sleep(2)
        self.driver.find_element_by_name("reserveFlights").click()

    def test_image_book_a_flight(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'/images/masts/mast_book.gif')]").is_displayed()
        self.assertTrue(image)


    #Reservar vuelo
    def test_enter_personal_data(self, name, lastname, meal, name2, lastname2):
        self.driver.find_element_by_name("passFirst0").send_keys(name)
        self.driver.find_element_by_name("passLast0").send_keys(lastname)

        self.driver.find_element_by_name("passFirst1").send_keys(name2)
        self.driver.find_element_by_name("passLast1").send_keys(lastname2)

        if meal == "Low Calorie":
            self.driver.find_element_by_xpath("//select[@name='pass.0.meal']/option[@value='LCML']").click()

    def test_enter_credit_card_data(self, credit_card, card_number, expiration_month, expiration_year, name, lastname, midname):
        if credit_card == "Visa":
            self.driver.find_element_by_xpath("//select[@name='creditCard']/option[@value='BA']").click()

        self.driver.find_element_by_name("creditnumber").send_keys(card_number)

        if expiration_month == "01":
            self.driver.find_element_by_xpath("//select[@name='cc_exp_dt_mn']/option[text()='01 \n                      ']")\
                .click()

        self.driver.find_element_by_xpath("//select[@name='cc_exp_dt_yr']/option[@value='{}']".format(expiration_year))\
            .click()
        self.driver.find_element_by_name("cc_frst_name").send_keys(name)
        self.driver.find_element_by_name("cc_mid_name").send_keys(lastname)
        self.driver.find_element_by_name("cc_last_name").send_keys(midname)

    def test_enter_billing_address(self, bill_address1, bill_address2, bill_city, bill_state, bill_zip, country):
        self.driver.find_element_by_name("billAddress1").clear()
        self.driver.find_element_by_name("billAddress1").send_keys(bill_address1)

        self.driver.find_element_by_name("billAddress2").clear()
        self.driver.find_element_by_name("billAddress2").send_keys(bill_address2)

        self.driver.find_element_by_name("billCity").clear()
        self.driver.find_element_by_name("billCity").send_keys(bill_city)

        self.driver.find_element_by_name("billState").clear()
        self.driver.find_element_by_name("billState").send_keys(bill_state)

        self.driver.find_element_by_name("billZip").clear()
        self.driver.find_element_by_name("billZip").send_keys(bill_zip)

        if country == "Colombia":
            self.driver.find_element_by_xpath("//select[@name='billCountry']/option[@value='42']").click()

    def test_enter_delivery_address(self, del_address1, del_address2, del_city, del_state, del_zip, country):
        self.driver.find_element_by_name("delAddress1").clear()
        self.driver.find_element_by_name("delAddress1").send_keys(del_address1)

        self.driver.find_element_by_name("delAddress2").clear()
        self.driver.find_element_by_name("delAddress2").send_keys(del_address2)

        self.driver.find_element_by_name("delCity").clear()
        self.driver.find_element_by_name("delCity").send_keys(del_city)

        self.driver.find_element_by_name("delState").clear()
        self.driver.find_element_by_name("delState").send_keys(del_state)

        self.driver.find_element_by_name("delZip").clear()
        self.driver.find_element_by_name("delZip").send_keys(del_zip)

        if country == "Colombia":
            self.driver.find_element_by_xpath("//select[@name='delCountry']/option[@value='42']").click()

        alert = self.driver.switch_to_alert()
        alert.accept()

    def test_book_flight(self):
        time.sleep(2)
        self.driver.find_element_by_name("buyFlights").click()

    def test_image_flight_confirmation(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'/images/masts/mast_confirmation.gif')]").is_displayed()
        self.assertTrue(image)


    # Confirmar reseva
    def test_flight_confirmation(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//img[contains(@src,'/images/forms/home.gif')]").click()

    def test_image_home(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'/images/hdr_findflight.gif')]").is_displayed()
        self.assertTrue(image)


    # Este método se ejecuta al final y cierra el navegador
    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()
        print("prueba completada con éxito")


if __name__ == '__main__':
    unittest.main()

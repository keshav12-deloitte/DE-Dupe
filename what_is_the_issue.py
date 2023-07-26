class WhatIsTheIssue:

    def if_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def open_website(self, url):
        self.driver.get(url)

    def click_element_by_id(self, element_id):
        element = self.driver.find_element_by_id(element_id)
        element.click()

    def fill_input_by_name(self, input_name, text):
        input_element = self.driver.find_element_by_name(input_name)
        input_element.send_keys(text)

    def tap_element(self, xpathFull):
        element = self.driver.find_element(xpathFull)
        element.click()

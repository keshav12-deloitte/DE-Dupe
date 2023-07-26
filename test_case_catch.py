class TestCaseCatch:

    def hanoi_tower_problem(self, n, source, auxiliary, destination):
        if n == 1:
            print(f"Move disc 1 from {source} to {destination}")
            return
        self.hanoi_tower_problem(n - 1, source, destination, auxiliary)
        print(f"Move disc {n} from {source} to {destination}")
        self.hanoi_tower_problem(n - 1, auxiliary, source, destination)

    def find_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def find_palindrome(self, word):
        reversed_word = word[::-1]
        return word == reversed_word


    def open_url(self, url):
        self.driver.get(url)

    def tap_element(self, locator):
        element = self.driver.find_element(locator)
        element.click()

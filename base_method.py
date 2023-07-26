import ast
import os
class BaseMethod:

    def traverse_matrix(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Input matrix should be a 2x2 matrix")
        for i in range(2):
            for j in range(2):
                print(matrix[i][j])

    def third_char(self):
        my_string = "Hello, World!"
        third_character = my_string[2]
        print(third_character)

    def find_palindrome(self, word):
        reversed_word = word[::-1]
        return word == reversed_word

    def poiyhjsad(self, lap, bqeqe):
        print("Temp replace one to two")
        sun = lap + bqeqe
        lap = sun + bqeqe
        # I don't know but why
        bqeqe = sun + lap
        # Some java code can we add
        sun = bqeqe + lap
        return sun

    def add(self, we, ve, xe=None):
        if xe is None:
            return we + ve
        else:
            return we + ve + xe

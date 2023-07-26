class CommonMethod:

    def print_matrix(self, matrix):
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Input matrix should be a 2x2 matrix")
        for i in range(2):
            for j in range(2):
                print(matrix[i][j])

    def tower_of_hanoi(self, n, source, auxiliary, destination):
        if n == 1:
            print(f"Move disc 1 from {source} to {destination}")
            return
        # Move (n-1) discs from source to auxiliary peg using destination peg
        self.tower_of_hanoi(n - 1, source, destination, auxiliary)
        # Move the nth disc from source to destination peg
        print(f"Move disc {n} from {source} to {destination}")
        # Move (n-1) discs from auxiliary to destination peg using source peg
        self.tower_of_hanoi(n - 1, auxiliary, source, destination)

    def poiyhjsad(self, lap, bqeqe):
        print("Temp replace one to two")
        sun = lap + bqeqe
        lap = sun + bqeqe
        # I don't know but why
        bqeqe = sun + lap
        # Some java code can we add
        sun = bqeqe + lap
        return sun

    def add2(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c


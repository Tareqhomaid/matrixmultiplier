from sys import exit


# [[5,2,3],
# [1,3,6]]

# [[1,3],
# [5,2],
# [4,-1]]

def get_input(row_count, m):  # Function to receive Input matrices
    return [[int(x) for x in
             input(f"Enter row number {i + 1} for matrix {m} elements separated by space (ex: 1 2 3): ").split()]
            for i in
            range(row_count)]  # using list comprehension, returning all the input using one line only :)


def multiply_matrix(a, b):
    if len(a[0]) != len(b):
        print("matrices can't be multiplied!! aj != bi")
        exit()

    c = [[0 for x in range(len(b[0]))] for y in range(len(a))]  # forming and filling the resulting matrix by zeroes

    for i in range(len(c)):  # turning the mathematical low into nested for loop
        for j in range(len(c[0])):
            c[i][j] = sum([a[i][k] * b[k][j] for k in range(len(b))])  # replacing the zeroes with real values
    return c


class Matrices:
    def __init__(self, A, B):
        self.len_a = A
        self.len_b = B
        self.A = get_input(A, "A")
        print()
        self.B = get_input(B, "B")
        self.C = multiply_matrix(self.A, self.B)


def main():
    rows = [int(i) for i in input("Enter the rows count for A and B separated by space (ex: 3 4): ").split()]
    print()
    result = Matrices(rows[0], rows[1])
    res = "The Result is:"
    print()
    print(res)
    print("*=" * int(len(res) / 2))
    for i in result.C:
        print(str(i).replace(",", ""))


if __name__ == "__main__":
    main()

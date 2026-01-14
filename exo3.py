import numpy as np

class MyMatrix:
    def __init__(self, N):
        """Create an NxN matrix with random values."""
        self.data = np.random.rand(N, N)

    def __str__(self):
        return str(self.data)

    # Addition
    def __add__(self, other):
        return MyMatrix.from_array(self.data + other.data)

    # Multiplication
    def __mul__(self, other):
        return MyMatrix.from_array(np.dot(self.data, other.data))

    # Determinant
    def determinant(self):
        return np.linalg.det(self.data)

    # Inverse
    def inverse(self):
        return MyMatrix.from_array(np.linalg.inv(self.data))

    # Eigenvalues
    def eigenvalues(self):
        return np.linalg.eigvals(self.data)

    @classmethod
    def from_array(cls, array):
        """Create a MyMatrix instance from a numpy array."""
        obj = cls(array.shape[0])
        obj.data = array
        return obj

# Example usage
if __name__ == "__main__":
    N = 4
    matrix1 = MyMatrix(N)
    matrix2 = MyMatrix(N)

    print("Matrix 1:\n", matrix1)
    print("\nMatrix 2:\n", matrix2)

    print("\nInverse of matrix1:\n", matrix1.inverse())
    print("\nDeterminant of matrix1:", matrix1.determinant())
    print("\nEigenvalues of matrix1:", matrix1.eigenvalues())
    print("\nmatrix1 + matrix2:\n", matrix1 + matrix2)
    print("\nmatrix1 * matrix2:\n", matrix1 * matrix2)

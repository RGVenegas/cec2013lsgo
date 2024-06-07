import numpy as np

class CEC2013LSGO:
    def __init__(self, dim):
        self.dim = dim
        self.shift = np.random.uniform(-100, 100, self.dim)
        self.rotation_matrix = self.random_rotation_matrix(self.dim)

    def random_rotation_matrix(self, dim):
        H = np.random.randn(dim, dim)
        Q, R = np.linalg.qr(H)
        return Q

    # Función 1: Shifted and Rotated Bent Cigar Function
    def shifted_bent_cigar(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return x_rotated[0]**2 + 10**6 * np.sum(x_rotated[1:]**2)

    # Función 2: Shifted and Rotated Sum of Different Powers Function
    def shifted_sum_of_different_power(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return np.sum(np.abs(x_rotated)**(2 + 4 * np.arange(len(x)) / (len(x) - 1)))

    # Función 3: Shifted and Rotated Zakharov Function
    def shifted_zakharov(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return np.sum(x_rotated**2) + (np.sum(0.5 * np.arange(1, len(x) + 1) * x_rotated))**2 + (np.sum(0.5 * np.arange(1, len(x) + 1) * x_rotated))**4

    # Función 4: Shifted Rosenbrock Function
    def shifted_rosenbrock(self, x):
        x_shifted = x - self.shift
        return np.sum(100 * (x_shifted[1:] - x_shifted[:-1]**2)**2 + (x_shifted[:-1] - 1)**2)

    # Función 5: Shifted and Rotated Rosenbrock Function
    def shifted_rotated_rosenbrock(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return np.sum(100 * (x_rotated[1:] - x_rotated[:-1]**2)**2 + (x_rotated[:-1] - 1)**2)

    # Función 6: Shifted Rastrigin Function
    def shifted_rastrigin(self, x):
        x_shifted = x - self.shift
        return 10 * len(x) + np.sum(x_shifted**2 - 10 * np.cos(2 * np.pi * x_shifted))

    # Función 7: Shifted and Rotated Rastrigin Function
    def shifted_rotated_rastrigin(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return 10 * len(x) + np.sum(x_rotated**2 - 10 * np.cos(2 * np.pi * x_rotated))

    # Función 8: Shifted and Rotated Non-Continuous Rastrigin Function
    def shifted_non_continuous_rastrigin(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        x_transformed = np.where(np.abs(x_rotated) < 0.5, x_rotated, np.round(2 * x_rotated) / 2)
        return 10 * len(x) + np.sum(x_transformed**2 - 10 * np.cos(2 * np.pi * x_transformed))

    # Función 9: Shifted Schwefel Function
    def shifted_schwefel(self, x):
        x_shifted = x - self.shift
        return 418.9829 * len(x) - np.sum(x_shifted * np.sin(np.sqrt(np.abs(x_shifted))))

    # Función 10: Shifted and Rotated Schwefel Function
    def shifted_rotated_schwefel(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return 418.9829 * len(x) - np.sum(x_rotated * np.sin(np.sqrt(np.abs(x_rotated))))

    # Función 11: Shifted Elliptic Function
    def shifted_elliptic(self, x):
        x_shifted = x - self.shift
        return np.sum(10**6**(np.arange(len(x)) / (len(x) - 1)) * x_shifted**2)

    # Función 12: Shifted and Rotated Elliptic Function
    def shifted_rotated_elliptic(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return np.sum(10**6**(np.arange(len(x)) / (len(x) - 1)) * x_rotated**2)

    # Función 13: Shifted Ackley Function
    def shifted_ackley(self, x):
        x_shifted = x - self.shift
        return -20 * np.exp(-0.2 * np.sqrt(np.mean(x_shifted**2))) - np.exp(np.mean(np.cos(2 * np.pi * x_shifted))) + 20 + np.e

    # Función 14: Shifted and Rotated Ackley Function
    def shifted_rotated_ackley(self, x):
        x_shifted = x - self.shift
        x_rotated = np.dot(self.rotation_matrix, x_shifted)
        return -20 * np.exp(-0.2 * np.sqrt(np.mean(x_rotated**2))) - np.exp(np.mean(np.cos(2 * np.pi * x_rotated))) + 20 + np.e

    # Función 15: Shifted Schwefel 1.2 Problem
    def shifted_schwefel_1_2(self, x):
        x_shifted = x - self.shift
        return np.sum(np.cumsum(x_shifted)**2)

    # Función ayuda para generar una matriz de rotación aleatoria
    def rotation_matrix(dim):
        H = np.random.randn(dim, dim)
        Q, R = np.linalg.qr(H)
        return Q

    if __name__ == "__main__":
        # Puedes agregar tu main aquí para probar si funciona correctamente
        pass
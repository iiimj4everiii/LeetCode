import numpy as np
import matplotlib.pyplot as plt


class Solution:
    def __init__(self):
        pass

    def order_2_polyfit(self, x_list, y_list):

        x_list = np.array(x_list)
        y_list = np.array(y_list)

        assert(x_list.shape[0] == y_list.shape[0])
        assert(x_list.shape[0] >= 3)
        assert(y_list.shape[0] >= 3)

        multiplier = 64             # Tunable parameter
        weighted_x_list, weighted_y_list = self.get_power_weights(x_list, y_list, multiplier)

        X = np.column_stack((
            np.ones(weighted_x_list.shape),
            weighted_x_list,
            np.multiply(weighted_x_list, weighted_x_list)
        ))

        pseudo_inverse = self.get_pseudo_inverse(X)

        coefficients = np.matmul(pseudo_inverse, weighted_y_list)

        x_MIN = -50                 # Tunable parameter
        alpha = 0.000001                 # Tunable parameter
        coefficients = self.gradient_descent(X, weighted_y_list, coefficients, x_MIN, alpha)

        return coefficients[::-1]

    def get_power_weights(self, x_list, y_list, multiplier):

        max_power = max(x_list)
        weighted_x_list = np.array([])
        weighted_y_list = np.array([])
        for i in range(x_list.shape[0]):

            x = x_list[i]
            y = y_list[i]

            weight = self.get_power_weight(x, max_power, multiplier)

            weighted_x = [x] * weight
            weighted_y = [y] * weight

            weighted_x_list = np.append(weighted_x_list, weighted_x)
            weighted_y_list = np.append(weighted_y_list, weighted_y)

        return weighted_x_list, weighted_y_list

    @staticmethod
    def get_power_weight(power, max_power, multiplier):
        delta = max_power - power

        weight = round(multiplier / (10 ** (delta / 10)))

        return max(weight, 1)

    @staticmethod
    def get_pseudo_inverse(X):
        X_T = np.transpose(X)
        X_T_X = np.matmul(X_T, X)

        X_T_X_inverse = np.linalg.inv(X_T_X)

        pseudo_inverse = np.matmul(X_T_X_inverse, X_T)

        return pseudo_inverse

    @staticmethod
    def gradient_descent(X, y, coeff, x_MIN, alpha):

        def get_gradient(X, y, coeff):

            X_T = np.transpose(X)

            y_hat = np.matmul(X, coeff)

            gradient = np.matmul(X_T, (y_hat - y))

            return gradient

        def get_square_error(X, y, coeff):

            N = y.shape[0]

            error = np.matmul(X, coeff) - y

            return np.dot(error, error) / N


        plt.scatter(X[:, 1], y, c=[0, 0, 0])
        x = np.linspace(-100, 30, 601)
        y_fit = coeff[2] * x * x + coeff[1] * x + coeff[0]
        plt.plot(x, y_fit)

        # coeff[1] = -2 * x_MIN * coeff[2]
        # y_fit = coeff[2] * x * x + coeff[1] * x + coeff[0]
        # plt.plot(x, y_fit)
        N = y.shape[0]

        for _ in range(100):

            prev_w1 = coeff[1]
            prev_w2 = coeff[2]

            error = get_square_error(X, y, coeff)
            print(error)

            gradient = get_gradient(X, y, coeff)
            coeff = coeff - (alpha / N) * gradient

            x_MIN_hat = -prev_w1 / (2 * prev_w2)

            coeff[1] = prev_w1 - (5 * alpha) * (-prev_w1 * (x_MIN - x_MIN_hat) ** 2 +
                                                prev_w2 * (x_MIN - x_MIN_hat) * (x_MIN ** 2 - x_MIN_hat ** 2))

            y_fit = coeff[2] * x * x + coeff[1] * x + coeff[0]
            plt.plot(x, y_fit)

        plt.show()

        return coeff


X = [23.5, 20.5, -10.5]
y = [4.92, 4.2, 0.6]
sol = Solution().order_2_polyfit(X, y)
print(sol)

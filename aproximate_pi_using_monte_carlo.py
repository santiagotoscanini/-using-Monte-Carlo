import random
import math
from statics import mean, standard_deviation


def random_coordinate():
    return random.random() * random.choice([-1, 1]);


def throw_needles(number_of_needles):
    inside_circle = 0

    for _ in range(number_of_needles):
        x = random_coordinate()
        y = random_coordinate()
        distance_from_center = math.sqrt(x ** 2 + y ** 2)
        if distance_from_center <= 1:
            inside_circle += 1

    return (4 * inside_circle) / number_of_needles


def estimation(number_of_needles, number_of_tries):
    estimated_pi_values = []
    for _ in range(number_of_tries):
        pi = throw_needles(number_of_needles)
        estimated_pi_values.append(pi)

    mu = mean(estimated_pi_values)
    sigma = standard_deviation(estimated_pi_values)
    print(f'Mean: {mu}, Standard deviation: {sigma}, Number of needles: {number_of_needles}')

    return mu, sigma


def estimate_pi(precision, confidence_interval, number_of_needles, number_of_tries):
    mean = 0
    sigma = precision

    while sigma >= precision / confidence_interval:
        mean, sigma = estimation(number_of_needles, number_of_tries)
        number_of_needles *= 2

    return mean


if __name__ == "__main__":
    confidence_interval_95 = 1.96
    pi = estimate_pi(0.01, confidence_interval_95, 1000, 1000)
    print(pi)

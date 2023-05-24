from random import randint
from time import time

PROBLEM_FORMAT = """

"""

RESULTS_FILE_NAME = "{max_digits}-digit-results.csv"
RESULT_ROW = "{num_correct},{num_problems},{max_digits},{latency}\n"

def main():
    num_problems, max_digits = get_inputs()
    ready_set()
    num_correct, latency = go(num_problems, max_digits)
    write_results(num_correct, num_problems, max_digits, latency)

def get_inputs():
    num_problems = None
    while num_problems is None:
        try:
            num_problems = int(input("How many problems? "))
        except ValueError:
            print("Please input an integer.\n")

    max_digits = None
    while max_digits is None:
        try:
            max_digits = int(input("Max digits per number? "))
        except ValueError:
            print("Please input an integer.\n")
            continue

        if max_digits <= 0:
            print("Please input an integer greater than 0.")
            max_digits = None

    return (num_problems, max_digits)

def ready_set():
    input("Press enter to start. ")
    print()

def go(num_problems, max_digits):
    generate_num = lambda: randint(1, 10**max_digits - 1)

    num_correct = 0

    start_s = time()
    for _ in range(num_problems):
        n1, n2 = generate_num(), generate_num()
        answer = int(input("{0} x {1} = ".format(n1, n2)))
        if answer == n1*n2:
            print("Correct.\n")
            num_correct += 1
        else:
            print("Correct answer was {0}.\n".format(n1*n2))
    latency = f"{time() - start_s:.1f}"

    print("{0}/{1} correct in {2} seconds.".format(num_correct, num_problems, latency))

    return (num_correct, latency)

def write_results(num_correct, num_problems, max_digits, latency):
    f = open(RESULTS_FILE_NAME.format(max_digits=max_digits), "a")
    f.write(RESULT_ROW.format(
        num_correct=num_correct,
        num_problems=num_problems,
        max_digits=max_digits,
        latency=latency)
    )
    f.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting.\n")

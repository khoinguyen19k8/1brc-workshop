# TODO: Rename this file to firstname_lastname.py
import sys


def print_measurements(cities: dict) -> None:
    """
    Print the minimum, mean and maximum measurements for each city in alphabetical order.
    
    Required Format: city=min/mean/max
    - measurements are doubles between -99.9 and 99.9
    - Always display with exactly one fractional digit
    - Cities should be printed in alphabetical order
    
    Example output:
    Amsterdam=5.2/15.7/25.1
    Berlin=-12.8/8.3/32.4
    London=1.9/11.2/28.7
    """
    ...

def main(measurements_file_path: str) -> dict:
    ... 


if __name__ == '__main__':
    cities = main(sys.argv[1])
    print_measurements(cities)

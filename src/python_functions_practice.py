def return_10():
    return 10


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 / number_2


def length_of_string(test_string):
    return len(test_string)


def join_string(string_1, string_2):
    return string_1 + string_2


def add_string_as_number(first_number, second_number):
    return int(first_number) + int(second_number)


def number_to_full_month_name(month_number):
    months_index = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months_index[month_number]


def number_to_short_month_name(month_number):
    months_index = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sept",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return months_index[month_number]


def volume_of_cube(length):
    return length * length * length


def reverse_string(word):
    return word[::-1]


def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5.0/9.0)
    return round(celcius, 2)

#test


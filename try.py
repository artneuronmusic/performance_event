
word = ["love", "whatever", "hope"]
# print(len(word))


# def check_number(number):
#     if not number > 0:
#         print("negative")
#         raise ValueError('Invalid phone number.')

#     # if not number < 9:
#     #     print("<9")
#     #     return False
#     if len(word) == 3:
#         print("elif")
#         print("wrong")

#     return True


# print(check_number(9))
number = 2
# print(number)


def check_it():

    if number != 3:
        # print('number is greater than 3')

        raise ValueError("Wrong")

    if len(word) == 3:
        print('number is not greater than 3')
        # return False

    return True


print(check_it())
# check_it()

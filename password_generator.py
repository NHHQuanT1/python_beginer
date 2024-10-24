import string
import random

LETTERS = string.ascii_letters #cac ki tu a,b,c
NUMBERS = string.digits #cac chu so
PUNCTUATION = string.punctuation #cac ki tu dac biet




def password_generator( length = 8): #do dai ki tu nhap vao
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printable = list(printable)  #chuyen doi thanh dang list thi ham random moi su dung duoc
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


def get_password_length():
    password_length = input("How long do you want your password: ")
    return int(password_length)



def main():
    password_length = get_password_length()
    password = password_generator(password_length)
    print(password)   

if __name__ == '__main__':
    main()

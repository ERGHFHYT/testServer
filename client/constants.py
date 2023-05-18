
# SIZE
WIDTH = 900
HEIGHT = 600
SIZE_OF_WINDOW = "900x600"
SIZE_OF_BACKGROUND_IMAGE = (1400, 1000)
ICON_IMAGE_SIZE = 20
CHECK_IMAGE_SIZE = (30, 25)

# commends for the server
CHECK_PASSWORD_FROM_TABLE = "chek_password_form_table"
GET_TABLE = "get_a_table"
PUPILS_IN_TEACHERS = "pupils_in_teachers"
REMOVE_ITEM_FROM_TABLE = "remove_item"
CIRCULATIONS_TABLE = "circulations_table"
COMPUTER_NAMES_TABLE = "computer_names_table"
TEACHERS_TABLE = "teachers_table"
SAVE_TABLE = "save_table"
PUPILS_TABLE = "pupils_table"
PASSWORD_TABLE = "password_table"
PRACTITIONERS_TABLE = "practitioners_table"
GET_MAX = "get_max_column_of_the_table"

# positions
MIDDLE = 0.5

# COLORS
RED = "#b20e1b"
NUM_BLUE = "#1f6aa5"
BACKGROUND_COLOR = "#2b2b2b"
BACKGROUND_COLOR_OF_CUSTOM_WINDOWS = "#333333"
DARK = "Dark"
BLUE = "blue"
DARK_GRAY = "#2a2d2e"

# image's
BACKGROUND_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's/" \
                   "background image.webp"
TEACHER_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's" \
                "/teacher_image.png"
CHECK_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's/ckenck.png"
HOME_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's/home.png"
MICROPHONE_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's" \
                   "/microphone" \
                   ".png"
ADD_LIST_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's/" \
                 "add-list.png"

ADD_USER_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's/add-user.png"
ADD_FOLDER_IMAGE = "C:/Users/User/PycharmProjects/testServer/imege's" \
                   "/add_folder.png" \

# receive from the server
CORRECT_PASSWORD = "True"
PASSWORD_ERROR = "password_error"
USERNAME_ERROR = "username_error"
USERNAME_ERROR_AND_PASSWORD_ERROR = "username_error_and_password_error"
# Messages to the user
WRONG_PASSWORD = "הסיסמה לא נכונה"
WRONG_USERNAME = "שם המשתמש לא נכון"
ALL_WRONG = "שם משתמש או סיסמה לא נכונים"
EMPTY_SPACE = ""

# show to the screen
THE_WORD_PASSWORD = "סיסמה"
ASTERISK = "*"

# Names of objects on the screen
LOGIN_SCREEN = "מסך פתיחה"

# fonts
DEFAULT_FONT = "Halvetica"

# Definitions of objects on the screen
ENTRY_JUSTIFY = 'right'


def CheckID(ID):
    if len(ID) != 9:
        return False

    try:
        id = list(map(int, ID))
    except:
        return False

    counter = 0

    for i in range(9):
        id[i] *= (i % 2) + 1
        if id[i] > 9:
            id[i] -= 9
        counter += id[i]

    if counter % 10 == 0:
        return True
    else:
        return False


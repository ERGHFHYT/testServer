import threading

from server_constants import *
import json
import socket
import os
import psycopg2
from psycopg2 import extensions
import traceback
auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
conct = STRING_CONNECSHN
mydb = psycopg2.connect(conct)
mydb.set_isolation_level(auto_commit)
mycursor = mydb.cursor()


def remove_item(the_name_of_the_table, typed):
    the_list_of_the_data = db(the_name_of_the_table)
    # בודק לפי מה שהמשתמש כתב מה הכי קרוב להיות מה שהוא רוצה למחוק
    for single_data in the_list_of_the_data:
        if the_name_of_the_table == CIRCULATIONS_TABLE or the_name_of_the_table == PASSWORD_TABLE:
            single = single_data[1]
        else:
            single = single_data[2]

        if single == typed:
            the_list_of_the_data.remove(single_data)
    sql = "DELETE FROM " + the_name_of_the_table
    mycursor.execute(sql)
    mydb.commit()
    data = [tuple(x) for x in the_list_of_the_data]
    add_items(the_name_of_the_table, data)
    # for d in the_list_of_the_data:
    #     add_item(the_name_of_the_table, d)
    return the_list_of_the_data


def pupils_in_teachers():
    sql = "SELECT \
    pupils_table.name AS name_p, \
    pupils_table.phone_number AS phone_p, \
    pupils_table.id AS id_p, \
    teachers_table.name AS name_t, \
    teachers_table.phone_number AS phone_t, \
    teachers_table.id AS id_t  \
    FROM pupils_table \
    INNER JOIN teachers_table ON pupils_table.teacher = teachers_table.id"

    mycursor.execute(sql)
    list_name = mycursor.fetchall()
    return list(list_name)


def check_password():
    #  בודק אם הסיסמה השם משתמש שנתנו לו היא נכונה
    mycursor.execute("SELECT password FROM password_table")
    myresult_password = mycursor.fetchall()
    myresult_password = [list(ele) for ele in myresult_password]
    mycursor.execute("SELECT username FROM password_table")
    myresult_username = mycursor.fetchall()
    myresult_username = [list(ele) for ele in myresult_username]
    bool_to_pass_to_password = False
    bool_to_pass_to_username = False
    bool_to_pass = False
    for i in range(len(myresult_password)):
        if str(myresult_username[i][0]) == str(data[1]) and str(
                myresult_password[i][0]) == str(data[2]):
            bool_to_pass = True
        if str(myresult_password[i][0]) == data[1]:
            bool_to_pass_to_password = True
        if str(myresult_username[i][0]) == data[2]:
            bool_to_pass_to_username = True
    if bool_to_pass:
        return "True"
    elif not bool_to_pass_to_password and not bool_to_pass_to_username:
        return "False"
    return False


def update_admin(is_admin):
    sql = "DELETE FROM save_table"
    mycursor.execute(sql)
    mydb.commit()
    sql = "INSERT INTO save_table (is_admin) VALUES (%s)"
    mycursor.execute(sql, (is_admin,))
    mydb.commit()


def db(the_name_of_the_table):
    #  הפונקציה לוקחת את כל הנתונים מה database
    mycursor.execute("SELECT * FROM " + the_name_of_the_table)
    my_results = mycursor.fetchall()
    my_final_result = []
    for result in my_results:
        my_final_result.append(list(result))
    return my_final_result


def check_which_item_this_is(the_name_of_the_table, item):
    items = db(the_name_of_the_table)
    for item_of_table in items:
        if the_name_of_the_table != "circulations_table":
            if item_of_table[1] == item:
                return item_of_table
        else:
            if item_of_table[1] == item:
                return item_of_table
    return None


# def check_items_from_exel(exel_list, the_name_of_the_table):
#     item_list = db(the_name_of_the_table)
#     for exel in exel_list:
#         bool_i = True
#         # בודק אם יש כבר את האיש שהוא כותב אם יש אז התוכנה לא מוסיפה איש חדש
#         for item in item_list:
#             if the_name_of_the_table == "teachers_table" or "practitioners_table" or "pupils_table":
#                 if item[1] == exel[1] and item[0] == exel[0] and item[2] == \
#                         exel[2]:
#                     bool_i = False
#             elif the_name_of_the_table == "password_table":
#                 if item[1] == exel[1] and item[0] == exel[0]:
#                     bool_i = False
#             else:
#                 if item[1] == exel[1]:
#                     bool_i = False
#         #  מוסיף את הdata לשולחן הנכון
#         if bool_i:
#             if the_name_of_the_table == "pupils_table":
#                 item_list = add_item(the_name_of_the_table, [exel[0], exel[1],
#                                                              exel[2]])
#             elif the_name_of_the_table == "teachers_table" or "practitioners_table" or "password_table":
#                 item_list = add_item(the_name_of_the_table, [exel[0], exel[1]])
#             else:
#                 item_list = add_item(the_name_of_the_table, [exel[0]])
#     return item_list


def get_max_column_of_the_table(the_name_of_the_table):
    highest = db(the_name_of_the_table)
    return int(highest[-1][0]) + 1


def add_teacher_to_pupil(teacher, pupil):
    remove_item("pupils_table", str(pupil[1]))
    if teacher[1].isnumeric():
        pupil[3] = teacher[1]
    else:
        pupil[3] = teacher[0]

    add_item("pupils_table", pupil)


def add_item(the_name_of_the_table, items_to_add):
    i = []
    the_list_of_the_data = db(the_name_of_the_table)
    if the_name_of_the_table == "password_table":
        sql = "INSERT INTO password_table (username,password,is_admin)VALUES(%s,%s,%s)"
        items_to_add.append("no")
    elif the_name_of_the_table == "circulations_table":
        sql = "INSERT INTO circulations_table (the_number_of_circulation,circulation) VALUES (%s,%s)"
    elif the_name_of_the_table == "pupils_table":
        sql = "INSERT INTO " + the_name_of_the_table + "(name,last_name,id,phone_number," \
                                                       "circulation,teacher)VALUES(%s,%s,%s,%s,%s,%s)"

    else:
        sql = "INSERT INTO " + the_name_of_the_table + "(name,last_name,id,phone_number)VALUES(%s,%s,%s,%s)"

    for item in items_to_add:
        i.append(str(item))
    the_list_of_the_data.append(i)
    mycursor.execute(sql, i)
    mydb.commit()
    return the_list_of_the_data


def add_items(the_name_of_the_table, items_to_add):
    if the_name_of_the_table == PASSWORD_TABLE:
        sql = "INSERT INTO password_table (username,password,is_admin)VALUES(%s,%s,%s)"
    elif the_name_of_the_table == CIRCULATIONS_TABLE:
        sql = "INSERT INTO circulations_table (the_number_of_circulation,circulation) VALUES (%s,%s)"
    elif the_name_of_the_table == PUPILS_TABLE:
        sql = "INSERT INTO " + the_name_of_the_table + "(name,last_name,id,phone_number," \
                                                       "circulation,teacher)VALUES(%s,%s,%s,%s,%s,%s)"

    else:
        sql = "INSERT INTO " + the_name_of_the_table + "(name,last_name,id,phone_number)VALUES(%s,%s,%s,%s)"
    mycursor.executemany(sql, items_to_add)
    mydb.commit()


# server_program


try:
    print("The server is running.....")
    while True:
        # get the hostname
        host = "localhost"
        port = 5050  # initiate port no above 1024

        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen()
        conn, address = server_socket.accept()  # accept new connection

        while True:
            exel_list = []
            items = []
            data1 = conn.recv(256 * 1024)
            if not data1:
                # if data is not received break
                break
            data = json.loads(data1.decode('utf-8'))

            the_name_of_the_function_to_execute = data[0]

            if the_name_of_the_function_to_execute == "chek_password_form_table":
                d = check_password()
            elif the_name_of_the_function_to_execute == "update_admin":
                d = update_admin(data[1])
            elif the_name_of_the_function_to_execute == "get_a_table":
                d = db(data[1])
            # elif the_name_of_the_function_to_execute == "add_exel":
            #     d = check_items_from_exel(data[1], data[2])
            elif the_name_of_the_function_to_execute == "add_item":
                d = add_item(data[1], data[2])
            elif the_name_of_the_function_to_execute == "pupils_in_teachers":
                d = pupils_in_teachers()
            elif the_name_of_the_function_to_execute == "remove_item":
                d = remove_item(data[1], data[2])
            elif the_name_of_the_function_to_execute == "add_teacher_to_pupil":
                d = add_teacher_to_pupil(data[1], data[2])
            elif the_name_of_the_function_to_execute == "check_which_item_this_is":
                d = check_which_item_this_is(data[1], data[2])
            elif the_name_of_the_function_to_execute == \
                    "get_max_column_of_the_table":
                d = get_max_column_of_the_table(data[1])
            else:
                d = ""
            if d != "":
                d = json.dumps(d)
                l_bytes = d.encode('utf-8')
                conn.send(l_bytes)


except Exception as e:
    print(e)
    print(traceback.format_exc())

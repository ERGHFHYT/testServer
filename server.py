import json
import socket
import os
import psycopg2
conct = "postgresql://gorgi:jZ2m-q_ieFujsuFc1trhpQ@free-tier13.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dready-pelican-3752"
mydb = psycopg2.connect(conct)
mycursor = mydb.cursor()

def remove_item(the_name_of_the_table, typed):
    the_list_of_the_data = db(the_name_of_the_table)
    #בודק לפי מה שהמשתמש כתב מה הכי קרוב להיות מה שהוא רוצה למחוק
    for single_data_from_the_list in the_list_of_the_data:
        if single_data_from_the_list[1] in typed:
            the_list_of_the_data.remove(single_data_from_the_list)
            sql = "DELETE FROM "+the_name_of_the_table
            mycursor.execute(sql)
            mydb.commit()
    for data in the_list_of_the_data:
        add_item(the_name_of_the_table, data)
    return the_list_of_the_data


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
        if str(myresult_username[i][0]) == data[2] and str(myresult_password[i][0]) == str(data[1]):
            bool_to_pass = True
        if str(myresult_password[i][0]) == str(data[1]):
            bool_to_pass_to_password = True
        if str(myresult_username[i][0]) == data[2]:
            bool_to_pass_to_username = True

    if bool_to_pass:
        return "True"
    if not bool_to_pass_to_password and bool_to_pass_to_username:
        return "password_error"
    if bool_to_pass_to_password and not bool_to_pass_to_username:
        return "username_error"
    if bool_to_pass_to_password and bool_to_pass_to_username:
        return "username_error_and_password_error"

    return False


def db(name):
    #  הפונקציה לוקחת את כל הנתונים מהdatabase
    mycursor.execute("SELECT * FROM " + name)
    myresults = mycursor.fetchall()
    my_final_result = []
    for result in myresults:
        my_final_result.append(list(result))
    print(my_final_result)
    return my_final_result

def check_which_item_this_is(item,the_name_of_the_table):
    items = db(the_name_of_the_table)
    for item_of_table in items:
        if item_of_table[1] in item:
            return item_of_table
    return None



def check_items_from_exel(exel_list, the_name_of_the_table):
    item_list = db(the_name_of_the_table)
    for exel in exel_list:
        bool_i = True
        # בודק אם יש כבר את האיש שהוא כותב אם יש אז התוכנה לא מוסיפה איש חדש
        for item in item_list:
            if the_name_of_the_table == "teachers_table" or "practitioners_table" or "pupils_table":
                if item[1] == exel[1] and item[0] == exel[0] and item[2] == exel[2]:
                    bool_i = False
            else:
                if item[1] == exel[1] and item[0] == exel[0]:
                    bool_i = False
        #  מוסיף את הdata לשולחן הנכון
        if bool_i:
            if the_name_of_the_table == "teachers_table" or "practitioners_table" or "pupils_table":
                item_list = add_item(the_name_of_the_table, [exel[0], exel[1],
                                                        exel[2]])
            else:
                item_list = add_item(the_name_of_the_table, [exel[0], exel[1]])
    return item_list


def add_item(the_name_of_the_table, items_to_add):
    the_list_of_the_data = db(the_name_of_the_table)
    if the_name_of_the_table == "password_table":
        i = [str(items_to_add[0]), str(items_to_add[1])]
        sql = "INSERT INTO password_table (username,password)VALUES(%s,%s)"

    else:
        i = [str(items_to_add[0]), str(items_to_add[1]), str(items_to_add[2])]
        sql = "INSERT INTO " + the_name_of_the_table + "(name,ID," \
                                                   "circulation)VALUES(%s,%s,%s)"
    the_list_of_the_data.append(i)
    mycursor.execute(sql, i)
    mydb.commit()
    return the_list_of_the_data

#server_program


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
        data = conn.recv(256*1024)
        print(data)
        if not data:
            # if data is not received break
            break
        data = json.loads(data.decode('utf-8'))
        the_name_of_the_function_to_execute = data[0]
        print(the_name_of_the_function_to_execute)
        if the_name_of_the_function_to_execute == "chek":
            d = check_password()
        elif the_name_of_the_function_to_execute == "human":
            d = db(data[1])
        elif the_name_of_the_function_to_execute == "add_exel":
            d = check_items_from_exel(data[1], data[2])
        elif the_name_of_the_function_to_execute == "add_item":
            d = add_item(data[1], data[2])

        elif the_name_of_the_function_to_execute == "remove_item":
            d = remove_item(data[1], data[2])
        elif the_name_of_the_function_to_execute == "check_which_item_this_is":
            d = check_which_item_this_is(data[1], data[2])
        else:
            d = ""
        d = json.dumps(d)
        l_bytes = d.encode('utf-8')
        conn.send(l_bytes)

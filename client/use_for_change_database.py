# from tkinter import ttk
#
# import customtkinter
# from constants import *
#
#
# conct = "postgresql://gorgi:jZ2m-q_ieFujsuFc1trhpQ@free-tier13.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dready-pelican-3752"
# import psycopg2
# mydb = psycopg2.connect(conct)
# mycursor = mydb.cursor()
#
# #
# #sql = "DROP TABLE teachers_table"
# #mycursor.execute(sql)
# #mycursor.execute("CREATE TABLE teachers_table (name "
#   #               "VARCHAR(100), id VARCHAR(10))")
# sql = "INSERT INTO pupils_table (name,id,circulation,teacher) VALUES (%s,%s,%s,%s)"
# val = ("dftrhr", "225434652", "a", "08765121")
# mycursor.execute(sql, val)
#
# mydb.commit()

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

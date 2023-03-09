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
def isEnglish(string):
    for s in string:
        if s.isascii():
            return True
    return False


def change_the_order_by_language(items_to_add):
    if not items_to_add:
        return False
    if isEnglish(items_to_add[0]):
        items_to_add.remove(items_to_add[0])
        return True
    items_to_add.remove(items_to_add[0])
    return False or change_the_order_by_language(items_to_add)

print(change_the_order_by_language(["46456346","fgdfgכעעג",]))







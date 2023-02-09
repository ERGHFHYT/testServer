from tkinter import ttk

import customtkinter
from constants import *


conct = "postgresql://gorgi:jZ2m-q_ieFujsuFc1trhpQ@free-tier13.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dready-pelican-3752"
import psycopg2
mydb = psycopg2.connect(conct)
mycursor = mydb.cursor()

#
# #sql = "DROP TABLE teachers_table"
# #mycursor.execute(sql)
# #mycursor.execute("CREATE TABLE teachers_table (name "
#   #               "VARCHAR(100), id VARCHAR(10))")
# sql = "INSERT INTO pupils_table (name,id,circulation,teacher) VALUES (%s,%s,%s,%s)"
# val = ("ads", "215464567", "א", "1213456789")
# mycursor.execute(sql,val)
#
# mydb.commit()
# app = customtkinter.CTk()
#
#
# def check(event):
#     print("dfgd")
#     typed = box.get()
#     list_data = ["option 1", "option 2"]
#     if typed == '':
#         data = list_data
#     else:
#         data = []
#         for item in list_data:
#             if typed.lower() in item.lower():
#                 data.append(item)
#     box["values"] = data
# def combobox_callback(choice):
#     print("sdfsd")
#     box["values"] = ["gg"]
# box = ttk.Combobox(master=app,
#                                      values=["option 1", "option 2"])
# box.pack(padx=20, pady=10)
#
#
# app.option_add('*TCombobox*Listbox.font', 14)
# box.bind("<KeyRelease>", check)
#
# app.mainloop()
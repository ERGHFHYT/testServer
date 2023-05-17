# from tkinter import ttk
#
# import customtkinter
# from constants import *
#
#
conct = "postgresql://gorgi:jZ2m-q_ieFujsuFc1trhpQ@free-tier13.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dready-pelican-3752"
import psycopg2

mydb = psycopg2.connect(conct)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM save_table;")

myresult = mycursor.fetchall()
print("  ")
for x in myresult:
   print("                                   ", x)
# #
# # #
# # sql = "DROP TABLE password_table"
# # mycursor.execute(sql)
# # mycursor.execute("CREATE TABLE save_table (is_admin "
# #                 "VARCHAR(100))")
# sql = "DELETE FROM password_table"
# mycursor.execute(sql)
# mydb.commit()
# sql = "INSERT INTO password_table (username,password,is_admin)VALUES(%s,%s,%s)"
# mycursor.execute(sql, ("ינון", "1234567890", "yes"))
# mydb.commit()

# #
# sql = "DELETE FROM password_table"
# mycursor.execute(sql)
# mydb.commit()

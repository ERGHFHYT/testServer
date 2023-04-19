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
# #
# # #
# # sql = "DROP TABLE password_table"
# # mycursor.execute(sql)
# # mycursor.execute("CREATE TABLE save_table (is_admin "
# #                 "VARCHAR(100))")
sql = "INSERT INTO save_table (is_admin) VALUES (%s)"
mycursor.execute(sql, ("yes",))
mydb.commit()

# #
# sql = "DELETE FROM password_table"
# mycursor.execute(sql)
# mydb.commit()

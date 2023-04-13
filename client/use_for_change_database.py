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
# # Import the required libraries
# from tkinter import *
# from tkinter import ttk
#
# # Create an instance of tkinter frame
# win = Tk()
#
# # Set the size of the tkinter window
# win.geometry("700x350")
# s = ttk.Style()
# s.theme_use('clam')
#
#
# # Define a function to clear all the items present in Treeview
# def clear_all():
#     for item in tree.get_children():
#         tree.delete(item)
# def add():
#     tree.column("# 1", anchor=CENTER)
#     tree.heading("# 1", text="ff")
#
#
# # Add a Treeview widget
# tree = ttk.Treeview(win, column=("c1", "c2", "c3"), show='headings', height=6)
# tree.column("# 1", anchor=CENTER)
# tree.heading("# 1", text="ID")
# tree.column("# 2", anchor=CENTER)
# tree.heading("# 2", text="FName")
#
# # Insert the data in Treeview widget
# tree.insert('', 'end', text="1", values=('1', 'Honda'))
# tree.insert('', 'end', text="2", values=('2', 'Hyundai'))
# tree.insert('', 'end', text="3", values=('3', 'Tesla'))
# tree.insert('', 'end', text="4", values=('4', 'Volkswagen'))
# tree.insert('', 'end', text="5", values=('5', 'Tata'))
# tree.insert('', 'end', text="6", values=('6', 'Renault'))
#
#
# tree.pack()
#
# # Create a Button for clearing the Treeview Item
# ttk.Button(win, text="Clear", command=clear_all).pack(pady=10)
# ttk.Button(win, text="add", command=add).pack(pady=5)
# win.mainloop()
p = ['שאולשבילי', 'נדיר', '225434652', '08765121', 'ח', '5734685366']


from constants import *
import tkinter
import customtkinter
import client.client_classes_folder.Base
from tkinter import ttk
import tkinter.messagebox

teachers_data = client.client_classes_folder.Base.Base.execution_server([
    GET_TABLE, TEACHERS_TABLE])
pupils_data = client.client_classes_folder.Base.Base.execution_server(
    [GET_TABLE, PUPILS_TABLE])
d = client.client_classes_folder.Base.Base.execution_server(
    ["pupils_in_teachers"])


def search():
    def event(event):
        finel_list = []
        data = client.client_classes_folder.Base.Base.execution_server(
            ["pupils_in_teachers"])
        for d in data:
            if d[3] in box_3.get():
                finel_list.append(d)
        box_4["values"] = finel_list

    def add_teacher_to_pupil():
        data = client.client_classes_folder.Base.Base.execution_server(
            ["check_which_item_this_is",
             "teachers_table", box_2.get()])
        client.client_classes_folder.Base.Base.execution_server(
            ["pupils_in_teachers", box_1.get(),
             (TEACHERS_TABLE, data)])

    def remove_teacher_to_pupil():
        client.client_classes_folder.Base.Base.execution_server(
            ["pupils_in_teachers", box_1.get(), "ריק"])

    root = customtkinter.CTk()
    tool = client.client_classes_folder.Base.Base(root, "מסך חיפוש תלמידים "
                                                        "לפי מורים",
                                                  "Dark",
                                                  "blue", None, None)
    tool.window()
    root.frame_1 = customtkinter.CTkFrame(master=root,
                                          corner_radius=0,
                                          height=550, width=650)
    root.frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_1 = customtkinter.CTkFrame(master=root.frame_1, height=550,
                                     width=650)
    label_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    box_1 = ttk.Combobox(root.frame_1, width=28, font=("Halvetica", 20),
                         values=teachers_data, justify='right')
    box_1.place(relx=0.2, rely=0.1)
    box_2 = ttk.Combobox(root.frame_1, width=28, font=("Halvetica", 20),
                         values=pupils_data, justify='right')
    box_2.place(relx=0.2, rely=0.2)
    box_3 = ttk.Combobox(root.frame_1, width=28, font=("Halvetica", 20),
                         values=teachers_data, justify='right')
    box_3.place(relx=0.2, rely=0.6)
    box_4 = ttk.Combobox(root, width=28, font=("Halvetica", 20),
                         values=d, justify='right')
    box_4.place(relx=0.28, rely=0.7)
    box_3.bind("<<ComboboxSelected>>", event)
    root.button_2 = customtkinter.CTkButton(master=root.frame_1, text="הוספה",

                                            corner_radius=6,
                                            command=add_teacher_to_pupil,
                                            width=150)
    root.button_2.place(relx=0.7, rely=0.33, anchor=tkinter.CENTER)
    root.button_3 = customtkinter.CTkButton(master=root.frame_1, text="מחיקה"
                                            ,

                                            corner_radius=6,
                                            command=remove_teacher_to_pupil,
                                            width=150)
    root.button_3.place(relx=0.4, rely=0.33, anchor=tkinter.CENTER)
    root.label_1 = customtkinter.CTkLabel(master=root.frame_1, width=75,
                                          height=40,
                                          fg_color="#343638",
                                          corner_radius=0,
                                          bg_color="#343638",
                                          text="שינוים",
                                          text_font=(DEFAULT_FONT, -20))
    root.label_1.place(relx=0.53, rely=0.05, anchor=tkinter.CENTER)
    root.label_2 = customtkinter.CTkLabel(master=root.frame_1, width=75,
                                          height=40,
                                          fg_color="#343638",
                                          corner_radius=0,
                                          bg_color="#343638",
                                          text="חיפוש",
                                          text_font=(DEFAULT_FONT, -20))
    root.label_2.place(relx=0.53, rely=0.55, anchor=tkinter.CENTER)
    root.mainloop()

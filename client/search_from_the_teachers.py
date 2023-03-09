from constants import *
import tkinter
import customtkinter
import client.client_classes_folder.Base
from tkinter import ttk
import tkinter.messagebox
from client.new_window import main_window


def search():
    def event(event):
        finel_list = []
        for pupil in pupils_in_teachers_data:
            print(pupil)
            print(search_box_teachers.get())
            if pupil[3] in search_box_teachers.get():
                finel_list.append(pupil)
        search_box_pupils["values"] = finel_list

    def add_teacher_to_pupil():
        the_teacher_to_add = client.client_classes_folder.Base.Base.execution_server(
            ["check_which_item_this_is",
             "teachers_table", update_box_teachers.get()])
        the_pupil_to_add = client.client_classes_folder.Base.Base.execution_server(
            ["check_which_item_this_is",
             "pupils_table", update_box_pupils.get()])

        client.client_classes_folder.Base.Base.execution_server(
            ["add_teacher_to_pupil", the_teacher_to_add,
             the_pupil_to_add])

        search_box_teachers["values"] = client.client_classes_folder.Base.Base.execution_server(
            ["pupils_in_teachers"])

    def remove_teacher_to_pupil():
        the_pupil_to_remove = client.client_classes_folder.Base.Base.execution_server(
            ["check_which_item_this_is",
             "teachers_table", update_box_teachers.get()])
        client.client_classes_folder.Base.Base.execution_server(
            ["add_teacher_to_pupil", the_pupil_to_remove, "ריק"])
        search_box_teachers["values"] = client.client_classes_folder.Base.Base.execution_server(
            ["pupils_in_teachers"])

    root = customtkinter.CTk()
    tool = client.client_classes_folder.Base.Base(root, "מסך חיפוש תלמידים "
                                                        "לפי מורים",
                                                  "Dark",
                                                  "blue", None, None)

    def go_back():
        root.destroy()
        client.new_window.main_window()

    teachers_data = client.client_classes_folder.Base.Base.execution_server([
        GET_TABLE, TEACHERS_TABLE])
    pupils_data = client.client_classes_folder.Base.Base.execution_server(
        [GET_TABLE, PUPILS_TABLE])
    pupils_in_teachers_data = client.client_classes_folder.Base.Base.execution_server(
        ["pupils_in_teachers"])
    tool.window()
    root.frame_1 = customtkinter.CTkFrame(master=root,
                                          corner_radius=0,
                                          height=550, width=650)
    root.frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_1 = customtkinter.CTkFrame(master=root.frame_1, height=550,
                                     width=650)
    label_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    update_box_teachers = ttk.Combobox(root.frame_1, width=28, font=("Halvetica", 20),
                                 values=teachers_data, justify='right')
    update_box_teachers.place(relx=0.2, rely=0.1)
    update_box_pupils = ttk.Combobox(root.frame_1, width=28, font=("Halvetica", 20),
                                values=pupils_data, justify='right')
    update_box_pupils.place(relx=0.2, rely=0.2)
    search_box_teachers = ttk.Combobox(root.frame_1, width=28, font=("Halvetica", 20),
                                 values=teachers_data, justify='right')
    search_box_teachers.place(relx=0.2, rely=0.6)
    search_box_pupils = ttk.Combobox(root, width=28, font=("Halvetica", 20),
                                values=pupils_in_teachers_data, justify='right')
    search_box_pupils.place(relx=0.28, rely=0.7)
    search_box_teachers.bind("<<ComboboxSelected>>", event)
    root.button_2 = customtkinter.CTkButton(master=root.frame_1, text="הוספה",

                                            corner_radius=0,
                                            command=add_teacher_to_pupil,
                                            width=150)
    root.button_2.place(relx=0.62, rely=0.33, anchor=tkinter.CENTER)
    root.button_3 = customtkinter.CTkButton(master=root.frame_1, text="מחיקה"
                                            ,

                                            corner_radius=0,
                                            command=remove_teacher_to_pupil,
                                            width=150)
    root.button_3.place(relx=0.32, rely=0.33, anchor=tkinter.CENTER)
    root.label_1 = customtkinter.CTkLabel(master=root.frame_1, width=75,
                                          height=40,
                                          fg_color="#333333",
                                          corner_radius=0,
                                          bg_color="#333333",
                                          text="שינוים",
                                          font=(DEFAULT_FONT, -20))
    root.label_1.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
    root.label_2 = customtkinter.CTkLabel(master=root.frame_1, width=75,
                                          height=40,
                                          fg_color="#333333",
                                          corner_radius=0,
                                          bg_color="#333333",
                                          text="חיפוש",
                                          font=(DEFAULT_FONT, -20))
    root.label_2.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    root.button_3 = customtkinter.CTkButton(master=root.frame_1,
                                            text="חזור",
                                            corner_radius=0,
                                            command=go_back,
                                            width=100)
    root.button_3.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    root.mainloop()

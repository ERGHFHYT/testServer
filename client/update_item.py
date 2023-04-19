from constants import *
import customtkinter
from tkinter import ttk
import client.client_classes_folder.Custom_window
import client.client_classes_folder.Base


def update(data_entry, the_name_of_the_table):
    if the_name_of_the_table == PASSWORD_TABLE:
        root_2 = customtkinter.CTk()
        tool = client.client_classes_folder.Custom_window.Custom_window(root_2,
                                                                        "בלבש סיסמה",
                                                                        "System",
                                                                        "green",
                                                                        "password_table",
                                                                        "#1f6aa5",
                                                                        data_entry)
        tool.start(["שם משתמש", "סיסמה"])
        tool.big_title_to_add(120, 60)
    else:
        root_2 = customtkinter.CTk()
        tool = client.client_classes_folder.Custom_window.Custom_window(root_2,
                                                                        "בלבש אנשים",
                                                                        "System",
                                                                        "blue",
                                                                        the_name_of_the_table,
                                                                        (
                                                                            "gray84",
                                                                            "gray25"),
                                                                        data_entry)
        if the_name_of_the_table == CIRCULATIONS_TABLE:
            tool.start(["מחזור"])
        elif the_name_of_the_table == PUPILS_TABLE:
            tool.start(["שם", "שם משפחה", "תעודת זהות", "מספר טלפון", "תעודת זהות מורה"])

        else:
            tool.start(["שם", "שם משפחה", "תעודת זהות", "מספר טלפון"])
        if the_name_of_the_table == PUPILS_TABLE:
            list_data = client.client_classes_folder.Custom_window. \
                Custom_window.execution_server([GET_TABLE,
                                                "circulations_table"])
            list_d = []
            for l in list_data:
                list_d.append(l[1])
                list_data = list_d
            label_1 = customtkinter.CTkLabel(root_2,
                                             text="מחזור", fg_color=("gray84", "gray25"),
                                             font=("Halvetica", -20))
            label_1.place(relx=0.36, rely=0.48)
            box = ttk.Combobox(root_2, width=12,
                               font=("Halvetica", 20),
                               values=list_data, justify='right')
            box.place(relx=0.3, rely=0.55)
            box.bind("<KeyRelease>", tool.check_for_update_puples)
            print("data entry", len(data_entry))
            if data_entry != EMPTY_SPACE:
                box.set(data_entry[4])
            tool.box = box
        if the_name_of_the_table == CIRCULATIONS_TABLE:
            tool.big_title_to_add(100, 50, "מחזור")
        elif the_name_of_the_table == PUPILS_TABLE:
            tool.big_title_to_add(100, 50, "תלמיד")
        elif the_name_of_the_table == PASSWORD_TABLE:
            tool.big_title_to_add(100, 50, "סיסמה")
        elif the_name_of_the_table == PRACTITIONERS_TABLE:
            tool.big_title_to_add(100, 50, "מתרגל")
        else:
            tool.big_title_to_add(100, 50, "מורה")
        tool.add_colors()
    tool.the_location = root_2
    tool.label = tool.create_masages(200, 80,
                                     BACKGROUND_COLOR_OF_CUSTOM_WINDOWS, "",
                                     0.5, 0.7, -16)
    root_2.mainloop()

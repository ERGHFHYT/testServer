import customtkinter
import classes


def update(data_entry, the_name_of_the_table):
    if the_name_of_the_table == "password_table":
        root_2 = customtkinter.CTk()
        tool = classes.custom_window(root_2, "בלבש סיסמה",
                                     "System", "green", "password_table",
                                     ("#1f6aa5"), "", "")
        data_entry = tool.sever_db(["check_which_item_this_is", data_entry,
                                    the_name_of_the_table])
        tool.start(["שם משתמש", "סיסמה"], data_entry)
        tool.big_title_to_add(120, 60)
    else:
        root_2 = customtkinter.CTk()
        tool = classes.custom_window(root_2, "בלבש אנשים",
                                     "System",  "blue", the_name_of_the_table,
                                     ("gray84", "gray25"), "", "")
        data_entry = tool.sever_db(["check_which_item_this_is", data_entry,
                                    the_name_of_the_table])
        tool.start(["שם", "מספר טלפון", "מחזור"], data_entry)
        tool.big_title_to_add(100, 50)
        tool.add_colors()
    tool.the_location = root_2
    tool.label = tool.create_masages(220, 80, "#343638", "", 0.5, 0.7, -16)
    root_2.mainloop()
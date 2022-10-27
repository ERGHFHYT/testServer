import customtkinter

import classes


def update_pass(data_entry):
    root_2 = customtkinter.CTk()
    tool = classes.custom_window(root_2, "בלבש סיסמה",
                                 "System",  "green", "password_table",
                                 ("#1f6aa5"))
    tool.start(["שם משתמש", "סיסמה"], data_entry,the_tables_data)
    tool.big_title_to_add(120, 60)
    root_2.mainloop()
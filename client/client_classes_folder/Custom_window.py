import tkinter

import customtkinter

import client.new_window
from client.client_classes_folder.Base import Base
from client.constants import *


class Custom_window(Base):
    def __init__(self, root, windows_name, appearance_mode,
                 default_color_theme, the_name_of_the_table, color_object,
                 data_entry,
                 label=None, the_location=None, box=None, entrys=None):
        super().__init__(root, windows_name, appearance_mode,
                         default_color_theme, label, the_location)
        self.root = root
        self.color_object = color_object
        self.windows_name = windows_name
        self.appearance_mode = appearance_mode
        self.default_color_theme = default_color_theme
        self.the_name_of_the_table = the_name_of_the_table
        self.label = label
        self.box = box
        self.the_location = the_location
        self.entrys = entrys
        self.data_entry = data_entry

        tool = Base(root, windows_name, appearance_mode, default_color_theme,
                    label, the_location)
        tool.window()

    def add_item(self):
        print(self.data_entry)
        no_duplicates = True
        if self.data_entry == EMPTY_SPACE:
            data = Base.execution_server([GET_TABLE, self.the_name_of_the_table])
            for i in data:
                if self.the_name_of_the_table == CIRCULATIONS_TABLE:
                    if i[0] == self.entrys[0].get():
                        no_duplicates = False
                elif self.the_name_of_the_table == PUPILS_TABLE:
                    if i[1] == self.entrys[2].get():
                        no_duplicates = False
                else:
                    print(self.entrys[0].get())
                    print(i[0])
                    if i[0] == self.entrys[2].get():
                        no_duplicates = False
        print(no_duplicates)
        if no_duplicates:
            if self.the_name_of_the_table == PASSWORD_TABLE:
                data = ["add_item", self.the_name_of_the_table,
                        [self.entrys[0].get(), self.entrys[1].get()]]
                Base.execution_server(data)
                self.label.configure(text="!קלט הוכנס בהצלחה")
                if self.data_entry != EMPTY_SPACE:
                    Base.execution_server([REMOVE_ITEM_FROM_TABLE,
                                           self.the_name_of_the_table, self.data_entry])
            elif self.the_name_of_the_table == CIRCULATIONS_TABLE:
                max_column = Base.execution_server(
                    [GET_MAX, self.the_name_of_the_table,
                     "the_number_of_circulation"])
                data = ["add_item", self.the_name_of_the_table,
                        [max_column, self.entrys[0].get()]]
                Base.execution_server(data)
                self.label.configure(text="!קלט הוכנס בהצלחה")
                if self.data_entry != EMPTY_SPACE:
                    Base.execution_server([REMOVE_ITEM_FROM_TABLE,
                                           self.the_name_of_the_table, self.data_entry])
            else:
                entry_to_add = []
                for num in range(2):
                    print(self.entrys[num].get())
                    entry_to_add.append(self.entrys[num].get())
                if CheckID(str(self.entrys[2].get())):
                    entry_to_add.append(str(self.entrys[2].get()))
                    entry_to_add.append(str(self.entrys[3].get()))
                    if self.the_name_of_the_table == PUPILS_TABLE:
                        data_entry = Base.execution_server(
                            ["check_which_item_this_is",
                             CIRCULATIONS_TABLE, self.box.get()])
                        entry_to_add.append(str(data_entry[1]))
                        if self.data_entry == EMPTY_SPACE:
                            entry_to_add.append("ריק")
                        else:
                            entry_to_add.append(str(self.data_entry[-1]))
                        print(entry_to_add)
                        print(self.the_name_of_the_table)
                    print(entry_to_add)
                    data = ["add_item", self.the_name_of_the_table,
                            entry_to_add]
                    Base.execution_server(data)
                    self.label.configure(text="!קלט הוכנס בהצלחה")
                    if self.data_entry != EMPTY_SPACE:
                        Base.execution_server([REMOVE_ITEM_FROM_TABLE,
                                               self.the_name_of_the_table, self.data_entry])
                else:
                    self.label.configure(text="הכנסת קלט שהוא לא תקין")
                    self.entrys[1].configure(fg_color="#d35b58")
        else:
            self.label.configure(text="הנתונים שהכנסת כבר קיימים")
            self.entrys[0].configure(fg_color="#d35b58")
            self.entrys[1].configure(fg_color="#d35b58")
        self.root.after(4000, self.clear_entrys)
        self.root.after(4000, self.clear_label)

    def start(self, the_names_of_the_entrys):
        def go_back():
            self.root.destroy()
            client.new_window.main_window()

        self.root.frame_1 = customtkinter.CTkFrame(master=self.root,
                                                   corner_radius=0,
                                                   height=550, width=650)
        self.root.frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        label_1 = customtkinter.CTkFrame(master=self.root.frame_1, height=550,
                                         width=650)
        label_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        entrys = []
        num = 0.25
        for name in range(len(the_names_of_the_entrys)):
            entrys.append(0)
            entrys[name] = self.root.my_entry_2 = customtkinter.CTkEntry(
                master=self.root.frame_1, corner_radius=0, width=200,
                placeholder_text=the_names_of_the_entrys[name], font=(
                    "Halvetica", -20),
                justify='right')
            self.root.my_entry_2.place(relx=0.75, rely=num,
                                       anchor=tkinter.CENTER)
            num += 0.15
        print(len(entrys))
        self.entrys = entrys

        self.root.button_2 = customtkinter.CTkButton(master=self.root.frame_1,
                                                     text="עדכן",
                                                     corner_radius=0,
                                                     command=
                                                     self.add_item,
                                                     width=200)
        self.root.button_2.place(relx=0.7, rely=0.85, anchor=tkinter.CENTER)
        self.root.button_3 = customtkinter.CTkButton(master=self.root.frame_1,
                                                     text="חזור",
                                                     corner_radius=0,
                                                     command=go_back,
                                                     width=200)
        self.root.button_3.place(relx=0.3, rely=0.85, anchor=tkinter.CENTER)
        try:
            if self.data_entry is not None:
                num = 0
                for data in self.data_entry:
                    entrys[num].insert(0, str(data))
                    num += 1
        except Exception as e:
            print(e)

    def big_title_to_add(self, width, height):
        name = self.the_name_of_the_table.split("_")
        self.root.frame_1.label_1 = customtkinter.CTkLabel(
            master=self.root.frame_1,
            width=width,
            height=height,
            fg_color=self.color_object,
            corner_radius=0,
            text=name[0],
            font=("Halvetica", -16))
        self.root.frame_1.label_1.place(relx=0.5, rely=0.1,
                                        anchor=tkinter.CENTER)

    def clear_entrys(self):
        if self.the_name_of_the_table != CIRCULATIONS_TABLE:
            self.entrys[1].configure(fg_color="#343638")
        self.entrys[0].configure(fg_color="#343638")

    def check(self, event):
        typed = self.box.get()
        list_data = Base.execution_server(
            [GET_TABLE, self.the_name_of_the_table])
        if typed == '':
            data = list_data
        else:
            data = []
            for item in list_data:
                for i in item:
                    if typed.lower() in i.lower():
                        data.append(item)
        self.box["values"] = data

    def add_colors(self):
        lis = [[0, 0.03, 20, 1500], [0.05, 0.03, 1500, 20],
               [0.95, 0.03, 1500, 20]]
        for i in range(len(lis)):
            self.root.frame_1.label_1 = customtkinter.CTkLabel(
                master=self.root.frame_1,
                width=lis[i][3],
                height=lis[i][2],
                corner_radius=0, text=EMPTY_SPACE,
                fg_color=self.color_object,
                font=("Halvetica", -16))
            self.root.frame_1.label_1.place(relx=lis[i][0], rely=lis[i][1],
                                            anchor=tkinter.CENTER)

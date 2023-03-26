from client.constants import *
import customtkinter
from client.client_classes_folder.Base import Base

from tkinter import filedialog as fd, ttk
from openpyxl import load_workbook
import pynput
import speech_recognition
from client import search_from_the_teachers, update_item


class New_wind(Base):
    def __init__(self, root, windows_name, appearance_mode,
                 default_color_theme, label,
                 the_location):
        super().__init__(root, windows_name, appearance_mode,
                         default_color_theme, label, the_location)
        self.the_name_of_the_table = TEACHERS_TABLE
        self.box = None
        self.root = root
        self.windows_name = windows_name
        self.appearance_mode = appearance_mode
        self.default_color_theme = default_color_theme
        self.list_of_buttons = None
        self.label = None
        self.label_2 = None
        self.label_3 = None
        self.the_location = None

    def change_the_screen_following_the_table(self, name_for_the_test,
                                              the_number_of_the_button,
                                              the_name_of_the_table):
        self.label_2.configure(text=EMPTY_SPACE)
        self.label_3.configure(text=EMPTY_SPACE)
        self.box.set(EMPTY_SPACE)
        self.the_name_of_the_table = the_name_of_the_table
        self.root.label_1.destroy()
        self.root.label_1 = customtkinter.CTkLabel(master=self.root.frame_right,
                                                   text=name_for_the_test,
                                                   font=(DEFAULT_FONT,
                                                         -25))
        self.root.label_1.place(relx=0.8, rely=0.03)
        for i in range(5):
            if i == the_number_of_the_button:
                self.list_of_buttons[i].configure(fg_color=BACKGROUND_COLOR)
            else:
                self.list_of_buttons[i].configure(fg_color=RED)
        list_data = Base.execution_server([GET_TABLE, the_name_of_the_table])
        if the_name_of_the_table == CIRCULATIONS_TABLE:
            list_d = []
            for l in list_data:
                list_d.append(l[1])
            self.box["values"] = tuple(list_d)
        else:
            self.box["values"] = tuple(list_data)

    def window_search_from_the_teachers(self):
        self.root.destroy()
        search_from_the_teachers.search()

    def button_pupils(self):
        New_wind.change_the_screen_following_the_table(self, "תלמידים", 1,
                                                       PUPILS_TABLE)

    def button_teacher(self):
        New_wind.change_the_screen_following_the_table(self, "מורים", 0,
                                                       TEACHERS_TABLE)

    def button_circulations(self):
        New_wind.change_the_screen_following_the_table(self, "מחזורים", 4,
                                                       "circulations_table")

    def button_password(self):
        New_wind.change_the_screen_following_the_table(self, "סיסמה", 3,
                                                       "password_table")

    def button_Practitioners(self):
        New_wind.change_the_screen_following_the_table(self, "מתרגלים", 2,
                                                       "practitioners_table")

    def remove_item(self):
        typed = self.box.get()
        Base.execution_server(
            [REMOVE_ITEM_FROM_TABLE, self.the_name_of_the_table,
             str(typed)])
        list_data = tuple(Base.execution_server([GET_TABLE,
                                                 self.the_name_of_the_table]))
        if self.the_name_of_the_table == CIRCULATIONS_TABLE:
            list_d = []
            for l in list_data:
                list_d.append(l[1])
            self.box["values"] = tuple(list_d)
        else:
            self.box["values"] = list_data
        self.box.set(EMPTY_SPACE)
        self.label_2.configure(text=EMPTY_SPACE)
        self.label_3.configure(text=EMPTY_SPACE)

    def update_single(self, the_execute):
        if the_execute == "chek":
            data = Base.execution_server(
                [GET_TABLE, self.the_name_of_the_table])
            global_entry = str(self.box.get())
            print("the global_entry ", global_entry)
            if global_entry != EMPTY_SPACE:
                for d in data:
                    if not self.the_name_of_the_table == CIRCULATIONS_TABLE:
                        if d[1] in global_entry:
                            global_entry = d
                            break
                    else:
                        if d[0] in global_entry:
                            global_entry = d
                            break
                self.root.destroy()
                update_item.update(global_entry,
                                   self.the_name_of_the_table)
            else:
                self.label.configure(text="לא בחרת איזה נתונים לעדכן")
                self.root.after(4000, self.clear_label)

        else:
            global_entry = EMPTY_SPACE
            self.root.destroy()
            update_item.update(global_entry, self.the_name_of_the_table)

    def catching_sound(self, typed):
        data = []
        list_data = Base.execution_server(
            [GET_TABLE, self.the_name_of_the_table])
        for item in list_data:
            if typed.lower() in item:
                data.append(item)
        self.box["values"] = data

    def excel(self):
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
        )
        try:
            print("----------")
            wb = load_workbook(filename)
            ws = wb.active
            A = ws["A"]
            print("A", A)
            if self.the_name_of_the_table in [PASSWORD_TABLE, PUPILS_TABLE,
                                              TEACHERS_TABLE,
                                              PRACTITIONERS_TABLE]:
                B = ws["B"]
            if self.the_name_of_the_table == PUPILS_TABLE:
                C = ws["C"]
                D = ws["D"]
            exel_list = []
            for current_row in range(len(A)):
                if A[current_row].value is None:
                    A[current_row].value = "ריק"
                if self.the_name_of_the_table == TEACHERS_TABLE or \
                        PUPILS_TABLE or PRACTITIONERS_TABLE or PASSWORD_TABLE:
                    if B[current_row].value is None:
                        B[current_row].value = "ריק"
                if self.the_name_of_the_table == PUPILS_TABLE:
                    if C[current_row].value is None:
                        C[current_row].value = "ריק"
                    if D[current_row].value is None:
                        D[current_row].value = "ריק"

            def add_item(item_list):
                for exel in exel_list:
                    bool_i = True
                    for P in item_list:
                        if P[1] == exel[1] and P[0] == exel[0] and P[2] == \
                                exel[2]:
                            bool_i = False
                    if bool_i:
                        item_list.append(exel)
                return item_list

            for current_row in range(len(A)):
                if self.the_name_of_the_table == PUPILS_TABLE:
                    row_to_add = [A[current_row].value,
                                  str(B[current_row].value),
                                  C[current_row].value, D[current_row].value]
                else:
                    row_to_add = [str(A[current_row].value),
                                  str(B[current_row].value)]
                exel_list.append(row_to_add)
            data_to_add = ["add_exel", exel_list, self.the_name_of_the_table]
            teachers = Base.execution_server(data_to_add)
            teachers = add_item(teachers)
            list_data = tuple(teachers)
            self.box = list_data
            self.label.configure(text="הקובץ שנתנת התווסף בהצלחה")
        except:
            self.label.configure(text="הקובץ שנתנת הוא לא קובץ אקסל")
        self.root.after(4000, self.clear_label)

    def clear_label(self):
        self.label.configure(text=EMPTY_SPACE)

    def voice(self):
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            try:

                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                mouse_listener = pynput.mouse.Listener(suppress=True)
                mouse_listener.start()
                audio = recognizer.listen(mic, phrase_time_limit=10)
                if audio != '':
                    self.box.set(str(recognizer.recognize_google(audio,
                                                                 language="he")))
                    self.catching_sound(str(recognizer.recognize_google(audio,
                                                                        language="he")))

            except:
                self.label = self.create_masages(220, 100, "#2a2d2e",
                                                 "לא הצליח לזהות קול", 0.15,
                                                 0.3, -16)
                self.root.after(4000, self.clear_label)
        mouse_listener.stop()

    def create_tree(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", backrground="D3D3D3",
                        forerground="black", rowheight=25,
                        fieldbackrground="D3D3D3")
        
        tree = ttk.Treeview(self.root, column=("c1", "c2"), show='headings',
                            height=6)

        tree.place(
            relx=0.5, rely=0.5)

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

# import json
# import socket
# import customtkinter
# import tkinter
# from tkinter import filedialog as fd
# from openpyxl import load_workbook
# import speech_recognition
#
# import update_item
# import pynput
#
#
# # from search_from_the_teachers import *
# import new_window
# from constants import *
#
#
# class Base:
#     def __init__(self, root, windows_name, appearance_mode,
#                  default_color_theme, label, the_location):
#         self.root = root
#         self.windows_name = windows_name
#         self.appearance_mode = appearance_mode
#         self.default_color_theme = default_color_theme
#         self.label = label
#         self.the_location = the_location
#
#     def window(self):
#         self.root.geometry(SIZE_OF_WINDOW)
#         self.root.title(self.windows_name)
#         self.root.resizable(True, True)
#         customtkinter.set_appearance_mode(
#             self.appearance_mode)
#         customtkinter.set_default_color_theme(
#             self.default_color_theme)
#
#     def create_masages(self, width, height, fg_color, text, x, y, text_size):
#         self.root.label = customtkinter.CTkLabel(
#             master=self.the_location,
#                                                 width=width,
#                                               height=height,
#                                               fg_color=fg_color,
#                                               corner_radius=0,
#                                               bg_color=("gray70",
#                                                         "gray25"), text=text,
#                                               text_font=(DEFAULT_FONT, text_size))
#         self.root.label.place(relx=x, rely=y, anchor=tkinter.CENTER)
#         return self.root.label
#     def change_the_text(self,text):
#         self.label.configure(text=text)
#         self.root.after(4000, self.clear_label)
#
#     def clear_label(self):
#         self.label.configure(text=EMPTY_SPACE)
#
#     @classmethod
#     def execution_server(self, message):
#         host = "localhost"  # as both code is running on same pc
#         port = 5050  # socket server port number
#         client_socket_1 = socket.socket()  # instantiate
#         client_socket_1.connect((host, port))  # connect to the server
#         message = json.dumps(message)
#         message = message.encode('utf-8')
#         client_socket_1.send(message)  # send message
#         data = client_socket_1.recv(256 * 1024).decode('utf-8')
#         data = json.loads(data)
#         if data:
#             client_socket_1.close()
#         return data
#
#
# class custom_window(Base):
#     def __init__(self, root, windows_name, appearance_mode,
#                  default_color_theme, the_name_of_the_table, color_object,
#                  label, the_location, box, entrys):
#         super().__init__(root, windows_name, appearance_mode,
#                          default_color_theme, label, the_location)
#         self.root = root
#         self.color_object = color_object
#         self.windows_name = windows_name
#         self.appearance_mode = appearance_mode
#         self.default_color_theme = default_color_theme
#         self.the_name_of_the_table = the_name_of_the_table
#         self.label = label
#         self.box = box
#         self.the_location = the_location
#         self.entrys = entrys
#
#         tool = Base(root, windows_name, appearance_mode, default_color_theme,
#                     label, the_location)
#         tool.window()
#
#     def add_item(self):
#         d = True
#         data = Base.execution_server([GET_TABLE, self.the_name_of_the_table])
#         for i in data:
#             if self.the_name_of_the_table == CIRCULATIONS_TABLE:
#                 if i[0] == self.entrys[0].get():
#                     d = False
#             else:
#                 if i[1] == self.entrys[1].get():
#                     d = False
#         print("נכנס להוספה")
#         if d:
#             if self.the_name_of_the_table == CIRCULATIONS_TABLE or \
#                     self.entrys[1].get().isnumeric() or \
#                     len(str(self.entrys[1].get())) == 10 \
#                     or not self.entrys[0].get().isnumeric():
#                 if self.the_name_of_the_table == CIRCULATIONS_TABLE or\
#                         self.entrys[ 1].get().isnumeric():
#                     if self.the_name_of_the_table == CIRCULATIONS_TABLE or len(
#                             str(self.entrys[1].get())) == 10:
#                         if not self.entrys[0].get().isnumeric():
#                             e = []
#                             if self.the_name_of_the_table == CIRCULATIONS_TABLE:
#                                 max_column = Base.execution_server(
#                                     [GET_MAX, self.the_name_of_the_table,
#                                      "the_number_of_circulation"])
#                                 e.append(max_column)
#                             for entry in self.entrys:
#                                 e.append(str(entry.get()))
#                                 print(self.the_name_of_the_table)
#                             if self.the_name_of_the_table == PUPILS_TABLE:
#                                 data_entry = Base.execution_server(
#                                     ["check_which_item_this_is",
#                                      str(self.box.get()),
#                                      CIRCULATIONS_TABLE])
#                                 e.append(str(data_entry[0]))
#                             print(e)
#                             data = ["add_item", self.the_name_of_the_table, e]
#                             Base.execution_server(data)
#                         else:
#                             self.label.configure(text="הכנסת תווים שהם לא מילים")
#                             self.entrys[0].configure(fg_color="#d35b58")
#                     else:
#                         self.entrys[1].configure(fg_color="#d35b58")
#                         self.label.configure(text="לא הכנסת עשר תווים במספר הטלפון")
#
#                 else:
#                     self.label.configure(text="הכנסת קלט שהוא לא מספר")
#                     self.entrys[1].configure(fg_color="#d35b58")
#             else:
#                 self.label.configure(text="שני הנתונים לא נכונים")
#                 self.entrys[1].configure(fg_color="#d35b58")
#                 self.entrys[0].configure(fg_color="#d35b58")
#         else:
#             self.label.configure(text="הנתון שהכנסת כבר קיים")
#             self.entrys[0].configure(fg_color="#d35b58")
#         self.root.after(4000, self.clear_entrys)
#         self.root.after(4000, self.clear_label)
#
#     def start(self, the_names_of_the_entrys, data_entry):
#         def go_back():
#             self.root.destroy()
#             new_window.main_window()
#
#         self.root.frame_1 = customtkinter.CTkFrame(master=self.root,
#                                                    corner_radius=0,
#                                                height=550, width=650)
#         self.root.frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#         label_1 = customtkinter.CTkFrame(master=self.root.frame_1, height=550,
#                                          width=650)
#         label_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#         entrys = []
#         num = 0.3
#         for name in range(len(the_names_of_the_entrys)):
#             entrys.append(0)
#             entrys[name] = self.root.my_entry_2 = customtkinter.CTkEntry(
#                 master=self.root.frame_1, corner_radius=0, width=200,
#                 placeholder_text=the_names_of_the_entrys[name], text_font=(
#                     "Halvetica", -20),
#                 justify='right')
#             self.root.my_entry_2.place(relx=0.5, rely=num, anchor=tkinter.CENTER)
#             num += 0.15
#         print(len(entrys))
#         self.entrys = entrys
#
#         self.root.button_2 = customtkinter.CTkButton(master=self.root.frame_1,
#                                                  text="עדכן",
#                                                 corner_radius=0,
#                                                      command=
#                                                      self.add_item,
#                                                      width=200)
#         self.root.button_2.place(relx=0.7, rely=0.85, anchor=tkinter.CENTER)
#         self.root.button_3 = customtkinter.CTkButton(master=self.root.frame_1,
#                                                  text="חזור",
#                                                 corner_radius=0,
#                                                      command=go_back,
#                                                      width=200)
#         self.root.button_3.place(relx=0.3, rely=0.85, anchor=tkinter.CENTER)
#         try:
#             if data_entry != EMPTY_SPACE:
#                 num = 0
#                 for data in data_entry:
#                     entrys[num].insert(0, str(data))
#                     num += 1
#         except Exception as e:
#             print(e)
#
#
#     def big_title_to_add(self, width, height):
#         name = self.the_name_of_the_table.split("_")
#         self.root.frame_1.label_1 = customtkinter.CTkLabel(master=self.root.frame_1,
#                                                            width=width,
#                                                            height=height,
#                                                            fg_color=self.color_object,
#                                                            corner_radius=0,
#                                                            text=name[0],
#                                                            text_font=("Halvetica", -16))
#         self.root.frame_1.label_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
#
#     def clear_entrys(self):
#         if self.the_name_of_the_table != CIRCULATIONS_TABLE:
#             self.entrys[1].configure(fg_color="#343638")
#         self.entrys[0].configure(fg_color="#343638")
#
#
#
#
#     def check(self):
#         typed = self.box.get()
#         list_data = Base.execution_server([GET_TABLE, self.the_name_of_the_table])
#         if typed == '':
#             data = list_data
#         else:
#             data = []
#             for item in list_data:
#                 for i in item:
#                     if typed.lower() in i.lower():
#                         data.append(item)
#         self.box["values"] = data
#     def add_colors(self):
#         lis = [[0, 0.03, 20, 1500], [0.05, 0.03, 1500, 20],
#                [0.95, 0.03, 1500, 20]]
#         for i in range(len(lis)):
#             self.root.frame_1.label_1 = customtkinter.CTkLabel(master=self.root.frame_1,
#                                                         width=lis[i][3],
#                                                   height=lis[i][2],
#                                                   corner_radius=0, text=EMPTY_SPACE,
#                                                                fg_color=self.color_object,
#                                                   text_font=("Halvetica", -16))
#             self.root.frame_1.label_1.place(relx=lis[i][0], rely=lis[i][1],
#                                             anchor=tkinter.CENTER)
#
#
# class new_wind(Base):
#     def __init__(self, root, windows_name, appearance_mode,
#                  default_color_theme, label,
#                  the_location):
#         super().__init__(root, windows_name, appearance_mode,
#                          default_color_theme, label, the_location)
#         self.the_name_of_the_table = TEACHERS_TABLE
#         self.box = None
#         self.root = root
#         self.windows_name = windows_name
#         self.appearance_mode = appearance_mode
#         self.default_color_theme = default_color_theme
#         self.list_of_buttons = None
#         self.label = None
#         self.label_2 = None
#         self.label_3 = None
#         self.the_location = None
#
#     def change_the_screen_following_the_table(self, name_for_the_test,
#         the_number_of_the_button,the_name_of_the_table):
#         self.label_2.configure(text=EMPTY_SPACE)
#         self.label_3.configure(text=EMPTY_SPACE)
#         self.box.set(EMPTY_SPACE)
#         self.the_name_of_the_table = the_name_of_the_table
#         self.root.label_1.destroy()
#         self.root.label_1 = customtkinter.CTkLabel(master=self.root.frame_right,
#                                               text=name_for_the_test,
#                                               text_font=(DEFAULT_FONT,
#                                                          -25))
#         self.root.label_1.place(relx=0.8, rely=0.03)
#         for i in range(5):
#             if i == the_number_of_the_button:
#                 self.list_of_buttons[i].configure(fg_color=BACKGROUND_COLOR)
#             else:
#                 self.list_of_buttons[i].configure(fg_color=RED)
#         list_data = Base.execution_server([GET_TABLE, the_name_of_the_table])
#         if the_name_of_the_table == CIRCULATIONS_TABLE:
#             list_d = []
#             for l in list_data:
#                 list_d.append(l[1])
#             self.box["values"] = tuple(list_d)
#         else:
#             self.box["values"] = tuple(list_data)
#
#     def window_search_from_the_teachers(self):
#         self.root.destroy()
#         # search_from_the_teachers.search()
#
#     def button_pupils(self):
#         new_wind.change_the_screen_following_the_table(self, "תלמידים", 1,
#                                                        PUPILS_TABLE)
#
#     def button_teacher(self):
#         new_wind.change_the_screen_following_the_table(self, "מורים", 0,
#                                                        TEACHERS_TABLE)
#
#     def button_circulations(self):
#         new_wind.change_the_screen_following_the_table(self, "מחזורים", 4,
#                                                        "circulations_table")
#     def button_password(self):
#         new_wind.change_the_screen_following_the_table(self, "סיסמה", 3,
#                                                        "password_table")
#
#     def button_Practitioners(self):
#         new_wind.change_the_screen_following_the_table(self, "מתרגלים", 2,
#                                                "practitioners_table")
#
#     def remove_item(self):
#         typed = self.box.get()
#         Base.execution_server([REMOVE_ITEM_FROM_TABLE, self.the_name_of_the_table,
#                                str(typed)])
#         self.box["values"] = tuple(Base.execution_server([GET_TABLE,
#                                                 self.the_name_of_the_table]))
#         self.box.set(EMPTY_SPACE)
#         self.label_2.configure(text=EMPTY_SPACE)
#         self.label_3.configure(text=EMPTY_SPACE)
#
#     def update_single(self, the_execute):
#         if the_execute == CHEK_PASSWORD_FROM_TABLE:
#             data = Base.execution_server([GET_TABLE, self.the_name_of_the_table])
#             global_entry = str(self.label_3.text)
#             print(global_entry)
#             if global_entry != EMPTY_SPACE:
#                 for d in data:
#                     if not self.the_name_of_the_table == CIRCULATIONS_TABLE:
#                         if d[1] in global_entry:
#                             global_entry = d
#                             break
#                     else:
#                         if d[0] in global_entry:
#                             global_entry = d
#                             break
#                 self.root.destroy()
#                 update_item.update(global_entry,
#                                           self.the_name_of_the_table)
#             else:
#                 self.label.configure(text="לא בחרת איזה נתונים לעדכן")
#                 self.root.after(4000, self.clear_label)
#
#         else:
#             global_entry = EMPTY_SPACE
#             self.root.destroy()
#             update_item.update(global_entry, self.the_name_of_the_table)
#
#     def catching_sound(self, typed):
#         data = []
#         list_data = Base.execution_server([GET_TABLE, self.the_name_of_the_table])
#         for item in list_data:
#             if typed.lower() in item:
#                 data.append(item)
#         self.box["values"] = data
#
#     def excel(self):
#         filename = fd.askopenfilename(
#             title='Open a file',
#             initialdir='/',
#         )
#         try:
#             wb = load_workbook(filename)
#             ws = wb.active
#             A = ws["A"]
#             if self.the_name_of_the_table in [PASSWORD_TABLE, PUPILS_TABLE,
#                                               TEACHERS_TABLE, PRACTITIONERS_TABLE]:
#                 B = ws["B"]
#             if self.the_name_of_the_table == PUPILS_TABLE:
#                 C = ws["C"]
#             exel_list = []
#             for a in range(len(A)):
#                 if A[a].value is None:
#                     A[a].value = "ריק"
#                 if self.the_name_of_the_table == TEACHERS_TABLE or \
#                         PUPILS_TABLE or PRACTITIONERS_TABLE or PASSWORD_TABLE:
#                     if B[a].value is None:
#                         B[a].value = "ריק"
#                 if self.the_name_of_the_table == PUPILS_TABLE:
#                     if C[a].value is None:
#                         C[a].value = "ריק"
#
#
#
#             def add_item(item_list):
#                 for exel in exel_list:
#                     bool_i = True
#                     for P in item_list:
#                         if P[1] == exel[1] and P[0] == exel[0] and P[2] == \
#                                 exel[2]:
#                             bool_i = False
#                     if bool_i:
#                         item_list.append(exel)
#                 return item_list
#
#             for i in range(len(A)):
#                 if self.the_name_of_the_table == "password_table":
#                     l = [str(A[i].value), str(B[i].value)]
#                 else:
#                     l = [A[i].value, str(B[i].value), C[i].value]
#                 exel_list.append(l)
#             data_to_add = ["add_exel", exel_list, self.the_name_of_the_table]
#             teachers = Base.execution_server(data_to_add)
#             teachers = add_item(teachers)
#             list_data = tuple(teachers)
#             self.box = list_data
#             self.label.configure(text="הקובץ שנתנת התווסף בהצלחה")
#         except:
#             self.label.configure(text="הקובץ שנתנת הוא לא קובץ אקסל")
#         self.root.after(4000, self.clear_label)
#
#
#     def clear_label(self):
#         self.label.configure(text=EMPTY_SPACE)
#
#
#
#     def voice(self):
#         recognizer = speech_recognition.Recognizer()
#         with speech_recognition.Microphone() as mic:
#             try:
#
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.5)
#                 mouse_listener = pynput.mouse.Listener(suppress=True)
#                 mouse_listener.start()
#                 audio = recognizer.listen(mic, phrase_time_limit=10)
#                 if audio != '':
#                     self.box.set(str(recognizer.recognize_google(audio,
#                                                              language="he")))
#                     self.catching_sound(str(recognizer.recognize_google(audio,
#                                                            language="he")))
#
#             except:
#                 self.label = self.create_masages(220, 100, "#2a2d2e",
#                                                  "לא הצליח לזהות קול", 0.15,
#                                                  0.3, -16)
#                 self.root.after(4000, self.clear_label)
#         mouse_listener.stop()
#
#     def check(self):
#         typed = self.box.get()
#         list_data = Base.execution_server([GET_TABLE, self.the_name_of_the_table])
#         if typed == '':
#             data = list_data
#         else:
#             data = []
#             for item in list_data:
#                 for i in item:
#                     if typed.lower() in i.lower():
#                         data.append(item)
#         self.box["values"] = data
#
#
#

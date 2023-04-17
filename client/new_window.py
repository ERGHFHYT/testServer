import tkinter
import customtkinter
from customtkinter import CTkImage
from PIL import Image, ImageTk  # <- import PIL for the images
from tkinter import ttk
import tkinter.messagebox
import client.client_classes_folder.New_wind
from constants import *


def main_window():
    app = customtkinter.CTk()
    root_2 = app
    tool = client.client_classes_folder.New_wind. \
        New_wind(root_2, "מסך בית", "System", "blue", None, None)
    tool.window()
    root_2.grid_columnconfigure(1, weight=1)
    root_2.grid_rowconfigure(0, weight=1)

    root_2.frame_left = customtkinter.CTkFrame(master=root_2,
                                               width=180,
                                               corner_radius=0)
    root_2.frame_left.grid(row=0, column=0, sticky="nswe")
    add_folder_image = ImageTk.PhotoImage(Image.open(ADD_FOLDER_IMAGE).resize((
        ICON_IMAGE_SIZE, ICON_IMAGE_SIZE), Image.ANTIALIAS))
    add_list_image = ImageTk.PhotoImage(Image.open(ADD_LIST_IMAGE).resize(
        (ICON_IMAGE_SIZE, ICON_IMAGE_SIZE), Image.ANTIALIAS))
    teacher_image = ImageTk.PhotoImage(
        Image.open(TEACHER_IMAGE).resize((ICON_IMAGE_SIZE, ICON_IMAGE_SIZE),
                                         Image.ANTIALIAS))
    check_list_image = ImageTk.PhotoImage(
        Image.open(CHECK_IMAGE).resize(CHECK_IMAGE_SIZE,
                                       Image.ANTIALIAS))
    mic_image = ImageTk.PhotoImage(
        Image.open(MICROPHONE_IMAGE).resize(CHECK_IMAGE_SIZE,
                                       Image.ANTIALIAS))
    root_2.frame_right = customtkinter.CTkFrame(master=root_2, height=550,
                                                width=650)
    root_2.frame_right.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)
    button_1 = customtkinter.CTkButton(master=root_2.frame_right,
                                       image=add_folder_image,
                                       text="אקסל טבלת הוסף", width=150,
                                       height=40,
                                       compound="right",
                                       command=tool.excel)
    button_1.place(relx=0.05, rely=0.75)
    # button_4 = customtkinter.CTkButton(master=root_2.frame_right,
    #                                    image=teacher_image,
    #                                    text="מורים בעזרת חיפוש",
    #                                    width=150, height=40,
    #                                    compound="right",
    #                                    command=tool.
    #                                    window_search_from_the_teachers)
    # button_4.place(relx=0.3, rely=0.75)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", backrground="D3D3D3",
                    forerground="black", rowheight=25,
                    fieldbackrground="D3D3D3")

    tree = ttk.Treeview(root_2, show='headings',
                        height=6)
    tree['column'] = ("c1", "c2", "c3", "c4", "c5", "c6")
    tree.column("# 1", anchor='n', width=120)
    tree.heading("# 1", text="שם")
    tree.column("# 2", anchor='n', width=120)
    tree.heading("# 2", text="שם משפחה")
    tree.column("# 3", anchor='n', width=120)
    tree.heading("# 3", text="תעודת זהות")
    tree.column("# 4", anchor='n', width=120)
    tree.heading("# 4", text="מספר טלפון")
    tree.column("# 5", anchor='n', width=90)
    tree.heading("# 5", text="")
    tree.column("# 6", anchor='n', width=120)
    tree.heading("# 6", text="")

    tree.place(
        relx=0.3, rely=0.4)
    tool.tree = tree
    button_3 = customtkinter.CTkButton(master=root_2.frame_right,
                                       image=check_list_image, text="נתון שנה",
                                       width=150, height=40,
                                       compound="right",
                                       command=lambda:
                                       tool.update_single("chek"))

    button_3.place(relx=0.05, rely=0.85)

    # ============ frame_left ============

    # configure grid layout (1x11)
    root_2.frame_left.grid_rowconfigure(0, minsize=10)
    root_2.frame_left.grid_rowconfigure(5, weight=1)
    root_2.frame_left.grid_rowconfigure(8, minsize=20)
    root_2.frame_left.grid_rowconfigure(11, minsize=10)

    root_2.label_1 = customtkinter.CTkLabel(master=root_2.frame_left,
                                            text="סוג",
                                            font=("Roboto Medium", -16))
    root_2.label_1.grid(row=1, column=0, pady=10, padx=10)
    root_2.label_1 = customtkinter.CTkLabel(master=root_2.frame_right,
                                            text="מורה",
                                            font=("Halvetica", -25))
    root_2.label_1.place(relx=0.7, rely=0.03)
    num = 2
    buttons_names = ["מורים", "תלמידים", "מתרגלים", "סיסמה", "מחזור", "מורים בתוך תלמידים"]
    buttons_commend = [tool.button_teacher, tool.button_pupils,
                       tool.button_Practitioners,
                       tool.button_password, tool.button_circulations, tool.button_pupils_in_teachers]
    list_of_buttons = [0, 0, 0, 0, 0, 0]
    for button in range(len(buttons_names)):
        list_of_buttons[button] = root_2.button_2 = customtkinter.CTkButton(
            master=root_2.frame_left, text=buttons_names[button],
             command=buttons_commend[button])
        root_2.button_2.grid(row=num, column=0, pady=10, padx=20)
        num += 1

    list_of_buttons[0].configure(fg_color=DARK_GRAY)
    root_2.button_5 = customtkinter.CTkButton(master=root_2.frame_right,
                                              text="", image=mic_image,
                                              height=40,
                                              width=40,
                                              corner_radius=15,
                                              command=tool.mic)
    root_2.button_5.place(relx=0.2, rely=0.1)
    tool.mic_button = root_2.button_5
    root_2.button_9 = customtkinter.CTkButton(master=root_2.frame_right,
                                              height=40,
                                              width=110, fg_color="#D35B58",
                                              hover_color="#C77C78",
                                              text="מחיקה",
                                              command=tool.remove_item)
    root_2.button_9.place(relx=0.8, rely=0.85)

    button_2 = customtkinter.CTkButton(master=root_2.frame_right,
                                       image=add_list_image, text="יחיד הוסף",
                                       width=150, height=40,
                                       compound="right",
                                       command=lambda:
                                       tool.update_single("add"))
    button_2.place(relx=0.3, rely=0.85)

    box = customtkinter.CTkEntry(root_2.frame_right, width=250,
                       font=("Halvetica", 20),
                       justify='right')
    box.place(relx=0.5, rely=0.1)
    tool.the_location = root_2.frame_right
    tool.label = tool.create_masages(200, 120, "#2b2b2b", "", 0.65, 0.7,
                                     -16)
    tool.label_2 = tool.create_masages(120, 120,
                                       "#2b2b2b", "", 0.85, 0.35, -25)
    tool.label_3 = tool.create_masages(120, 120,
                                       "#2b2b2b", "", 0.65, 0.35, -25)
    tool.box = box

    # def event(event):
    #     list_items = tool.execution_server(["check_which_item_this_is",
    #                                         tool.the_name_of_the_table,
    #                                         tool.box.get()
    #                                         ])
    #     if tool.the_name_of_the_table == "password_table":
    #         item_string = " :שם משתמש" + "\n" + " :סיסמה"
    #         item_string_2 = list_items[0] + "\n" + list_items[1]
    #     elif tool.the_name_of_the_table == "circulations_table":
    #         item_string = " :מחזור"
    #         item_string_2 = list_items[1]
    #     elif tool.the_name_of_the_table == "pupils_table":
    #         item_string = " :שם" + "\n" + " :תעודת זהות" + "\n" + " :מחזור"
    #         item_string_2 = list_items[0] + "\n" + list_items[1] + "\n" + \
    #                         list_items[2]
    #     else:
    #         item_string = " :שם" + "\n" + " :תעודת זהות"
    #         item_string_2 = list_items[0] + "\n" + list_items[1]
    #
    #     tool.label_2.configure(text=item_string)
    #     tool.label_3.configure(text=item_string_2)

    tool.list_of_buttons = list_of_buttons
    root_2.option_add('*TCombobox*Listbox.font', 14)
    box.bind("<KeyRelease>", tool.check)
    # box.bind("<<ComboboxSelected>>", event)
    tool.button_teacher()
    root_2.mainloop()

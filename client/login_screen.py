
import tkinter.messagebox

import customtkinter

import new_window
import socket

from PIL import Image, ImageTk  # <- import PIL for the images
import tkinter.messagebox

import client.client_classes_folder.Base
from constants import *


# ניבא את הספרייה שתאפשר לנו להתחבר למסד נתונים


def entry_window():
    root = customtkinter.CTk()
    tool = client.client_classes_folder.Base.Base(root, LOGIN_SCREEN, DARK,
                                                  BLUE, None, None)
    tool.window()

    # load image with PIL and convert to PhotoImage
    image = Image.open(BACKGROUND_IMAGE).resize(SIZE_OF_BACKGROUND_IMAGE)
    bg_image = ImageTk.PhotoImage(image)

    root.image_label = tkinter.Label(master=root, image=bg_image)
    root.image_label.place(relx=MIDDLE, rely=MIDDLE, anchor=tkinter.CENTER)

    root.frame = customtkinter.CTkFrame(master=root,
                                        width=300,
                                        height=HEIGHT,
                                        corner_radius=0)
    root.frame.place(relx=MIDDLE, rely=MIDDLE, anchor=tkinter.CENTER)

    root.label_1 = customtkinter.CTkLabel(master=root.frame, width=200,
                                          height=100,
                                          fg_color=DARK_GRAY,
                                          corner_radius=0,
                                          bg_color=BACKGROUND_COLOR,
                                          text="תתחבר",
                                          font=(DEFAULT_FONT, -30))
    root.label_1.place(relx=MIDDLE, rely=0.3, anchor=tkinter.CENTER)

    root.entry_password = customtkinter.CTkEntry(master=root.frame,
                                                 corner_radius=6, width=200,
                                                 placeholder_text=
                                                 THE_WORD_PASSWORD,
                                                 show=ASTERISK,
                                                 justify=ENTRY_JUSTIFY)
    root.entry_password.place(relx=MIDDLE, rely=0.6, anchor=tkinter.CENTER)

    def clear_entry():
        root.entry_username.configure(fg_color=BACKGROUND_COLOR)
        root.entry_password.configure(fg_color=BACKGROUND_COLOR)

    def start_new():
        message = [CHECK_PASSWORD_FROM_TABLE, root.entry_username.get(),
                   root.entry_password.get()]
        password_response_form_the_table = tool.execution_server(message)
        if password_response_form_the_table == CORRECT_PASSWORD:
            root.destroy()
            new_window.main_window()
        elif password_response_form_the_table == \
                USERNAME_ERROR_AND_PASSWORD_ERROR:
            tool.change_the_text(ALL_WRONG)
            root.entry_username.configure(fg_color=RED)
            root.entry_password.configure(fg_color=RED)
            root.after(4000, clear_entry)

    root.entry_username = customtkinter.CTkEntry(master=root.frame,
                                                 corner_radius=6, width=200,
                                                 placeholder_text="שם משתמש",
                                                 justify=ENTRY_JUSTIFY)
    root.entry_username.place(relx=MIDDLE, rely=0.52, anchor=tkinter.CENTER)
    root.button_2 = customtkinter.CTkButton(master=root.frame, text="תתחבר",

                                            corner_radius=6, command=start_new,
                                            width=200)
    root.button_2.place(relx=MIDDLE, rely=0.7, anchor=tkinter.CENTER)
    tool.the_location = root.frame
    tool.label = tool.create_masages(300, 100, DARK_GRAY, None, MIDDLE, 0.9,
                                     -16)
    root.mainloop()


the_names_of_the_computers = \
    client.client_classes_folder.Base.Base.execution_server([GET_TABLE,
                                                            COMPUTER_NAMES_TABLE])
the_name_of_this_computer = str(socket.gethostname())
booli = False
for name in the_names_of_the_computers:
    if name == the_name_of_this_computer:
        booli = True

if booli:
    new_window.main_window()
else:
    entry_window()

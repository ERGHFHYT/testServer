import tkinter
import customtkinter
from tkinter import ttk
import tkinter.messagebox
import classes
import exelfile
import update_item
import speech_recognition
from PIL import Image, ImageTk
import pyaudio
class main_window():
    def __init__(self):
        app = customtkinter.CTk()
        root_2 = app
        tool = classes.new_wind(root_2, "מסך בית", "System",  "blue", "", "",
                                "", "", "")
        tool.window()
        root_2.grid_columnconfigure(1, weight=1)
        root_2.grid_rowconfigure(0, weight=1)
        IMAGE_SIZE = 20
        teachers = classes.Base.sever_db(["human", "teachers_table"])
        list_data = [tuple(sub) for sub in teachers]
        root_2.frame_left = customtkinter.CTkFrame(master=root_2,
                                                 width=180,
                                                 corner_radius=0)
        root_2.frame_left.grid(row=0, column=0, sticky="nswe")
        add_folder_image = ImageTk.PhotoImage(Image.open("add_folder.png").resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS))
        add_mic_image = ImageTk.PhotoImage(Image.open("microphone7.png").resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS))
        add_list_image = ImageTk.PhotoImage(Image.open("add-list.png").resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS))
        root_2.frame_right = customtkinter.CTkFrame(master=root_2, height=550,
                                                    width=650)
        root_2.frame_right.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)
        button_1 = customtkinter.CTkButton(master=root_2.frame_right,
                                           image=add_folder_image, text="אקסל טבלת הוסף", width=10, height=40,
                                           compound="right", command=tool.excel)
        button_1.place(relx=0.05, rely=0.7)
        button_3 = customtkinter.CTkButton(master=root_2.frame_right,
                image=add_list_image, text="נתון שנה", width=150, height=40,
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
                                              text_font=("Roboto Medium", -16))
        root_2.label_1.grid(row=1, column=0, pady=10, padx=10)
        root_2.label_1 = customtkinter.CTkLabel(master=root_2.frame_right,
                                              text="מורה",
                                              text_font=("Halvetica", -25))
        root_2.label_1.place(relx=0.83, rely=0.03)
        num = 2
        buttons_names = ["מורים", "תלמידים", "מתרגלים", "סיסמה"]
        buttons_commend = [tool.button_teacher, tool.button_pupils,
                           tool.button_Practitioners,
                           tool.button_password]
        list_of_buttons = [0, 0, 0, 0]
        for button in range(len(buttons_names)):
            list_of_buttons[button] = root_2.button_2 = customtkinter.CTkButton(
                master=root_2.frame_left, text=buttons_names[button],
                fg_color=("#1f6aa5"), command=buttons_commend[button])
            root_2.button_2.grid(row=num, column=0, pady=10, padx=20)
            num += 1

        list_of_buttons[0].configure(fg_color=("gray84", "gray25"))
        root_2.button_5 = customtkinter.CTkButton(master=root_2.frame_right, height=40,
                                                width=40,
                                                text="", image=add_mic_image,
                                                corner_radius=15,
                                                command=tool.voice)
        root_2.button_5.place(relx=0.2, rely=0.1)
        root_2.button_9 = customtkinter.CTkButton(master=root_2.frame_right, height=40,
                width=110, fg_color="#D35B58", hover_color="#C77C78",
                                                text="מחיקה",
                                                command=tool.remove_item)
        root_2.button_9.place(relx=0.8, rely=0.85)

        button_2 = customtkinter.CTkButton(master=root_2.frame_right,
                image=add_list_image, text="יחיד הוסף", width=150, height=40,
                                           compound="right",
                                           command=lambda:
                                           tool.update_single("add"))
        button_2.place(relx=0.30, rely=0.85)

        box = ttk.Combobox(root_2.frame_right, width=28, font=("Halvetica", 20),
                           values=list_data, justify='right')
        box.place(relx=0.3, rely=0.1)
        tool.the_location = root_2.frame_right
        tool.label = tool.create_masages(220, 100, "#2a2d2e", "", 0.45, 0.75,
                                         -16)
        tool.label_2 = tool.create_masages(300, 200,
                            "#2a2d2e", "", 0.7, 0.35, -30)
        tool.box = box
        def event(event):
            list_items = tool.sever_db(["check_which_item_this_is",
                                        tool.box.get(),
                                        tool.the_name_of_the_table])
            if tool.the_name_of_the_table == "password_table":
                item_string = list_items[0] + " :שם משתמש" + "\n" + list_items[
                    1] + " :סיסמה"
            else:
                item_string = list_items[0]+" :שם"+"\n" +list_items[
                    1]+ " :מספר טלפון"+"\n"+list_items[2]+" :מחזור"

            tool.label_2.configure(text=item_string)
        tool.list_of_buttons = list_of_buttons
        root_2.option_add('*TCombobox*Listbox.font', 14)
        box.bind("<KeyRelease>", tool.check())
        box.bind("<<ComboboxSelected>>", event)
        tool.button_teacher()
        root_2.mainloop()
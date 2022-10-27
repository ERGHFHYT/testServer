import new_window
from new_window import *
import classes
import socket
from PIL import Image, ImageTk  # <- import PIL for the images
#ניבא את הספרייה שתאפשר לנו להתחבר למסד נתונים

def entry_window():
    WIDTH = 900
    HEIGHT = 600
    root = customtkinter.CTk()
    tool = classes.Base(root, "מסך פתיחה", "Dark", "blue", "", "")
    tool.window()

    # load image with PIL and convert to PhotoImage
    image = Image.open("hand-painted-background-violet-orange-colours_23"
                       "-2148427578.webp").resize((1400, 1000))
    bg_image = ImageTk.PhotoImage(image)

    root.image_label = tkinter.Label(master=root, image=bg_image)
    root.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    root.frame = customtkinter.CTkFrame(master=root,
                                        width=300,
                                        height=HEIGHT,
                                        corner_radius=0)
    root.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    root.label_1 = customtkinter.CTkLabel(master=root.frame, width=200, height=100,
                                          fg_color="#2a2d2e",
                                          corner_radius=0, bg_color=("gray70",
                                                                    "gray25"), text="תתחבר",
                                          text_font=("Halvetica", -30))
    root.label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    root.entry_password = customtkinter.CTkEntry(master=root.frame,
                                                 corner_radius=6, width=200,
                                                 placeholder_text="סיסמה",
                                                 show="*", justify='right')
    root.entry_password.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def start_new():
        message = [tool.CHEK, root.entry_password.get(), root.entry_username.get()]
        data = tool.sever_db(message)
        if data == "True":
            root.destroy()
            new_window.main_window()
        elif data == "password_error":
            tool.change_the_text("הסיסמה לא נכונה")
        elif data == "username_error":
            tool.change_the_text("שם המשתמש לא נכון")
        elif data == "username_error_and_password_error":
            tool.change_the_text("שם המשתמש או סיסמה לא נכונים")
        else:
            tool.change_the_text("שם המשתמש וסיסמה לא נכונים")

    root.entry_username = customtkinter.CTkEntry(master=root.frame, corner_radius=6, width=200,
                                             placeholder_text="שם משתמש", justify='right')
    root.entry_username.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)
    root.button_2 = customtkinter.CTkButton(master=root.frame, text="תתחבר",

                                            corner_radius=6, command=start_new,
                                            width=200)
    root.button_2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    tool.the_location = root.frame
    tool.label = tool.create_masages(300, 100, "#2a2d2e", "", 0.5, 0.9, -16)
    root.mainloop()


the_names_of_the_computers = classes.Base.sever_db(["human",
                                                    "computer_names_table"])
the_name_of_this_computer = str(socket.gethostname())
booli = False
for name in the_names_of_the_computers:
    if name == the_name_of_this_computer:
        booli = True

if booli:
    new_window.main_window()
else:
    entry_window()


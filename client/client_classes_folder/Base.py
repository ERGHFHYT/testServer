from client.constants import *
import tkinter
import customtkinter
import socket
import json
import tkinter.messagebox


class Base:
    def __init__(self, root, windows_name, appearance_mode,
                 default_color_theme, label, the_location):
        self.root = root
        self.windows_name = windows_name
        self.appearance_mode = appearance_mode
        self.default_color_theme = default_color_theme
        self.label = label
        self.the_location = the_location

    def window(self):
        self.root.geometry(SIZE_OF_WINDOW)
        self.root.title(self.windows_name)
        self.root.resizable(False, False)
        customtkinter.set_appearance_mode(
            self.appearance_mode)
        customtkinter.set_default_color_theme(
            self.default_color_theme)

    def create_masages(self, width, height, fg_color, text, x, y, text_size):
        self.root.label = customtkinter.CTkLabel(
            master=self.the_location,
                                                width=width,
                                              height=height,
                                              fg_color=fg_color,
                                              corner_radius=0,
                                              bg_color=("gray70",
                                                        "gray25"), text=text,
                                              font=(DEFAULT_FONT, text_size))
        self.root.label.place(relx=x, rely=y, anchor=tkinter.CENTER)
        return self.root.label

    def change_the_text(self, text):
        self.label.configure(text=text)
        self.root.after(4000, self.clear_label)

    def clear_label(self):
        self.label.configure(text=EMPTY_SPACE)

    @classmethod
    def execution_server(self, message):
        host = "localhost"  # as both code is running on same pc
        port = 5050  # socket server port number
        client_socket_1 = socket.socket()  # instantiate
        client_socket_1.connect((host, port))  # connect to the server
        message = json.dumps(message)
        message = message.encode('utf-8')
        client_socket_1.send(message)  # send message
        data = client_socket_1.recv(256 * 1024).decode('utf-8')
        data = json.loads(data)
        if data:
            client_socket_1.close()
        return data
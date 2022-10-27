import tkinter as tk

window = tk.Tk()
window.minsize(710, 500)
window.state('zoomed')
window.title('Example')

# the frame will be the main container, it's a child of the root window
frame = tk.Frame(window)
frame.grid(row=0, column=0, stick='news')
# tell our root window that its grid should be stretchable
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# create a label, child of the frame, in row 0, column 0. It wiil span for 3 cells
tk.Label(frame, text="Example", fg='red3',
      font=('Eras Bold ITC', '65', 'bold')).grid(row=0, column=0, columnspan=3)

# create another label, child of the frame, in row 1, column 2
tk.Label(frame, text="Label1", fg='blue',
      font=('Calibri', '25', 'bold')).grid(row=1, column=2)


# create another label, child of the frame, in row 1, column 3
tk.Label(frame, text="Label2", fg='blue',
      font=('Calibri', '25', 'bold')).grid(row=1, column=3)

# create a button, child of the frame, in row 2, column 0
tk.Button(frame, height='10', width='20', text = 'image1').grid(row = 2, column = 0, padx = 20, pady=40)
# create a button, child of the frame, in row 2, column 1
tk.Button(frame, height='10', width='20', text = 'image2').grid(row = 2, column = 1, padx = 20, pady=40)
# create a button, child of the frame, in row 2, column 2
tk.Button(frame, height='10', width='20', text = 'image3').grid(row = 2, column = 2, padx = 20, pady=40)

# tell our frame that its grid should resize (stretchable) with same ratio for row heights and column widths
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

window.mainloop()

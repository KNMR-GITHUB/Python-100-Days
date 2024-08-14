import tkinter

window = tkinter.Tk()
window.title('Hi Bye')
window.minsize(width=500, height=500)

#label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


# defining button activity
def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="hello", command=button_clicked)
button.pack()

# taking user inputs
input = tkinter.Entry(width=10)
input.pack()

#needs to be at the end
window.mainloop()
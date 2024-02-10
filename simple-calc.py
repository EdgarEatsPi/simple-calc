import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calc?")

        self.button1 = Gtk.Button(label="Click Here")
        self.button1.connect("clicked", self.hello_world)
        self.add(self.button1)
    def hello_world(self, widget):
        print("Hello World")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

# print("Python Calculator\nEnter \"quit\" or \"exit\" to exit the program.")

# while True:
    # equation = input("")
    # if (equation == "quit") or (equation == "exit"):
        # break
    # solution = eval(equation)
    # print(solution)

# print("Exiting program...")

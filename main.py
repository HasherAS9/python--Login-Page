from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x600+100+50")

        self.bg = ImageTk.PhotoImage(file="photo.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_Login = Frame(self.root, bg="#FFBAE7")
        Frame_Login.place(x=100, y=150, width=500, height=500)

        title = Label(Frame_Login, text="LOGIN PAGE", font=("ALGERIAN", 40, "bold"), fg="#924DB0", bg="#FFBAE7").place(
            x=90, y=30)

        Username = Label(Frame_Login, text="Username", font=("Copperplate Gothic Light", 20, "bold"), fg="#463274",
                         bg="#FFBAE7").place(
            x=90, y=140)
        self.user = Entry(Frame_Login, font=("Sylfaen", 20), fg="#463274",
                          bg="#FFBAE7")
        self.user.place(x=110, y=180)

        Password = Label(Frame_Login, text="Password", font=("Copperplate Gothic Light", 20, "bold"), fg="#463274",
                         bg="#FFBAE7").place(
            x=90, y=250)
        self.passw = Entry(Frame_Login, font=("Sylfaen", 20), fg="#463274",
                           bg="#FFBAE7")
        self.passw.place(x=110, y=290)

        ForgetB = Button(Frame_Login,cursor="hand2", text="Forget Password?", bd=0, font=("Copperplate Gothic Light", 10, "bold"),
                         fg="#463274",
                         bg="#FFBAE7").place(
            x=85, y=340)
        Submit = Button(Frame_Login,command=self.functions,cursor="hand2", text="SUBMIT", font=("Copperplate Gothic Light", 10, "bold"),
                        fg="#463274",
                        bg="#FFBAE7").place(
            x=200, y=380)

    def functions(self):
        if self.user.get() == "" or self.passw.get() == "":
            messagebox.showerror("ERROR", "Please fill all the above requirements", parent=self.root)
        if self.user.get() != "Hasher" or self.passw.get() != "HasherAS9":
            messagebox.showerror("ERROR", "Above Username or Password is Incorrect", parent=self.root)
        else:
            messagebox.showinfo("WELCOME" , f"Hi {self.user.get()}")


root = Tk()
obj = login(root)
root.mainloop()

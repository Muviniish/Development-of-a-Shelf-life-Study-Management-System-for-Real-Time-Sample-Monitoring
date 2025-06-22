from customtkinter import *
import customtkinter as ctk
from PIL import Image

class GIFLabel(ctk.CTkLabel):
    def __init__(self, master, image_path, **kwargs):
        self._gif_image = Image.open(image_path)
        # set the size of the label to the same as the GIF image
        kwargs.setdefault("width", 500)
        kwargs.setdefault("height", 500)
        # don't show the text initially
        kwargs.setdefault("text", "")
        # delay for the after loop
        self._duration = kwargs.pop("duration", "45")# or self._gif_image.info["duration"]
        super().__init__(master, **kwargs)
        # load all the frames
        self._frames = []
        for i in range(self._gif_image.n_frames):
            self._gif_image.seek(i)
            self._frames.append(ctk.CTkImage(self._gif_image.copy(), size=(self["width"], self["height"])))
        # start animation
        self._animate()

    def _animate(self, idx=0):
        self.configure(image=self._frames[idx])
        self.after(self._duration, self._animate, (idx+1)%len(self._frames))

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)


def page():
    window = CTk()
    LoginForm(window)
    backgroundImg = CTkImage(Image.open('background.jpg'), size=(1166,718))
    bacxkgroundImgLabel = CTkLabel(window, image=backgroundImg, text="")
    bacxkgroundImgLabel.place(x=0, y=0)
    Frame = CTkFrame(window, fg_color='#ffeae0', width=950, height=600)
    Frame.place(x=100, y=50)
    Frame2 = CTkFrame(Frame, fg_color='#FCD8CD', width=400, height=510, corner_radius=30)
    Frame2.place(x=520, y=50)
    gif = GIFLabel(Frame, "loginPage.gif")
    gif.place(x=5, y=55)
    header = CTkLabel(Frame, text="AMBU Shelf-Life Study Management System", width=300, height=30, font=('yu gothic ui', 25, 'bold'), fg_color="#ffeae0", text_color='black')
    header.place(x=470, y=20, anchor=CENTER)
    img = CTkImage(Image.open('signIn.jpeg'), size=(120,100))
    imgLabel = CTkLabel(Frame, image=img, text="")
    imgLabel.place(x=660, y=110)
    signLabel= CTkLabel(Frame, text="Sign In", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 19, 'bold'))
    signLabel.place(x=690, y=210)
    usernameLabel= CTkLabel(Frame, text="Username", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 17, 'bold'))
    usernameLabel.place(x=550, y=270)
    usernameEntry= CTkEntry(Frame, width=270, fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 15, 'bold'), border_color='#FCD8CD')
    usernameEntry.place(x=580, y=300)
    usernameLine = CTkCanvas(Frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    usernameLine.place(x=550, y=330)
    usernameIcon = CTkImage(Image.open('usernameIcon.jpg'), size=(30,20))
    usernameIconLabel = CTkLabel(Frame, image=usernameIcon, text="")
    usernameIconLabel.place(x=550, y=300)

    passwordLabel= CTkLabel(Frame, text="Password", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 17, 'bold'))
    passwordLabel.place(x=550, y=350)
    passwordEntry= CTkEntry(Frame, width=270, show="*", fg_color="#FCD8CD", bg_color='#FCD8CD', font=('yu gothic ui', 15, 'bold'), border_color='#FCD8CD')
    passwordEntry.place(x=580, y=380)
    passwordLine = CTkCanvas(Frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    passwordLine.place(x=550, y=410)
    passwordIcon = CTkImage(Image.open('passwordIcon.jpg'), size=(30,20))
    passwordIconLabel = CTkLabel(Frame, image=passwordIcon, text="")
    passwordIconLabel.place(x=550, y=380)
    showImg = CTkImage(Image.open('show.jpg'), size=(30,20))
    hideImg = CTkImage(Image.open('hide.jpg'), size=(30,20))
    def show():
        if passwordEntry.cget('show')=='*':
            passwordEntry.configure(show='')
            imgBtn.configure(image=hideImg)
        else:
            passwordEntry.configure(show='*')
            imgBtn.configure(image=showImg)

    
    imgBtn = CTkButton(Frame, text="", image=showImg,width=30,bg_color='#FCD8CD',
                           cursor='hand2', fg_color='#FCD8CD', command=show)
    imgBtn.place(x=850, y=380)
    
    
    

    loginBtn = CTkButton(Frame, text="LOGIN",  font=('yu gothic ui', 20, 'bold'), width=337,
                         bg_color='blue', cursor='hand2', fg_color='blue')
    loginBtn.place(x=550, y=430)

    window.mainloop()

if __name__ == '__main__':
    page()
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
import main


def main_screen():
    main_frame.pack()
    home_frame.pack_forget()


def home_screen():
    home_frame.pack()
    main_frame.pack_forget()


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("manifest file",
                                                      "*.xml*"),
                                                     ("all files",
                                                      "*.*")))
    if filename == "":
        messagebox.showerror("Error!!!", "File not founds")
        file_name_label.configure(text="No files are selected")
    elif filename[-4:] != ".xml":
        messagebox.showerror("Error!!!", "Wrong files format")
        file_name_label.configure(text="Wrong files format")
    else:
        file_name_label.configure(text="File Opened: " + filename)
    testfilename.append(filename)


def process():
    if len(testfilename) == 0 or testfilename[len(testfilename) - 1] == "":
        messagebox.showerror("Error!!!", "No files are selected")
    else:
        result = main.process(testfilename[len(testfilename) - 1])
        last_label.configure(text=result)


def reset():
    testfilename.clear()
    file_name_label.configure(text="Choose your file")
    last_label.configure(text="")


# -----------------------------------------------------------------------------------------------------------#
app = Tk()
app.title("Test GUI App")
app.geometry("900x600")
app.resizable(False, False)

# Home Frame
home_frame = Frame(app, width=900, height=600)
home_frame.pack()

# 1.Background
home_bg = ImageTk.PhotoImage(Image.open("img/Bg1.png", "r").resize((900, 600)))
home_bg_label = Label(home_frame, image=home_bg)
home_bg_label.pack()

# 2. PTIT Logo
ptit_logo = ImageTk.PhotoImage(Image.open("img/ptit_logo_3.png", "r").resize((80, 80)))
logo_label = Label(home_frame, image=ptit_logo, bg="#010510")
logo_label.place(relx=0.05, rely=0.05, anchor=NW)

# 3. Home Screen Title
canvas = Canvas(home_frame)
title_font = CTkFont(family="r0c0i Linotte Bold", size=45)
group_name = Label(home_frame, text="BTL Python nhóm 5", font=title_font, justify=CENTER,
                   fg="white", bg="#010220")
group_name.place(relx=0.05, rely=0.25, anchor=NW)

title_font = CTkFont(family="r0c0i Linotte Semi Bold", size=30)
group_topic = Label(home_frame, text="Chủ đề: Phát hiện mã độc Android", font=title_font, justify=CENTER,
                    fg="white", bg="#010225")
group_topic.place(relx=0.05, rely=0.35, anchor=NW)

# 4. Member
title_font = CTkFont(family="r0c0i Linotte Regular", size=20)
teacher_label = Label(home_frame, text="GV: Vũ Minh Mạnh", font=title_font, justify=CENTER, fg="white", bg="#010221")
teacher_label.place(relx=0.05, rely=0.43, anchor=NW)
member_names = ["Phạm Hoài Nam", "Đàm Tiến Quân", "Cam Hải Đăng", "Nguyễn Đình Văn"]
member_msv = ["B21DCCN554", "B21DCCN554", "B21DCCN554", "B21DCCN554"]

title_font = CTkFont(family="r0c0i Linotte Light", size=20)
name_label = Label(home_frame, text="Thành viên nhóm:", font=title_font, fg="white", bg="#020129")
name_label.place(relx=0.05, rely=0.53, anchor=NW)
for i in range(4):
    name_label = Label(home_frame, text=f"{i + 1}" + ". " + member_names[i], font=title_font, fg="white", bg="#020031")
    msv_label = Label(home_frame, text=member_msv[i], font=title_font, fg="white", bg="#020031")
    name_label.place(relx=0.05, rely=0.6 + i * 0.075, anchor=NW)
    msv_label.place(relx=0.25, rely=0.6 + i * 0.075, anchor=NW)

# 5. Start Button
start_button_img = ImageTk.PhotoImage(Image.open("img/start_button_1.png").resize((154, 53)))
start_button = Button(home_frame, image=start_button_img, command=main_screen, bg="#000034", borderwidth=0,
                      activebackground="#000034")
start_button.place(relx=0.96, rely=0.875, anchor=SE)

# Main Frame
main_frame = Frame(app, width=900, height=600)
main_frame.pack()
# 1. Background
main_bg = ImageTk.PhotoImage(Image.open("img/main_screen_bg.jpg", "r").resize((900, 600)))
main_bg_label = Label(main_frame, image=main_bg)
main_bg_label.pack()

# 2. Home Button
home_button_img = ImageTk.PhotoImage(Image.open("img/home_button1.png", "r").resize((100, 100)))
home_btn = Button(main_frame, image=home_button_img, borderwidth=0, command=home_screen, bg="#000308",
                  activebackground="#000308")
home_btn.place(relx=0.05, rely=0.05, anchor=NW)

# 3. Browse Files
title_font = CTkFont(family="Lexend", size=30)
browse_files_label = Label(main_frame, text="Import Files:", font=title_font, fg="white", bg="#080d18")
browse_files_label.place(relx=0.05, rely=0.2, anchor=NW)

btn_font = CTkFont(family="Amasis MT Pto Medium", size=15)
browse_files_btn = Button(main_frame, padx=22.5, pady=5, text="Browse Files", font=btn_font, command=browse_files,
                          border=0,
                          justify=CENTER)
browse_files_btn.place(relx=0.055, rely=0.29, anchor=NW)

normal_font = CTkFont(family="Amasis MT Pto Medium", size=20)
file_name_label = Label(main_frame, text="Choose your file", font=normal_font, fg="white", bg="#080d18")
file_name_label.place(relx=0.05, rely=0.38, anchor=NW)

# 4. Processing
testfilename = []
test_btn = Button(main_frame, padx=15, pady=5, text="Start Test", font=btn_font, command=process, border=0,
                  justify=CENTER)
test_btn.place(relx=0.055, rely=0.46, anchor=NW)

# 5. Result
result_label = Label(main_frame, text="Result:", font=title_font, fg="white", bg="#080d18")
result_label.place(relx=0.05, rely=0.57, anchor=NW)

last_label = Label(main_frame, font=normal_font, fg="white", bg="#151621")
last_label.place(relx=0.05, rely=0.70, anchor=NW)

# 6. Reset
reset_button = Button(main_frame, padx=15, pady=5, text="Try New Test", font=btn_font, border=0, command=reset,
                      justify=CENTER)
reset_button.place(relx=0.5, rely=0.9, anchor=N)
# ---------------------------------------------------------------------------------------------------------------------#
app.mainloop()

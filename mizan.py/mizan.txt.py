from tkinter import *

main_window = Tk()
main_window.geometry('200x200')
thelabel = Label(main_window, text = "Applikasi Hitung BMI")
thelabel.pack()

lbl_username = Label(main_window, text = "Nama" )
lbl_userusia = Label(main_window, text = "Usia" )
input_nama = Entry(main_window, width = 20)
input_usia =Entry(main_window, width = 20)

lbl_username = Label(text="masukan nama anda")
lbl_userusia = Label(text="masukan usia anda")

btn_proses = Button(main_window, text = "Reset " )
btn_proses = Button(main_window, text = "Sumbit " )

main_window.mainloop()
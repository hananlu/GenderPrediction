import tkinter
from tkinter import ttk
from tkinter.constants import END
from PIL import ImageTk, Image
from sklearn import tree
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split # Import train_test_split function

# #Mengambil dataset
df = pd.read_csv('./dataset/prediksi_gender.csv')

def hide_label(widget):
    widget.place_forget()

#Def generate
def clickgenerate():
    # # Mengambil feature dan target
    feature_cols = ['tinggi', 'berat', 'ukuran_sepatu']
    X = df[feature_cols]
    y = df['gender']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% training and 30% test

    # # memanggil metode DecisionTreeClassifier() dari onjek tree
    clf = tree.DecisionTreeClassifier(max_depth=3)
    # # training data, memanggil metode fit(param), param = data dan gender
    clf = clf.fit(X_train, y_train)

    #checking acuracy score
    yTrainPred = clf.predict(X_train)
    yTestPred =  clf.predict((X_test))
    print("Accuracy Score : ", accuracy_score(y_train, yTrainPred))

    # # memasukkan data baru untuk di prediksi
    # # memanggil metode predict([data])
    databaru = []
    databaru.extend([entry_tinggi.get(), entry_berat.get(), entry_sepatu.get()])
    y_pred = clf.predict([databaru])  # Ditampilkan untuk hasil prediksi
    print("Input Data : ",databaru)
    print("Output Data : ",y_pred)

    if y_pred == "Male":
        lbl_output.configure(image=img_pria, background='#f8f4f4')
    elif y_pred == "Female":
        lbl_output.configure(image=img_wanita, background='#f8f4f4')

#Def Clear
def clickclear():
    entry_tinggi.delete(0, END)
    entry_berat.delete(0, END)
    entry_sepatu.delete(0,END)
    lbl_output.configure(image = "", background='#f8f4f4' )
    img.configure(image = "")
    visLbl.configure(image = "", background='#f8f4f4')

def modelVisual():
    img.configure(image = imgVis, background = '#f8f4f4')
    visLbl.configure(image = lblVis, background = '#f8f4f4')

window = tkinter.Tk()
window.geometry("1200x550")
window.resizable(0,0)
window.title('Gender Guess Machine')
window.iconbitmap('./img/logogender.ico')

#Image.Tk (pop up image)
logo_pria = "./img/output_pria.png"
logo_wanita = "./img/output_wanita.png"
img_pria = ImageTk.PhotoImage(Image.open(logo_pria))
img_wanita = ImageTk.PhotoImage(Image.open(logo_wanita))

visImage = Image.open("./img/WhatsApp Image 2021-08-17 at 10.44.38.jpeg")
visImageResize = visImage.resize((500, 400), Image.ANTIALIAS)
imgVis = ImageTk.PhotoImage(visImageResize)

vislbl = Image.open("./img/lbl_visualisasi.png")
lblVis = ImageTk.PhotoImage(vislbl)

#Background Utama
background_utama = ImageTk.PhotoImage(file='./img/background1285_3entry.jpg')
bckgrd_image = tkinter.Label(window, image=background_utama)
bckgrd_image.place(x=0,y=0,relwidth=1,relheight=1)

#Entry Tinggi
entry_tinggi = tkinter.Entry(window, font=('Josefin Sans', 17), bg="#ebe8eb", borderwidth=0)
entry_tinggi.place(x=42, y=220, width=312, height=48)

#Entry Berat
entry_berat = tkinter.Entry(window, font=('Josefin Sans', 17), bg="#ebe8eb", borderwidth=0)
entry_berat.place(x=42, y=305, width=312, height=48)

#Entry sepatu
entry_sepatu = tkinter.Entry(window, font=('Josefin Sans', 17), bg="#ebe8eb", borderwidth=0)
entry_sepatu.place(x=42, y=400, width=312, height=48)

#Button Clear
button_clear = tkinter.PhotoImage(file='./img/btn_clear.png')
btn_clear = tkinter.Button(window, image=button_clear, bg="#f8f4f4", activebackground="#f8f4f4", borderwidth=0, command=clickclear)
btn_clear.place(x=80, y=455)

#Button Generate
button_generate = tkinter.PhotoImage(file='./img/btn_generate.png')
btn_generate = tkinter.Button(window, image=button_generate, command=clickgenerate, bg="#f8f4f4", activebackground="#f8f4f4", borderwidth=0)
btn_generate.place(x=211, y=455)

#Button visual model
btn_visualisasi = tkinter.PhotoImage(file='./img/btn_visualisasi.png')
button_visualisasi = tkinter.Button(window, image=btn_visualisasi, command = modelVisual, bg="#f8f4f4", activebackground="#f8f4f4", borderwidth=0)#, command=clickgenerate, bg="#f8f4f4", activebackground="#f8f4f4", borderwidth=0)
button_visualisasi.place(x=140, y=500)

#lbl Dummy Output (pop up)
global lbl_output
lbl_output = ttk.Label(window)
lbl_output.place(x=428, y=69)

# img visualisasi model
global img
img = tkinter.Label(window)
img.place(x=550, y=80)

#label visualisasi
global visLbl
visLbl = tkinter.Label(window)
visLbl.place(x=720, y = 50)

window.mainloop()


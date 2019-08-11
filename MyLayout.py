from tkinter import *

# for URL import
import webbrowser
def callback(url):
    webbrowser.open_new(url)
# ending of url define



root = Tk()
root.title('WELCOME TO MY PROFILE')
#root.geometry('200x150')

frame1=Frame(root)
frame1.pack(fill=X)

frame2=Frame(root)
frame2.pack()

#My information like and profile link

topFrame_L1 = Label(frame1, text= 'WELCOME TO MY WORLD.', font=("Arial Bold", 18), height= 1, fg= 'blue', bg = 'orange')

topFrame_L2 = Label(frame1, text=  'I am Md. Surat-E-Mostafa, Completed my MSc in Biomedical Engineering: Signal and Image Processing from University of '
                               'Oulu, Finland at January 2019.'
                               'Now I am actively seeking full time opportunity.' , font=("Arial Bold", 10), height= 1, fg= 'blue', bg = 'orange')

topFrame_L3 = Label(frame1, text=  'My key skills are:'
                               '   ', font=("Arial Bold", 15), height= 1, fg= 'blue', bg = 'orange')
topFrame_L4 = Label(frame1, text=  '1. Physiological signal and Image processing'
                               '   ', font=("Arial Bold", 10), height= 1, fg= 'blue', bg = 'orange')
topFrame_L5 = Label(frame1, text=  '2. Communication Engineering '
                               '   ', font=("Arial Bold", 10), height= 1, fg= 'blue', bg = 'orange')
topFrame_L6 = Label(frame1, text=  'Programming skills: '
                               '   ', font=("Arial Bold", 15), height= 1, fg= 'blue', bg = 'orange')
topFrame_L7 = Label(frame1, text=  '1. Proficient User: Python and MATLAB'
                               '   ', font=("Arial Bold", 10), height= 1, fg= 'blue', bg = 'orange')
topFrame_L8 = Label(frame1, text=  '2. Competitive User: R Programming and C++'
                               '   ', font=("Arial Bold", 10), height= 1, fg= 'blue', bg = 'orange')
topFrame_L9 = Label(frame1, text=  '3. Basic user: Java, HTML and CSS'
                               '   ', font=("Arial Bold", 10), height= 1, fg= 'blue', bg = 'orange')

topFrame_L1.pack(fill=X)
topFrame_L2.pack(fill=X)
topFrame_L3.pack(fill=X)
topFrame_L4.pack(fill=X)
topFrame_L5.pack(fill=X)
topFrame_L6.pack(fill=X)
topFrame_L7.pack(fill=X)
topFrame_L8.pack(fill=X)
topFrame_L9.pack(fill=X)


topFrame2 = Label (frame1, text = 'Please Visit My Linkdin Profile For Details', font=("Arial Bold", 15), height= 3, fg= 'white', bg = 'blue' )
topFrame2.pack(fill=X)




# for url a link for linkdin
link1 = Label(frame1, text="CLICK HERE", font=("Arial Bold", 15), fg="white", bg= 'orange', cursor="hand2")
link1.pack(fill=X)
link1.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/md-surat-e-mostafa-b9184784/"))

topFrame3 = Label (frame1, text = 'Please Visit My Researchgate Profile For my Research Experince Details', font=("Arial Bold", 15), height= 3, fg= 'white', bg = 'blue' )
topFrame3.pack(fill=X)



# for url a link for linkdin
link2 = Label(frame1, text="CLICK HERE", font=("Arial Bold", 15), fg="white", bg= 'orange', cursor="hand2")
link2.pack(fill=X)
link2.bind("<Button-1>", lambda e: callback("https://www.researchgate.net/profile/Md_Surat_E-Mostafa"))

topFrame3 = Label (frame1, text = 'If you want to keep in touch with me, Please login:', font=("Arial Bold", 15), height= 3, fg= 'white', bg = 'black' )
topFrame3.pack(fill=X)


# for messagebox
#from tkinter import messagebox
#def clicked():
   # messagebox.showinfo('Follow the given link(if it does not work please copy and past new tab.', 'https://www.linkedin.com/in/md-surat-e-mostafa-b9184784/')
#btn = Button(frame2, text='CLICK HERE', command= clicked)
#btn.grid(row=1, column=1)

# Cv:pdf file upload



#login credential

bottomFrame1 =Label(frame2, text = 'User Name',fg= 'green', font=("Arial Bold", 10), height= 1)
entry1 = Entry(frame2)
bottomFrame1.grid(row=2, sticky=E)
entry1.grid(row=2, column= 1)

bottomFrame2 =Label(frame2, text = 'Password', fg= 'green', font=("Arial Bold", 10), height= 3)
entry2 = Entry(frame2)
bottomFrame2.grid(row=3, sticky=E)
entry2.grid(row=3, column= 1)

c = Checkbutton(frame2, text= 'keep me logged in')
c.grid(columnspan=10)

btn=Button(frame2,text='SUBMIT')
btn.grid(row=5,column=1)



root.mainloop()



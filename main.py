
import string
from tkinter import *

import sys
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox




import time


from instascrape import Reel
#function for download button


def download(link):
    try:
        
        if link:
            SESSIONID="31048373111%3AzGII5GQRKmLAbb%3A166" 
            headers2={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "cookie" : f'sessionId= {SESSIONID}'

            }

            google_reel = Reel(link)
            google_reel.scrape(headers=headers2)
            google_reel.download(fp= f".\\reel{int(time.time())}.mp4")
            messagebox.showinfo("Status", "Reel was downloaded successfully")
        else:
            messagebox.showwarning("Empty Field", "Please enter the link")
    except Exception as e:
        messagebox.showerror("Error", "Something went wrong, please try again later")
        print(e)

root= Tk()
root.title("Instagram Downloader")
root.minsize(800,500)
root.maxsize(800,500)
HEIGHT= 500
WIDTH= 200
FONT= font.Font(family = "Times New Roman", size = "18", weight="bold")

canvas = Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

frame = Frame(root, bg= "#4d3d73")
frame.place(relwidth=1, relheight=1)

background_image= ImageTk.PhotoImage(Image.open("C:/Users/Charlotte/Pictures/insta-search.png"))
background_image2= ImageTk.PhotoImage(Image.open("C:/Users/Charlotte/Pictures/image11.jpg"))
background_label= Label(frame,image= background_image2)
background_label.place(relx= -0.25, relwidth= 0.7, relheight=1)

FONT = font.Font(family = "Times New Roman", size = "24", weight="bold")

label1= Label(frame, text= "Instagram Downloader", font = FONT, bd = 10, fg="#cd486b", bg = "white")
label1.place(relx=0, rely=0, relheight= 0.1, relwidth= 0.45)


#label2= Label(frame, text= "Enter link address: ", font = FONT, bd=5, fg = "#e52165", bg = "white")
#label2.place(relx=0.48,rely=0.25,  relheight= 0.1, relwidth= 0.1)




entry= Entry(frame, font= FONT, fg= "#feda77", bg= "hot pink",text="enter link address")
#entry.insert(0,'enter your link')
entry.place(relx=0.45, rely=0.4, relwidth=0.4, relheight=0.1)



button1= Button(root,image= background_image , font= FONT, bg= "pink", fg= "black", activeforeground="pink", 
             activebackground="black", command= lambda:download(entry.get()))
button1.place(relx=0.84, rely=0.4, relwidth=0.08,relheight=0.1) 





#label2= Label(frame, text="Instructions: ", font= FONT, bd=5, fg="#cd486b",bg="#8134af", justify="center")
#label2.place(relx=0.68, rely=0.45, relheight=0.1)

#FONT= font.Font(family="Times New Roman", size="10", weight= "bold")
#TEXT=  "1.Only download public Instagram reels\n "\
       #"2.Enter the link for the reel to be downloaded from Instagram"

#label2= Label(frame, text= TEXT, font= FONT, bd=5, fg="#cd486b",justify="center", bg="#8134af")
#label2.place(relx=0.48, rely=0.52, relheight=0.1)

root.mainloop()
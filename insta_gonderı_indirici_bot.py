import instaloader
import tkinter as tk
from tkinter import messagebox

def download_post():
    username = entry_username.get() 

    try:
        #nesne olustur
        bot = instaloader.Instaloader()

        #profil nesnesi oluşturma
        profil = instaloader.Profile.from_username(bot.context,username) 

        #kullanıcının gönderilerini al
        posts = profil.get_posts()

        #gönderileri indir
        for index,post in enumerate(posts,1):
            bot.download_post(post , target=f"{profil.username}_{index}") #1. gönderiden itibaren postları indirir

        messagebox.showinfo("Başarılı","Gönderiler İndirildi")

    except Exception as e:
        messagebox.showerror("Hata",str(e))


# tkinter arayüz
root = tk.Tk()
root.title("İnstagram Gönderi İndirici")
root.geometry("300x200")


label = tk.Label(root,text="Kullanıcı adı:")
label.pack(pady=10)

entry_username = tk.Entry(root) 
entry_username.pack()

download_button = tk.Button(root,text="Bilgileri İndir",command=download_post)
download_button.pack(pady=10)

root.mainloop()
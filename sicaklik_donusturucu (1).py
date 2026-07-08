import tkinter as tk

def cevir():
    try:
        c=float(giris.get())
        f=c*9/5+32
        sonuc.config(text=f"{f:.1f} °F")
    except:
        sonuc.config(text="Geçersiz değer")

p=tk.Tk()
p.title("Sıcaklık Dönüştürücü")
p.geometry("320x200")
tk.Label(p,text="Santigrat (°C)").pack(pady=8)
giris=tk.Entry(p)
giris.pack()
tk.Button(p,text="Fahrenheit'e Çevir",command=cevir).pack(pady=10)
sonuc=tk.Label(p,text="",font=("Arial",16))
sonuc.pack()
p.mainloop()

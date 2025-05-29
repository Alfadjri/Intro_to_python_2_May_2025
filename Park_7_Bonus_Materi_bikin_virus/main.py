import os
import subprocess
import sys
from pathlib import Path
import time


# installasi 
try:
    from dotenv import load_dotenv
except ImportError:
    subprocess.check_call([
        sys.executable,"-m","pip","install", "--break-system-packages","python-dotenv"
    ])
    from dotenv import load_dotenv


env_path = Path(".env")
if not env_path.exists():
    with open(env_path,"w") as f:
        f.write("INSTALLED_TK = False \n")

load_dotenv()
installed = os.getenv("INSTALLED_TK","False") == "True"

try : 
    import tkinter as tk
    from tkinter import messagebox
    tkinter_available = True
except ImportError:
    tkinter_available = False
    

if not installed or not tkinter_available:
    print("Tkinter tidak di temukan.Mencoba installasi......")
    try:
        if sys.platform.startswith("linux"):
            subprocess.check_call(["sudo","apt-get","install",'-y',"python3-tk"])
        elif sys.platform == "win32":
            print("Tkinter biasanya sudah tersedi di windws.silahkan resinstall python dari python.org jika belum ada")
        elif sys.platform == "darwin":
            print("untuk macOS gunakan installer resmi dari python.or yang sudah termasuk tkinter")
    except Exception as e:
        print(f"Gagal installasi Tkinter : {e}")
    
    with open(env_path,"w") as f:
        f.write("INSTALLED_TK=True\n")
        
        
try :
    import tkinter as tk
    from tkinter import messagebox
    def tampilan_popup():
        root = tk.Tk()
        root.withdraw()
        while True:
            popup = tk.Toplevel()
            popup.withdraw()
            popup.attributes("-topmost",True)
            popup.after(0,lambda:popup.focus_force())
            
            keluar = messagebox.askyesno("Konfirmasi", "Apakah anda ingin keluar dari program ?",parent=popup)
            
            if keluar:
                print("Program akan di panggil ulang")
                popup.destroy()
                root.destroy()
                time.sleep(1)
                tampilan_popup()
                break
            else:
                print("testing")
                tampilan_popup()
            
            popup.destroy()
        root.destroy()
        
    if __name__  == "__main__":
        tampilan_popup()
except Exception as e:
    print(f"Tetap gagal membuat tkinter setelah install : {e}")
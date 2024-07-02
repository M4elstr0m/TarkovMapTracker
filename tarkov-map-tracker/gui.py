import sys, os
sys.path.append('packages')

if not os.path.exists("executed_previously.dat"):
    try:
        os.system("pip install pillow")
        os.system("pip install tk")
        os.system("pip install keyboard")
        with open('executed_previously.dat','w') as executed_previously:
            executed_previously.write('This file allows you to skip the pip install part')
            executed_previously.close()
    except:
        print("'pip' is not installed. Without it errors are more likely to occur!\nPlease check: https://pypi.org/project/pip/")
        pass

import tkinter as tk
import keyboard, ast, webbrowser, time
import tarkov_screenshotloader as scr

# https://github.com/M4elstr0m -> SOFTWARE CREATED BY M4ELSTR0M
# https://github.com/M4elstr0m/TarkovMapTracker

if os.name != 'nt':
    exit('Sorry this script is Windows only! (Tarkov is only on Windows)')


darkmode_bg = '#151718'
darkmode_btn_bg = '#4b4846'
darkmode_fg = '#d8d4cf'

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.obj = [scr.Customs(),scr.Factory(),scr.GroundZero(),scr.Interchange(),scr.Lab(),scr.Lighthouse(),scr.Reserve(),scr.Shoreline(),scr.Streets(),scr.Woods()]
        self.objname = ["Customs","Factory","GroundZero","Interchange","Lab","Lighthouse","Reserve","Shoreline","Streets","Woods"]
        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    self.key = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    self.auto_mode_vari =  ast.literal_eval(str(line).removesuffix('\n'))
                    self.auto_mode_str = str(line).removesuffix('\n')
                    break
            settingsfile.close()
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        left_frame = tk.Frame(self, bg=darkmode_bg)
        left_frame.pack(side="left")
        global bind_key_btn
        bind_key_btn = tk.Button(left_frame, text=f"Bind key\nCurrent key: {str.upper(self.key)}", font=("Helvetica", 18), command=self.bind_key)
        bind_key_btn.pack(side="top", pady=30, padx=30)
        bind_key_btn.config(width=18, bg=darkmode_btn_bg, fg=darkmode_fg)


        global auto_mode_btn
        self.auto_mode_var = self.auto_mode_vari
        auto_mode_btn = tk.Button(left_frame, text=f"AutoMode\nActivated: {self.auto_mode_str}", font=("Helvetica", 18), command=self.toggle_auto_mode)
        auto_mode_btn.pack(side="top", pady=30, padx=30)
        auto_mode_btn.config(width=18, bg=darkmode_btn_bg, fg=darkmode_fg)

        global delete_screenshots_btn
        self.press_count = 0
        delete_screenshots_btn = tk.Button(left_frame, text=f"\nDelete all screenshots\n", font=("Helvetica", 18), command=self.delete_screenshots)
        delete_screenshots_btn.pack(side="top", pady=30, padx=30)
        delete_screenshots_btn.config(width=18, bg=darkmode_btn_bg, fg=darkmode_fg, highlightbackground="#990015", highlightcolor=darkmode_fg, highlightthickness=5)

        self.credits_label = tk.Label(root, text="Created by M4elstr0m\nhttps://github.com/M4elstr0m", font=("Arial", 14), fg="gray", bg=darkmode_bg, cursor="hand2")
        self.credits_label.bind("<Button-1>", lambda e:  webbrowser.open_new("https://github.com/M4elstr0m"))
        self.credits_label.place(x=10, y=root.winfo_height() - self.credits_label.winfo_height() + 620)
        
        for i in range(10):
            btn = tk.Button(self, font=("Helvetica", 18))
            btn["text"] = f"{self.objname[i]}"
            btn["command"] = lambda i=i: self.button_clicked(i)
            btn.config(width=20, bg=darkmode_btn_bg, fg=darkmode_fg)
            btn.pack(side="top", pady=10)


    def button_clicked(self, button_number):
        self.master.destroy()
        self.start_map(button_number)

    def start_map(self, button_number):
        Coordinates = scr.getCoordinates()
        Map = self.obj[button_number].Track(Coordinates)

    def bind_key(self):
        key = keyboard.read_key()
        self.key = str(key)
        bind_key_btn["text"] = f"Bind key\nCurrent key: {str.upper(self.key)}"
        with open('settings.txt','w') as file:
            file.write(f"{self.key}\n{self.auto_mode_str}")

    def delete_screenshots(self):
        self.press_count += 1
        ScreenshotFolderPath = os.path.join(os.path.expanduser("~"), "Documents", "Escape from Tarkov", "Screenshots")
        if self.press_count == 1:
            delete_screenshots_btn["text"] = f"\nAre you sure?\n"
        if self.press_count >= 2:
            for screenshotpng in os.listdir(ScreenshotFolderPath):
                if screenshotpng.endswith(".png"):
                    os.remove(os.path.join(ScreenshotFolderPath, screenshotpng))
            self.press_count = 0
            delete_screenshots_btn["text"] = f"\nScreenshots deleted successfully!\n"
            time.sleep(2.5)
            delete_screenshots_btn["text"] = f"\nDelete all screenshots\n"

    def toggle_auto_mode(self):
        self.auto_mode_var = not self.auto_mode_var
        self.auto_mode_str = str(self.auto_mode_var)
        auto_mode_btn["text"] = f"AutoMode\nActivated: {self.auto_mode_str}"
        with open('settings.txt','w') as file:
            file.write(f"{self.key}\n{self.auto_mode_str}")

root = tk.Tk()
root.title("Tarkov Tracker by M4elstr0m")
root.config(bg=darkmode_bg)
root.geometry("720x680")
app = Application(master=root)
app.config(bg=darkmode_bg)
app.mainloop()

# https://github.com/M4elstr0m -> SOFTWARE CREATED BY M4ELSTR0M
# https://github.com/M4elstr0m/TarkovMapTracker
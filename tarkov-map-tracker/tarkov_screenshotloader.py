import glob, os, time, sys, ast
sys.path.append('packages')
import keyboard
import tkinter as tk
from PIL import Image, ImageTk

# https://github.com/M4elstr0m -> SOFTWARE CREATED BY M4ELSTR0M
# https://github.com/M4elstr0m/TarkovMapTracker

def getCoordinates():
    """Get the coordinates in a list from the screenshot in the Screenshots folder"""

    home_dir_var = os.path.expanduser("~")
    ScreenshotFolderPath = os.path.join(home_dir_var, "Documents", "Escape from Tarkov", "Screenshots")

    TarkovScreenshots = glob.glob(os.path.join(ScreenshotFolderPath, "*.png"))
    try:
        LatestScreenshot = max(TarkovScreenshots, key=os.path.getctime)
        ScreenshotFile = os.path.basename(LatestScreenshot)
        #ScreenshotFile = '2024-02-10[16-49]_205.5, 2.7, -136.1_-0.2, 0.6, 0.1, 0.8_17.83 (0).png' #CUSTOMS
        #ScreenshotFile = '2024-02-19[16-04]_-52.5, -5.5, 30.5_0.0, -1.0, 0.1, 0.2_12.54 (0).png' #GROUND ZERO
        #ScreenshotFile = '2024-02-19[16-04]_40.5, 0.5, -180.5_0.0, -1.0, 0.1, 0.2_12.54 (0).png' #INTERCHANGE
        #ScreenshotFile = '2024-02-19[16-04]_81.5, 0.5, 132_0.0, -1.0, 0.1, 0.2_12.54 (0).png' #STREETS
        #ScreenshotFile = '2024-02-19[16-04]_133.5, -5.5, 287.5_0.0, -1.0, 0.1, 0.2_12.54 (0).png' #LIGHTHOUSE
        #ScreenshotFile = '2024-06-27[16-53]_-239.2, -27.4, 186.9_0.0, 0.0, 0.0, 1.0_11.24 (0).png' #SHORELINE
        #ScreenshotFile = '2024-02-10[16-49]_62.5, 2.7, -656.1_-0.2, 0.6, 0.1, 0.8_17.83 (0).png' #WOODS
        #ScreenshotFile = '2024-02-19[16-04]_88.5, -5.5, -10.5_0.0, -1.0, 0.1, 0.2_12.54 (0).png' #RESERVE
        #ScreenshotFile = '2024-02-19[16-04]_29, -5.5, 44.0_0.0, -1.0, 0.1, 0.2_12.54 (0).png' #FACTORY WIP
        #ScreenshotFile = '2024-02-10[16-49]_-145.5, 2.7, -396.1_-0.2, 0.6, 0.1, 0.8_17.83 (0).png' #LAB WIP
        try:
            ScreenshotFile = ScreenshotFile.split("_", 1)[1]
            ScreenshotFile = ScreenshotFile.split("_", 1)[0]

            #Coordinates = [x, y, z]
            Coordinates = list(ScreenshotFile.split(", "))
        except IndexError:
            Coordinates = [-1000, 0, -1000]
            
        try:
            Coordinates[0], Coordinates[2] = float(Coordinates[0]), float(Coordinates[2])
        except ValueError or IndexError:
            Coordinates[0], Coordinates[2] = float(-1000), float(-1000)
        return Coordinates
    except ValueError or IndexError:
        Coordinates = [-1000, 0, -1000]

    if Coordinates == [-1000, 0, -1000]:
        print('WARNING: No screenshot found in /Documents/Escape From Tarkov/Screenshots')

    return Coordinates

class Customs:
    def __init__(self):
        """Initialize the tarkov Tracker for Customs"""
        self.name = "Customs"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [674.0,0.0,293.0]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        # Create the main window
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                    #SettingsHotkey = '$'
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    #SettingsAutoMode = False
                    break
            settingsfile.close()

        # Open the image to fit the canvas
        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        # Create a canvas to draw on
        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*0.95, self.beacon[2]+float(Coordinates[2])*0.95
            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()


class GroundZero:
    def __init__(self):
        """Initialize the tarkov Tracker for GroundZero"""
        self.name = "GroundZero"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [390.0,0.0,192.0]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*1.6, self.beacon[2]+float(Coordinates[2])*1.6
            
            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Interchange:
    def __init__(self):
        """Initialize the tarkov Tracker for Interchange"""
        self.name = "Interchange"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [455.0,0.0,380.0]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*0.8, self.beacon[2]+float(Coordinates[2])*0.8

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Streets:
    def __init__(self):
        """Initialize the tarkov Tracker for Streets"""
        self.name = "Streets"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [370.0,0.0,312.0]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*0.86, self.beacon[2]+float(Coordinates[2])*0.86

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Lighthouse:
    def __init__(self):
        """Initialize the tarkov Tracker for Lighthouse"""
        self.name = "Lighthouse"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [202.0,0.0,410.5]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*0.4, self.beacon[2]+float(Coordinates[2])*0.4

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Shoreline:
    def __init__(self):
        """Initialize the tarkov Tracker for Shoreline"""
        self.name = "Shoreline"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [330.0,0.0,261.5]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                    #SettingsHotkey = '$'
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    #SettingsAutoMode = False
                    break
            settingsfile.close()
                    

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*0.64, self.beacon[2]+float(Coordinates[2])*0.64

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Woods:
    def __init__(self):
        """Initialize the tarkov Tracker for Woods"""
        self.name = "Woods"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [345.0,0.0,517.5]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0])*0.57, self.beacon[2]+float(Coordinates[2])*0.57

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Reserve:
    def __init__(self):
        """Initialize the tarkov Tracker for Reserve"""
        self.name = "Reserve"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [488.0,0.0,472.0]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()

        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0]), self.beacon[2]+float(Coordinates[2])

            if x >= 730:
                x = 850
            elif x <= 121:
                x = 121
            elif float(Coordinates[0]) > 0:
                x -= 2/3*float(Coordinates[0])
            elif float(Coordinates[0]) < 0:
                x -= 2/3*float(Coordinates[0])

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Factory: #WIP
    def __init__(self):
        """Initialize the tarkov Tracker for Factory"""
        self.name = "Factory"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [345.0,0.0,375.5]
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        print('FACTORY IS IN PROGRESS -> TOTALLY WRONG COORDINATES')
        # Create the main window
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        image = ImageTk.PhotoImage(image)

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = self.beacon[0]-float(Coordinates[0]), self.beacon[2]+float(Coordinates[2])

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

class Lab: #WIP
    def __init__(self):
        """Initialize the tarkov Tracker for Lab"""
        self.name = "Lab"
        self.map = os.path.join("assets", "maps", f"{str.lower(self.name)}.png")
        self.windowtitle = self.name
        self.beacon = [370.0,0.0,640.0] #vent shaft
        self.showbeacon = False

    def Track(self, Coordinates=None):
        """Track the position of the player using the Coordinates"""
        print('LAB IS IN PROGRESS -> TOTALLY WRONG COORDINATES')
        root = tk.Tk()
        root.title(self.windowtitle)
        root.attributes("-topmost", False)

        with open('settings.txt','r') as settingsfile:
            i = 0
            for line in settingsfile:
                i += 1
                if i == 1:
                    SettingsHotkey = str.lower(line.removesuffix('\n'))
                elif i == 2:
                    SettingsAutoMode = ast.literal_eval(str(line).removesuffix('\n'))
                    break
            settingsfile.close()

        image = Image.open(self.map)
        imwidth, imheight = image.size
        
        image = ImageTk.PhotoImage(image)
        imwidth, imheight = imwidth, imheight

        canvas = tk.Canvas(root, width=imwidth, height=imheight)
        canvas.pack()
        canvas.create_image(0, 0, image=image, anchor='nw')

        def redraw_canvas():
            Coordinates = getCoordinates()
            if self.showbeacon:
                x, z = self.beacon[0], self.beacon[2]
            else:
                x, z = (self.beacon[0]-float(Coordinates[0])), (self.beacon[2]+float(Coordinates[2]))

            canvas.delete("all")
            canvas.create_image(0, 0, image=image, anchor='nw')
            canvas.create_oval(x, z, x+10, z+10, fill='red')
            canvas.create_text(x+5, z-10, fill='red', text="YOU ARE HERE")

        redraw_canvas()

        def add_hotkeys():
            keyboard.add_hotkey(f"{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"ctrl+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"maj+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"shift+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"alt+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"w+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"z+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"a+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"q+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"d+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)
            keyboard.add_hotkey(f"s+{SettingsHotkey}", lambda: (redraw_canvas()), suppress=False)

        def auto_redraw():
            if SettingsAutoMode:
                redraw_canvas()
                keyboard.press_and_release(SettingsHotkey)
                root.after(4700, auto_redraw)

        if SettingsAutoMode:
            auto_redraw()
        if not SettingsAutoMode:
            add_hotkeys()

        root.mainloop()

# https://github.com/M4elstr0m -> SOFTWARE CREATED BY M4ELSTR0M
# https://github.com/M4elstr0m/TarkovMapTracker
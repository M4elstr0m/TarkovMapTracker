## ****HUGE UPDATE COMING SOON****
## ****HUGE UPDATE COMING SOON****
## ****HUGE UPDATE COMING SOON****

# **Tarkov Map Tracker by M4elstr0m ![visitor badge](https://visitor-badge.laobi.icu/badge?page_id=M4elstr0m.TarkovMapTracker&left_text=Visitors)**
[//]:<[![Github All Releases](https://img.shields.io/github/downloads/M4elstr0m/TarkovMapTracker/total.svg)]()>
Tarkov Map Tracker is designed to help beginners to find themselves on the huge maps of <a href="https://www.escapefromtarkov.com/">Escape From Tarkov</a>
<br>I made this software because I did not find any app that really tracks your location in real time in Tarkov

<br>

**Please star this repository if you find it useful** ⭐ <br> 
Don't hesitate to reach me, or donate using the links on <a href="https://github.com/M4elstr0m/">my profile</a>, all donations are appreciated 😉
<br>

<br>There is no specific rules from Battlestate Games that does'nt allow to use screenshots, but beware if it is the case and please contact me!<br>
**This is not a cheat since it only uses screenshots from the game, but use this software on your own risks if there is a rule about this in the future ⚠️ I'm not responsible of any loss**<br>
## 🖥️ Platforms
This software is Windows-only<br>
Notice that this software is only helpful when you have Escape From Tarkov installed on your computer.

## 🛠️ Installation
**Please install Python 3.10 version or higher before installing Tarkov Map Tracker and be sure that you also have "pip" installed**<br>

Command installation (for CLI-Github users):
```bash
git clone https://github.com/M4elstr0m/TarkovMapTracker.git
```

ZIP (Archive) Installation:
1. Just download the repository by clicking on **< > Code** then click on **Download ZIP**
2. Unzip the archive using WinRAR or 7zip for example
3. Keep the folder where you want to store your **Tarkov Map Tracker**

<br>

⚠️ **If you get a missing module error, just type the command "pip install -r requirements.txt" in the main folder**

<br>

If you don't have **pip** installed yet, just type the command ```py -m ensurepip --upgrade```

## 📚 Usage
You just have to double click on "start.exe" (if Windows is blocking you just click on 'More infos' then 'Run anyway')
<br>
⚠️ **If there is not any window showing up**, maybe the problem is from the "start.exe", then you can go in the "_tarkov-map-tracker_" folder and type the following command in a terminal window: ```py gui.py``` or ```python gui.py```
<br>
<br>
- The software is tracking your position using screenshots so you have to take a screenshot and then refresh your map using the Keybind (by default "$") or not, depending on AutoMode state.<br><br>
- The software won't be able to recognize on which map you are automatically (since a screenshot does'nt have this information inside it), you have to choose the right map by yourself.<br><br>
- I suggest you to rebind your Tarkov in-game Screenshot keybind for the same as Keybind in Tarkov Map Tracker (notice that ImpScreen may not work because it triggers the Windows service himself) :  for eg if your in-game key is "M" to do a screenshot, bind the Tarkov Map Tracker with "M" as well.<br><br>

![image](https://github.com/user-attachments/assets/612e93a8-a3ac-455f-a761-2e3846520d7b)

## 🔧 Setting-up

In the GUI you have 4 types of button:

**Keybind**: You can bind a key to refresh the map (with AutoMode activated, please bind the same key as your in-game Tarkov screenshot key). "$" key by default<br><br>
**AutoMode**: Will refresh the map automatically every 5 seconds, **if the Keybind is the same as Tarkov**, it will also take a screenshot at the same time, so you don't have anything to do but looking at the map.<br><br>
**Delete Screenshots**: This button has to be pressed two times in order to fully clear **all** your Tarkov Screenshot directory.<br> **WHEN DELETED YOU CANNOT RETRIEVE YOUR FILES ANYMORE**<br>

**Maps button**: When you click on the button corresponding to a map, this map opens and either you or the software have to refresh it (depending on AutoMode state)<br><br>

Settings are also accessible from /tarkov-map-tracker/settings.txt

## 🧩 Supported Maps
<div>
<table>
  <tr>
    <th>Map</th>
    <th>Supported</th>
    <th>Software Version</th>
  </tr>
  <tr>
    <td>Customs</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Factory</td>
    <td>🚧</td>
    <td>?</td>
  </tr>
  <tr>
    <td>Ground Zero</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Interchange</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Lab</td>
    <td>🚧</td>
    <td>?</td>
  </tr>
  <tr>
    <td>Lighthouse</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Reserve</td>
    <td>✅  (not 100% accurate)</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Shoreline</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Streets</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
  <tr>
    <td>Woods</td>
    <td>✅</td>
    <td>v1.0</td>
  </tr>
</table>
</div>

## 🗒️ Credits
<a href="https://www.escapefromtarkov.com/">Escape From Tarkov</a>: this software was made for this game after all<br>
<a href="https://tarkov.dev">Tarkov.dev</a> and <a href="https://github.com/Shebuka">Shebuka</a>: for the maps used in this software and their help to check for potential copyright issues<br>
This software was made using the following Python modules: ```pillow```, ```tkinter```, ```keyboard```

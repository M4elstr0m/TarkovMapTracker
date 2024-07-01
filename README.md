# **Tarkov Map Tracker**
Tarkov Map Tracker is designed to help beginners to find themselves on the huge maps of <a href="https://www.escapefromtarkov.com/">Escape From Tarkov</a>
<br>I made this script because I did not find any app that really tracks your location in Tarkov

<br>
Don't hesitate to reach me, or donate using the links on <a href="https://github.com/M4elstr0m/">my profile</a>, all donations are appreciated 😉

## 🖥️ Platforms
This script is Windows-only
Notice that this script is only helpful when you have Escape From Tarkov installed on your computer.

## 🛠️ Installation
**Please install Python 3.10 version or higher before installing Tarkov Map Tracker**

Manual installation (not suggested):
```bash
git clone https://github.com/M4elstr0m/OneCompiler.git
```

ZIP (Archive) Installation:
1. Just download the repository by clicking on **< > Code** then click on **Download ZIP**
2. Unzip the archive using WinRAR or 7zip for example
3. Keep the folder where you want to store your **Tarkov Map Tracker**
## 📚 Usage
You just have to double click on "Start.bat"

Content of 'Start.bat':

```bash
@echo off
cd tarkov-map-tracker
start /min python ./gui.py
```
<br>
- The script is tracking your position using screenshots so you have to take a screenshot and then refresh your map using the BindKey **(by default "$")** or not, depending on AutoMode state.
- The script won't be able to recognize on which map you are automatically (since a screenshot does'nt have this information inside it), you have to choose the right map by yourself.
- I suggest you to rebind your Tarkov in-game Screenshot keybind for the same as Bindkey in Tarkov Map Tracker (notice that ImpScreen may not work because it triggers the Windows service himself) :  for eg if your in-game key is "M" to do a screenshot, bind the Tarkov Map Tracker with "M" as well.

## 🔧 Setting-up

In the GUI you have 4 types of button:

**Bind Key**: You can bind a key to refresh the map (with AutoMode activated, please bind the same key as your in-game Tarkov screenshot key)<br>
**AutoMode**: Will refresh the map automatically every 5 seconds, **if the BindKey is the same as Tarkov**, it will also take a screenshot at the same time, so you don't have anything to do but looking at the map.<br>
**Delete Screenshots**: This button has to be pressed two times in order to fully clear **all** your Tarkov Screenshot directory. **WHEN DELETED YOU CANNOT RETRIEVE YOUR FILES ANYMORE**<br>

**Maps button**: When you click on the button corresponding to a map, this map opens and either you or the script have to refresh it (depending on AutoMode state)<br>

Settings are also accessible from /tarkov-map-tracker/settings.txt

## 🧩 Supported Maps
<div>
<table>
  <tr>
    <th>Language Name</th>
    <th>Supported</th>
    <th>Version</th>
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
    <td>✅ (not 100% accurate)</td>
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
<a href="https://www.escapefromtarkov.com/">Escape From Tarkov</a> (this script was made for this game after all)<br>
<a href="https://tarkov.dev">Tarkov.dev</a> and <a href="https://github.com/Shebuka">Shebuka</a> (for the maps used in my script)<br>
This script was made using the following Python modules: ```pillow```, ```tkinter```, ```keyboard```


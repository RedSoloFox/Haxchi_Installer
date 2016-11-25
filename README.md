# Haxchi_Installer
This is a python script to help users to install haxchi.

Here is the main thread : http://gbatemp.net/threads/release-haxchi-installer-1-1-noob-friendly.448890/


#Customisation :
If you want to customise the files, you can :
- If you want different bootsound that the wii Homebrew Channel, replace : /files/sound/bootSound.btsnd
- If you want customs icons, use option 1 and replace files in : /files/icon/hax/...
- You can now change the channel name the way you want

#Included :
- Haxchi v1.8 by FIX94
- Modified wupclient.py
- A tool to find your Wii U IP adress (windows only).
- Support for buttons config (new in haxchi 1.6)

#Tutorial :
- Install Python 2.7 (Supports 3.5 since v1.2).
- Place fw.img on sd card root. (If you install haxchi it for the first time, choose a fw.img that boot on sysnand and install your NDS game via sysnand the legit way, you may use haxchi again on rednand if you want additional shortcut with another game)
- Put Homebrew Launcher in SD:\wiiu\apps
- Put CFW Booter in SD:\wiiu\apps
- Launch Homebrew launcher
- Load CFW Booter
- Unzip Haxchi_Installer.zip
- Double-click haxchi_installer_v1.1.py
- Follow instructions !
- The installation will take around 10min if you replace bootsound and icons

#Troubleshoot : 
1) The script doesnt start :
- Go in the haxchi folder. Shift + Right click --> open CMD here :
- "C:\Python27\python.exe haxchi_installer_v1.2.py"
- Make sure you have python 2.7 (or 3.5) installed

2) I get connexion error \ Program crash when installing files :
- Make sure you don't have any VPN or modem restrictions running.
- Make sure you entered the correct Wii U IP adress. If you don't know how to find it, the program will help you.

3) Other problems :
- You can ask here if you have any other problem.
- Go to check in data settings if your game is on USB or Internal Memory

4) The icons are good but the NDS game (Brain Age) starts instead :
- This is because you have an old version of the NDS game that doesnt work, try deleting it and download it again from eShop.

#Credits :
FIX94, smea, plutoo, yellows8, naehrwert, derrek, dimok and vickdu31
Big thanks to RedSoloFox for helping me !
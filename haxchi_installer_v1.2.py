from __future__ import absolute_import
from __future__ import print_function
import os
import sys
try:
    import urllib.request
except ImportError:
    import urllib
import shutil
import os.path

#Set input to raw_input
try:
    input = raw_input
except NameError:
    pass

""" WELCOME """
print("******************************")
print("*   Haxchi Installer 1.2     *")
print("******************************\n")
print("******************************")
print("*    (FIX94  Haxchi v1.8)    *")
print("*                            *")
print("*       25-nov-2016          *")
print("*                            *")
print("*   Script by Vickdu31       *")
print("* email : vickdu31@yahoo.fr  *")
print("******************************")
input("Press enter to start...")
os.system('cls' if os.name == 'nt' else 'clear') 
print("**************************************")
print("*         DISCLAIMER :               *")
print("**************************************\n")
print("**************************************")
print("*  I AM NOT RESPONSIBLE FOR BRICK    *")
print("*    DO NOT MODIFY THIS TOOL         *")
print("*                                    *")
print("*  This tool have been tested a lot  *")
print("*          It should be safe         *")
print("**************************************")
input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 


""" ASK REGION """
print("******************************")
print("*    Haxchi Installer 1.2    *")
print("******************************\n")
for retry in range(5):
    creg = input("What is your console region ? (eur/us/jap)  ").lower()
    if creg in ['eur', 'us', 'jap']:
        ansr = input("Your console region is " + creg + ". Is that correct ? (y/n)  ")
        if ansr.lower() in ['y', 'yes']:
            break
    print("\nPlease enter values correctly.\n")
else:
    sys.exit(1)


""" ASK WCHICH NDS GAME """
for retry in range(5):
    print("\nWhat NDS (eShop) game do you want to hack ?")
    print("1) Dr. Kawashima : Brain Age   2) Kirby Squeak Squad(Mouse Attack)")
    print("3) WarioWare: Touched          4) Yoshi's Island DS ")
    print("5) Maroi Kart DS               6) New Super Mario Bros DS ")
    print("7) Star Fox Command            8) Zelda Phantom Hourglass")
    print("9) Super Mario 64 DS           10) Yoshi Touch and Go")
    print("11) Big Brain Academy          12) Mario and Luigi: Partners in Time")
    print("13) DK Jungle Climber          14) Kirby Canvas Curse")
    print("15) Zelda Spirit Tracks        16) Kirby Mass Attack")
    print("17) Wario Master of Disguise \n")
    game_number = input("Enter a number :  ")
    try:
        if int(game_number)-1 in range(17):
            ansr = input("Your NDS eShop game is the game number " + game_number + ". Is that correct ? (y/n)  ")
            if ansr.lower() in ['y', 'yes']:
                break
        print("\nPlease enter number from 1 to 17.\n")
    except ValueError:
        print("\nPlease enter number from 1 to 17.\n")

else:
    sys.exit(1)


""" CALCULATING TITLEID """
print("\n*We will replace the necessary files...* \n")
# Dict Structure is {"GameTitle": ["eur_id", "us_id", "jpn_id", "GAME_NAME", "ZIPFILE"]}
game_dict = {1  : ["10179C00", "10179B00", "10179A00", "Dr. Kawashima : Brain Age", "brainage.zip"],
             2  : ["101A5700", "101A5600", "101A5500", "Kirby : Mouse Attack", "kirby.zip"],
             3  : ["101A2000", "101A1F00", "101A1E00", "WarioWare: Touched", "wwtouched.zip"],
             4  : ["10198A00", "10198900", "10198800", "Yoshi's Island DS", "yoshids.zip"],
             5  : ["10195800", "10195700", "10195600", "Mario Kart DS", "mariokartds.zip"],
             6  : ["10195B00", "10195A00", "10195900", "New Super Mario Bros", ['newsmb_eur.zip', "newsmb.zip"]],
             7  : ["101AC200", "101AC100", "101AC000", "Star Fox Command", "sfcommand.zip"],
             8  : ["101C3800", "101C3700", "101C3600", "Zelda Phantom Hourglass", "zeldaph.zip"],
             9  : ["101C3500", "101C3400", "101C3300", "Super Mario 64 DS", "sm64ds.zip"],
             10 : ["10179F00", "10179E00", "10179D00", "Yoshi Touch and Go", "yoshitouchandgo.zip"],
             11 : ["10198D00", "10198C00", "10198B00", "Big Brain Academy", "bigbrainacademy.zip"],
             12 : ["101A2300", "101A2200", "101A2100", "Mario and Luigi: Partners in Time", "partnersintime.zip"],
             13 : ["101A5400", "101A5300", "101A5200", "DK Jungle Climber", "dkjclimber.zip"],
             14 : ["101B8A00", "101B8900", "101B8800", "Kirby Canvas Curse", "kirbycanvascurse.zip"],
             15 : ["101B8D00", "101B8C00", "101B8B00", "Zelda Spirit Tracks", "zeldast.zip"],
             16 : ["101C8800", "101C8700", "101C8600", "Kirby Mass Attack", "kirbymassattack.zip"],
             17 : ["101ABF00", "101ABE00", "101ABD00", "Wario Master of Disguise", "masterofdisguise.zip"]}
if game_number == "6":
    game_name = game_dict[6][3]
    if creg == "eur":
        shutil.copy2('files/haxchi/{0}'.format(game_dict[6][4][0]), 'rom.zip')
        game_id = game_dict[6][0]
    else:
        shutil.copy2('files/haxchi/{0}'.format(game_dict[6][4][1]), 'rom.zip')
        if creg == "us":
            game_id = game_dict[6][1]
        elif creg == "jap":
            game_id = game_dict[6][2]
else:
    int_game_number = int(game_number)
    game_name = game_dict[int_game_number][3]
    shutil.copy2('files/haxchi/{0}'.format(game_dict[int_game_number][4]), "rom.zip")
    if creg == 'eur':
        game_id = game_dict[int_game_number][0]
    if creg == 'us':
        game_id = game_dict[int_game_number][1]
    if creg == 'jap':
        game_id = game_dict[int_game_number][2]


input("Please check that you now have a rom.zip file and please press enter to continue...")


""" ASK GAME LOCATION """
os.system('cls' if os.name == 'nt' else 'clear') 
print("******************************")
print("*    Haxchi Installer 1.2    *")
print("******************************\n")
for retry in range(15):
    gloc = input("Where is your game located ?\n  1) USB   2) NAND/REDNAND/INTERNAL MEMORY  ")
    if gloc == '1':
        game_storage = 'USB'
        storage_code = 'usb01'
        ansr = input("Are you sure it is on USB ? (y/n)  ")
        if ansr.lower() in ['y', 'yes']:
            break
        break
    if gloc == '2':
        game_storage = 'NAND'
        storage_code = 'mlc01'
        ansr = input("Are you sure it is on SYSNAND or REDNAND ? (y/n)  ")
        if ansr.lower() in ['y', 'yes']:
            break
        break       
    print("\nPlease enter 1 or 2.\n")
else:
    sys.exit(1)

""" DEFINE LOGO """
for retry in range(10):
    hmode = input("\nWhich icon do you want to use for " + game_name + " stored on  " + game_storage + " ?\n  1) Haxchi Icon   2) Hombrew Launcher\n  3) CFW Booter    4) Keep the current icon  ")
    if hmode in ['1', '2', '3', '4']:
        ansr = input("Are you sure ? (y/n)  ")
        if ansr.lower()in ['y', 'yes']:
            break
    print("\nPlease enter 1, 2, 3 or 4.\n")
else:
    sys.exit(1)

""" DEFINE CHANNEL NAME """    
checkmeta = '0'
if hmode == '1':
    channel_name = "Haxchi"
if hmode == '2':
    channel_name = "Homebrew Launcher"
if hmode == '3':
    channel_name = "CFW Booter" 
if hmode in ['1', '2', '3']:
    for retry in range(10):
        ansr = input("The game name will be replaced with --> " + channel_name + " <-- Do you want to change that ? (y/n)  ")
        if ansr.lower() in ['y', 'yes']:
            channel_name = input("Please enter the new channel name : ")
            ansr = input("The game name will be replaced with --> " + channel_name + " <-- Are you sure ? (y/n)  ")
            if ansr.lower() in ['y', 'yes']:
                break 
        if ansr.lower() in ['n', 'no']:
            break     
    else:
        sys.exit(1)
if hmode == '4':
    for retry in range(10):
        checkmeta = input("\nDo you want to edit game name ? (y/n)  ")
        if checkmeta.lower() in ['y', 'yes']:
            channel_name = input("Please enter the new channel name : ")
            ansr = input("The game name will be replaced with --> " + channel_name + " <-- Are you sure ? (y/n)  ")
            if ansr.lower() in ['y', 'yes']:
                checkmeta = '1'
                break
        elif checkmeta.lower() in ['no', 'n']:
            ansr = input("Are you sure you want to keep the current name ? (y/n)  ")
            if ansr.lower() in ['y', 'yes']:
                break
    else:
        sys.exit(1)


""" DEFINE BOOTSOUND """
for retry in range(10):
    sound = input("\nDo you want to use the Wii Hombrew Channel Boot Sound ? (y/n)  ")
    if sound.lower() in ['y', 'yes', 'n', 'no']:
        ansr = input("Are you sure ? (y/n)  ")
        if ansr.lower() in ['y', 'yes']:
            if sound.lower() in ['y', 'yes']:
                sound = "1"
            break
    print("\nPlease decide if you want it.\n")
else:
    sys.exit(1)


""" IP FINDER FOR USER """
for retry in range(10):
    know_ip = input("\nDo you have your Wii U IP adress somewhere ? (y/n)  ")
    if know_ip.lower() in ['y', 'yes']:
        wiiuip = input("Please write the Wii U Ip adress Ex :(192.168.x.x)\n").replace('\n', '')
        f = open('Your_Wii_U_IP.txt', 'w')
        f.write(wiiuip)
        f.close()
        break
    elif know_ip.lower() in ['n', 'no']:
        print("Downloading WNetwatcher...(800KB)")
        try:
            urllib.urlretrieve('http://www.nirsoft.net/utils/wnetwatcher.zip', "wnetwatcher.zip")
        except AttributeError:
            urllib.request.urlretrieve('http://www.nirsoft.net/utils/wnetwatcher.zip', "wnetwatcher.zip")
        print("Please open the .exe and try to find the IP address of a Nintendo device Ex.(192.168.X.X)\n"
              "Once you found it, press enter to continue\n")
        os.startfile('wnetwatcher.zip')
        input("")
        wiiuip = input("Please write the Wii U IP address (192.168.x.x)\n").replace('\n', '')
        f = open('Your_Wii_U_IP.txt', 'w')
        f.write(wiiuip)
        f.close()
        break
    print("\nChoose between yes or no...\n")
else:
    sys.exit(1)

""" IP CHECK """
for retry in range(10):
    with open('Your_Wii_U_IP.txt', 'r') as ipfile:
        ipcheck = ipfile.read().replace('\n', '')
    ansr = input("Your console IP address is -->" + ipcheck + "<--  Is that correct ? (y/n)  ")
    if ansr.lower() in ['y', 'yes']:
        break
    wiiuip = input("Please write the Wii U Ip address. Use correct format : 192.168.x.x\n").replace('\n', '')
    f = open('Your_Wii_U_IP.txt', 'w')
    f.write(wiiuip)
    f.close()  # Someone forgot to close it *Finger Wag*
else:
    sys.exit(1)

""" ASK CONFIG """
os.system('cls' if os.name == 'nt' else 'clear')
for retry in range(30):
    print("Would you like to use current config.txt ? "
          "(default configuration as below) (Apply when you start your NDS game) \n")
    print("Default (Press nothing) : /wiiu/apps/homebrew_launcher/homebrew_launcher.elf")
    print("Button A : fw.img")
    print("Button B : /rednand/fw.img")
    print("Button Y : wiiu/apps/loadiine_gx2/loadiine_gx2.elf")
    print("Button X : wiiu/apps/ftpiiu/ftpiiu.elf")
    print("Down : wiiu/apps/snes9x2010_libretro/snes9x2010_libretro.elf")
    ansr = input("\nYes to continue, no to edit the config file. (y/n)")
    if ansr.lower() in ['y', 'yes']:
        break
    if ansr.lower() in ['n', 'no']:
        os.startfile('files\config.txt')
        input("Please modify the file, SAVE IT and press enter continue")
        ansr = input("Are you sure your config file is OK and you saved it ? (y/n)  ")
        if ansr.lower() in ['y', 'yes']:
            break
        break    
    print("Please answer by yes or no...")
else:
    sys.exit(1)

""" wupclient INIT """
os.system('cls' if os.name == 'nt' else 'clear')
print("*  Initialize connection :  *\n")
print("\nWe will now try to connect to the your Wii U via Wupserver.\n"
      "\n Please make sure that :\n- Your Wii U is turned ON and connected to internet\n"
      "- You started CFW Booter using Wupserver fw.img\n- You are currently on Rednand (only if you have one)")
print("\nYour Wii U region is " + creg)
print("Your Wii U IP address is " + ipcheck)
print("The game you are hacking is " + game_name + " (Game ID : " + game_id + ")")
print("Your game is stored on " + game_storage)
if hmode in ['1', '2', '3'] or checkmeta == '1':
    print("You will replace the name --> " + game_name + " <-- by the name : --> " + channel_name + " <--\n")
input("Make sure this is correct, press enter when you are ready!")


print("\n*  Initialise connexion  *\n")

# I'll leave this so it's together
from wupclient import wupclient
wupclient = wupclient()

print("*  If an error is displayed, your IP address is wrong or the Wii U is not reachable  *\n")
input("We are now connected to WUPServer on your Wii U, press enter when you are ready!")
os.system('cls' if os.name == 'nt' else 'clear')


""" REPLACING META.XML """
if hmode in ['1', '2', '3'] or checkmeta == '1':
    print("\n* Installing files, please wait.. (Takes a while if you change logo or Boot sound...) *\n")
    PATH8 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/meta.xml"
    wupclient.dl(PATH8)
    print("\n\n* meta.xml downloaded ! *")
    from shutil import copyfile
    copyfile('meta.xml', 'meta.xml.bak')
    print("* meta.xml backup created ! *")
    import xml.etree.ElementTree as ET
    import codecs
    tree = ET.parse("meta.xml")
    root = tree.getroot()
    for child in root:
        if child.tag.startswith("longname_") or child.tag.startswith("shortname_"):
            child.text = channel_name
    with codecs.open("meta.xml", "w", "utf-8-sig") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        tree.write(f, encoding="utf-8", method="html")
    wupclient.up("meta.xml", PATH8)

""" FLASHING ROM AND CONFIG """


PATH1 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/content/0010/rom.zip"
wupclient.up("rom.zip", PATH1)


""" FLASHING BOOTSOUND"""

if sound == '1':
    PATH6 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootSound.btsnd"
    wupclient.up("files/sound/bootSound.btsnd", PATH6)


""" FLASHING ICONS """
if hmode == '1':
    PATH2 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/iconTex.tga"
    PATH3 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootDrcTex.tga"
    PATH4 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootTvTex.tga"
    wupclient.up("files/icon/hax/iconTex.tga", PATH2)
    wupclient.up("files/icon/hax/bootDrcTex.tga", PATH3)
    wupclient.up("files/icon/hax/bootTvTex.tga", PATH4)
if hmode == '2':
    PATH2 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/iconTex.tga"
    PATH3 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootDrcTex.tga"
    PATH4 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootTvTex.tga"
    wupclient.up("files/icon/hbl/iconTex.tga", PATH2)
    wupclient.up("files/icon/hbl/bootDrcTex.tga", PATH3)
    wupclient.up("files/icon/hbl/bootTvTex.tga", PATH4)
if hmode == '3':
    PATH2 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/iconTex.tga"
    PATH3 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootDrcTex.tga"
    PATH4 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootTvTex.tga"
    wupclient.up("files/icon/cfb/iconTex.tga", PATH2)
    wupclient.up("files/icon/cfb/bootDrcTex.tga", PATH3)
    wupclient.up("files/icon/cfb/bootTvTex.tga", PATH4) 
PATH5 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/content/config.txt"       
wupclient.up("files/config.txt", PATH5)        
wupclient.chmod(PATH5, 0x644)        
wupclient.kill()
print("\n* Success ! *\n")


""" GOODBYE """  
print("******************************")
print("*    Haxchi Installer 1.2    *")
print("******************************\n")
print("******************************")
print("*  You now have Haxchi v1.8  *")
print("*       On your Wii U        *")
print("******************************\n")
print("******************************")
print("*    SHUTDOWN YOUR WII U     *")
print("*   Once program is closed   *")
print("*                            *")
print("*                            *")
print("*   Script by Vickdu31       *")
print("* email : vickdu31@yahoo.fr  *")
print("******************************")
input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 

""" CREDITS """ 
print("******************************")
print("*    Haxchi Installer 1.2    *")
print("******************************\n")
print("* Your game is now replaced by Haxchi ! *\n")
print("**************************************")
print("*            CREDITS :               *")
print("**************************************\n")
print("**************************************")
print("*   @smealum for original Haxchi     *")
print("*   @smealum for iosuhax/wupserver   *")
print("*   @FIX94   for forked Haxchi       *")
print("*  @FIX94 helping me with the script *")
print("* @RedSoloFox for improving the script *")
print("**************************************")
input("Press enter to exit program...")
sys.exit()
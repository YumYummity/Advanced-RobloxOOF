def pause():
    print(Fore.GREEN + Style.BRIGHT)
    programPause = input("Press the <ENTER> key to continue...")
def complete():
    print(Fore.BLUE + Style.BRIGHT)
    print("Thank you for using YumYummity#0042's Advanced RobloxOOF script! Please star on github!")
    print(Fore.GREEN + Style.BRIGHT)
    programPause = input("Press the <ENTER> key to exit...")
try:
    import os, platform, sys, shutil
except:
    print("[!] Error while replacing: Looks like being paranoid paid off! I don't know how this happened (maybe new python version?), but it looks like you're missing one or more of the following modules: OS, PLATFORM, SYS, SHUTIL, GLOB")
    pause()
    exit()
if sys.version_info[0] != 3 or sys.version_info[1] < 10:
    print("[!] Error while replacing: This script requires Python version 3.10 or later!")
    pause()
    exit()

try:
    from colorama import Fore, Back, Style, init
    init()
except:
    os.system("pip install -U colorama")
    try:
        from colorama import Fore, Back, Style, init
        init()
        print(Fore.GREEN + "[+] Successfully installed/upgraded " + Fore.BLUE + "COLORAMA" + Fore.RESET)
    except:
        try:
            os.system("python -m pip install --upgrade pip")
            os.system("pip install -U colorama")
            print(Fore.GREEN + "[+] Successfully upgraded/installed " + Fore.BLUE + "PIP & COLORAMA" + Fore.RESET)
        except:
            print("[!] Error while replacing: PIP does not exist, or it is not in PATH! Already attempted to install PIP.")
            pause()
            exit()
try:
    import requests
    init()
except:
    os.system("pip install -U requests")
    try:
        import requests
        init()
        print(Fore.GREEN + "[+] Successfully installed/upgraded " + Fore.BLUE + "REQUESTS" + Fore.RESET)
    except:
        try:
            os.system("python -m pip install --upgrade pip")
            os.system("pip install -U requests")
            print(Fore.GREEN + "[+] Successfully upgraded/installed " + Fore.BLUE + "PIP & REQUESTS" + Fore.RESET)
        except:
            print("[!] Error while replacing: PIP does not exist, or it is not in PATH! Already attempted to install PIP.")
            pause()
            exit()

if not platform.system() == "Windows":
    print(Fore.RED + "[!] Error while replacing: " + Fore.YELLOW + "Incompatible Operating System! Requires:" + Fore.BLUE + "WINDOWS" + Fore.RESET)
    pause()
    exit()
try:
    from pathlib import Path
except:
    print(Fore.RED + "[!] Error while replacing: " + Fore.YELLOW + "Module " + Fore.BLUE + "PATHLIB" + Fore.YELLOW + " was not found!" + Fore.RESET)
    pause()
    exit()

print("")
print(Fore.GREEN + '[*] Setup succeeded! Imported OS, PLATFORM, SYS, SHUTIL, COLORAMA, and REQUESTS!' + Fore.RESET)
print("")




latestver = requests.get("http://setup.roblox.com/version").text
localappdata = os.environ['LOCALAPPDATA']
path = localappdata + "/Roblox/Versions/"
obj = Path(path + latestver)
conpath = "/content/sounds"
def replace(ver):
    content = requests.get('https://cdn.discordapp.com/attachments/1001305931864342548/1009140978789126164/Ouch2.ogg').content
    try:
        with open(ver + '\content\sounds\ouch.ogg', 'wb') as oof:
            oof.truncate(0)
            oof.write(content)
            oof.close()
    except:
        return
if obj.exists():
        version = obj
        print(Fore.GREEN + "[*] Replacing latest Roblox version! " + Fore.BLUE + latestver + Fore.RESET)
        replace(version)
        dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        hi = 0
        if len(dirs) == 0:
            print(Fore.RED + "[!] Error while replacing: " + Fore.YELLOW + "Do you have ROBLOX installed? Could not find a valid ROBLOX version at " + Fore.BLUE + path + Fore.RESET)
            pause()
            exit()
        else:
            if len(dirs) > 1:
                print(Fore.RED + Style.BRIGHT + "[Notice] Replacing multiple ROBLOX versions!" + Fore.RESET + Style.NORMAL)
            while hi < len(dirs):
                version = path + dirs[hi]
                replace(version)
                hi = hi + 1
                print(Fore.GREEN + "[*] Replacing Roblox version(s) " + Fore.BLUE + version + Fore.RESET)
else:
    try:
        print(Fore.YELLOW + "[!] Warning: Is ROBLOX updated? The next time Roblox updates, the OOF sound will be removed! Please verify you have the latest version of ROBLOX by launching!" + Fore.RESET)
        dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        hi = 0
        if len(dirs) == 0:
            print(Fore.RED + "[!] Error while replacing: " + Fore.YELLOW + "Do you have ROBLOX installed? Could not find a valid ROBLOX version at " + Fore.BLUE + path + Fore.RESET)
            pause()
            exit()
        else:
            if len(dirs) > 1:
                print(Fore.RED + Style.BRIGHT + "[Notice] Replacing multiple ROBLOX versions!" + Fore.RESET + Style.NORMAL)
            while hi < len(dirs):
                version = path + dirs[hi]
                replace(version)
                hi = hi + 1
                print(Fore.GREEN + "[*] Replacing Roblox version(s) " + Fore.BLUE + version + Fore.RESET)
    except:
        print(Fore.RED + "[!] Error while replacing: " + Fore.YELLOW + "Do you have ROBLOX installed? Could not find ROBLOX at location " + Fore.BLUE + path + Fore.RESET)
        pause()
        exit()
print(Fore.GREEN + "[*] Successfully executed!" + Fore.RESET)
print(Fore.RED + Style.BRIGHT + "[Notice] You have to run this script every time ROBLOX updates!" + Fore.RESET + Style.NORMAL)
print("")
print(Fore.BLUE + Style.BRIGHT + "[?] Have you read and agreed to the above NOTICE?" + Fore.RESET + Style.NORMAL)
yes = set(['yes','y'])
no = set(['no','n'])
while True:
    print(Fore.GREEN + Style.BRIGHT)
    yn = input("Y/N: ").lower()
    if yn in yes:
        complete()
        exit()
    elif yn in no:
        print(Fore.RED + Style.BRIGHT + "[Notice] You have to run this script every time ROBLOX updates!" + Fore.RESET + Style.NORMAL)
        print("")
        print(Fore.BLUE + Style.BRIGHT + "[?] Have you read and agreed to the above NOTICE?" + Fore.RESET + Style.NORMAL)
    else:
        print(Fore.RED + "Please respond with 'y' or 'n'!")
#### Femboy Alex CLI 


## Invasive Imports 


import sys 
import os 
import time 
import platform 
import rsa 
from secrets import choice 
import tkinter 
from typing import TextIO, IO, Callable, Final 

from colorama import Fore, Back, Style 


## Native Imports 


matter:TextIO=open("info.txt","r") 
passmat:IO=open("extras.txt","r") 
## matteredit=open("info.txt","w") 
## ^ This Clears The File. Commented Out 


## Any Constants 
pi: Final[float] = 3.14159265358 


name="" 
sexuality="" 
gender="" 
content:list=matter.readlines() 
if content != []: 
  name=content[0] or content is None 
  sexuality=content[1] or sexuality is None 
  gender=content[2] or gender is None 
  
prk="" 
encrypass=b"" 
cont:list=passmat.readlines() 
if cont != []: 
  encrypass=cont[0] or encrypass is None 
  prk=cont[1] or prk is None 
  password:bool=True 
else: 
  password:bool=False 


def cpp(file: str) -> int: 
  ## Send In As Multi-Line String For Multiple Lines Of Code 
  res: int = 0 
  matcpp: TextIO = open("csans.cpp", "w") 
  matcpp.write(file) 
  matcpp.close() 
  res = os.system("g++ -g -o csans csans.cpp") 
  res = os.system("./csans") 
  return res 


def printAex(*args: tuple) -> tuple: 
  for value in args: 
    sys.stdout.write(str(value)) 
  return args 


def retString(*args: tuple, spaces: bool = False) -> str: 
  cout: list[str] = [] 
  for value in args: 
    cout.append(str(value)) 
    if spaces: 
      ind: int = 0 
      if ind != len(args) -1: 
        cout.append(" ") 
        ind += 1 
  return "".join(cout) 


def makegui(wsize: str, title:str="") -> tkinter.Tk: 
  ## Size String Format: "WidthxHeight" 
  root: tkinter.Tk = tkinter.Tk() 
  root.geometry(wsize) 
  root.title("Alex Femboy Window " + title) 
  return root 


def printgui(window: tkinter.Tk, text: str) -> tkinter.Label: 
  label = tkinter.Label(window, text=text) 
  label.pack() 
  return label 


def buttongui(window: tkinter.Tk, text: str, gresponse:str="") -> tkinter.Button: 
  def buttaction() -> tkinter.Label: 
    ftext: str = text 
    if gresponse != "": 
      ftext = gresponse 
    return printgui(window, ftext) 
  butt: tkinter.Button = tkinter.Button(window, text=text, command=buttaction) 
  butt.pack() 
  return butt 


class astd(): 
  def __init__(self): 
    pass 
  @staticmethod 
  def basegui(text: str, title:str="") -> tkinter.Tk: 
    guiobj: tkinter.Tk = makegui("800x500", title) 
    printgui(guiobj, text) 
    return guiobj 
  @staticmethod 
  def defgui() -> tkinter.Tk: 
    return astd.basegui("Alex Femboy CLI Window Activated ") 
  @staticmethod 
  def makebutt(window: tkinter.Tk) -> tkinter.Button: 
    return buttongui(window, "Gay Sex! ") 
  @staticmethod 
  def completewin() -> tkinter.Tk: 
    stdgui: tkinter.Tk = astd.defgui() 
    astd.makebutt(stdgui) 
    stdgui.mainloop() 
    return stdgui 


def cli(line: str): 
  try: 
    global name 
    global sexuality 
    global gender 
    global data 
    match line: 
      case "help": 
        print("Welcome to the Gay Femboy CLI, By Alex. Enter \"cummands\" For Info. UwU Hehe~ ")
      case "cummands": 
        print("CUMMANDS: help, cummands, exit, delete, cumclear, run, whoami, alexfetch, datawipe, window, custwin, custwin2, c++linker, password(under works) ") 
      case "whoami": 
        if name == "": 
          cin: str = input("No User Found Hehe UwU. Create User? (Y/N): ") 
          if cin == "Y": 
            name = input("Enter Name: ") 
            sexuality=input("Gay, Bisexual, Or Pansexual?: ") 
            while sexuality != "Gay" and sexuality != "Bisexual" and sexuality != "Pansexual": 
              sexuality=input("Gay, Bisexual, Or Pansexual?: ") 
            gender=input("Male Or Enby?: ") 
            while gender != "Male" and gender != "Enby": 
              gender=input("Male Or Enby?: ") 
            matteredit: TextIO = open("info.txt", "w") 
            matteredit.write(name + "\n" + sexuality + "\n" + gender + "\n") 
            print("Hot Ass Gay User Created: \n\n", name, "\n", sexuality, "\n", gender, "\n") 
            ## File Format: Name, Sexuality, Gender
            matteredit.close() 
          else: 
            inp: str = input("UwU> ") 
            cli(inp) 
        else: 
          print("Hot Ass Gay User Found: \n\n", name, "\n", sexuality, "\n", gender, "\n") 
      case "alexfetch": 
        alexfemfetch() 
      case "alexfetchtest": 
        print() 
      case "run": 
        file: str = input("Enter File Name To Wun Hehe: ") 
        try: 
          os.system(file)
        except: 
          print("Ewwor: File Nawt Found, Or File Could Nawt Be Executed: ", file)
          cli(line)  
      case "delete": 
        file = input("Enter File Name To Delete: ") 
        try: 
          os.remove(file) 
        except: 
          print("Ewwor: File Nawt Found: ", file) 
          cli(line)
      case "password": 
        if "Windows" in platform.system(): 
          os.system("cls") 
        else: 
          os.system("") 
        print("This Is To Create A Password To Lock Your Terminal Behind. ")
        pcin: str = input("WARNING: CREATING A PASSWORD WILL LOCK ALL YOUR DATA BEHIND IT. PROCEED? (Y/N): ") 
        if pcin == "Y": 
          pacin: str = input("Enter A Password: ") 
          zlist: list[int] = [420, 666] 
          pubKey, privKey=rsa.newkeys(choice(zlist)) 
          encryptpass = rsa.encrypt(pacin.encode(),pubKey) 
          passfile = open("extras.txt", "w") 
          passfile.write(str(encryptpass)) 
          passnext=open("extras.txt", "a") 
          passnext.write("\n") 
          passnext.write(str(privKey)) 
          ## File Format: Encrypted Password, Private Key 
          passfile.close() 
          passnext.close() 
          print("Done. Your Password Is Now Encrypted And Is Now Required To Use The Terminal With The Associated Data. ") 
        else: 
          print("r", end="") 
      case "cumclear": 
        if "Windows" in platform.system():
          os.system("cls") 
        else: 
          os.system("clear") 
      case "exit": 
        print("Exiting.... ") 
        sys.exit() 
      case "window": 
        print("GUI Element Initiated.... ") 
        nwin: tkinter.Tk = astd.completewin() 
      case "custwin": 
        cox: str = input("Enter Window Content: ") 
        cox2: str = input("Enter Window Title: ") 
        astd.basegui(cox, title=cox2).mainloop() 
      case "custwin2": 
        cox1: str = input("Enter Window Content: ") 
        astd.basegui(cox1, title="Bisexual Custom Window ").mainloop() 
      case "c++linker": 
        cpplinklauncher() 
      case "filesize": 
        print(os.path.getsize("main.py"), " Bytes") 
      case "datawipe": 
        wcon: str = input("This Will Erase All Of Your Data. Proceed Anyways? (Y/N): ") 
        if wcon == "Y": 
          print("Clearing Data, Deleting User.... ")
          for i in range(11): 
            print(f"Progress: {i*10}%", end="\r") 
            time.sleep(0.6) 
          matteredit = open("info.txt", "w") 
          matteredit = open("extras.txt", "w") 
          print("Deletion Complete! ") 
  except: 
    print("Ewwor: Invalid Cummand: ", line) 
    cli(line) 
  return 0 


def alexfemfetch() -> int: 
  print("\n") 
  print("        ,'''''.\n       |   ,.  |\n       |  |  '_'\n  ,....|  |..\n.'  ,_;|   ..'\n|  |   |  |\n|  ',_,'  |\n '.     ,'\n   '''''") 
  if "Ubuntu" in platform.version(): 
    print("Ubuntu Linux Version: ", platform.version()) 
  elif "Fedora" in platform.version(): 
    print("Fedora Linux Version: ", platform.version()) 
    print("        ,'''''.\n       |   ,.  |\n       |  |  '_'\n  ,....|  |..\n.'  ,_;|   ..'\n|  |   |  |\n|  ',_,'  |\n '.     ,'\n   '''''") 
  elif "Debian" in platform.version(): 
    print("Debian Linux Version: ", platform.version()) 
  elif "Kali" in platform.version(): 
    print("Kali Linux Version: ", platform.version()) 
  elif "Arch" in platform.version(): 
    print("Arch Linux Version: ", platform.version()) 
  elif "Gentoo" in platform.version(): 
    print("Gentoo Linux Version: ", platform.version()) 
  elif "Nix" in platform.version(): 
    print("NixOS Linux Version: ", platform.version()) 
  elif "Manjaro" in platform.version(): 
    print("Manjaro Linux Version: ", platform.version()) 
  elif "FreeBSD" in platform.version(): 
    print("FreeBSD Unix Version: ", platform.version()) 
  elif "Red Hat" in platform.version(): 
    print("Red Hat Linux Version: ", platform.version()) 
  elif platform.system() == "Linux": 
    print(platform.version()) 
    print(platform.system()) 
  elif "Windows" in platform.system(): 
    print("Windows Version: ", platform.version()) 
  else: 
    print(platform.system()) 
    print(platform.version()) 
  print("CPU Architecture (Instruction Set)", platform.machine()) 
  if platform.system() == "Linux": 
    print("Linux Kernel Version: ", platform.release()) 
  else: 
    print(platform.version()) 
  print("\nAlex Femboy Furry CLI Version 0.6.9 (Beta) ")
  return 0 


## If In cli Function, Do Command Line Natively. Else, Use alexreturn() To Return To The Command Line 

def alexreturn() -> int: 
  inp: str = input("UwU> ") 
  cli(inp) 
  return 0 


def alexrestart(): 
  if __name__ == '__main__': 
    try: 
      ## os.execv(__file__, sys.argv) 
      os.system("main.py") 
    except: 
      print("Ewwor: Restart Unsuccessful UwU ")
      alexreturn() 
  return "Restart Unsuccessful UwU: File Name Not Main " 


def alexdecrypt(message, privateKey) -> str: 
  decryptpass = rsa.decrypt(message,privateKey) 
  lastly: str = decryptpass.decode() 
  return lastly 


def alexlog(checkthis:str) -> bool: 
  return checkthis == alexdecrypt(encrypass, prk) 


matter.close() ## Prevents Memory Leakage 
passmat.close() 
print("Running Python Version", sys.version)
print("Enter help For Help :3 ") 


def sepNumCum(x: int) -> str: 
  return "{:,}".format(x) 

def acpplinker(linkster: str): 
  ## Alex C++ Linker 
  ret2: str = "" 
  fnextn: list[str] = linkster.split(".") 
  fnext: str = "".join(fnextn) 
  if fnext != "cpp" or fnext != "c": 
    return "Ewwor: Invalid File Type: " + fnext + " (Only .cpp And .c Files Allowed.) \nLinker Exited With Ewwor Code 11 ", 11 
  else: 
    try: 
      ret: int = os.system("g++ -g -o main " + linkster) 
      print(os.system("g++ -g -o main " + linkster)) 
      print(os.system("./main")) 
      ret = os.system("./main") 
      print("C++ Program Completed Without Error: ", ret) 
    except: 
      print("Rip ") 
      ret: int = 18 
      ret2 = " LinkerError: Linker Fucking Failed To Execute Code. Git Gud.: " 
  return ret2, ret 

def cpplinklauncher() -> None: 
  os.system("clear") 
  print(Fore.GREEN + "Alex C++ Linker! :3 ")
  print(Fore.RED + Back.YELLOW + "Enter -options For Cummands " + Back.RESET) 
  while True: 
    link: str = input(Fore.RED + "UwU> " + Fore.RESET) 
    h: list[str] = link.split(" ") 
    hn: str = "".join(h) 
    hd: str = link[4:] 
    if link == "-exit": 
      print(Fore.RESET) 
      break 
    elif link == "-options": 
      print(Back.YELLOW + "Cummands: -exit, -link, -options " + Back.RESET) 
    elif hd == "-link": 
      acpplinker(hn) 
  return None 
  


try: 
  if not password: 
    while True: 
      inp: str = input("UwU> ") 
      cli(inp) 
  else: 
    print("NOTICE: You Have A Password. If You Cannot Or Do Not Wish To Enter The Password, You Can Create A New User. \nWarning: Doing This Will Wipe All Terminal Data. ")
    pascin: str = input("Login Or Clear Data? (Login/C): ") 
    if pascin == "Login": 
      boolvar:bool=False 
      while not boolvar: 
        passwrd: str = input("Enter Password: ") 
        if alexlog(passwrd): 
          print("Welcome Back! ") 
          boolvar=True 
          while True: 
            inp: str=input("UwU> ") 
            cli(inp) 
        else: 
          print("Incorrect Password. ") 
    else: 
      print("Clearing Data.... ")
      syswipe: TextIO = open("info.txt", "w") 
      syswipe2: IO = open("extras.txt", "w") 
      syswipe.close() 
      syswipe2.close() 
      password=False 
      alexreturn() 
        
except: 
  print("Ewwor: Unknown Reading Ewwor.") 




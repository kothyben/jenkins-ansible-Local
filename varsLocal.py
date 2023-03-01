# ----------------------------- LOCAL VARIABLES GLOBALES  -----------------------------------------------

# librairies 
import os 
import pandas as pd
import win32print, pywintypes, win32con, win32api
import wmi 
import shutil, os, glob

# Get Server Name 
c = wmi.WMI()
serverName = c.Win32_OperatingSystem()[0].CSName
print("ServerName : ....", serverName, "\n")

# tests locals paths 
global_path = r'C:\TEST_ONLY'
les_repertoires = os.listdir(global_path)
same_path = r'export\exported_configurations'
save_path = r'./'


# paths and directories
DirName = serverName
sourcePath = r'C:\Users\akiko.ext\OneDrive - GENERIX\Documents'
srcDir = r'C:\Users\akiko.ext\OneDrive - GENERIX\Documents'
dstDir = r'C:\Users\akiko.ext\OneDrive - GENERIX\Documents\{}'.format(DirName)

#-------------------------------------------------------------------------------------------
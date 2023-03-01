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
save_path = r'./'

#-------------------------------------------------------------------------------------------
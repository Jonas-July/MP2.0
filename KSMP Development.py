################################################################################
####importieren
import socket
import _thread
import time
import random
import os
import sys
import math
import shutil
import ftplib
from  tkinter import *
import pickle
import tkinter
import pygame
from pygame.locals import *
from WindowColorChange import WindowColorChangeFunction

#############################################################################################################################################################################################################################################
####Globale Variablen
def ImportVariable():
   global connected, isSecured, vol2, IsClosed, paused, label, online, offlinemode, first, activesong, backg, foreg
   online = False
   offlinemode = False
   IsClosed = False
   isSecured = False
   activesong = 50*" "
   backg = "#10186B"
   foreg = "white"
   paused = False
   vol2 = 0
   label = 2
   first = 0
   connected = 0
   
ImportVariable()


#############################################################################################################################################################################################################################################


#############################################################################################################################################################################################################################################
####Bis Anmeldefenster
def BisAnmeldung():
   global currentLanguage,langdicts,socket1,connected,doConnect
   #Pygame einstellen
   pygame.mixer.init()
   pygame.display.init()
   pygame.init()
   
   ####Dateien öffnen
   try:
      lang41 = open("options/lang.txt", "r", encoding="UTF-8")
      lang41.close()
      nl = 0
   except:
      os.mkdir("options")
      lang41 = open("options/lang.txt", "w", encoding="UTF-8")
      lang41.write("EN")
      lang41.close()
      nl = 1

   lang41 = open("options/lang.txt", "r", encoding="UTF-8")
   currentLanguage = lang41.read()
   print(currentLanguage)
   lang41.close()

   ####Internetverbindung erstellen
   try:
      socket1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   except socket.error:
      print("ERROR")
      
   def Binding():
      try:
         port=random.randint(48000,50000)
         socket1.bind(("",port))
         print("Bound to",port)
      except:
         print("Binding failed")
         Binding()
         
   Binding()

   def connect():
      global connected,connected2,IsClosed
      connected2 = False

      def TryConnect():
         global connected,connected2
         try:
            socket1.connect(("Jonas-PC",9000))#109.230.227.167
            print("Connected")
            connected = 1
            connected2 = True
      
         except:
            print("Connection failed")
            connected2 = True
                           
      def ConFen3():
         global lcon2,lcon3,confen
         confen = Tk()
         confen.title("Connecting...")
         confen.geometry("300x150")
         lcon = Label(confen,text="",bg="#7A7A7A")
         lcon.place(x=50,y=40,height=10,width=200)
         lcon2 = Label(confen,text="",bg="#545454")
         lcon2.place(x=51,y=41,height=8,width=198)
         lcon3 = Label(confen,text="",bg="#B7B7B7")
         lcon3.place(x=51,y=41,height=8,width=11)
         
         def ConFen2():
            global lcon2,lcon3,connected2,IsClosed,confen
            xcoord2=49
            xcoord=49
            a=1
            chwidth=0
            
            while a==1:
               time.sleep(0.025)
               xcoord2 += 2
               lcon2.place(x=51,y=41,height=8,width=198)
               lcon3.place(x=xcoord,y=41,height=8,width=chwidth)
               if xcoord2 <73:
                  chwidth = xcoord2-51
                  
               elif xcoord2 == 271:
                  xcoord2 = 49
                  xcoord = 49
                  chwidth= xcoord2-51
                  
               elif xcoord2 >= 249:                  
                  chwidth = 271-xcoord2
                  xcoord = xcoord2-22

               else:
                  xcoord = xcoord2-22
                  
               if connected2 == True:
                  break

            def destroycon():
               global IsClosed
               IsClosed = True
               confen.destroy()

            def tryagain():
               global connected2
               connected2 = False
               confen.destroy()
               ConFen3()
            bcon = Button(confen,text="Continue",command=destroycon)
            lcon4 = Label(confen,text="Connection failed.\nTry again later.")
            lcon5 = Label(confen,text="Connected successfully")
            bcon2 = Button(confen,text="Try Again?",command=tryagain)
            if connected == 1:
               lcon5.place(x=70,width=160,y=60,height=30)
               bcon.place(x=110,width=80,y=100,height=30)
               
            elif connected == 0:
               lcon4.place(x=70,width=160,y=60,height=30)
               bcon.place(x=155,width=80,y=100,height=30)
               bcon2.place(x=65,width=80,y=100,height=30)
            
            _thread.exit()

         _thread.start_new_thread(ConFen2,())
         _thread.start_new_thread(TryConnect,())
         confen.mainloop()

      ConFen3()
      if IsClosed == False:
         try:
            socket1.sendall(bytes("Closing~","UTF-8"))
            socket1.close()
         except:
            pass
         sys.exit()

   try:
      doConnect = int(open("options/testforconnect.txt", "r", encoding="UTF-8").readlines()[0])
   except:
      connect2 = open("options/testforconnect.txt", "w", encoding="UTF-8")
      connect2.write(str(int(True)))
      connect2.close()
      doConnect = int(open("options/testforconnect.txt", "r", encoding="UTF-8").readlines()[0])

   if doConnect:
      connect()

   def sprache2():
      lang0 = open("langdict/Sprache", "w", encoding="UTF-8")
      lang0.close()
      version = "InDev 1.01.03"
      EN = open("langdict/EN.txt", "wb")
      pickle.dump({"Version":version,"Neue Lieder":"New songs","VL":"Available songs","Ausgewählte Lieder":"Chosen songs","Eigene Lieder":"Own songs","Start":"Start","Keine Verbindung":"No connection","Lied hinzufügen":"Add song","Lied entfernen":"Remove song","Auswählen":"Select","Einstellungen":"Settings","Lautstärke":"Volume","Sprache":"Language","Auflösung":"Dimensions","Registrieren":"Register","Anmeldung":"Login","Benutzername":"Username","Passwort":"Password","Fortfahren":"Continue","Offlinemodus":"Offlinemode","Benutzername zu kurz":"Username too short","Passwort zu kurz":"Password too short","Profil":"Profile","Hilfe und Support":"Help and Support","Fülle alles aus":"Fill in all Entries","Connect":"Connect","ConnectTrue":"Do doConnect","ConnectFalse":"Do not doConnect","Anaus":"Turn On/Off","FH":"Colored Background","Aktivieren":"Activate","AI":"Additional Information","Künstler":"Creator","Songs":"Songs","by":"by","Fullscreen":"Fullscreen","NL":"Add new Song","SN":"Songtitle:","ans":"Add new song","Click":"Click on the songtitle to add a new one.","Dur":"Duration:","FN":"Filename:","desc":"Description","Finished":"Files created!","Open":"Open...","SL":"Delete Song","DC":"Do you want to delete this song?","FI":"The entries with stars(*) have to be filled.","CV":"Turn CustomVolume on","CV2":"Turn CustomVolume off","NC":"Do not use ß,ä,ö,ü or ? in the filename.","FNF":"File not found"},EN)
      EN.close()           #1                    #2               #3                                     #4                             #5                  #6                         #7                                #8                          #9                        #10                      #11                     #12                #13                    #14                         #15                    #16                    #17                   #18                     #19                       #20                                  #21                                     #22                           #23                           #24                                  #25                             #26                     #27                         #28                      #29                #30                               #31             #32                                 #33               #34          #35               #36               #37                 #38                #39                    #40                                              #41              #42                #43                      #44                     #45            #46                #47                                     #48                                                 #49                          #50                          #51                                              #52
      DE = open("langdict/DE.txt", "wb")
      pickle.dump({"Version":version,"Neue Lieder":"Neue Lieder","VL":"Verfügbare Lieder","Ausgewählte Lieder":"Ausgewählte Lieder","Eigene Lieder":"Eigene Lieder","Start":"Start","Keine Verbindung":"Keine Verbindung","Lied hinzufügen":"Lied hinzufügen","Lied entfernen":"Lied entfernen","Auswählen":"Auswählen","Einstellungen":"Einstellungen","Lautstärke":"Lautstärke","Sprache":"Sprache","Auflösung":"Dimensionen","Registrieren":"Registrieren","Anmeldung":"Anmeldung","Benutzername":"Benutzername","Passwort":"Passwort","Fortfahren":"Fortfahren","Offlinemodus":"Offlinemodus","Benutzername zu kurz":"Benutzername zu kurz","Passwort zu kurz":"Passwort zu kurz","Profil":"Profil","Hilfe und Support":"Hilfe und Support","Fülle alles aus":"Fülle alles aus", "Connect":"Verbinden","ConnectTrue":"Verbinden","ConnectFalse":"Nicht verbinden","Anaus":"An-/Ausschalten","FH":"Farblicher Hintergrund","Aktivieren":"Aktivieren","AI":"Zusätzliche Informationen","Künstler":"Künstler","Songs":"Songs","by":"von","Fullscreen":"Vollbild","NL":"Song hinzufügen","SN":"Songtitel:","ans":"Neuer Song","Click":"Klicke auf den Songtitel, um einen Song hinzuzufügen","Dur":"Dauer:","FN":"Dateiname:","desc":"Beschreibung","Finished":"Dateien erstellt!","Open":"Öffnen...","SL":"Song löschen","DC":"Willst du diesen Song löschen?","FI":"Die Felder mit Sternen(*) müssen ausgefüllt werden.","CV":"Schalte CustomVolume an","CV2":"Schalte CustomVolume aus","NC":"Du darfst ß,ä,ö,ü oder ?\nnicht im Dateinamen verwenden.","FNF":"Datei nicht gefunden"},DE)
      DE.close()
   try:
      lang0 =  open("langdict/Sprache", "w", encoding="UTF-8")
      lang0.close()

   except:
         
      def selectlanguage():
         os.mkdir("langdict")
      
         def selectlang():
            global currentLanguage
            lang1 = selectable.curselection()
            lang2 = selectable.get(lang1)
            currentLanguage = lang2
            langchange = open("options/lang.txt", "w", encoding="UTF-8")
            langchange.write(currentLanguage)
            langchange.close()
            sprache2()
            sprache.destroy()

         if nl == 1:
            sprache = Tk()
            sprache.geometry("180x200")
            selectable = Listbox(sprache,height=2)            
            lang = Button(sprache,text="Select",command=selectlang)
            selectable = Listbox(sprache,height=6)
            selectable.insert(1,"DE")
            selectable.insert(2,"EN")
            selectable.insert(3,"ES")
            selectable.insert(4,"PO")
            selectable.insert(5,"IT")
            selectable.insert(6,"FR")

            selectable.pack()
            lang.pack()
            sprache.mainloop()
         else:
            sprache2()
            
      selectlanguage()   
   language = open("langdict/"+currentLanguage+".txt", "rb")
   langdicts = pickle.load(language)
   language.close()
   try:
      if langdicts["Version"] != "InDev 1.01.04":
         shutil.rmtree("langdict")
         os.mkdir("langdict")
         sprache2()
   except:
      shutil.rmtree("langdict")
      os.mkdir("langdict")
      sprache2()

###############################################################################################################################################################################################################

BisAnmeldung()

#############################################################################################################################################################################################################################################
####Anmeldefenster
def anmeldung():
   global isActive
   isActive="Anmeldung"
   #Fenster
   af=Tk()
   af.geometry("300x300")
   af.title(langdicts["Anmeldung"])

   def Change(word):
      bitwort = ''.join(format(ord(x), 'b') for x in word)
      bitwort2 = ' '.join(format(ord(x), 'b') for x in word)
      bitwort3 = bitwort2.split(" ")
      bitwort4 = ""
      for item in bitwort3:
          bitwort4 += str(len(item))
      x = 0
      ubitwort = ""
      for a in bitwort:
          x = x+1
          add = bitwort[len(bitwort)-x]
          ubitwort = ubitwort + add
      count = 19243
      for a in ubitwort:
          if a == "0":
              count = count+1
          else:
              break
      Base64 = ["d","e","f","l","m","W","X","0","Y","Z","a","D","E","6","F","G","M","N","3","O","P","v","Q","b","c","!","?","p","q","4","r","s","7","t","u","J","K","2","L","g","w","x","H","I","1","h","n","o","A","B","5","C","R","S","T","9","U","V","i","8","j","k","y","z"]
      def convertto64(Zahl):
          Ans = ""
          x = int(math.log(Zahl,64))
          while x >= 0:
              zahl = Zahl/(64**x)
              zahl2 = Zahl%(64**x)
              Zahl = zahl2
              Ziffer = Base64[int(zahl)]
              Ans = Ans + Ziffer
              x = x-1
          return Ans
      Nullen = convertto64(count)
      bitwort5 = convertto64(float(bitwort4))
      bitcode = len(bitwort5)+34687
      bitcode2 = convertto64(bitcode)
      def convertfrom2(Zahl):
          Zahl = str(Zahl)
          a = len(Zahl)-1
          zahl2 = int(0)
          for b in Zahl:
              if b == "0":
                  a = a-1
                  continue
              zahl = int(b)*(2**int(a))
              zahl2 = zahl2 + zahl
              a = a-1
          return zahl2
      zahl10 = convertfrom2(bitwort)
      zahl64 = convertto64(zahl10)
      x = 0
      uzahl64 = ""
      for a in zahl64:
          x = x+1
          add = zahl64[len(zahl64)-x]
          uzahl64 = uzahl64 + add
      Code = bitcode2 + bitwort5 + Nullen + uzahl64
      return Code

   def login():
      global online
      Benutzer=(User.get()).strip()
      Pass=(Password.get()).strip()
      
      if Benutzer == "":
         print("Please fill all Entries!")
         
      elif Pass == "":
         print("Please fill all Entries!")
         
      if len(Benutzer)>0:
         AD="Login~"+Change(Benutzer)+","+Change(Pass)
         AD=str(AD)
         
         try:
            socket1.sendall(bytes(AD, "UTF-8"))
            Answer = socket1.recv(1024)
            Answer = bytes.decode(Answer)
            if Answer == "Correct":
               online = True
               af.destroy()
            else:
                print("Incorrect")
         except:
            print("You need an internetconnection to login")
      
         
   def offlinemodus():
      global offlinemode
      offlinemode=True
      try:
         socket1.sendall(bytes("Closing~","UTF-8"))
         socket1.close()
      except:
         pass        
      af.destroy()
      
   #########################
   ####Registrierungsfenster   
   def register():
      reg = Tk()
      wreg = 300
      hreg = 300
      reg.geometry(str(wreg)+"x"+str(hreg))
      reg.title(langdicts["Registrieren"])
      
      ####Registrierung
      def registry():
         Username=(potUser.get()).strip()
         Password=(potPass.get()).strip()
         if Username == "":
            ic = Label(reg,text=langdicts["Fülle alles aus"],fg="red")
            ic.place(x=0.8/3*wreg,y=0.75*hreg,width=1.4/3*wreg,height=20) 
         elif Password == "":
            ic = Label(reg,text=langdicts["Fülle alles aus"],fg="red")
            ic.place(x=0.8/3*wreg,y=0.75*hreg,width=1.4/3*wreg,height=20) 
         elif len(Username)>=5:
            if len(Password)>=5:
               User="Register~"+Change(Username)+","+Change(Password)
               try:
                  socket1.sendall(bytes(User,"UTF-8"))
                  isFree = socket1.recv(4096)
                  isFree = bytes.decode(isFree)
                  print(isFree)
                  isFree=isFree.split(",")
                  UserisFree = isFree[0]
                  PassisFree = isFree[1]
                  if UserisFree == "False":
                     print("Username is not free")
                  if PassisFree == "False":
                     print("Password is not free")
               except:
                  ic = Label(reg,text=langdicts["Keine Verbindung"],fg="red")
                  ic.place(x=0.8/3*wreg,y=0.75*hreg,width=1.4/3*wreg,height=20) 
            else:
               ic = Label(reg,text=langdicts["Passwort zu kurz"],fg="red")
               ic.place(x=0.8/3*wreg,y=0.75*hreg,width=1.4/3*wreg,height=20) 
         else:
            ic = Label(reg,text=langdicts["Benutzername zu kurz"],fg="red")
            ic.place(x=0.8/3*wreg,y=0.75*hreg,width=1.4/3*wreg,height=20) 
   
      #Anzeigeelemente(reg)
      canvas=Canvas(reg)
      Usernameinput=Label(reg,text=langdicts["Benutzername"]+":",bg="blue",fg="white")
      Passwordinput=Label(reg,text=langdicts["Passwort"]+":",bg="blue",fg="white")
      potUser=Entry(reg,bg="gold")
      potPass=Entry(reg,bg="gold")
      register=Button(reg,text=langdicts["Registrieren"],command=registry,bg="green",activebackground="green")

      #Erstellen(reg)
      canvas.place(x=0,y=0)
      Usernameinput.place(x=int(1/3*wreg),y=int(0.25*hreg),height=1/15*hreg)
      Passwordinput.place(x=(1/3*wreg),y=(0.4*hreg),height=(1/15*hreg))
      potUser.place(x=(1/3*wreg),y=((0.95/3)*hreg),width=(1/3*wreg),height=(1/15*hreg))
      potPass.place(x=1/3*wreg,y=1.4/3*hreg,width=1/3*wreg,height=1/15*hreg)
      register.place(x=1/3*wreg,y=1.75/3*hreg,width=1/3*wreg,height=0.25/3*hreg)
      
      #Canvaspatterns(reg)
      canvas.create_rectangle(0.8/3*wreg,0.65/3*hreg,2.20/3*wreg,0.7*hreg,fill="blue")
      mainloop()

      ###############################################################################################################################################################################################################################
      
   #Anzeigeelemente(af)
   can=Canvas(af)
   Username=Label(af,text=langdicts["Benutzername"]+":")
   Password2=Label(af,text=langdicts["Passwort"]+":")
   User=Entry(af)
   Password=Entry(af)
   Weiter=Button(af,text=langdicts["Fortfahren"],command=login)
   Offlinemode=Button(af,text=langdicts["Offlinemodus"],command=offlinemodus)
   Regis=Button(af,text=langdicts["Registrieren"],command=register)
   
   #Erstellen(af)
   can.place(x=0,y=0)
   Username.place(x=50,y=100,height=20)
   Password2.place(x=50,y=125,height=20)
   Offlinemode.place(x=145,y=150,width=80,height=25)
   User.place(x=135,y=100,width=90,height=20)
   Password.place(x=135,y=125,width=90,height=20)
   Weiter.place(x=75,y=150,width=70,height=25)
   Regis.place(x=100,y=180,width = 100,height=25)

   af.mainloop()

anmeldung()

def Anforderung_Daten():
   #Anforderung von Daten
   Data = "Data~age,lang,favor,group,chronik"
   socket1.sendall(bytes(Data,"UTF-8"))

   data1 = socket1.recv(1048576)

   data1 = bytes.decode(data1)
   data1list = data1.split(",")

   Age = data1list[0]
   if Age != "None":     
      Age = Age[2:(len(Age)-2)]
      
   favor= data1list[1]
   if favor != "None":
      favor = favor[1:len(favor)-2]
      favor = favor.split[","]

   group = data1list[2]
   if group != "None":
      group = group[2:len(group)-2]

   chronik = data1list[3]
   if chronik != "None":
      chronik = chronik[1:len(chronik)-2]
      chronik = chronik.split(",")

def Continue():   
   if online == True:
      Anforderung_Daten()

   elif online == False:
      if offlinemode == False:
         try:
            socket1.sendall(bytes("Closing~","UTF-8"))
            socket1.close()
         except:
            pass
         sys.exit()

Continue()


#############################################################################################################################################################################################################################################


#############################################################################################################################################################################################################################################
####Titeldateierstellung bzw. Lesen
def titeldatei():
   global ordner,liedzahl,songnames,ordner,included,GetSongData,songordner
   try:
      Lieder = open("music/titles.txt", "r", encoding="UTF-8").readlines()
   except:
      try:
         os.mkdir("music")
      except:
         pass
      data = open("music/titles.txt", "w", encoding="UTF-8")
      data.write("AddANewSong\n")
      data.close()
      try:
         os.mkdir("music/AddANewSong")
      except:
         pass
      ans = open("music/AddANewSong/addinfo.txt", "w", encoding="UTF-8")
      ans.write(langdicts["Click"])
      ans.close()
      ans = open("music/AddANewSong/author.txt", "w", encoding="UTF-8")
      ans.write("KisumSoft")
      ans.close()
      ans = open("music/AddANewSong/desc.txt", "w", encoding="UTF-8")
      ans.write("This is a very nice song. You should try it!")
      ans.close()
      ans = open("music/AddANewSong/duration.txt", "w", encoding="UTF-8")
      ans.write("It does take too long to write it into this file.")#\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMaybe pressing F5?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n18:43 27.10.2016\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nF5 has worked! Hurray!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat ya doing here?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDear Diary, please make the reader leave this document.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSeriously, nothing special here!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDo you know what I took to make this document?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMaybe if I press F5 again?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n18:45 27.10.2016\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNo, it didn't help anything\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWe now have over 1000 lines, can you  please stop reading now?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThat's too much for me. I'll leave now.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThanks for reading this document and for using my program. I hope you enjoy it!\nGreetful,\nKisumSoft")
      ans.close()
      ans = open("music/AddANewSong/fileend.txt", "w", encoding="UTF-8")
      ans.write("Most songfiles end with \".mp3\". I prefer \".wav\", but I don't have enough internet.")
      ans.close()
      ans = open("music/AddANewSong/title.txt", "w", encoding="UTF-8")
      ans.write(langdicts["ans"])
      ans.close()
      ans = open("music/AddANewSong/"+langdicts["ans"]+".mp3", "w", encoding="UTF-8")
      ans.close()
      Lieder = open("music/titles.txt", "r", encoding="UTF-8").readlines()

   ordner = list() 
   for item in Lieder:
      if item == "":
         continue
      elif item[0] == "-":
         try:
            if item[len(item)-1] != "\n":
               ordner.remove(item[1:]+"\n")
            else:
               ordner.remove(item[1:len(item)-1])
            continue
         except:
            continue
      else:
         if item[len(item)-1] == "\n":
            item = item[:len(item)-1]
         ordner.append(item)
   liedzahl = len(ordner)

   songnames = list()
   for items in ordner:
      names = open("music/"+items+"/title.txt", "r", encoding="UTF-8")
      names2 = names.readlines()[0]
      songnames.append(names2)

   songordner = dict(zip(songnames,ordner))
      
   def GetSongData(ordner,value):
      if value == "Titel":
         title = open("music/"+ordner+"/title.txt", "r", encoding="UTF-8").readlines()[0]
         return title
      elif value == "Filename":
         filename = open("music/"+ordner+"/file.txt", "r", encoding="UTF-8").readlines()[0].split(".")[0]
         return filename
      elif value == "Speicherform":
         fileend = open("music/"+ordner+"/file.txt", "r", encoding="UTF-8").readlines()[0].split(".")[1]
         return fileend
      elif value == "Komponist":
         author = open("music/"+ordner+"/author.txt", "r", encoding="UTF-8").readlines()[0]
         return author
      elif value == "Dauer":
         duration = open("music/"+ordner+"/duration.txt", "r", encoding="UTF-8").readlines()[0]
         return duration
      elif value == "Addinfo":
         addinfo = open("music/"+ordner+"/addinfo.txt", "r", encoding="UTF-8").readlines()
         if addinfo == []:
            pass
         else:
            addinfo = addinfo[0]
         return addinfo

class TwoListBoxes(): 
    def __init__(self, master):
        scrollbar = Scrollbar(master, orient=VERTICAL)
        self.b10 = Listbox(master,height=int(stdh*1.1), yscrollcommand=scrollbar.set,selectmode=MULTIPLE,bg=backg,fg=foreg)
        self.b11 = Listbox(master,height=int(stdh*1.1), yscrollcommand=scrollbar.set,selectmode=MULTIPLE,bg=backg,fg=foreg)
        self.b12 = Listbox(master,height=int(stdh*1.1), yscrollcommand=scrollbar.set,selectmode=MULTIPLE,bg=backg,fg=foreg)
        scrollbar.config(command=self.yview)
        scrollbar.place(height = stdh*17.5,width = stdw*0.05,x=6*stdw+3*stdw2,y=5*stdh+5*stdh2)
        self.b10.place(x=1.5*stdw+stdw2,y=5*stdh+5*stdh2,width=1.5*stdw)
        self.b11.place(x=1.5*stdw+stdw2+1.5*stdw,y=5*stdh+5*stdh2,width=1.5*stdw)
        self.b12.place(x=1.5*stdw+stdw2+3*stdw,y=5*stdh+5*stdh2,width=1.5*stdw)
    
    def yview(self, *args):
        self.b10.yview(*args)
        self.b11.yview(*args)
        self.b12.yview(*args)

##############################################################################################################################################################################################################################################

        
#############################################################################################################################################################################################################################################
####Hauptfenster
def Fenster():
   global fenster,wfen,hfen,vol,language,stdw,stdw2,stdh,stdh2,cvtextvar,has2
   fenster = Tk()
   try:
      reso = open("options/dim.txt", "r", encoding="UTF-8").readlines()
   ##   if reso[2] == "Fullscreen":
   ##      wm.attributes(fenster,"-fullscreen",True)
##      else:
      wfen = reso[0]
      wfen = int((wfen[:(len(wfen)-1)]))
      hfen = reso[1]
      hfen = int(hfen)
   except:
      reso = open("options/dim.txt", "w", encoding="UTF-8")
      reso.write("1200\n750")
      reso.close()
      reso = open("options/dim.txt", "r", encoding="UTF-8").readlines()
      wfen = reso[0]
      wfen = int(wfen[:(len(wfen)-1)])
      hfen = int(reso[1])   
   fenster.geometry(str(wfen)+"x"+str(hfen))
   
   try:
      vol = open("options/vol.txt", "r", encoding="UTF-8").readlines()
      vol = vol[0]
      vol = float(vol)
   except:
      vol = open("options/vol.txt", "w", encoding="UTF-8")
      vol.write("0.7")
      vol.close()
      vol = open("options/vol.txt", "r", encoding="UTF-8").readlines()
      vol = float(vol[0])

   try:
      cv = open("options/CustomVolume.txt", "r", encoding="UTF-8")
      cv2 = cv.readline()
      cv.close()
   except:
      cv = open("options/CustomVolume.txt", "w", encoding="UTF-8")
      cv.write("False")
      cv.close()
      cv2 = "False"

   try:
      has = open("options/HaS.txt", "r", encoding="UTF-8")
      has2 = has.readline()
      has.close()
   except:
      has = open("options/HaS.txt", "w", encoding="UTF-8")
      has2 = has.write("show")
      has.close()
      has = open("options/HaS.txt", "r", encoding="UTF-8")
      has2 = has.readline()
      has.close()

   fenster.title("KS Musicplayer")
   newFrame = Label(fenster,text="",bg=backg,fg=foreg)
   language = open("langdict/"+currentLanguage+".txt", "rb")
   langdicts = pickle.load(language)
   language.close()
   stdw=wfen/9
   stdw2=wfen/450
   stdh=hfen/26
   stdh2= hfen*0.0026
   
   if cv2 == "True":
      cvtextvar = "CV2"
   else:
      cvtextvar = "CV"

def Mainwindow():
   titeldatei()
   global x,included2,z,y,yx,currentsong,isActive
   isActive="Mainwindow"
   
   #Anzeigeelemente
   newFrame = Label(fenster,text="",bg=backg,fg=foreg)
   newFrame.place(x=0,y=0,width=wfen,height=hfen)
   mylistboxes = TwoListBoxes(fenster)
   author = mylistboxes.b11
   titles = mylistboxes.b10
   addinfo = mylistboxes.b12
   #stdv = StringVar()
   currentsong = Label(fenster,text = (50*" "),bg=backg,fg=foreg)
   #Enter = Entry(fenster,bg=backg,fg=foreg,textvariable=stdv)
   #stdv.set("Songname.Speicher \"Künstler\" Dauer")
   availsong = Label(fenster,text=langdicts["VL"]+":",bg=backg,fg=foreg)
   creators = Label(fenster,text=langdicts["Künstler"]+":",bg=backg,fg=foreg)
   songtitles = Label(fenster,text=langdicts["Songs"]+":",bg=backg,fg=foreg)
   addinfo2 = Label(fenster,text=langdicts["AI"]+":",bg=backg,fg=foreg)
   currentversion = Label(fenster,text="Kisumsoft MusicPlayer\nVersion: InDev 1.1.01.01",bg=backg,fg=foreg)

   def Currentsong(selectedlist):
      global currentsong,chsong,chosensongs,scroll2,chosesong
      chsong=Label(fenster,text="",bg=backg,fg=foreg)
      chosensongs=Listbox(fenster,height = int(hfen/750*21-4),bg=backg,fg=foreg,selectmode=MULTIPLE)
      scroll2 = Scrollbar(fenster,command=chosensongs.yview,bg=backg)
      chosensongs.config(yscrollcommand=scroll2.set)
      chosesong = Label(fenster,text=langdicts["Ausgewählte Lieder"]+":",bg=backg,fg=foreg)

      chsong.place(x=6*stdw+3*stdw2+stdw*0.08,y=8*stdh+8*stdh2,width=2*stdw,height=8*stdh)                            
      chosesong.place(x=6*stdw+3*stdw2+stdw*0.08,width = 2*stdw,height=stdh/2,y=7.5*stdh+7.75*stdh2)
      chosensongs.place(x=6*stdw+3*stdw2+stdw*0.08,y=8*stdh+8*stdh2,width=2*stdw)
      scroll2.place(height=7.5*stdh+4*stdh2+4*(stdh2**2)+1.5*(stdh2**3)+0.02*(stdh**2),width = stdw*0.05,y=8*stdh+8*stdh2,x=8*stdw+5.25*stdw2+stdw*0.08)

      currentsong.config(text=activesong)
      currentsong.place(x=6*stdw+4*stdw2+stdw*0.08,y=6*stdh+6*stdh2,height = stdh)

      line = len(selectedlist)
      for item in selectedlist:
         content = str(GetSongData(item,"Titel"))
         chosensongs.insert(line,content)
         line -= 1


   ####Lieder, die man haben möchte, hinzufügen(Teil 2)
   def addiere(title,creator,duration,filename,addinfo,desc):
      num = ""
      title2 = title.replace("ß","ss")
      title2 = title2.replace("ä","ae")
      title2 = title2.replace("ö","oe")
      title2 = title2.replace("ü","ue")
      title2 = title2.replace("?","")
      while True:
         try:
            os.mkdir("music/"+title2+num)
            break
         except:
            if num == "":
               num = "1"
            else:
               num = str(int(num)+1)
            continue

      ordner = open("music/"+title2+num+"/title.txt", "w", encoding="UTF-8")
      ordner.write(title)
      ordner.close()
      ordner = open("music/"+title2+num+"/author.txt", "w", encoding="UTF-8")
      ordner.write(creator)
      ordner.close()
      ordner = open("music/"+title2+num+"/duration.txt", "w", encoding="UTF-8")
      ordner.write(duration)
      ordner.close()
      ordner = open("music/"+title2+num+"/file.txt", "w", encoding="UTF-8")
      ordner.write(filename)
      ordner.close()
      ordner = open("music/"+title2+num+"/addinfo.txt", "w", encoding="UTF-8")
      ordner.write(addinfo)
      ordner.close()
      ordner = open("music/"+title2+num+"/desc.txt", "w", encoding="UTF-8")
      ordner.write(desc)
      ordner.close()
      file = open("music/titles.txt", "a", encoding="UTF-8")
      file.write(title2+num+"\n")
      file.close()
      finish = Label(fenster,text=langdicts["Finished"],bg=backg,fg=foreg)
      finish.place(x=0.25*stdw,y=15.5*stdh+16.5*stdh2,width=0.5*stdw,height=stdh)
      def OpenFile():
         os.startfile("music/"+title2+num)
      openfile = Button(fenster,text=langdicts["Open"],command=OpenFile,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      openfile.place(y=15.5*stdh+16.5*stdh2,x=0.75*stdw,width=0.5*stdw,height=stdh)

   ####Teil 1 des Hinzufügens
   def hinzufuegen():
      stitle = songtitle.get()
      sauthor = songauthor.get()
      sduration = songduration.get()
      sfilename = songfilename.get()
      saddinfo = songaddinfo.get()
      sdesc = songdesc.get()
      for char in sfilename:
         if char == "ß":
            notchar = Label(fenster,text=langdicts["NC"],bg=backg,fg=foreg)
            notchar.place(x=0.25*stdw,y=14.5*stdh+15.5*stdh2,width=1*stdw,height=stdh)
            sfilename = ""
            break
         elif char == "ä":
            notchar = Label(fenster,text=langdicts["NC"],bg=backg,fg=foreg)
            notchar.place(x=0.25*stdw,y=14.5*stdh+15.5*stdh2,width=1*stdw,height=stdh)
            sfilename = ""
            break
         elif char == "ö":
            notchar = Label(fenster,text=langdicts["NC"],bg=backg,fg=foreg)
            notchar.place(x=0.25*stdw,y=14.5*stdh+15.5*stdh2,width=1*stdw,height=stdh)
            sfilename = ""
            break
         elif char == "ü":
            notchar = Label(fenster,text=langdicts["NC"],bg=backg,fg=foreg)
            notchar.place(x=0.25*stdw,y=14.5*stdh+15.5*stdh2,width=1*stdw,height=stdh)
            sfilename = ""
            break
         elif char == "?":
            notchar = Label(fenster,text=langdicts["NC"],bg=backg,fg=foreg)
            notchar.place(x=0.25*stdw,y=14.5*stdh+15.5*stdh2,width=1*stdw,height=stdh)
            sfilename = ""
            break
      if stitle == "":
         print("Bitte trage einen gültigen Namen ein!")
      elif sauthor == "":
         print("Bitte trage einen gültigen Namen ein!")
      elif sduration == "":
         print("Bitte trage einen gültigen Namen ein!")
      elif sfilename == "":
         print("Bitte trage einen gültigen Namen ein!")
      else:
         addiere(stitle,sauthor,sduration,sfilename,saddinfo,sdesc)
         
   def delete():
      title = open("music/titles.txt", "a", encoding="UTF-8")
      title.write("-"+choose5ordner+"\n")
      title.close() 
      Mainwindow()

   def loeschen():
      delconf = Button(fenster,text=langdicts["DC"],command=delete,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      delconf.place(x=0.25*stdw,width=stdw,height=stdh,y=absatz*0.4*stdh+11.1*stdh+13*stdh2)

   #############################
   ####Eigentliche Abspielengine
   def playing(ordner, listOfSongs):
      global activethread,activesong,checkstate,ordner10,paused
      if activethread == False:
         activethread = True
         ordner10 = ordner

         song = GetSongData(ordner,"Speicherform")
         song2 = GetSongData(ordner,"Filename")
         song21 = GetSongData(ordner,"Titel")
         activesong = song21
         
         if isActive == "Mainwindow":
            time.sleep(0.1)
            currentsong.config(text=song21)

         cv = open("options/CustomVolume.txt", "r", encoding="UTF-8")
         cv2 = cv.readline()
         cv.close()
         if cv2 == "True":
            try:
               cvsong = open(ordner+"/CustomVolume.txt", "r", encoding="UTF-8")
               cvvol = cvsong.readline()
               cvsong.close()
            except:
               cvvol = vol
         else:
            cvvol = vol
         pygame.mixer.music.set_volume(cvvol)
         try:
            print("music/"+ordner+"/"+song2+"."+song)
            pygame.mixer.music.load("music/"+ordner+"/"+song2+"."+song)
         except:
            filenotfound = Label(fenster,text=langdicts["FNF"],fg=foreg,bg=backg)
            filenotfound.place(x=6*stdw+4*stdw2+stdw*0.08,y=6.75*stdh+8*stdh2,height=stdh)
         try:
            pygame.mixer.music.play()
         except:
            return 0
         if pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
         checkstate = 10.3

         if paused == True:
            pygame.mixer.music.unpause()
            paused = False
            timer = 0.15
            stop = Button(fenster,text="Pause",command=pause,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
            stop.place(x=6.5*stdw+7.5*stdw2+stdw*0.08,y=5*stdh+5*stdh2,width=0.5*stdw,height=stdh)
            
         def liedstelle(zeit):
            zeit2 = zeit/60
            sek2 = zeit2-int(zeit2)
            sek1 = int(sek2*60+(1/10000))
            if sek1 < int(10):
               sek1 = "0"+str(sek1)
            time=str(int(zeit2))+":"+str(sek1)
            return time
               
         def time2(ordner):
            global checkstate,active,label,liedzeit,timer
            def Has():
               global has2,liedzeit
               if has2 == "hide":
                  has2 = "show"
                  has = open("options/HaS.txt", "w", encoding="UTF-8")
                  has.write("show")
                  has.close()
               elif has2 == "show":
                  has2 = "hide"
                  liedzeit.config(text=15*" ")
                  has = open("options/HaS.txt", "w", encoding="UTF-8")
                  has.write("hide")
                  has.close()
            
            if label == 2:
               liedzeit = Button(fenster,text=15*" ",command=Has,relief=FLAT,borderwidth=0,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
               liedzeit.place(x=6*stdw+4*stdw2+stdw*0.08,y=6.75*stdh+7*stdh2,height=0.5*stdh)

               
            label = 1
            zeit0=0
            
            def Dauer(ordner):
               dauer = GetSongData(ordner,"Dauer")
               return str(dauer)
            
            dauer = Dauer(ordner)
            time.sleep(0.1)
            dauer = Dauer(ordner)
            time.sleep(0.1)
            dauer = Dauer(ordner)

            time1 = time.time()
            timer = 0
            while checkstate >= 1:
               if timer > 0:
                  time.sleep(timer)
                  timer = 0
               if dauer != Dauer(ordner10):
                  time.sleep(1)
                  if dauer != Dauer(ordner10):
                     time.sleep(1)
                     if dauer != Dauer(ordner10):
                        time.sleep(1)
                        _thread.exit()

                  
               zeit0=int((pygame.mixer.music.get_pos())/1000)  #int(round(float(str(time.time() - time1).split(".")[0])))
               
                   
               if isActive != "Mainwindow":
                  label = 0
               
               elif isActive == "Mainwindow":
                  zeit2 = liedstelle(zeit0)
                  if label == 1:
                     if has2 == "show":
                        liedzeit.config(text=zeit2+"/"+dauer)
                     
                  elif label == 0:
                     liedzeit = Button(fenster,text=15*" ",command=Has,relief=FLAT,borderwidth=0,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
                     liedzeit.place(x=6*stdw+4*stdw2+stdw*0.08,y=6.75*stdh+7*stdh2,height=0.5*stdh)
                     if has2 == "show":
                        liedzeit.config(text=zeit2+"/"+dauer)
                     label = 1

               time.sleep(1/120)
               
            _thread.exit()
         _thread.start_new_thread(time2,(ordner,))
         #has.place(x=6.35*stdw+4*stdw2+stdw*0.1,y=6.75*stdh+7*stdh2,width=stdw*0.25)
         time.sleep(1)
         while checkstate >= 1:
            if activethread==False:
               _thread.exit()
            time.sleep(1/120)
            if checkstate < 10:
               checkstate = pygame.mixer.music.get_busy()
            else:
               checkstate = checkstate - 0.1

         play(listOfSongs)
         _thread.exit()

   ##########################################################################################################################################################################################################################
      
   def play(liste):
      global activethread
      activethread = False
      a=random.randrange(0,len(liste))
      ordner=liste[a]
      print(GetSongData(ordner,"Titel"))
      time.sleep(0.1)
      _thread.start_new_thread(playing,(ordner, liste))

   ######################      
   ####Nach dem Auswählen
   def starting():
      global chosensongs,besetzt,z,first,activethread
      if first == 0:
         first = 1
         besetzt = 0

         def variable():
            global first
            time.sleep(3)
            first=0
            _thread.exit()

         time.sleep(0.1)
         selsongs=chosensongs.curselection()
         selectedlist = list()
         try:
            if len(selsongs) > 0:
               for item in selsongs:
                  selected2=chosensongs.get(item)
                  ordner2 = songordner[selected2]
                  selectedlist.append(ordner2)
                  
               selectedlist2 = selectedlist
               play(selectedlist2)
               besetzt = 1
               _thread.start_new_thread(variable,())
            else:
               dora = elefant

         except:
            time.sleep(0.2)
            if besetzt == 0:
               try:
                  selauthors=author.curselection()
                  selectedlist = list()
                  if len(selauthors) > 0:
                     for item in selauthors:
                        selected2=titles.get(item)
                        laenge=(len(selected2))
                        selected2=selected2[0:laenge]
                        selectedlist.append(GetSongData(selected2,"Titel"))
                        print(selectedlist)

                     Currentsong(selectedlist)
                        
                     selectedlist3 = selectedlist
                     print(selectedlist3)

                     play(selectedlist3)
                     besetzt = 1
                     _thread.start_new_thread(variable,)
                     
                  elif len(selauthors) == 0:
                     dara = elefant

               except:
                  if besetzt == 0:
                     try:
                        seltitles=titles.curselection()
                        selectedlist = list()
                        time.sleep(0.2)
                        if len(seltitles) > 0:
                           #Liste abzuspielender Lieder
                           for item in seltitles:
                              selected2 = ordner[int(item)]
                              selectedlist.append(selected2)
                        
                           Currentsong(selectedlist)
                           
                           selectedlist3=selectedlist
                           play(selectedlist3)
                           besetzt = 1
                           _thread.start_new_thread(variable,())
                           
                        else:
                           _thread.start_new_thread(variable,())
                     except:
                        print("Something happened (not)")
      elif first > 0:
         pass

   def pause():
      global paused
      pygame.mixer.music.pause()
      paused = True
      def weiter():
         global timer,paused
         pygame.mixer.music.unpause()
         paused = False
         timer = 0.15
         stop = Button(fenster,text="Pause",command=pause,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
         stop.place(x=6.5*stdw+7.5*stdw2+stdw*0.08,y=5*stdh+5*stdh2,width=0.5*stdw,height=stdh)

      unpause = Button(fenster,text="Unpause",command=weiter,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      unpause.place(x=6.5*stdw+7.5*stdw2+stdw*0.08,y=5*stdh+5*stdh2,width=0.5*stdw,height=stdh)

   ##################################################################################################################################################################################################################################

   ###############
   ####Neue Lieder
   def newsongs():
      global newFrame,isActive
      isActive="Newsongs"
      newFrame = Label(fenster,text="",bg = backg,fg=foreg)
      songs = Button(fenster,text=langdicts["Eigene Lieder"],command=Mainwindow,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      songlist = Label(fenster,text = langdicts["Neue Lieder"],bg=backg,fg=foreg)
      bsettings = Button(fenster,text = langdicts["Einstellungen"],command = settings,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bsupport = Button(fenster,text = langdicts["Hilfe und Support"],command = support,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bprofile = Button(fenster,text = langdicts["Profil"],command = profile,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)

      newFrame.place(x=0,y=0,width=wfen,height=hfen)
      songlist.place(x=0,y=0,width=stdw,height=stdh)
      songs.place(x=stdw+stdw2,y=0,width=stdw,height=stdh)
      bsettings.place(x=2*stdw+2*stdw2,y=0,width=stdw,height=stdh)
      bprofile.place(x=3*stdw+3*stdw2,y=0,width=stdw,height=stdh)
      bsupport.place(x=4*stdw+4*stdw2,y=0,width=stdw,height=stdh)
      
      if online == False:
         internet = Label(fenster,text=langdicts["Keine Verbindung"],bg=backg,fg=foreg)
         internet.place(x=0,width=wfen,y=stdh,height=hfen)
         pass
         
      else:
         Songs = "Songs~songlist"
         socket1.sendall(bytes(Songs,"UTF-8"))

         songlist = socket1.recv(1048576)
         songlist = bytes.decode(songlist)
         songlist = songlist.split("~")[1]
         songlist = songlist.split(",")
         print(songlist)
         songlist2 = list()
         ID = 0
         
         for item in songlist:
            ID += 1
            song = songlist[(len(songlist)-ID)]
            songlist2.append(song)
            
         print(songlist2)
         class TwoListBoxes2():
            def __init__(self, master):
               scrollbar = Scrollbar(master, orient=VERTICAL)
               self.b3 = Listbox(fenster,height=int(stdh*1.1), yscrollcommand=scrollbar.set,selectmode=SINGLE,bg=backg,fg=foreg)
               self.b4 = Listbox(master,height=int(stdh*1.1), yscrollcommand=scrollbar.set,selectmode=SINGLE,bg=backg,fg=foreg)
               scrollbar.config(command=self.yview)
               scrollbar.place(height = stdh*17.5,width = stdw*0.05,x=6*stdw+3*stdw2,y=5*stdh+5*stdh2)
               self.b3.place(x=2*stdw+stdw2,y=5*stdh+5*stdh2,width=2*stdw)
               self.b4.place(x=4*stdw+stdw2,y=5*stdh+5*stdh2,width=2*stdw)
            
            def yview(self, *args):
               self.b3.yview(*args)
               self.b4.yview(*args)

         listboxes = TwoListBoxes2(fenster)
         possongs = listboxes.b3
         poscreators = listboxes.b4
         yx = len(songlist2)-1
         print(yx)
         liedzahl = yx
         while yx >= 1:
            z = yx
            yx -= 1
            linie3 = songlist2[z]
            possongs.insert(z,linie3)
            continue

         def Choice():
            global songch, creator
            choose = ()
            choose3 = ()
            choose2 = ()
            choose4 = ()
            while isActive == "Newsongs":
               try:
                  choose = possongs.curselection()
               except:
                  try:
                     choose2 = poscreators.curselection()
                  except:
                     continue
                  
               if len(choose) != len(choose3):
                  #Mehr Einträge
                  if len(choose) > len(choose3):
                     for i in choose3:
                        for item in choose:
                           if item == i:
                              choose.remove(i)
                     print(choose)
                     
                     songch = possongs.get(choose[0])
                     ##Aktionen
                     sendsongch = "Songs~song,"+songch
                     socket1.sendall(bytes(sendsongch,"UTF-8"))
                     
                     songinforaw = socket1.recv(1048576)
                     songinforaw2 = bytes.decode(songinforaw)
                     songinfo2 = songinforaw2.split("~")[1]
                     songinfo = songinfo2.split(",")
                     #Icon = songinfo[x]
                     description = songinfo[0]
                     duration = songinfo[1]
                     groesse = songinfo[2]

                     ##Reset
                     choose3 = choose
                  

               elif len(choose2) > 0:
                  creator = poscreators.get(choose2[0])
                  sendcreator = "Songs~creator,"+creator
                  socket1.sendall(bytes(sendcreator,"UTF-8"))
                  
                  creatorinforaw = socket1.recv(1048576)
                  creatorinfo2 = creatorinforaw.split("~")[1]
                  creatorinfo = creatorinfo2.split(",")


         _thread.start_new_thread(Choice,())
  

   ###########################################################################################################################################################################

   #####################
   ####Hilfe und Support
   def support():
      global isActive
      isActive = "Support"
      newFrame = Label(fenster,text="",bg = backg,fg=foreg)
      songs = Button(fenster,text=langdicts["Eigene Lieder"],command=Mainwindow,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      songlist = Button(fenster,text = langdicts["Neue Lieder"],command=newsongs,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bsettings = Button(fenster,text = langdicts["Einstellungen"],command = settings,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bsupport = Label(fenster,text = langdicts["Hilfe und Support"],bg=backg,fg=foreg)
      bprofile = Button(fenster,text = langdicts["Profil"],command = profile,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)

      if online == False:
         internet = Label(fenster,text=langdicts["Keine Verbindung"],bg=backg,fg=foreg)
         internet.place(x=0,width=wfen,y=stdh,height=hfen)
         pass
         
      else:
         SupEntry = Entry(fenster)
         

         SupEntry.place(x=0.5*stdw,y=2*stdh+2*stdh2,width=2*stdw,height=stdh)
         
      newFrame.place(x=0,y=0,width=wfen,height=hfen)
      songlist.place(x=0,y=0,width=stdw,height=stdh)
      songs.place(x=stdw+stdw2,y=0,width=stdw,height=stdh)
      bsettings.place(x=2*stdw+2*stdw2,y=0,width=stdw,height=stdh)
      bprofile.place(x=3*stdw+3*stdw2,y=0,width=stdw,height=stdh)
      bsupport.place(x=4*stdw+4*stdw2,y=0,width=stdw,height=stdh)

   ###########################################################################################################################################################################

   #####################
   ####Hilfe und Support
   def profile():
      global isActive
      isActive = "Profile"
      newFrame = Label(fenster,text="",bg = backg,fg=foreg)
      songs = Button(fenster,text=langdicts["Eigene Lieder"],command=Mainwindow,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      songlist = Button(fenster,text = langdicts["Neue Lieder"],command=newsongs,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bsettings = Button(fenster,text = langdicts["Einstellungen"],command = settings,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bsupport = Button(fenster,text = langdicts["Hilfe und Support"],command = support,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      bprofile = Label(fenster,text = langdicts["Profil"],bg=backg,fg=foreg)
      
      newFrame.place(x=0,y=0,width=wfen,height=hfen)
      songlist.place(x=0,y=0,width=stdw,height=stdh)
      songs.place(x=stdw+stdw2,y=0,width=stdw,height=stdh)
      bsettings.place(x=2*stdw+2*stdw2,y=0,width=stdw,height=stdh)
      bprofile.place(x=3*stdw+3*stdw2,y=0,width=stdw,height=stdh)
      bsupport.place(x=4*stdw+4*stdw2,y=0,width=stdw,height=stdh)

      tempstats = Button(fenster,text="TempStats",bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      tempstats.place(x=0,y=1.5*stdh+stdh2,height=stdh,width=3*stdw)
                  
   #################
   ####Einstellungen
   def settings():
      global newFrame,isActive
      isActive="Settings"
      
      #############################
      ####Einstellen der Lautstärke
      def lauter():
         global vol
         if vol < 1:
            if int(vol*100) > vol*100:
               vol = (int(vol*100)+1)/100
            vol = vol+0.01
            vol1 = Label(fenster,text=int(vol*100),bg=backg,fg=foreg)
            vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
            pygame.mixer.music.set_volume(vol)
            newvol = open("options/vol.txt", "w", encoding="UTF-8")
            newvol.write(str(vol))
            newvol.close()
         
      def leiser():
         global vol
         if vol > 0:
            if int(vol*100) > vol*100:
               vol = int(vol*100)+1
            vol = vol-0.01
            vol1 = Label(fenster,text=int(vol*100),bg=backg,fg=foreg)
            vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
            pygame.mixer.music.set_volume(vol)
            newvol = open("options/vol.txt", "w", encoding="UTF-8")
            newvol.write(str(vol))
            newvol.close()

      def lauter2():
         global vol
         if vol < 0.91:
            if int(vol*100) > vol*100:
               vol = int(vol*100)+1
            vol = vol+0.1
            vol1 = Label(fenster,text=round(vol*100),bg=backg,fg=foreg)
            vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
            pygame.mixer.music.set_volume(vol)
            newvol = open("options/vol.txt", "w", encoding="UTF-8")
            newvol.write(str(vol))
            newvol.close()
         else:
            vol = 1
            vol1 = Label(fenster,text=round(vol*100),bg=backg,fg=foreg)
            vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
            pygame.mixer.music.set_volume(vol)
            newvol = open("options/vol.txt", "w", encoding="UTF-8")
            newvol.write(str(vol))
            newvol.close()            
            
      def leiser2():
         global vol
         if vol > 0.1:
            if int(vol*100) > vol*100:
               vol = int(vol*100)+1
            vol = vol-0.1
            vol1 = Label(fenster,text=round(vol*100),bg=backg,fg=foreg)
            vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
            pygame.mixer.music.set_volume(vol)
            newvol = open("options/vol.txt", "w", encoding="UTF-8")
            newvol.write(str(vol))
            newvol.close()
         else:
            vol = 0
            vol1 = Label(fenster,text=round(vol*100),bg=backg,fg=foreg)
            vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
            pygame.mixer.music.set_volume(vol)
            newvol = open("options/vol.txt", "w", encoding="UTF-8")
            newvol.write(str(vol))
            newvol.close()

      def AnAus():
         global vol,vol2
         if vol > 0:
            vol2 = vol
            vol = 0
         elif vol == 0:
            vol = vol2
         vol1 = Label(fenster,text=int(vol*100),bg=backg,fg=foreg)
         vol1.place(x=1.5*stdw+2*stdw*0.4+1.5*stdw2,y=2*stdh+2*stdh2,height=stdh,width=2*stdw/5)
         pygame.mixer.music.set_volume(vol)
         
      def CV(): #not implemented
         cv = open("options/CustomVolume.txt", "r", encoding="UTF-8")
         cv2 = cv.readline()
         cv.close()
         if cv2 == "True":
            cv = open("options/CustomVolume.txt", "w", encoding="UTF-8")
            cv.write("False")
            cv.close()
         else:
            cv = open("options/CustomVolume.txt", "w", encoding="UTF-8")
            cv.write("True")
            cv.close()


      #########################################################################################################################################
               
      ##########################
      ####Einstellen der Sprache
      def setNewLanguage(langCode):
         global tempLang
         tempLang = langCode

      def langend():
         global langdicts, language, currentLanguage
         try:
            language = open("langdict/" + tempLang + ".txt", "rb")
            langdicts = pickle.load(language)
            try:
               newlang = open("options/lang.txt", "w")
               newlang.write(tempLang)
               currentLanguage = tempLang
            finally:
               newlang.close()
               settings()
         finally:
            language.close()

      #######################################################################################################################################################

      ###########################################
      ####Einstellen der Dimensionen des Fensters
      def selectNewResolution(resolution):
         global newResolution
         newResolution = resolution
         
      def setNewResolution():
         try:
            rfile = open("options/dim.txt", "w")
            rfile.write(newResolution + "\nNoFS")
         finally:
            rfile.close()
            settings()


      #############################################################################################################################################################


      ##########################
      ####Colored Background
      def ChangeBG(changingButton):
          WindowColorChangeFunction(changingButton, [0, 0, 255])
          _thread.exit()
          
      def closeFarbBG():
         global stopColorChange
         settings()
         stopColorChange = True
         
         def secureNotToFrequentChangesOfColor():
            global isSecured
            isSecured = True
            time.sleep(0.5)
            isSecured = False
            
         _thread.start_new_thread(secureNotToFrequentChangesOfColor,())
           
      def FarbBG():
         global BnewFrame, stopColorChange, IsActive
         if isSecured != True:
            IsActive="FarbBG"
            stopColorChange = False
            BnewFrame = Button(fenster, text = "", command = closeFarbBG)
            BnewFrame   .place(x = 0, y = 0, width = wfen, height = hfen)
            _thread.start_new_thread(ChangeBG,(BnewFrame,))

      #############################################################################################################################################################


      ############################
      ####Verbinde mit Server
      def testforconnect3(doConnect):
         connect2 = open("options/testforconnect.txt", "w", encoding="UTF-8")
         connect2.write(str(int(not doConnect)))
         connect2.close()

         connecttest.config(text=langdicts["Connect"+str(bool(doConnect))])
         connecttest.config(command = lambda: testforconnect3(int(not doConnect)))
         connectionnow.config(text=langdicts["Connect"+str(not doConnect)])

      #############################################################################################################################################################


      ################################
      ####create functions for widgets      

      def createLabel(master, text, bg, fg, x, y, width, height):

         label = Label(master, text = text, bg = bg, fg = fg)
         label.place(x = x, y = y, width = width, height = height)
         
         return label


      def createButton(master, text, command, bg, fg, x, y, width, height):

         button = Button(master, text = text, command = command,
                         bg = bg, fg = fg, activebackground = bg, activeforeground = fg)
         button.place(x = x, y = y, width = width, height = height)
         
         return button


      def createRadioButtons(master, texts, command, indicatoron, bg, fg, startX, startY, incX, incY, width, height):

         variable = IntVar()
         for index in range(len(texts)):
            text = texts[index]
            realCommand = lambda: command(text)
            radioButton = Radiobutton(master, text = texts[index], variable = variable, value = index+1, command = realCommand, indicatoron = indicatoron,
                                      bg = bg, fg = fg, activebackground = bg, activeforeground = fg)
            radioButton.place(x = startX + index*incX, y = startY + index*incY, width = width, height = height)


      ################################
      ####Creation of settings widgets
      
      createLabel(fenster, text = "Clear old frame"         , bg = backg, fg = backg, x = 0               , y = 0, width = wfen, height = hfen)
      createLabel(fenster, text = langdicts["Einstellungen"], bg = backg, fg = foreg, x = 2*stdw + 2*stdw2, y = 0, width = stdw, height = stdh)
      
      createButton(fenster, text = langdicts["Eigene Lieder"], command = Mainwindow, bg = backg, fg = foreg,
                   x = stdw + stdw2    , y = 0, width = stdw, height = stdh)
      createButton(fenster, text = langdicts["Neue Lieder"], command = newsongs, bg = backg, fg = foreg, 
                   x = 0               , y = 0, width = stdw, height = stdh)
      createButton(fenster, text = langdicts["Hilfe und Support"], command = support, bg = backg, fg = foreg, 
                   x = 4*stdw + 4*stdw2, y = 0, width = stdw, height = stdh)
      createButton(fenster, text = langdicts["Profil"], command = profile, bg = backg, fg = foreg,
                   x = 3*stdw + 3*stdw2, y = 0, width = stdw, height = stdh)
      
      #Creation of volume widgets
      createLabel(fenster, text = langdicts["Lautstärke"] + ":", bg = backg, fg = foreg, x = 0.5*stdw            , y = 2*stdh + 2*stdh2, height = stdh, width = None    )
      createLabel(fenster, text = int(vol*100)                 , bg = backg, fg = foreg, x = 2.3*stdw + 1.5*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 2/5*stdw)
      
      createButton(fenster, text = "+1" , command = lauter , bg = backg, fg = foreg, 
                   x = 1.5*stdw + 3*0.4*stdw + 2*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 2/5*stdw)
      createButton(fenster, text = "-1" , command = leiser , bg = backg, fg = foreg, 
                   x = 1.5*stdw + 1*0.4*stdw + 1*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 2/5*stdw)
      createButton(fenster, text = "+10", command = lauter2, bg = backg, fg = foreg,
                   x = 1.5*stdw + 4*0.4*stdw + 3*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 2/5*stdw)
      createButton(fenster, text = "-10", command = leiser2, bg = backg, fg = foreg,
                   x = 1.5*stdw + 0*0.4*stdw + 0*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 2/5*stdw)
      
      createButton(fenster, text = langdicts["Anaus"]  , command = AnAus, bg = backg, fg = foreg,
                   x = 1.5*stdw + 5*0.4*stdw + 4*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 4/5*stdw)
      createButton(fenster, text = langdicts[cvtextvar], command = CV   , bg = backg, fg = foreg,
                   x = 2.3*stdw + 5*0.4*stdw + 5*stdw2, y = 2*stdh + 2*stdh2, height = stdh, width = 4/5*stdw)

      #Creation of language widgets
      supportedLanguages = ["EN", "DE", "IT", "ES", "FR"]
      createLabel(fenster, text = langdicts["Sprache"] + ":", bg = backg, fg = foreg, x = 0.5*stdw, y = 4*stdh + 4*stdh2, width = None    , height = stdh)
      createLabel(fenster, text = currentLanguage           , bg = backg, fg = foreg, x = 1.5*stdw, y = 4*stdh + 4*stdh2, width = 1/2*stdw, height = stdh)
      
    #  createRadioButtons(fenster, texts = supportedLanguages, command = setNewLanguage, indicatoron = False, bg = backg, fg = foreg,
    #                     startX = 1.5*stdw + 0.5*stdw + stdw2, startY = 4*stdh + 4*stdh2, incX = 0.5*stdw + 1*stdw2, incY = 0, width = 1/2*stdw, height = stdh)
      langb = IntVar()
      choselang1 = Radiobutton(fenster,text="EN",variable=langb,value=1,command=lambda: setNewLanguage("EN"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      choselang2 = Radiobutton(fenster,text="DE",variable=langb,value=2,command=lambda: setNewLanguage("DE"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      choselang3 = Radiobutton(fenster,text="IT",variable=langb,value=3,command=lambda: setNewLanguage("IT"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      choselang4 = Radiobutton(fenster,text="ES",variable=langb,value=4,command=lambda: setNewLanguage("ES"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      choselang5 = Radiobutton(fenster,text="FR",variable=langb,value=5,command=lambda: setNewLanguage("FR"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      choselang6 = Radiobutton(fenster,text="PT",variable=langb,value=6,command=lambda: setNewLanguage("PT"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      choselang1.place(x=1.5*stdw+stdw2+0.5*stdw,y=4*stdh+4*stdh2,width=stdw/2,height=stdh)
      choselang2.place(x=1.5*stdw+2*stdw2+stdw,y=4*stdh+4*stdh2,width=stdw/2,height=stdh)
      choselang3.place(x=1.5*stdw+3*stdw2+1.5*stdw,y=4*stdh+4*stdh2,width=stdw/2,height=stdh)
      choselang4.place(x=1.5*stdw+4*stdw2+2*stdw,y=4*stdh+4*stdh2,width=stdw/2,height=stdh)
      choselang5.place(x=1.5*stdw+5*stdw2+2.5*stdw,y=4*stdh+4*stdh2,width=stdw/2,height=stdh)
      choselang6.place(x=1.5*stdw+6*stdw2+3*stdw,y=4*stdh+4*stdh2,width=stdw/2,height=stdh)

      createButton(fenster, text = langdicts["Auswählen"], command = langend, bg = backg, fg = foreg,
                   x = 1.5*stdw, y = 5*stdh + 5*stdh2, width = 1/2*stdw, height = stdh)

      #Creation of resolution widgets
      supportedResolutions = ["1920x1080", "1200x750", "1680x920", "1080x760", "760x600", str(wfen) + "x" + str(hfen) + "\nFullscreen"]
      createLabel(fenster, text = langdicts["Auflösung"] + ":", bg = backg, fg = foreg, x = 0.5*stdw, y = 7*stdh + 7*stdh2, width = None, height = stdh)
      createLabel(fenster, text = str(wfen) + "x" + str(hfen) , bg = backg, fg = foreg, x = 1.5*stdw, y = 7*stdh + 7*stdh2, width = stdw, height = stdh)
      
      resVar = IntVar()
    #  createRadioButtons(fenster, texts = supportedResolutions, command = setNewResolution, indicatoron = False, bg = backg, fg = foreg,
    #                     startX = 1.5*stdw + 0.5*stdw + stdw2, startY = 4*stdh + 4*stdh2, incX = 0.5*stdw + 1*stdw2, incY = 0, width = 1/2*stdw, height = stdh)
      resolbutton1 = Radiobutton(fenster,text="1920x1080",variable=resVar,value=1,command=lambda: selectNewResolution("1920\n1080"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      resolbutton2 = Radiobutton(fenster,text="1200x750",variable=resVar,value=2,command=lambda: selectNewResolution("1200\n750"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      resolbutton3 = Radiobutton(fenster,text="1680x920",variable=resVar,value=3,command=lambda: selectNewResolution("1680\n920"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      resolbutton4 = Radiobutton(fenster,text="1080x760",variable=resVar,value=4,command=lambda: selectNewResolution("1080\n760"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      resolbutton5 = Radiobutton(fenster,text="760x600",variable=resVar,value=5,command=lambda: selectNewResolution("760\n600"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      resolbutton6 = Radiobutton(fenster,text=langdicts["Fullscreen"],variable=resVar,value=6,command=lambda: selectNewResolution(str(wfen) + "\n" + str(hfen) + "\nFullscreen"),indicatoron=False,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
      resolbutton1.place(x=1.5*stdw+2*stdw2+stdw,y=7*stdh+7*stdh2,width=stdw,height=stdh)
      resolbutton2.place(x=1.5*stdw+4*stdw2+2*stdw,y=7*stdh+7*stdh2,width=stdw,height=stdh)
      resolbutton3.place(x=1.5*stdw+6*stdw2+3*stdw,y=7*stdh+7*stdh2,width=stdw,height=stdh)
      resolbutton4.place(x=1.5*stdw+2*stdw2+stdw,y=8*stdh+8*stdh2,width=stdw,height=stdh)
      resolbutton5.place(x=1.5*stdw+4*stdw2+2*stdw,y=8*stdh+8*stdh2,width=stdw,height=stdh)
      resolbutton6.place(x=1.5*stdw+6*stdw2+3*stdw,y=8*stdh+8*stdh2,width=stdw,height=stdh)

      createButton(fenster, text = langdicts["Auswählen"], command = setNewResolution, bg = backg, fg = foreg,
                      x = 1.5*stdw, y = 8*stdh + 8*stdh2, width = stdw, height = stdh)

      #Erstellen des Farbigen Hintergrundes
      createButton(fenster, text = langdicts["Aktivieren"], command = FarbBG, bg = backg, fg = foreg, 
                   x = 1.5*stdw, y = 10*stdh + 10*stdh2, width = stdw, height = stdh)
      createLabel(fenster, text = langdicts["FH"] + ":", bg = backg, fg = foreg, x = 0.5*stdw, y = 10*stdh + 10*stdh2, width = None, height = stdh)

      #Erstellen der Verbindungselemente
      createLabel(fenster, text = langdicts["Connect"] + ":", bg = backg, fg = foreg, x = 0.5*stdw, y = 12*stdh + 12*stdh2, width = None, height = stdh)
      cfile = open("options/testforconnect.txt", "r", encoding="UTF-8")
      connect = int(cfile.readlines()[0])
      cfile.close()
      connectStatus = "Connect" + str(bool(    connect))
      connectChange = "Connect" + str(bool(not connect))
          
      connectionnow = createLabel(fenster, text = langdicts[connectStatus], bg = backg, fg = foreg, x = 1.5*stdw, y = 12*stdh + 12*stdh2, width = stdw, height = stdh)
      connecttest = createButton(fenster, text = langdicts[connectChange], command = lambda: testforconnect3(connect), bg = backg, fg = foreg,
                                 x = 1.5*stdw + 1*stdw + 2*stdw2, y = 12*stdh + 12*stdh2, width = stdw, height = stdh)



   #######################################################################################################################################################################################################
            
   #Schalter etc.
   start = Button(fenster,text=langdicts["Start"],command=starting,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   stop = Button(fenster,text="Pause",command=pause,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   #ADD = Button(fenster,text=langdicts["Lied hinzufügen"],command=hinzufuegen,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   #DELETE = Button(fenster,text=langdicts["Lied entfernen"],command = loeschen,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   
   songs = Label(fenster,text=langdicts["Eigene Lieder"],bg=backg,fg=foreg)
   songlist = Button(fenster,text = langdicts["Neue Lieder"],command = newsongs,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   bsettings = Button(fenster,text = langdicts["Einstellungen"],command = settings,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   bsupport = Button(fenster,text = langdicts["Hilfe und Support"],command = support,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
   bprofile = Button(fenster,text = langdicts["Profil"],command = profile,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)

   #Erstellung der Listboxanzeige(Verfügbare Titel)
   for item in ordner:
      zeile = ordner.index(item)
      linie = GetSongData(item,"Titel")
      linie = str(linie)
      titles.insert(zeile,linie)
      
   #Erstellung der Listboxanzeige(Komponisten)
   for item in ordner:
      zeile = ordner.index(item)
      linie = GetSongData(item,"Komponist")
      author.insert(zeile,linie)

   #Erstellung der Listboxanzeige(Addinfo)
   for item in ordner:
      zeile = ordner.index(item)
      linie = GetSongData(item,"Addinfo")
      addinfo.insert(zeile,linie)

   Currentsong(list())
   
   #Festsetzen
   songlist.place(x=0,y=0,width=stdw,height=stdh)
   songs.place(x=stdw+stdw2,y=0,width=stdw,height=stdh)
   bsettings.place(x=2*stdw+2*stdw2,y=0,width=stdw,height=stdh)
   bprofile.place(x=3*stdw+3*stdw2,y=0,width=stdw,height=stdh)
   bsupport.place(x=4*stdw+4*stdw2,y=0,width=stdw,height=stdh)
   
   songtitles.place(width = 1.5*stdw,y=4.25*stdh+5*stdh2,x=1.5*stdw+stdw2,height = 0.75*stdh)
   creators.place(width = 1.5*stdw,y=4.25*stdh+5*stdh2,x=3*stdw+stdw2,height = 0.75*stdh)
   addinfo2.place(width = 1.5*stdw,y=4.25*stdh+5*stdh2,x=4.5*stdw+stdw2,height = 0.75*stdh)
   availsong.place(width = 4.5*stdw,y=3.5*stdh+5*stdh2,x=1.5*stdw+stdw2,height = 0.75*stdh)   
   #DELETE.place(y=7*stdh+7*stdh2,x=0.5*stdw,width=stdw,height=stdh)
   start.place(x=6*stdw+4*stdw2+stdw*0.08,y=5*stdh+5*stdh2,width=0.5*stdw,height=stdh)
   stop.place(x=6.5*stdw+7.5*stdw2+stdw*0.08,y=5*stdh+5*stdh2,width=0.5*stdw,height=stdh)
   titles.place(x=1.5*stdw+stdw2,y=5*stdh+5*stdh2,width=1.5*stdw)
   author.place(x=1.5*stdw+stdw2+1.5*stdw,y=5*stdh+5*stdh2,width=1.5*stdw)
   addinfo.place(x=1.5*stdw+stdw2+3*stdw,y=5*stdh+5*stdh2,width=1.5*stdw)
   currentversion.place(x=0.05*stdw,y=hfen-2.1*stdh,height=2*stdh)
   #ADD.place(y=6*stdh+6*stdh2,x=0.5*stdw,width=stdw,height=stdh)
   #Enter.place(width=stdw,x=0.5*stdw,height = stdh,y=5*stdh+5*stdh2)

   def curchosen():
      global songtitle,songauthor,songduration,songfilename,songaddinfo,songdesc,choose5ordner,absatz
      ####Annahme und Verwertung der letzten Auswahlen der Listboxen in Mainwindow
      choosen = list()
      choosen2 = list()
      choose5 = ""
      while isActive == "Mainwindow":
         time.sleep(0.00833)
         choose = titles.curselection()
         choose3 = list(choose)
         if (len(choose3) + len(choosen)) == 0:
            choosen = list(choose)    
         ##Veränderung der Songliste
         elif len(choose3) != len(choosen):
            #Mehr Einträge
            if len(choose3) > len(choosen):
               for i in choosen:
                  for item in choose3:
                     if item == i:
                        choose3.remove(i)
               print(choose3)
               try:
                  choose35 = titles.get(choose3[0])
               except:
                  choosen = list(choose)
                  continue
               if choose35 == choose5:
                  choosen = list(choose)
                  continue
               choose5 = titles.get(choose3[0])
               print(choose5)
               choose5ordner = ordner[int(choose3[0])]
               #Aufteilen in CreateNewSong und eigene Songs
               if choose5ordner == "AddANewSong":
                  #Überdecken des Vorherigen
                  verdeck = Label(fenster,bg=backg)
                  verdeck.place(x=0,y=5*stdh,width=1.5*stdw,height=17.5*stdh)
                  #Erschaffen der Elemente
                  titel = Label(fenster,text=langdicts["NL"],bg=backg,fg=foreg)
                  fillin = Label(fenster,text=langdicts["FI"],bg=backg,fg=foreg)
                  title = Label(fenster,text=langdicts["SN"]+"*",bg=backg,fg=foreg)
                  songtitle = Entry(fenster,bg=backg,fg=foreg)
                  author2 = Label(fenster,text=(langdicts["Künstler"]+":*"),bg=backg,fg=foreg)
                  songauthor = Entry(fenster,bg=backg,fg=foreg)
                  duration = Label(fenster,text=langdicts["Dur"]+"*",bg=backg,fg=foreg)
                  songduration = Entry(fenster,bg=backg,fg=foreg)
                  filename = Label(fenster,text=langdicts["FN"]+"*",bg=backg,fg=foreg)
                  songfilename = Entry(fenster,bg=backg,fg=foreg)
                  addinfo = Label(fenster,text=langdicts["AI"].replace(" ","\n")+":",bg=backg,fg=foreg)
                  songaddinfo = Entry(fenster,bg=backg,fg=foreg)
                  desc = Label(fenster,text=langdicts["desc"]+":",bg=backg,fg=foreg)
                  songdesc = Entry(fenster,bg=backg,fg=foreg)
                  accept = Button(fenster,text = langdicts["Auswählen"],command=hinzufuegen,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)

                  #Platzieren der Elemente
                  titel.place(width=1.5*stdw,x=0,height = stdh,y=5*stdh+5*stdh2)
                  fillin.place(width=1.5*stdw,x=0,height = stdh,y=6*stdh+6*stdh2)
                  title.place(x=0.1*stdw,height = stdh,y=7.5*stdh+7*stdh2)
                  songtitle.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=7.5*stdh+9.5*stdh2)
                  author2.place(x=0.1*stdw,height = stdh,y=8.5*stdh+8*stdh2)
                  songauthor.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=8.5*stdh+10.5*stdh2)
                  duration.place(x=0.1*stdw,height = stdh,y=9.5*stdh+9*stdh2)
                  songduration.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=9.5*stdh+11.5*stdh2)
                  filename.place(x=0.1*stdw,height = stdh,y=10.5*stdh+10*stdh2)
                  songfilename.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=10.5*stdh+12.5*stdh2)
                  addinfo.place(x=0.1*stdw,height = stdh,y=11.5*stdh+11*stdh2)
                  songaddinfo.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=11.5*stdh+13.5*stdh2)
                  desc.place(x=0.1*stdw,height = stdh,y=12.5*stdh+12*stdh2)
                  songdesc.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=12.5*stdh+14.5*stdh2)
                  accept.place(x=0.5*stdw,y=13.5*stdh+15.5*stdh2,width=0.5*stdw,height=0.75*stdh)
                  pass
               else:
                  #Überdecken des Vorherigen
                  verdeck = Label(fenster,bg=backg)
                  verdeck.place(x=0,y=5*stdh,width=1.5*stdw,height=17.5*stdh)
                  ##Gestaltung des Randes
                  songtitle = Label(fenster,text=choose5+"\n"+langdicts["by"]+" "+GetSongData(choose5ordner,"Komponist"),bg=backg,fg=foreg)
                  songimage = Label(fenster,text="Maybe in future",bg="green",fg=foreg)
                  delete = Button(fenster,text=langdicts["SL"],command=loeschen,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
                  #Addinfo
                  rawtext = GetSongData(choose5ordner,"Addinfo")
                  raw1 = ""
                  for x in rawtext:
                     raw1 += str(x[0:(len(x))])
                  raw2 = raw1.split(" ")
                  rawlen = list()
                  textlen = 0
                  raw3 = ""
                  turn = 0
                  texts = ""
                  absatz1 = 1
                  for word in raw2:
                     rawlen.append(str(len(word)))
                  for word in raw2:
                     textlen += int(rawlen[turn])
                     if textlen >= int(stdw/7):
                        raw3 += texts + "\n"
                        absatz1 += 1
                        texts = word
                        textlen = int(rawlen[turn])
                     else:
                        texts += " " + word
                     turn += 1
                  raw3 += texts
                  songai = Label(fenster,text=raw3,bg=backg,fg=foreg)
                  #Beschreibung
                  desc1 = (open("music/"+choose5ordner+"/desc.txt", "r", encoding="UTF-8").readlines())
                  desc2 = ""
                  for x in desc1:
                     desc2 += str(x)
                  desc4 = desc2.split(" ")
                  char2 = 0
                  desc3 = ""
                  wordlen = 0
                  turn = 0
                  desclen = list()
                  words = ""
                  absatz = absatz1 + 1
                  for item in desc4:
                     desclen.append(str(len(item)))
                  for word in desc4:
                     N = 0
                     wordlen += int(desclen[turn])
                     for char in word:
                        if char == "\n":
                           word2 = word[:word.index(char)] + "\n"
                           word3 = word[word.index(char)+1:]
                           desc3 += words + word2
                           absatz += 1
                           words = word3 + " "
                           N = 1
                           break
                     if N == 1:
                        wordlen = int(len(word3))-int(desclen[turn])
                     if wordlen >= int(stdw/7):
                        desc3 += words + "\n"
                        absatz += 1
                        words = word + " "
                        wordlen = int(desclen[turn])
                        N = 1
                        turn += 1
                     if N == 0:
                        words += word + " "
                        turn += 1
                        continue
                     elif N == 1:
                        N = 0
                        continue
                     turn += 1
                  desc3 += words
                  songdesc = Label(fenster,text=desc3,anchor="w",justify=LEFT,bg=backg,fg=foreg)
                  #Openfile
                  def openFile():
                     os.startfile("music/"+choose5ordner)
                  openfile = Button(fenster,text=langdicts["Open"],command=openFile,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
                  
                  #Platzieren der Elemente
                  songtitle.place(width=1.5*stdw,x=0,height = stdh,y=5*stdh+5*stdh2)
                  songimage.place(width=stdw,x=0.25*stdw,height = 3*stdh,y=6*stdh+6*stdh2)
                  songai.place(width=stdw,x=0.25*stdw,y=9.2*stdh+7*stdh2)
                  songdesc.place(x=0.24*stdw,y=9.6*stdh+11*stdh2+absatz1*0.2*stdh)
                  openfile.place(width=0.5*stdw,x=0.75*stdw+0.5*stdw2,height=stdh,y=absatz*0.3*stdh+10.1*stdh+11*stdh2)
                  delete.place(x=0.25*stdw-0.5*stdw2,width=0.5*stdw,height=stdh,y=absatz*0.3*stdh+10.1*stdh+11*stdh2)
                  
               #Reset des Ganzen
               choosen = list(choose)
               
            #Weniger Einträge
            elif len(choose3) < len(choosen):
               if len(choose3) == 0:
                  choosen = choosen
               else:
                  for i in choose3:
                     for item in choosen:
                        if item == i:
                           choosen.remove(i)
               print(choosen)
               try:
                  choose35 = titles.get(choosen)
               except:
                  choosen = list(choose)
                  continue
               if choose35 == choose5:
                  choosen = list(choose)
                  continue
               choose5 = titles.get(choosen)
               print(choose5)
               choose5ordner = ordner[int(choosen[0])]
               if choose5ordner == "AddANewSong":
                  #Überdecken des Vorherigen
                  verdeck = Label(fenster,bg=backg)
                  verdeck.place(x=0,y=5*stdh,width=1.5*stdw,height=17.5*stdh)
                  #Erschaffen der Elemente
                  titel = Label(fenster,text=langdicts["NL"],bg=backg,fg=foreg)
                  fillin = Label(fenster,text=langdicts["FI"],bg=backg,fg=foreg)
                  title = Label(fenster,text=langdicts["SN"]+"*",bg=backg,fg=foreg)
                  songtitle = Entry(fenster,bg=backg,fg=foreg)
                  author2 = Label(fenster,text=(langdicts["Künstler"]+":*"),bg=backg,fg=foreg)
                  songauthor = Entry(fenster,bg=backg,fg=foreg)
                  duration = Label(fenster,text=langdicts["Dur"]+"*",bg=backg,fg=foreg)
                  songduration = Entry(fenster,bg=backg,fg=foreg)
                  filename = Label(fenster,text=langdicts["FN"]+"*",bg=backg,fg=foreg)
                  songfilename = Entry(fenster,bg=backg,fg=foreg)
                  addinfo = Label(fenster,text=langdicts["AI"].replace(" ","\n")+":",bg=backg,fg=foreg)
                  songaddinfo = Entry(fenster,bg=backg,fg=foreg)
                  desc = Label(fenster,text=langdicts["desc"]+":",bg=backg,fg=foreg)
                  songdesc = Entry(fenster,bg=backg,fg=foreg)
                  accept = Button(fenster,text = langdicts["Auswählen"],command=hinzufuegen,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)

                  #Platzieren der Elemente
                  titel.place(width=1.5*stdw,x=0,height = stdh,y=5*stdh+5*stdh2)
                  fillin.place(width=1.5*stdw,x=0,height = stdh,y=6*stdh+6*stdh2)
                  title.place(x=0.1*stdw,height = stdh,y=7.5*stdh+7*stdh2)
                  songtitle.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=7.5*stdh+9.5*stdh2)
                  author2.place(x=0.1*stdw,height = stdh,y=8.5*stdh+8*stdh2)
                  songauthor.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=8.5*stdh+10.5*stdh2)
                  duration.place(x=0.1*stdw,height = stdh,y=9.5*stdh+9*stdh2)
                  songduration.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=9.5*stdh+11.5*stdh2)
                  filename.place(x=0.1*stdw,height = stdh,y=10.5*stdh+10*stdh2)
                  songfilename.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=10.5*stdh+12.5*stdh2)
                  addinfo.place(x=0.1*stdw,height = stdh,y=11.5*stdh+11*stdh2)
                  songaddinfo.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=11.5*stdh+13.5*stdh2)
                  desc.place(x=0.1*stdw,height = stdh,y=12.5*stdh+12*stdh2)
                  songdesc.place(width=0.75*stdw,x=0.6*stdw,height = 0.75*stdh,y=12.5*stdh+14.5*stdh2)
                  accept.place(x=0.5*stdw,y=13.5*stdh+15.5*stdh2,width=0.5*stdw,height=0.75*stdh)
                  pass
               else:
                  #Überdecken des Vorherigen
                  verdeck = Label(fenster,bg=backg)
                  verdeck.place(x=0,y=5*stdh,width=1.5*stdw,height=17.5*stdh)
                  ##Gestaltung des Randes
                  songtitle = Label(fenster,text=choose5+"\n"+langdicts["by"]+" "+GetSongData(choose5ordner,"Komponist"),bg=backg,fg=foreg)
                  songimage = Label(fenster,text="Maybe in future",bg="green",fg=foreg)
                  delete = Button(fenster,text=langdicts["SL"],command=loeschen,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
                  #Addinfo
                  rawtext = GetSongData(choose5ordner,"Addinfo")
                  raw1 = ""
                  for x in rawtext:
                     raw1 += str(x[0:(len(x))])
                  raw2 = raw1.split(" ")
                  rawlen = list()
                  textlen = 0
                  raw3 = ""
                  turn = 0
                  texts = ""
                  absatz1 = 1
                  for word in raw2:
                     rawlen.append(str(len(word)))
                  for word in raw2:
                     textlen += int(rawlen[turn])
                     if textlen >= int(stdw/7):
                        raw3 += texts + "\n"
                        absatz1 += 1
                        texts = word
                        textlen = int(rawlen[turn])
                     else:
                        texts += " " + word
                     turn += 1
                  raw3 += texts
                  songai = Label(fenster,text=raw3,bg=backg,fg=foreg)
                  #Beschreibung
                  desc1 = (open("music/"+choose5ordner+"/desc.txt", "r", encoding="UTF-8").readlines())
                  desc2 = ""
                  for x in desc1:
                     desc2 += str(x)
                  desc4 = desc2.split(" ")
                  desc3 = ""
                  wordlen = 0
                  turn = 0
                  desclen = list()
                  words = ""
                  absatz = absatz1 + 1
                  for item in desc4:
                     desclen.append(str(len(item)))
                  for word in desc4:
                     N = 0
                     wordlen += int(desclen[turn])
                     for char in word:
                        if char == "\n":
                           word2 = word[:word.index(char)] + "\n"
                           word3 = word[word.index(char)+1:]
                           desc3 += words + word2
                           absatz += 1
                           words = word3 + " "
                           N = 1
                           break
                     if N == 1:
                        wordlen = int(len(word3))-int(desclen[turn])
                     if wordlen >= int(stdw/7):
                        desc3 += words + "\n"
                        absatz += 1
                        words = word + " "
                        wordlen = int(desclen[turn])
                        N = 1
                        turn += 1
                     if N == 0:
                        words += word + " "
                        turn += 1
                        continue
                     elif N == 1:
                        N = 0
                        continue
                  desc3 += words
                  songdesc = Label(fenster,text=desc3,anchor="w",justify=LEFT,bg=backg,fg=foreg)
                  #Openfile
                  def openFile():
                     os.startfile("music/"+choose5ordner)
                  openfile = Button(fenster,text=langdicts["Open"],command=openFile,bg=backg,fg=foreg,activebackground=backg,activeforeground=foreg)
                  
                  #Platzieren der Elemente
                  songtitle.place(width=1.5*stdw,x=0,height = stdh,y=5*stdh+5*stdh2)
                  songimage.place(width=stdw,x=0.25*stdw,height = 3*stdh,y=6*stdh+6*stdh2)
                  songai.place(width=stdw,x=0.25*stdw,y=9.2*stdh+7*stdh2)
                  songdesc.place(x=0.24*stdw,y=9.6*stdh+11*stdh2+absatz1*0.2*stdh)
                  openfile.place(width=0.5*stdw,x=0.75*stdw+0.5*stdw2,height=stdh,y=absatz*0.3*stdh+10.1*stdh+11*stdh2)
                  delete.place(x=0.25*stdw-0.5*stdw2,width=0.5*stdw,height=stdh,y=absatz*0.3*stdh+10.1*stdh+11*stdh2)
               #Reset
               choosen = list(choose)

         choose2 = author.curselection()
         choose4 = list(choose2)
         if len(choose4) == 0:
            choosen2 = list(choose2)
         #Veränderung der Autorenliste
         if len(choose4) != len(choosen2):
            if len(choose4) > len(choosen2):
               for i in choosen2:
                  for item in choose4:
                     if item == i:
                        choose4.remove(i)
               print(choose4)
               choosen2 = list(choose2)

            elif len(choose4) < len(choosen2):
               choosen2 = list(choosen2)
               for i in choose4:
                  for item in choosen2:
                     if item == i:
                        choosen2.remove(i)
               print(choosen2)
               choosen2 = list(choose2)
      _thread.exit()
               
   _thread.start_new_thread(curchosen,())

   fenster.mainloop()

Fenster() 
Mainwindow()


#############################################################################################################################################################################################################################################


def Ending():
   global activethread
   activethread=False
   time.sleep(0.5)
   activethread=False
   try:
      socket1.sendall(bytes("Closing~","UTF-8"))
      socket1.close()
   except:
      pass
   sys.exit()
   
Ending()


#############################################################################################################################################################################################################################################

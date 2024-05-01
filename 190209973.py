import turtle
import time
from tkinter import messagebox
import pic
#unnamed picture
from turtle import Turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
sc = turtle.Screen()
sc.title("Provinces in turkey")
sc.setup(1280,720)
turtle.bgpic("pic/unnamed.gif")
sc.update()
time.sleep(0)
turtle.bgcolor('black')

# to find every proviness number,
#for x in range (-600,600,50):
 #   for y in range(-360,360,20):
  #      t.goto(x,y)
   #     t.write(f"({x},{y})")
#########
#for output to check if it works thats why i print anything...
print("1")
#81 provinces
Turkey_provinces = {
"ADANA":(0,-120),
"ADIYAMAN": (150,-100),
"AFYONKARA":(-300,0),
"AĞRI":(450,80),
"AMASYA": (0,140),
"ANKARA": (-200,80),
"ANTALAYA":(-300,-140),
"ARTVIN": (350,200),
"AYDIN":(-500,-80),
"BALIKESİR":(-500,60),
"BİLECİK":(-350,100),
"BİNGÖL":(300,0),
"BİTLİS": (400,-40),
"BOLU":(-250,120),
"BURDUR":(-350,-100),
"BURSA":(-400,100),
"ÇANAKKALE": (-550,100),
"ÇANKIN":(-100,140),
"ÇORUM": (-50,-120),
"DENİZLİ":(-400,-80),
"DİYARBAKIR": (300,-60),
"EDİRNE": (-550,160),
"ELAZIĞ": (200,-20),
"ERZİNCAN": (200,60),
"ERZURUM": (350,100),
"ESKİŞEHİR": (-300,60),
"GAZİANTEP": (100,-140),
"GİRESUN": (100,140),
"GÜMÜŞHANE": (200,120),
"HAKKARI": (500,-100),
"HATAY":(-50,200),
"ISPARTA": (-300,-80),
"MERSİN": (-100,-180),
"İSTANBUL": (-400,180),
"İZMİR":(-500,-40),
"KARS": (450,140),
"KASTAMONU": (-100,200),
"KAYSERİ": (0,-20),
"KIRKLARELİ": (-500,220),
"KIRŞEHİR": (-100,20),
"KOCAELİ": (-350,160),
"KONYA":(-200,-60),
"KÜTAHYA":(-350,40),
"MALATYA": (150,-40),
"MANİSA":(-450,0),
"KAHRAMANMARAŞ":(100,-60),
"MARDIN": (300,-120),
"MUĞLA": (-450,-120),
"MUŞ": (400,20),
"NEVŞEHİR": (-50,-20),
"NİĞDE": (-50,-80),
"ORDU":(100,140),
"RİZE": (300,160),
"SAKARYA": (-300,160),
"SAMSUN": (50,160),
"SİİRT": (400,-60),
"SİNOP": (-50,220),
"SİVAS": (100,60),
"TEKİRDAĞ": (-500,180),
"TOKAT":(50,100),
"TARABZON":(250,140),
"TUNCELİ": (200,20),
"ŞANLIURFA": (200,-140),
"UŞAK": (-400,-20),
"VAN": (500,-20),
"YOZGAT": (0,60),
"ZONGULDAK":(-200,200),
"AKSARAY":(-100,-40),
"BAYBURT": (250,100),
"KARAMAN":(-150,-140),
"KIRIKKALE": (-100,80),
"BATMAN": (350,-80),
"ŞIRNAK": (450,-100),
"BARTIN": (-200,220),
"ARDAHAN": (450,180),
"IĞDIR": (500,100),
"YALOVA":(-400,140),
"KARABÜK":(-200,180),
"KİLİS": (100,-180),
"OSMANİYE": (50,-140),
"DÜZCE": (-250,160),
"KKTC": (-150,-280),

}

correct_guesses=[]
while len(correct_guesses)!=len(Turkey_provinces.keys()) :
    province = turtle.textinput("title", f"{len(correct_guesses)}provinces guessed correctly\nEnter a province")
    #when i write quit in the messagebox will be closed like the game is over
    if province == "quit":
       break
    if province in Turkey_provinces.keys():
     x ,y =Turkey_provinces[province]
     t.goto(x,y)
     t.write(province,font=("courier",18,"bold"))
     correct_guesses +=[province]

    else :
     messagebox.showinfo("incorrect",f"{province} is not a province of Turkey :( " )

#for score and put a name of province
    province =turtle.textinput("title",f"{len(correct_guesses)}provinces guessed correctly\nEnter a province")
turtle.done()







    key = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17","18", "19", "20", "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30", "31"]
    alfabe = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z',' ','.']
    txt = open("/Users/noor/Desktop/zehrapythonklasor/zehrapython.txt","r",encoding="utf-8")
    oku = txt.read()
    notdefteri= oku.split(".")
    notdefteri.remove('')

    sifrelenmisyazı = ""
    
    for i in notdefteri:
        index = key.index(i)
        sifrelenmisyazı += alfabe[index]
   
    print("Şifreli Yazı:",oku)
    print()
    print("Orjinal Yazı:",sifrelenmisyazı)
 cıktı=open("/Users/noor/Desktop/zehrapythonklasor/sonuc.txt","w",encoding="utf-8")
    cıktı.write(sifrelenmisyazı)

name = input("Sisesta enda nimi: ")
print("Tervitus!", name)
location = input("Sisesta enda elukoht: ")
if "saaremaa" in location.lower():
 print("Super, kardsin, et oled hiidlane")
if "hiiumaa" in location.lower():
 print("Norm tross oled")
age = input("Sisesta vanus: ")    
age = int(age)
if age < 18:
 print("Sa tatt küll rooli ei roni")
elif age == 18:
 print("Õnnitlused täisealiseks saamise puhul!")
else: 
 print("Võid autot juhtida :)")
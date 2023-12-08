import datetime

# Iegūst pašreizējo stundu
pašreizējā_stunda = datetime.datetime.now().hour

# Nosaka atbilstošo sveicienu
if 5 <= pašreizējā_stunda < 12:
    sveiciens = "Labrīt!"
elif 12 <= pašreizējā_stunda < 18:
    sveiciens = "Labdien!"
else:
    sveiciens = "Labvakar!"

# Izvada sveicienu
print(sveiciens)

# Useless translator - A simple translator that does nothing useful
import webbrowser

print("Translator V1.0")
print("Created by WollyDev24")
print("Translating from English to German")
print("Enter text to translate:")
input1 = input(">> ")
print("[TRANSLATING] Please wait...")
if input1.strip() == "i hate you":
    print("[TRANSLATED] Ich hasse dich")
elif input1.strip() == "How are you":
    print("[TRANSLATED] Wie geht es dir")
else:
    print("[ERROR] I can't translate that yet")
    print("Do you want to open Google Translate in your browser? (y/n)")
    choice = input(">> ")
    if choice.lower() == "y":
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
    else:
        print("Okay, exiting translator.")
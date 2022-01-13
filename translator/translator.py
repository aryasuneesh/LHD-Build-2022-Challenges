import googletrans as gt

print()
print("============Translator==============".center(30))
print()

translator = gt.Translator()



ui = input("Input words to translate: ")
print()
print("========Available Languages=========".center(30))
print("1. English (en)")
print("2. Hindi (hi)")
print("3. French (fr)")
print("4. German (de)")
print("5. Spanish (es)")
print("Which language would you like to convert it to?")
lang = input("Enter code: ")

print()
op = translator.translate(ui, dest=lang)
print("Translated message: ", op.text)
print("Pronounciation: ", op.pronunciation)
print()

# TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt", mode="r")as invited:
    names_list = invited.read().splitlines()


with open("./Input/Letters/starting_letter.txt", mode="r")as starting_letter:
    letter_list = (starting_letter.read())

print(letter_list, invited)
# for each name in invited_names.txt
# Para cada nombre en la lista de nombres de invitados
for name in names_list:
    # Crear una nueva carta personalizada reemplazando "[name]" con el nombre actual
    customized_letter = letter_list.replace("[name]", name)

    # Escribir la carta personalizada en un archivo para el invitado actual
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_file:
        output_file.write(customized_letter)

    # Imprimir la carta personalizada para verificar
    print(customized_letter)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
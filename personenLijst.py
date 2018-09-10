def openFile(mode):
    return open("personen.txt", mode)

def printFile():
    file = openFile("r")

    for line in file: 
        print(line)

printFile()

def vraagNaam():
    naam = input("Naam van student: ")
    if len(naam) <= 3:
        print("Naam moet langer zijn dan 3 karakters")
        return vraagNaam()
    return naam

def vraagStudentNummer():
    nummer = input("Student nummer van student: ")
    if len(nummer) != 7:
        print("Student nummer moet 7 karakters lang zijn")
        return vraagStudentNummer()
    return nummer

def vraagTelefoonNummer():
    nummer = input("Telefoon nummer van student: ")
    if len(nummer) != 10:
        print("Telefoon nummer moet 10 karakters lang zijn")
        return vraagTelefoonNummer()
    return nummer

def vraagJaNee():
    antwoord = input("Print nieuw bestand? [Y/N]: ")
    if antwoord == 'Y' or antwoord == 'y':
        return True
    else:
        return False

def voegPersoonToe():
    naam = vraagNaam()
    student_nummer = vraagStudentNummer()
    telefoon_nummer = vraagTelefoonNummer()

    file = openFile("a")
    
    new_line = f'{student_nummer},{naam},{telefoon_nummer}\n'
    file.write(new_line)
    file.close()

    print_new_file = vraagJaNee()
    if print_new_file:
        printFile()

voegPersoonToe()

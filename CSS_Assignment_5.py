def abbrev_name(name):
    First_Letter = [ ]
    word = name.split()
    for letter in word:
        First_Letter.append(letter[0])
    return (".".join(First_Letter).upper())
print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feeney"))
print(abbrev_name("Evan C"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))
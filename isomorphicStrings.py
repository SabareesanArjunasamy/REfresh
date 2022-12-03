def checkIsIsoMorphic(s: str, t: str) -> bool:
    print('freq of chars in string 1 -> ', [s.index(i) for i in s])
    print('freq of chars in string 2 -> ', [t.index(i) for i in t])
    return ([s.index(i) for i in s] == [t.index(i) for i in t])


ch = 'y'
while ch == 'y':
    string1 = input('Enter string 1 : ')
    string2 = input('Emter string 2 : ')
    if (checkIsIsoMorphic(string1, string2)):
        print('Strings are isomorphic :)')
    else:
        print('Not Isomorphic Strings !')
    ch = input('wanna check again ? y/n : ')

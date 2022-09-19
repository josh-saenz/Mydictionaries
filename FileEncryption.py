def encryption(codes):
    origFile = open('info_security.txt', 'r')
    ReadOrigFile = origFile.read()

    encrypted_file = open('encrypted.txt', 'w')

    for charac in ReadOrigFile:
        if charac in codes:
            encrypted_file.write(codes[charac])
        else:
            encrypted_file.write(charac)
    
    encrypted_file.close()



def main(): 
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', \
    'E':'5', 'e':'6', 'F':'7', 'f': '8', 'G':'9', 'g':'0', 'H':'{', 'h':'}', 'I':'[', \
    'i':']', 'J': '$', 'j':'^', 'K':'&', 'k':'*', 'L':'!', 'l':'(', 'M':')', 'm':'~', \
    'N':'Z', 'n':'-', 'O':'\\', 'o':'X', 'P':'+', 'p':'=', 'Q':'r', 'q':'V', 'R':':', \
    'r':'<', 'S':'>', 's':'?', 'T':';', 't':'E', 'U':'b', 'u':'_', 'V':'i', 'v':'`', \
    'W':'d', 'w':'j', 'X':'a', 'x':'"', 'Y':'A', 'y':'a', 'Z':',', 'z':'.'}

    encryption(codes)

main()
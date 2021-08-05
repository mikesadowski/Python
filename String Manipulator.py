import re


def encryption(S, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    newString = ""
    for letter in S:
        if letter != ' ':
            letter = alphabet.index(letter)
            newletter = letter + n
            newletter = newletter % 26  # keeps it under 26
            newString += (alphabet[newletter])
        else:
            newString += ' '

    newString += str(n)
    return newString


def decryption(W):
    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    num = re.findall(r"\d+", W)  # list, I need the first and only entry (num(0))
    num = int(num[0])
    newerString = ''.join([i for i in W if not i.isdigit()])
    newestString = ""
    for newletter in newerString:
        if newletter != ' ':
            newletter = alpha.index(newletter)
            newerletter = newletter - num
            newerletter = newerletter % 26  # keeps it under 26
            newestString += (alpha[newerletter])
        else:
            newestString += ' '
    return newestString


def main():
    S = input("Please enter a string: ")
    S = S.lower()
    n = int(input("Please enter an integer: "))
    print(encryption(S, n))
    W = encryption(S, n)
    print(decryption(W))


main()
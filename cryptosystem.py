def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]

    encryptionDict = dict(zip(keys, values))
    decryptionDict = dict(zip(values, keys))

    message = input("Enter you message")
    mode = input("Enter the mode: Encode(E) or Decode(D)")

    if mode.upper() == 'E':
        newMessage = ''.join(
            [encryptionDict[letter] for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join(
            [decryptionDict[letter] for letter in message.lower()])
    else:
        print("Please enter correct option")

    return newMessage.capitalize()


print(machine())

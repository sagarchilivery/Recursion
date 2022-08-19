
text = input("Enter any value: ")
n = len(text)

def palligang(text, n):

    # if(len(text)== n):
        # r = len(text)-1
        # f = 0   


    partialAns1 = palligang(text[0:r-1], n-1)
    partialAns2 = palligang(text[f+1:-1], n-1)
    
    if(partialAns1== partialAns2):
        return True
    else:
        return False

    if(text[f]==text[r]):
        return True
    else:
        return False
    





    if(partialAns2 == text):
        return "palligand"
    else:
        return "No palli"

print(palligang(text, n))

# temp = text[::-1]
# if(text == temp):
#     print("Palli gand")
# else:
#     print("No palli")
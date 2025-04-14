def is_palindrome(word:str) -> bool:
    word= word.lower().replace(" ","").replace(":","").replace(",","").replace(".","").replace("?","")
    j = -1
    resultado = True
    for i in word:
         j += 1
         n = (j*(-1)-1)
         if i != (word[n]):
            resultado = False
         n = 0
    return resultado
def ejecucion_programa():
    while True:
        my_word= input("Ingrese una palabra o frase: ")
        is_palindrome(my_word)
        resultado1 = is_palindrome(my_word)
        if resultado1 == True:
            print(f"{my_word} es palindorme")
        else:
            print(f"{my_word} no es palindrome")

if __name__ == "__main__":
    ejecucion_programa()
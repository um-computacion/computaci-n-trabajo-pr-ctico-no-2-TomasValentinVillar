def is_palindrome(word:str) -> bool:
    word= word.lower().replace(" ","").replace(":","").replace(",","").replace(".","").replace("?","")

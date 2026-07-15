# 4. Write a function that receives two strings as parameters and
# returns the number of occurrences of the first string in the second.

def numara_aparitii(text_cautat: str,text_sursa: str) -> int:
    return text_sursa.count(text_cautat)

print(numara_aparitii("ana", "ana are mere, iar ana rade"))

"""Challenge question to practice with dict."""

def zip(words: list[str], numbers: list[int]) -> dict[str,int]: 
    new_dict: dict[str, int] = {}
    list_len: int = range(len(words))
    i = 0
    
    if len(words) != len(numbers): 
       print("The two lists should be the same length!") 
       return new_dict
    if len(words) == 0 or len(numbers) == 0: 
       print("The lists cannot be empty.")
       return new_dict

    new_dict: dict[str, int] = {}
    list_len: int = range(len(words))
    i = 0 

    for i in list_len: 
       new_dict[words[i]] = numbers[i] 
    return new_dict
       
       
print(zip(('apple', 'banana', 'grape'), (1, 2, 8)))





# Example: Go over words in a file and group them according to their length.
# 
# Four alternative methods for updating the lists are shown (A, B, C, D).

wordsbylen = {}

with open("D:/UA/1ano/FP/aula07/examples/pg3333.txt") as f:
    for line in f:
        word = line.strip()
        lw = len(word)
        
        """
        #A: Check for the key and either assign a new list or append
        if lw not in wordsbylen:
            wordsbylen[lw] = [word]
        else:
            wordsbylen[lw].append(word)
        
        #B: Check for the key, create if needed, then append
        if lw not in wordsbylen:
            wordsbylen[lw] = []
        wordsbylen[lw].append(word)
        
        #C: Using the get method
        lst = wordsbylen.get(lw, [])
        wordsbylen[lw] = lst
        lst.append(word)
        """

        #D: Using the setdefault method
        wordsbylen.setdefault(lw, []).append(word)
        
print("Words of length 20:")
print(wordsbylen[20])


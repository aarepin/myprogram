def longest_palindromic(text):
    words=([text[i:i+j]
      for i in range(len(text)+1) 
        for j in range(len(text)-i+1) if j>0 and text[i:i+j]==text[i:i+j][::-1]])
    return ([words[i] 
      for i in range(len(words)) 
        if len(words[i])==max(len(words[i]) 
          for i in range(len(words)))])[0]

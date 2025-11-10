def translate(text):
    # If input is a phrase (multiple words), translate each word separately
    if ' ' in text:
        return ' '.join(translate(word) for word in text.split())

    text = text.lower()
    vowels = set('aeiou')
    # Rule 1: If a word begins with a vowel, or starts with `"xr"` or `"yt"`
    if text.startswith(('a','e','i','o','u','xr','yt')):
        return text + 'ay'
    
    # Rule 3: Handle words with 'qu'
    elif 'qu' in text:
        qu_index = text.index('qu')
        if qu_index == 0:  # word starts with 'qu'
            return text[2:] + text[:2] + 'ay'
        else:  # word has consonants and/or vowels before 'qu'
            if text[qu_index - 1] in vowels: # Word has vowel before 'qu'
                return text[qu_index-1:] + text[:qu_index-1] + 'ay'
            else: # word has consonant before 'qu'
                return text[qu_index+2:] + text[:qu_index+2] + 'ay' 
        
    # Rule 4: Handle words with 'y'
    if 'y' in text:
        y_index = text.index('y')
        if y_index == 0: # word starts with 'y'
            return text[1:] + text[:1] + 'ay'
        else: # word has consonants before 'y'
            if not any(ch in vowels for ch in text[:y_index]):
                return text[y_index:] + text[:y_index] + 'ay'
            
        
    # Rule 2: Handle words beginning with consonants
    for i, ch in enumerate(text):  # Find first vowel
        if ch in vowels:
            return text[i:] + text[:i] + 'ay'
    # No vowels found
    return text + 'ay'
        


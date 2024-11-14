API made with Python's flask library. 
Generates wordsearch from supplied json of words, if none supplied it simply creates a 15 word, wordsearch that are randomly selected.
Return looks like {'search': list[list[chars]], 'words': list[strings]} where search is a list of lists, to form the grid, and words is the list of words that were selected or supplied.

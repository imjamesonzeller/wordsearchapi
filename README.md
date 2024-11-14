API made with Python's flask library. 
Generates wordsearch from supplied JSON of words, if none supplied it simply creates a 15 word, wordsearch that are randomly selected.
Return looks like {'search': list[list[chars]], 'words': list[strings]} where search is a list of lists, to form the grid, and words is the list of words that were selected or supplied.
Self-hosted on my home server at https://wordsearch.jamesonzeller.com/generate_word_search where you submit a POST request with a JSON body of words. {'words': list[strings]}
In use at https://www.jamesonzeller.com/wordsearch where I implemented it to take in words and delimiter for the input and return a word search that can be saved as a CSV in order to print.

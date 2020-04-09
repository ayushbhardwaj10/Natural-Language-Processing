This python code removes *Single Line* headers/footers from pdf documents.
It's very helpful for pre-pocessing PDF's which are used for natural language processing in later steps.

NOTE : Code is developed for general requirements, it can be manipulated for specific requirements. Code is very scalable :) 
Scalability is kept in mind since PDF documents have different formats and require different set of rules to handel it's processing.

Features of code :

1. Code uses tika library which is used for text extraction from PDF. 
2. Fuzzywuzzy library( GNU General Public License v2 (GPLv2) ) is a very strong library used for calculating similarity between two strings. 
3. The need for Fuzzywuzzy arised because text extraction can sometimes be very ambiguous and can have texts in changed order or unintended concatination. 
3. BeautifulSoup library is used to extract text from XML content of tika. 
4. Output is the text of the pdf without *single line* header and footers.
5. Hashing concept is used to make processing faster and also save the memory - used while looking for headers and footers in the entire chunk of text extracted.

Dependencies of code :

1. bs4 library - MIT license
2. fuzzywuzzy library - GNU General Public License v2 (GPLv2)
3. tika- Apache Software License


Licensed under GNU GENERAL PUBLIC LICENSE
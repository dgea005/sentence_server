# sentence_server
output simple sentences to learn German

+ idea is to get sentences from source such as project gutenberg
+ from having a corpus can find the most common words and possibly the simplest sentences
+ can then serve these sentences or construct vocabulary flashcard decks to learn from

Download DE texts from gutenberg:
<pre><code>
mkdir books
cd books
wget -w 2 -m -H "http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=de"
</code></pre>

Then run extract_books.py to unzip books and insert them into a single folder

Issues:
+ books contains don't contain German entirely; some books have non German forewords but main text in German. Need to somehow get rid of these to have a clean text


spaCy installation (assumes anaconda with python3 installed)
<pre><code>
conda config --add channels spacy
conda install spacy

#install german language model
sputnik --name spacy --repository-url http://index.spacy.io install de==1.0.0
</code></pre>

Other notes / resources:
+ useful for spacy
  + https://nicschrading.com/project/Intro-to-NLP-with-spaCy/

+ books not in de from text dump
  + 417
  + 607


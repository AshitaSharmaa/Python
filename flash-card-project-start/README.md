FLASHCARD - capstone project.
(looking at handling exceptions using the JSON data format, parsing and reading Csvs,
using pandas, opening and writing to files, and a whole lot more)

 This project is especially great with studying for languages.

>Step 1 - Create Dictionary of words
There's a wiki for the frequency lists of different languages, and it lists most of the common languages.
I take 100 words from this frequency dictionary and I put it into a Google sheet, and in the next column  I type in formula called Google Translate, the word’s English translation will appear in the column. So now that I've created my Excel sheet essentially of French and English words, I've got potentially100 flashcards with the front and back data already saved inside this Google sheet.
Now all I have to do is simply download it as a CSV, named french_words.csv and we'll be able to work with it very easily. Using Pandas Library.

>Step 2 - Create UI with TKinter: Create a canvas for The flash card  with 1 image and 2 pieces of text. Which is “French “and the word in French

>Step 3 - Create New Flash Cards
1. Read the data from the french_words.csv file in the data folder.
2. Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.

>Step 4 - Flip the Cards!
1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
2. The card image should change to the card_back.png and the text colour should change to white. The title of the card should change to "English" from "French".

>Step 5 - Save the progress
1. When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word should be removed from the list of words that might come up.
2. The updated data should be saved to a new file called words_to_learn.csv
3. The next time the program is run, it should check if there is a words_to_learn.csv file. If it exists, the program should use those words to put on the flashcards. If the words_to_learn.csv does not exist (i.e., the first time the program is run), then it should use the words in the french_words.csv
We want our flashcard program to only test us on things we don't know. So if the user presses the ✅ button, that means the current card should not come up again.



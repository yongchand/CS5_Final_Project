# CS5_Final_Project

Yongchan Hong
Text ID Project

This Text ID project the given text with two different kinds of texts and suggest which one is the closer text with the given text. This was used to find out that The Cuckoo’s Calling was written by J.K Rowling. Before you use this machine, it is clear to know that there should not be a weird feature—like having double spece (ex. Harvey__Mudd) as it counts by the number of space. The usage of this feature is simple. Use “compareTextWithTwoModels” function and put original text, and two models that you are curious. Then, using logistic calculation of comparison in categories of punctuation, word, word length, stem, and sentence length, it will show which one is more closer. This tool can be powerful when you want to compare the text from same author. 

For final project, I selected Mark Twain’s article, “Project Gutenberg” as “MT.txt” and Ernest Hemingway’s article, “Indian Camp” as “HW.txt” for trained models. For test texts, I selected “MT2.txt” as Mark Twain’s “The Adventure of Tom Sawyer Chapter 1” and Hemingway’s “A Very Short Story.” In order to perform the experiment, we used readTextFromFile function to each read txt files and made dictionary for each sentence length, word length, word, stems and punctuation by using function createAllDictionaries. And then, we used compareTextWithModels function to check the result. The result was pretty clear. For compareTextWithModels(HW,HW2,MT), the result was shown that Model 1 was a better fit by 4 to 1 which means that HW and HW2 are similar in its writing style. Also,  we compared compareTextWithModels(MT2,HW2,MT), and found out MT was more fit by 4 to 1, meaning that MT2 and MT matches a lot. However, compareTextWithModels(MT2,HW,MT) showed HW was better by 3 to 2 and compareTextWithModels(MT,HW2,MT2) also showed that HW2 was more fit by 4 to 2. Therefore, we found out that text editor is mostly effective, but should need modification in order to be accurate. Some components like semi colon or dash should be also included. Also, we should doubt if Mark Twain has written the article in same style for two articles. Text ID was practical and appealing coding experience for me. 

Special thanks to Prof Ron who helped me to finish this project!

## Explanation for each file
Porter.py is prewritten code and explains about the algorithm.
textmodel.py is the code I developed.
3esl.txt is text file with all existing words.
Rest of texts are those I used for evaluating my model.

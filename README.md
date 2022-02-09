# Tournament-Draft-Creator
This python script will launch a gui where you can input the amount of players and teams you want. It will distribute them based on skill level and let you know of any outliers. It uses a .csv from a google sheets response sheet.

## Tutorial for the draft creator
Create a google form that includes these 3 options.
1. A question asking for their discord ID - for example mine is 406560334623539200 regex is ^[0-9]{18}, you can
2. A question asking for their IGN - for example mine is [VGBD]HypeLites 
3. A question asking for their skill level - this is just on a scale of 1 - 3, anything works as long as it returns an integer from 1 to 3 where 1 is beginner and 3 is advanced

Here is an example draft form
https://forms.gle/iqcMe59of892eN4C8

Now lets learn how to use the program, its pretty simple
1. Download and run the .py in your ide of choice
2. Go to the google sheet from the form and download it as csv
3. Follow the steps in the program, find the csv file
4. For the header section, copy the header - the header on the sheet is the question on the form. The script will look for this and use it 
5. Once you set every value you can press the green calculate button
Have fun!

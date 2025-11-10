**TRIVIA Quiz APP

Uses Trivia Database which has over 3,000 verified questions. we can pick questions randomly using API to fill into our Quiz Application

Here we are creating GUI App using TKinter which uses API endpoints to send request to a particular endpoint to ask for a particular data

First I used Trivia Database API using Parameters to get the questions and store in Question_data

quiz_brain.py takes questions from data.py and Then apply HTML's Unescape method to format/unescape HTML entities (questions with strange strings like  &quot; which is basically double quote ")
and return the question and checks answer using check_answer method and also keep track of the score

ui.py is responsible for creating GUI using TKinter and uses a function "get_next_question" from quiz_brain. It uses two methods for True and False Buttons as a command to the buttons.
These methods call check_answer method from quiz_brain and pass over "True" and "False" respectively to check whether the player is right or wrong.






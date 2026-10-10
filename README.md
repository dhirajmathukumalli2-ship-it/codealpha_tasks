\# CodeAlpha FAQ Chatbot



\## CodeAlpha Artificial Intelligence Internship - Task 2



This project is an FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.



The chatbot uses Natural Language Processing (NLP) techniques to understand user questions and find the most relevant answer from a predefined FAQ dataset.



\## Features



\- FAQ-based chatbot

\- Text preprocessing

\- TF-IDF vectorization

\- Cosine similarity for question matching

\- Similarity threshold for unknown questions

\- Flask web interface

\- Interactive chat interface

\- Responsive and simple user interface



\## Technologies Used



\- Python

\- Flask

\- NLTK

\- Scikit-learn

\- NumPy

\- HTML

\- CSS

\- JavaScript



\## How It Works



1\. The chatbot loads FAQ questions and answers from `faqs.json`.

2\. User input is cleaned using text preprocessing.

3\. FAQ questions are converted into TF-IDF vectors.

4\. The user's question is also converted into a TF-IDF vector.

5\. Cosine similarity is calculated between the user's question and the FAQ questions.

6\. The FAQ with the highest similarity is selected.

7\. If the similarity is below the threshold, the chatbot asks the user to rephrase the question.

8\. Otherwise, the corresponding answer is displayed.



\## Project Structure



```text

CodeAlpha\_Task2\_FAQ\_Chatbot/

│

├── app.py

├── chatbot.py

├── faqs.json

├── requirements.txt

├── README.md

├── .gitignore

│

├── templates/

│   └── index.html

│

└── venv/


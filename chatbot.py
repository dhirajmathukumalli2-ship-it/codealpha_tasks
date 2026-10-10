import json
import re

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:

    def __init__(self, faq_file):
        self.faqs = self.load_faqs(faq_file)

        self.questions = [
            faq["question"]
            for faq in self.faqs
        ]

        # Convert FAQ questions into TF-IDF vectors
        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def load_faqs(self, faq_file):
        with open(
            faq_file,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    def preprocess(self, text):
        # Convert text to lowercase
        text = text.lower()

        # Remove special characters
        text = re.sub(
            r"[^a-zA-Z0-9\s]",
            "",
            text
        )

        # Remove extra spaces
        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        return text

    def get_response(self, user_question):

        # Preprocess user's question
        cleaned_question = self.preprocess(
            user_question
        )

        if not cleaned_question:
            return "Please enter a question."

        # Convert user question into TF-IDF vector
        user_vector = self.vectorizer.transform(
            [cleaned_question]
        )

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        # Find the most similar FAQ
        best_match_index = np.argmax(
            similarity_scores
        )

        # Get similarity score
        best_score = similarity_scores[
            0,
            best_match_index
        ]

        # Minimum similarity required
        threshold = 0.20

        # If no FAQ is sufficiently similar
        if best_score < threshold:
            return (
                "I'm sorry, I couldn't find a "
                "relevant answer to your question. "
                "Please try asking in a different way."
            )

        # Return the answer of the best matching FAQ
        return self.faqs[
            best_match_index
        ]["answer"]
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np
import gradio as gr
from qa import QA


class ChatBot:
    def __init__(self, threshold: float = 0.6):
        self.threshold = threshold
        self.model = None
        self.llm = None
        self.questions = []
        self.answers = []
        self.q_embeddings = None

        self._load_qa(QA)
        self._set_embedding_model("all-MiniLM-L6-v2")
        self._set_fallback_model("distilgpt2")


    def _set_embedding_model(self, model_name: str):
        self.model = SentenceTransformer(model_name)
        self.q_embeddings = self.model.encode(self.questions)

    def _set_fallback_model(self, model_name: str):
        self.llm = pipeline("text-generation", model=model_name)

    def _load_qa(self, qa_data: dict):
        for item in qa_data.get("questions", []):
            self.questions.append(item["question"])
            self.answers.append(item["answer"])


    def retrieve(self, query: str):
        query_emb = self.model.encode([query])[0]
        sims = np.dot(self.q_embeddings, query_emb)
        best_idx = np.argmax(sims)
        return sims[best_idx], self.answers[best_idx]

    def fallback(self, query: str):
        result = self.llm(query, max_new_tokens=80)[0]["generated_text"]
        return result

    def chat(self, user_input: str, history=None):
        score, answer = self.retrieve(user_input)
        if score >= self.threshold:
            return answer
        return self.fallback(user_input)


def main():
    bot = ChatBot()
    ui = gr.ChatInterface(bot.chat)
    ui.launch()


if __name__ == "__main__":
    main()

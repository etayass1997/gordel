import json
import os
import re
from rank_bm25 import BM25Okapi

DB_PATH = os.path.join(os.path.dirname(__file__), 'kb_data.json')


def _tokenize(text):
    return re.findall(r'[\w֐-׿]+', text.lower())


class RAGEngine:
    def __init__(self):
        self.docs = []       # list of {'id', 'text', 'metadata'}
        self._bm25 = None
        self._load()

    def _load(self):
        if os.path.exists(DB_PATH):
            with open(DB_PATH, encoding='utf-8') as f:
                self.docs = json.load(f)
            self._rebuild()

    def _save(self):
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.docs, f, ensure_ascii=False, indent=2)

    def _rebuild(self):
        if self.docs:
            corpus = [_tokenize(d['text']) for d in self.docs]
            self._bm25 = BM25Okapi(corpus)
        else:
            self._bm25 = None

    def add_document(self, text, metadata, doc_id):
        # Remove old chunks with same base id
        self.docs = [d for d in self.docs if not d['id'].startswith(doc_id)]
        for i, chunk in enumerate(self._chunk(text)):
            if len(chunk.strip()) < 20:
                continue
            self.docs.append({'id': f"{doc_id}_{i}", 'text': chunk, 'metadata': metadata})
        self._rebuild()
        self._save()

    def search(self, query, n=4):
        if not self._bm25 or not self.docs:
            return {'documents': [[]], 'metadatas': [[]]}
        tokens = _tokenize(query)
        scores = self._bm25.get_scores(tokens)
        top_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:n]
        docs = [self.docs[i]['text'] for i in top_idx if scores[i] > 0]
        metas = [self.docs[i]['metadata'] for i in top_idx if scores[i] > 0]
        return {'documents': [docs], 'metadatas': [metas]}

    def count(self):
        return len(self.docs)

    def _chunk(self, text, max_chars=700):
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        chunks, current, current_len = [], [], 0
        for p in paragraphs:
            if current_len + len(p) > max_chars and current:
                chunks.append('\n\n'.join(current))
                current, current_len = [], 0
            current.append(p)
            current_len += len(p)
        if current:
            chunks.append('\n\n'.join(current))
        return chunks or [text[:max_chars]]

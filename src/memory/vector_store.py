"""Vector memory store backed by ChromaDB."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)

COLLECTION_NAME = "oarl_knowledge"
DEFAULT_N_RESULTS = 5


class VectorStore:
    """Persistent vector memory using ChromaDB.

    Stores embeddings of text documents (insights, reasoning traces,
    experiment summaries) for semantic retrieval.
    """

    def __init__(self, persist_dir: str = "./memory/chroma_data") -> None:
        try:
            import chromadb  # noqa: WPS433

            self._client = chromadb.PersistentClient(path=persist_dir)
        except ImportError:
            logger.warning("chromadb not installed — using in-memory fallback")
            import chromadb

            self._client = chromadb.Client()

        self._collection = self._client.get_or_create_collection(name=COLLECTION_NAME)
        logger.info("VectorStore ready (collection=%s)", COLLECTION_NAME)

    def add(
        self,
        doc_id: str,
        text: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Add a document to the vector store."""
        self._collection.upsert(
            ids=[doc_id],
            documents=[text],
            metadatas=[metadata or {}],
        )

    def query(self, text: str, n_results: int = DEFAULT_N_RESULTS) -> list[dict[str, Any]]:
        """Semantic search — returns the most similar documents."""
        results = self._collection.query(query_texts=[text], n_results=n_results)
        docs: list[dict[str, Any]] = []
        for i, doc_id in enumerate(results["ids"][0]):
            docs.append({
                "id": doc_id,
                "document": results["documents"][0][i] if results["documents"] else "",
                "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                "distance": results["distances"][0][i] if results["distances"] else 0.0,
            })
        return docs

    def delete(self, doc_id: str) -> None:
        """Remove a document by ID."""
        self._collection.delete(ids=[doc_id])

    @property
    def count(self) -> int:
        return self._collection.count()

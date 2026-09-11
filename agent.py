from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex
from llama_index.core.graph_stores import SimpleGraphStore

def create_kg_index(data_dir):
    documents = SimpleDirectoryReader(data_dir).load_data()
    graph_store = SimpleGraphStore()
    index = KnowledgeGraphIndex.from_documents(
        documents,
        max_triplets_per_chunk=3,
        graph_store=graph_store
    )
    return index

if __name__ == "__main__":
    print("LlamaIndex Knowledge Graph agent ready.")

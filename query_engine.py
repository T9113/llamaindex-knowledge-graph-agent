def get_kg_query_engine(index):
    return index.as_query_engine(
        include_text=True,
        response_mode="tree_summarize",
        similarity_top_k=5
    )

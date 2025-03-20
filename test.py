
text = "./data/books/AliceInWonderland.txt"

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=500,
    length_function=len,
    add_start_index=True,
)

chunks = text_splitter.split_text(text) 
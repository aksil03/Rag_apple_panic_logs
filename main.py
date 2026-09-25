from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser

# charge le doc
documents = SimpleDirectoryReader("data").load_data()

# parseur markdown
parser = MarkdownNodeParser()
nodes = parser.get_nodes_from_documents(documents)

print(f"Nombre de chunks: {len(nodes)}\n")

# verif des chunks
for i, node in enumerate(nodes):
    print(f"Chunk n°{i + 1} :")
    print(node.text)
    print("=" * 50)

from backend.rag.loader import load_pdf

pages = load_pdf("documents/rag_loader_test.pdf")

print(f"Total pages extracted: {len(pages)}")

for page in pages:
    print(f"\n--- Page {page['page']} ---")
    print(page["text"])

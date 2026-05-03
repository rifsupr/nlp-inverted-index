import pandas as pd
import re

# =========================
# 1. LOAD DATASET
# =========================
df = pd.read_csv("datasets/data_berita.csv")

# =========================
# 2. PREPROCESSING SEDERHANA
# =========================
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# gabungkan title + content
df['text'] = df['title'].fillna('') + ' ' + df['content'].fillna('')
df['text'] = df['text'].apply(preprocess)

# =========================
# 3. BUILD INVERTED INDEX
# =========================
inverted_index = {}

for idx, row in df.iterrows():
    doc_id = row['id']
    words = row['text'].split()
    
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = {}
        
        if doc_id not in inverted_index[word]:
            inverted_index[word][doc_id] = 0
        
        inverted_index[word][doc_id] += 1

# =========================
# 4. SEARCH FUNCTION
# =========================
def search(query):
    query = preprocess(query)
    terms = query.split()
    
    result_docs = None
    
    for term in terms:
        if term in inverted_index:
            docs = set(inverted_index[term].keys())
            
            if result_docs is None:
                result_docs = docs
            else:
                result_docs = result_docs.intersection(docs)
        else:
            return []
    
    return list(result_docs)

# =========================
# 5. DISPLAY RESULT
# =========================
def show_results(doc_ids):
    results = df[df['id'].isin(doc_ids)]
    return results[['id', 'title']]

# =========================
# 6. TEST SEARCH
# =========================
query = input("Masukkan query: ")
result_ids = search(query)

if result_ids:
    print("\nHasil ditemukan:")
    print(show_results(result_ids))
else:
    print("\nTidak ada hasil ditemukan.")
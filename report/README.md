# Project Concept: Customized Khmer Stop-Word Removal System

## 1. Project Overview
Information Retrieval (IR) and Natural Language Processing (NLP) in the Khmer language face unique challenges due to the lack of explicit word segmentation and the complex role of function words. In standard IR tasks (like search engines or text classification), common words (stopwords) usually carry little meaning but appear frequently, skewing the results (e.g., high TF frequencies for "and", "the", "in").

**The Goal:**
This project aims to develop, implement, and evaluate a **customized Khmer stop-word removal system**. By identifying and filtering out "noise" words (linguistic particles, prepositions, conjunctions) based on their linguistic category rather than just frequency, we aim to improve the accuracy of TF-IDF weighting and search ranking.

---

## 2. Methodology & Team Workflow
The project is divided into four distinct phases, each corresponding to a specific notebook and team role.

### Phase 1: Preprocessing & Data Preparation (Person 1)
**Objective:** Clean the raw text and integrate the custom stop-word list.
- **Input:** Raw text corpus (`news_text_file_150k.txt`) + Master Stopword CSV (`FIle_Stopwords.csv`).
- **Process:**
  1.  **Normalization:** Fix invisible spaces and Khmer character anomalies.
  2.  **Segmentation:** Use `khmer-nltk` to split continuous text into tokens.
  3.  **Filtering:** Compare tokens against the master stopword list.
- **Output:** Two datasets:
  - `dataset_with_stopwords.txt` (Full text)
  - `dataset_remove_stopwords.txt` (Cleaned text)
- **Notebook:** `notebooks/01_preprocessing.ipynb, Text_Apply_StopWord.ipynb, and Text_preprocessing.ipynb`

### Phase 2: TF-IDF Analysis (Person 2)
**Objective:** Analyze how stop-word removal affects term weighting.
- **Process:**
  1.  Compute Term Frequency (TF) for both datasets.
  2.  Compute Inverse Document Frequency (IDF).
  3.  Generate TF-IDF vectors.
  4.  Compare the top-ranked keywords for documents.
- **Finding:** We expect "content words" (nouns, specific verbs) to rise in rank after removal, while "function words" disappear.
- **Notebook:** `notebooks/02_tfidf_analysis.ipynb`

### Phase 3: IR & Ranking Evaluation (Person 3)
**Objective:** Measure the impact on Search Engine performance.
- **Process:**
  1.  Implement a Vector Space Model (VSM) using Cosine Similarity.
  2.  **Task:** Known-Item Retrieval. Take a random document, use it as a query, and see if the system can find the original document in the corpus.
  3.  **Metrics:**
      - **Mean Rank:** Average position of the correct document (Lower is better).
      - **Recall@10:** How often the correct document is in the top 10 results.
- **Notebook:** `notebooks/03_ir_evaluation.ipynb`

### Phase 4: Linguistic Analysis & Recommendations (Person 4)
**Objective:** Provide standardized rules for Khmer NLP.
- **Process:**
  1.  Analyze the `linguistic_group` of the removed words.
  2.  Measure the "Noise Contribution" of each category (e.g., How often do *Particles* appear vs *Pronouns*?).
  3.  **Recommendation Tiers:**
      - **Tier 1 (Remove):** Particles, Prepositions, Conjunctions.
      - **Tier 2 (Optional):** Pronouns, Determiners.
      - **Tier 3 (Keep):** Content Words, Negations (sometimes).
- **Notebook:** `notebooks/04_linguistic_analysis.ipynb`

---

## 3. Step-by-Step Execution Guide

### Prerequisites
Ensure you have the necessary libraries installed:
```bash
pip install khmer-nltk scikit-learn pandas matplotlib seaborn
```

### Step 1: Run Preprocessing
1. Open `notebooks/01_preprocessing.ipynb`.
2. Ensure the `FIle_Stopwords.csv` is present in `stopwords/` directory.
3. Run all cells to generate `dataset_with_stopwords.txt` and `dataset_remove_stopwords.txt` in the `data/` folder.

### Step 2: Run TF-IDF Analysis
1. Open `notebooks/02_tfidf_analysis.ipynb`.
2. Run the cells to see the comparison of top keywords.
3. Observe how the "Top Words" list changes from generic terms (e.g., "នៃ", "និង") to specific topics (e.g., "សេដ្ឋកិច្ច", "អភិវឌ្ឍន៍").

### Step 3: Run Evaluation
1. Open `notebooks/03_ir_evaluation.ipynb`.
2. Ensure the datasets from Step 1 are ready.
3. Run the evaluation script.
4. Check the **Mean Rank** improvement. A lower mean rank indicates that removing stop-words made the search more accurate.

### Step 4: Run Linguistic Analysis
1. Open `notebooks/04_linguistic_analysis.ipynb`.
2. Run the visualization cells.
3. View the bar charts showing which linguistic categories contribute the most noise.
4. Use these charts to justify the "Removal Rules" in your final report.

---

## 4. Expected Outcomes
- A robust, linguistically motivated stop-word list for Khmer.
- Empirical evidence (via IR metrics) that using this list improves text processing tasks.
- A standardized pipeline that future Khmer NLP projects can adopt.

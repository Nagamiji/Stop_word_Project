# Comparative Analysis of IR Performance and Linguistic Characteristics of Khmer Stopwords

## 1. Information Retrieval (IR) Evaluation

**Notebook Reference:** `03_ir_evaluation.ipynb`

### 1.1 theoretical Foundation

The evaluation of the stopword removal system is grounded in the **Vector Space Model (VSM)** of Information Retrieval. This phase directly builds upon the TF-IDF vectorization established in the previous phase (`02_tfidf_analysis.ipynb`).

The core hypothesis is that high-frequency function words (stopwords) introduce "noise" into the vector space, reducing the orthogonality between non-relevant documents and increasing the cosine similarity between unrelated texts. By removing these stopwords, we hypothesize that the **Signal-to-Noise Ratio (SNR)** of the document vectors will increase, leading to improved retrieval accuracy.

### 1.2 Mathematical Formulation

The connection between Phase 2 (TF-IDF) and Phase 3 (IR) is established through the **Cosine Similarity** function. For a given Query ($q$) and a Document ($d$) in the corpus, both represented as TF-IDF vectors derived in Phase 2:

$$ \vec{q} = (w*{q,1}, w*{q,2}, ..., w*{q,n}) $$
$$ \vec{d} = (w*{d,1}, w*{d,2}, ..., w*{d,n}) $$

The similarity score is computed as:

$$ \text{sim}(\vec{q}, \vec{d}) = \frac{\sum*{i=1}^{n} w*{q,i} \cdot w*{d,i}}{\sqrt{\sum*{i=1}^{n} w*{q,i}^2} \cdot \sqrt{\sum*{i=1}^{n} w\_{d,i}^2}} $$

**Connection to Previous Step:**
In `02_tfidf_analysis.ipynb`, we observed that retaining stopwords results in large weights ($w_{i}$) for terms like "នៃ" (of) or "និង" (and). In the formula above, if both the Query and a non-relevant Document share these high-weight stopwords, the numerator ($\sum w_{q,i} \cdot w_{d,i}$) increases significantly. This artificially inflates the similarity score, causing non-relevant documents to be ranked highly (False Positives).

### 1.3 Evaluation Methodology: Known-Item Retrieval

To empirically validate the hypothesis, we employed a **Known-Item Retrieval** experiment.

1.  **Query Selection**: A subset of $N$ documents is randomly selected from the corpus to act as "queries". Let $d_{target}$ be one such document.
2.  **Retrieval Simulation**: The text of $d_{target}$ is treated as the search query $q$.
3.  **Ranking**: The system computes $\text{sim}(q, d_i)$ for all $d_i$ in the corpus and produces a ranked list $L$.
4.  **Performance Measurement**: We locate the rank of $d_{target}$ within $L$. Ideally, $Rank(d_{target}) = 1$.

### 1.4 Performance Metrics

We utilize two primary metrics to quantify performance:

**A. Mean Rank (MR)**
The average position of the target document across all queries. A lower Mean Rank indicates higher precision.

$$ MR = \frac{1}{|Q|} \sum*{i=1}^{|Q|} Rank(d*{target, i}) $$

**B. Recall at K (Recall@K)**
The probability that the relevant document appears within the top $K$ results (e.g., $K=10$).

$$ Recall@K = \frac{\text{Number of targets found in top K}}{|Q|} $$

---

## 2. Linguistic Analysis of Stopwords

**Notebook Reference:** `04_linguistic_analysis.ipynb`

### 2.1 Objective

While the IR evaluation provides quantitative evidence of performance improvement, the Linguistic Analysis provides the qualitative **"Why"**. It dissects the stopword list to understand which linguistic categories contribute most significantly to the noise reduction observed in the IR phase.

### 2.2 Structural vs. Frequency Analysis

**A. Structural Analysis (Dictionary Level)**
This measures the diversity of the stopword list itself.

- _Metric_: Count of unique terms per linguistic group (e.g., $N_{pronouns}$, $N_{prepositions}$).
- _Observation_: Some categories, like **Particles**, contains very few unique terms (low vocabulary size).

**B. Frequency Analysis (Corpus Level)**
This measures the impact of those terms on the actual data.

- _Metric_: Total Term Frequency ($TF_{total}$) of a category across the entire corpus.
- _Formula_:
  $$ TF*{category} = \sum*{t \in category} \sum\_{d \in Corpus} tf(t, d) $$

**Critical Insight**: A category might be structurally small (few unique words) but functionally massive (high corpus frequency). For example, Khmer **Particles** (like "ដ៏", "នូវ") have a low unique count but an extremely high $TF_{total}$. This identifies them as the primary source of vector noise.

### 2.3 Stopword Tiering Comparison

Based on the intersection of Structural and Frequency analysis, we classify words into removal tiers:

| Tier    | Category                           | Frequency Impact   | Semantic Value             | Recommendation        |
| :------ | :--------------------------------- | :----------------- | :------------------------- | :-------------------- |
| **I**   | **Particles** (e.g., ដ៏, នូវ)      | **Extremely High** | None (Syntactic only)      | **Mandatory Removal** |
| **I**   | **Prepositions** (e.g., នៃ, ក្នុង) | High               | Low (Relational)           | **Mandatory Removal** |
| **II**  | **Pronouns** (e.g., ខ្ញុំ, គេ)     | Medium             | Context-Dependent          | **Remove for Search** |
| **III** | **Auxiliary Verbs** (e.g., មិន)    | Medium             | **High** (Changes meaning) | **Retain**            |

### 2.4 Conclusion

The study concludes that the effectiveness of the Khmer Stopword Removal System is not due to random deletion, but due to the targeted removal of **Tier I** words. These words, identified via Linguistic Analysis, contribute disproportionately to the vector similarity noise mathematically proven in the IR Evaluation phase.

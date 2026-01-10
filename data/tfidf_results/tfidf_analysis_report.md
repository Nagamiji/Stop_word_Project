# TF-IDF Analysis Report

## Overview

Analysis conducted on 12 different corpora.

## Corpus Statistics

| Corpus            |   Documents |   Total_Terms |   Unique_Terms |   Avg_Doc_Length |   Vocabulary_Size |
|:------------------|------------:|--------------:|---------------:|-----------------:|------------------:|
| Original          |       58409 |       1703731 |          45524 |          29.169  |              2481 |
| No_All            |       58409 |       1207390 |          45325 |          20.6713 |              2478 |
| No_Auxiliary      |       58409 |       1636650 |          45506 |          28.0205 |              2481 |
| No_Conjunctions   |       58409 |       1597449 |          45486 |          27.3494 |              2480 |
| No_Determiners    |       58409 |       1658928 |          45509 |          28.4019 |              2481 |
| No_Function_Nouns |       58409 |       1655447 |          45486 |          28.3423 |              2481 |
| No_Numbers        |       58409 |       1685022 |          45513 |          28.8487 |              2481 |
| No_Particles      |       58409 |       1660710 |          45496 |          28.4324 |              2481 |
| No_Politeness     |       58409 |       1691024 |          45520 |          28.9514 |              2481 |
| No_Prepositions   |       58409 |       1588604 |          45495 |          27.1979 |              2480 |
| No_Pronouns       |       58409 |       1678950 |          45512 |          28.7447 |              2480 |
| No_Questions      |       58409 |       1688185 |          45518 |          28.9028 |              2481 |

## Key Findings

### Impact of Stopword Removal

- **Term Reduction**: 29.1% of total terms removed
- **Unique Term Reduction**: 0.4% of unique terms removed
- **Vocabulary Size Reduction**: 0.1% of TF-IDF features removed

### Most Effective Stopword Groups

Groups that removed the most terms:

| Rank | Corpus | Total Terms | Reduction from Original |
|------|--------|-------------|-------------------------|
| 10 | No_Prepositions | 1,588,604 | 6.8% |
| 4 | No_Conjunctions | 1,597,449 | 6.2% |
| 3 | No_Auxiliary | 1,636,650 | 3.9% |
| 6 | No_Function_Nouns | 1,655,447 | 2.8% |
| 5 | No_Determiners | 1,658,928 | 2.6% |

## Files Generated

1. **Top terms files** (`top_terms_*.txt`) - Top 100 terms by TF-IDF for each corpus
2. **TF-IDF matrices** (`tfidf_matrix_*.npz`) - Sparse TF-IDF matrices
3. **Feature lists** (`features_*.txt`) - Vocabulary for each corpus
4. **Summary files** - CSV files with statistics and comparisons
5. **Visualizations** - PNG charts showing distributions and comparisons
6. **This report** - Summary of findings

## Recommendations

1. **For information retrieval**: Use the 'No_All' corpus for best results
2. **For linguistic analysis**: Compare specific group removals
3. **For efficiency**: Consider 'No_Conjunctions' and 'No_Auxiliary' as they remove many frequent terms
4. **For precision**: Analyze which stopword groups affect your specific domain most

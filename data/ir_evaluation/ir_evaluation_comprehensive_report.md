# Information Retrieval Evaluation Report

## Executive Summary

### Key Findings:
- **Best Performing Corpus**: No_Questions (Mean Rank: 116.05)
- **Worst Performing Corpus**: No_All (Mean Rank: 295.06)
- **Improvement over Baseline**: 0.1% reduction in mean rank
- **Best Recall@10**: 0.990
- **Worst Recall@10**: 0.960

## Detailed Results

### Performance Ranking (by Mean Rank)
| Corpus            |   Mean_Rank |   Recall@5 |   Recall@10 |   Recall@20 |
|:------------------|------------:|-----------:|------------:|------------:|
| No_Questions      |      116.05 |       0.99 |        0.99 |        0.99 |
| No_Determiners    |      116.09 |       0.98 |        0.99 |        0.99 |
| No_Prepositions   |      116.1  |       0.98 |        0.99 |        0.99 |
| No_Particles      |      116.1  |       0.96 |        0.99 |        0.99 |
| No_Politeness     |      116.12 |       0.97 |        0.99 |        0.99 |
| Original          |      116.14 |       0.97 |        0.99 |        0.99 |
| No_Function_Nouns |      116.15 |       0.96 |        0.99 |        0.99 |
| No_Auxiliary      |      116.15 |       0.97 |        0.99 |        0.99 |
| No_Numbers        |      116.26 |       0.95 |        0.98 |        0.99 |
| No_Conjunctions   |      116.34 |       0.95 |        0.98 |        0.99 |
| No_Pronouns       |      294.87 |       0.97 |        0.97 |        0.98 |
| No_All            |      295.06 |       0.95 |        0.96 |        0.98 |

### Statistical Significance Analysis
Comparison of each filtered corpus against the Original baseline:
| Corpus            |   Percent_Improvement |   P_Value | Significant   |
|:------------------|----------------------:|----------:|:--------------|
| No_Questions      |             0.0774927 | 0.226699  | False         |
| No_Determiners    |             0.0430515 | 0.355752  | False         |
| No_Prepositions   |             0.0344412 | 0.581666  | False         |
| No_Particles      |             0.0344412 | 0.668443  | False         |
| No_Politeness     |             0.0172206 | 0.639699  | False         |
| No_Auxiliary      |            -0.0086103 | 0.656991  | False         |
| No_Function_Nouns |            -0.0086103 | 0.84851   | False         |
| No_Numbers        |            -0.103324  | 0.0702292 | False         |
| No_Conjunctions   |            -0.172206  | 0.227039  | False         |
| No_Pronouns       |          -153.892     | 0.319694  | False         |
| No_All            |          -154.055     | 0.319178  | False         |

### Impact by Stopword Group
Analysis of individual stopword group removal:
| Group_Type     |   Mean_Rank |   Recall@10 |
|:---------------|------------:|------------:|
| Questions      |      116.05 |        0.99 |
| Determiners    |      116.09 |        0.99 |
| Prepositions   |      116.1  |        0.99 |
| Particles      |      116.1  |        0.99 |
| Politeness     |      116.12 |        0.99 |
| Function_Nouns |      116.15 |        0.99 |
| Auxiliary      |      116.15 |        0.99 |
| Numbers        |      116.26 |        0.98 |
| Conjunctions   |      116.34 |        0.98 |
| Pronouns       |      294.87 |        0.97 |

### Most Impactful Groups
No groups showed statistically significant improvement.

### Query Analysis
- **Total Queries**: 100
- **Average Query Difficulty**: 146.0
- **Most Difficult Query**: Q027 (Avg Rank: 11495.0)
- **Easiest Query**: Q100 (Avg Rank: 1.0)

## Recommendations

### For Information Retrieval Systems:
1. **Recommended Corpus**: Use **No_Questions** for best retrieval performance

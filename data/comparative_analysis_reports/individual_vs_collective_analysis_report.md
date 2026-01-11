# Individual vs Collective Stopword Removal: Comprehensive Analysis

## Executive Summary

This report compares two approaches to Khmer stopword removal:
1. **Individual Group Removal**: Removing stopwords from one linguistic category at a time
2. **Collective Removal**: Removing all stopwords together

### Key Findings:
- **Collective improvement**: -178.92 rank improvement (-154.1%)
- **Best individual group**: Questions (0.09 improvement)
- **Synergy effect**: Collective removal is -0.09 (-0.1%) better than sum of individual removals
- **Most efficient group**: Questions (Efficiency: 0.001)

## 1. Performance Comparison

| Metric | Baseline | Collective | Best Individual |
|--------|----------|------------|-----------------|
| Mean Rank | 116.14 | 295.06 | 116.05 |
| Recall@10 | 0.990 | 0.960 | 0.990 |
| Improvement | 0.00 | -178.92 | 0.09 |

## 2. Synergy Analysis

When removing groups together:
- **Expected (additive model)**: 294.97
- **Actual (collective)**: 295.06
- **Synergy**: -0.09 (-0.1%)

**Conclusion**: Negative synergy - removing groups together is LESS effective than the sum of individual removals.

## 3. Group Rankings

### By Absolute Improvement:
| Rank | Group | Improvement | Efficiency |
|------|-------|-------------|------------|
| 1 | Questions | 0.09 | 0.001 |
| 2 | Determiners | 0.05 | 0.000 |
| 3 | Prepositions | 0.04 | 0.000 |
| 4 | Particles | 0.04 | 0.000 |
| 5 | Politeness | 0.02 | 0.000 |

### By Efficiency (Improvement/Rank):
| Rank | Group | Efficiency | Improvement |
|------|-------|------------|-------------|
| 1 | Questions | 0.001 | 0.09 |
| 2 | Determiners | 0.000 | 0.05 |
| 3 | Prepositions | 0.000 | 0.04 |
| 4 | Particles | 0.000 | 0.04 |
| 5 | Politeness | 0.000 | 0.02 |

## 4. Cost-Benefit Analysis

### Most Cost-Effective Groups:
| Group | Benefit/Stopword | Benefit/Token | Frequency % |
|-------|------------------|---------------|-------------|
| Questions | 0.0000 | 0.000000 | 0.00% |
| Determiners | 0.0000 | 0.000000 | 0.00% |
| Prepositions | 0.0000 | 0.000000 | 0.00% |
| Particles | 0.0000 | 0.000000 | 0.00% |
| Politeness | 0.0000 | 0.000000 | 0.00% |

## 5. Strategic Recommendations

### When to Use Individual Removal:
1. **Limited processing resources**: Remove only the most efficient groups
2. **Specific applications**: Target Questions for maximum efficiency
3. **Gradual implementation**: Start with top groups and expand as needed
4. **Domain-specific needs**: Customize based on your text characteristics

### When to Use Collective Removal:
1. **Maximum performance needed**: Use when every bit of improvement matters
2. **Sufficient resources available**: Processing power can handle full removal
3. **General-purpose applications**: When application domain is unknown
4. **Synergy benefits**: Take advantage of positive interaction effects

### Hybrid Strategy Recommendations:
1. **Start with**: Questions, Determiners, Prepositions
2. **Add if needed**: Particles, Politeness, Function Nouns
3. **Consider context**: Numbers, Conjunctions, Pronouns

## 6. Implementation Guidelines

### Quick Start:
1. For most applications: Use **collective removal**
2. For efficiency: Remove **top 3 groups** by improvement
3. For maximum ROI: Remove **Questions** only

### Advanced Tuning:
1. Monitor your specific corpus characteristics
2. Test different combinations for your application
3. Consider computational constraints
4. Balance between noise reduction and information preservation

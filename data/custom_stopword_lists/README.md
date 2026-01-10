# Custom Khmer Stopword Lists

These stopword lists are generated based on comprehensive linguistic analysis.

## Available Lists:

### Information Retrieval (Optimized)
- **File**: `khmer_stopwords_information_retrieval.txt`
- **Description**: Optimized for search and retrieval tasks
- **Aggressiveness**: high
- **Stopwords**: 388
- **Categories**: 6

### Text Mining & Topic Modeling
- **File**: `khmer_stopwords_text_mining.txt`
- **Description**: Balanced approach for topic modeling and analysis
- **Aggressiveness**: medium
- **Stopwords**: 437
- **Categories**: 8

### Linguistic Analysis
- **File**: `khmer_stopwords_linguistic_analysis.txt`
- **Description**: Conservative approach preserving grammatical words
- **Aggressiveness**: low
- **Stopwords**: 172
- **Categories**: 2

### Aggressive Filtering
- **File**: `khmer_stopwords_aggressive.txt`
- **Description**: Maximum noise reduction for preprocessing
- **Aggressiveness**: maximum
- **Stopwords**: 510
- **Categories**: 10

### Minimal Filtering
- **File**: `khmer_stopwords_minimal.txt`
- **Description**: Only the most critical stopwords
- **Aggressiveness**: minimal
- **Stopwords**: 55
- **Categories**: 1

## Recommendation Summary:

| Tier | Description | When to Use |
|------|-------------|-------------|
| 1 | Critical to remove | Always |
| 2 | Recommended to remove | Most applications |
| 3 | Context dependent | Specific tasks only |
| 4 | Optional/Specialized | Keep unless specifically targeting noise |

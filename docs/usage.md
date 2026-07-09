# Usage

This document explains how to use **UzbekTaggerBERT** for part-of-speech tagging of Uzbek text.

## Basic Python API

```python
from uzbek_tagger_bert import UzbekTaggerBERT

tagger = UzbekTaggerBERT()

text = "U yuz burib ketdi va yuz soat ishladi."
result = tagger(text)

print(result)
```

Expected output:

```text
U/PRON yuz/NOUN burib/VERB ketdi/VERB va/CCONJ yuz/NUM soat/NOUN ishladi/VERB ./PUNCT
```

The example demonstrates contextual homonym disambiguation. The word `yuz` is tagged as `NOUN` in one context and as `NUM` in another context.

## Tag a sentence

```python
from uzbek_tagger_bert import UzbekTaggerBERT

tagger = UzbekTaggerBERT()

result = tagger.tag_sentence("Bugun talabalar yangi mavzuni o‘rgandilar.")
print(result)
```

The output is a list of dictionaries:

```python
[
    {"token": "Bugun", "pos": "ADV", "start": 0, "end": 5},
    {"token": "talabalar", "pos": "NOUN", "start": 6, "end": 15},
    ...
]
```

## Tag multiple sentences

```python
from uzbek_tagger_bert import UzbekTaggerBERT

tagger = UzbekTaggerBERT()

sentences = [
    "Bugun talabalar yangi mavzuni o‘rgandilar.",
    "Bozordan olma olib kel.",
    "O‘rgan yaxshi odatdir."
]

results = tagger.tag_batch(sentences)

for tagged_sentence in results:
    print(tagger.to_slash(tagged_sentence))
```

## Output formats

UzbekTaggerBERT supports three output styles.

### Slash format

```python
tagger("Bugun talabalar keldi.", output_format="slash")
```

Example:

```text
Bugun/ADV talabalar/NOUN keldi/VERB ./PUNCT
```

### JSON format

```python
tagger("Bugun talabalar keldi.", output_format="json")
```

Example:

```python
[
    {"token": "Bugun", "pos": "ADV", "start": 0, "end": 5},
    {"token": "talabalar", "pos": "NOUN", "start": 6, "end": 15},
    {"token": "keldi", "pos": "VERB", "start": 16, "end": 21},
    {"token": ".", "pos": "PUNCT", "start": 21, "end": 22}
]
```

### CoNLL-like format

```python
tagged = tagger.tag_text("Bugun talabalar keldi.")
print(tagger.to_conll(tagged))
```

Example:

```text
Bugun    ADV
talabalar    NOUN
keldi    VERB
.    PUNCT
```

## Command-line usage

```bash
uzbek-tagger "U yuz burib ketdi va yuz soat ishladi."
```

JSON output:

```bash
uzbek-tagger "Bugun talabalar yangi mavzuni o‘rgandilar." --format json
```

CoNLL-like output:

```bash
uzbek-tagger "Bozordan olma olib kel." --format conll
```

## Integration into Uzbek NLP pipelines

UzbekTaggerBERT can be used as a preprocessing module for:

- morphological analysis;
- syntactic analysis;
- corpus annotation;
- educational NLP systems;
- retrieval-augmented grammar assistants;
- lexical-statistical text analysis.

Example integration:

```python
from uzbek_tagger_bert import UzbekTaggerBERT

tagger = UzbekTaggerBERT()
tokens = tagger.tag_text("Bugun talabalar yangi mavzuni o‘rgandilar.")

for item in tokens:
    token = item["token"]
    pos = item["pos"]
    # pass token and pos to a downstream morphological or syntactic analyzer
```

## Notes

The current public version is designed primarily for Uzbek Latin text. Cyrillic and mixed-script support can be added through additional transliteration or normalization modules in future releases.

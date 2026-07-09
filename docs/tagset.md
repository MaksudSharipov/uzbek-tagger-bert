# POS Tagset

UzbekTaggerBERT supports 16 Universal POS tags adapted for Uzbek part-of-speech tagging.

| Tag | English description | Uzbek explanation | Example |
|---|---|---|---|
| ADJ | Adjective | Sifat | yangi, katta, qizil |
| ADP | Adposition | Ko‘makchi | uchun, bilan, kabi |
| ADV | Adverb | Ravish | bugun, tez, sekin |
| AUX | Auxiliary | Yordamchi fe’l | edi, ekan, bo‘ladi |
| CCONJ | Coordinating conjunction | Teng bog‘lovchi | va, hamda, yoki |
| INTJ | Interjection | Undov | voy, eh, afsus |
| MOD | Modal word | Modal so‘z | kerak, lozim, mumkin |
| NOUN | Noun | Ot | kitob, talaba, maktab |
| NUM | Numeral | Son | bir, ikki, yuz |
| PART | Particle | Yuklama | -mi, -chi, faqat |
| PRON | Pronoun | Olmosh | men, u, biz |
| PROPN | Proper noun | Atoqli ot | Alisher, Toshkent, O‘zbekiston |
| PUNCT | Punctuation | Tinish belgisi | ., ,, !, ? |
| SCONJ | Subordinating conjunction | Ergash bog‘lovchi | chunki, agar, garchi |
| SYM | Symbol | Simvol | %, $, + |
| VERB | Verb | Fe’l | keldi, o‘qidi, ishladi |

## Notes on Uzbek POS tagging

Uzbek is an agglutinative language. A single word may contain several suffixes that express grammatical meanings such as possession, case, tense, person, number, and modality. For this reason, POS tagging in Uzbek requires contextual analysis rather than simple dictionary lookup.

## Contextual ambiguity

Some Uzbek words may belong to different POS classes depending on context.

Example:

```text
U yuz burib ketdi.
```

Here `yuz` means “face” and is tagged as `NOUN`.

```text
U yuz soat ishladi.
```

Here `yuz` means “hundred” and is tagged as `NUM`.

UzbekTaggerBERT uses a fine-tuned Tahrirchi-BERT Transformer model to resolve such contextual ambiguities.

## Apostrophe normalization

Uzbek Latin texts often contain several apostrophe-like characters:

```text
O'zbekiston
O‘zbekiston
Oʼzbekiston
Oʻzbekiston
```

The package normalizes common variants to reduce tokenization errors and improve alignment between subword tokens and original word boundaries.

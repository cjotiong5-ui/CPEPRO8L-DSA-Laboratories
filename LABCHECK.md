# Laboratory Submission Recheck

**Course:** CPEPRO8L — Data Structures and Algorithms Laboratory  
**Student:** Cristan Jay N. Otiong  
**Repository:** `cjotiong5-ui/CPEPRO8L-DSA-Laboratories`  
**Recheck date:** August 26, 2026  
**Status:** Provisional repository-based evaluation

## Recheck Summary

- Labs found: **1–10**
- Newly evaluated: **Labs 6, 7, 8, 9, and 10**
- Missing from the current sequence (Labs 1–7): **None**
- All submitted Python files compile successfully.
- All ten implementations pass the functional and edge-case tests.
- Six of the eight corrections from the August 14 recheck were applied.

## Evaluation Criteria

| Criterion | Weight |
|---|---:|
| Program Correctness and Functionality | 40% |
| Code Quality and Organization | 20% |
| Analysis and Understanding | 20% |
| Documentation (`README.md`) | 10% |
| GitHub Repository Organization and Submission | 10% |
| **Total** | **100%** |

## Updated Results

| Laboratory | Correctness /40 | Code /20 | Analysis /20 | Documentation /10 | Repository /10 | Grade |
|---:|---:|---:|---:|---:|---:|---:|
| Lab 1 | 40 | 17 | 17 | 9 | 8 | **91/100** |
| Lab 2 | 40 | 19 | 20 | 9 | 8 | **96/100** |
| Lab 3 | 40 | 17 | 18 | 9 | 8 | **92/100** |
| Lab 4 | 40 | 17 | 16 | 7 | 8 | **88/100** |
| Lab 5 | 40 | 18 | 10 | 6 | 8 | **82/100** |
| Lab 6 | 40 | 17 | 15 | 8 | 8 | **88/100** |
| Lab 7 | 40 | 18 | 20 | 9 | 8 | **95/100** |
| Lab 8 | 40 | 18 | 20 | 9 | 8 | **95/100** |
| Lab 9 | 40 | 18 | 19 | 8 | 8 | **93/100** |
| Lab 10 | 40 | 18 | 17 | 6 | 8 | **89/100** |
| **Average of submitted labs** | **40.0** | **17.7** | **17.2** | **8.0** | **8.0** | **90.9/100** |

Labs 1–7 are all present, so no completion adjustment applies to the required sequence.

## Corrections Verification (August 14 list)

| # | Correction | Status |
|---|---|---|
| 1 | Lab 5 documents five customized mathematical expressions | **Applied** |
| 2 | Lab 5 includes a step-by-step stack trace for `{[()]}` | **Applied** |
| 3 | Lab 5 README references `lab5_bracket_parser.py` | **Applied** |
| 4 | Lab 4 report placeholder name and date replaced | **Applied** |
| 5 | Reports renamed `read.md` → `README.md` | **Applied** |
| 6 | Root README expanded with a laboratory index | **Not applied** — still a title only |
| 7 | Leftover `TODO` comments and Lab 3 `pass` removed | **Applied** |
| 8 | Labs 6 and 7 submitted | **Applied** — Labs 8–10 also submitted |

## Verified Tests

- Labs 1–5: all previously passing tests remain passing.
- Lab 6: FIFO ordering, overflow rejection, underflow warning, and circular wraparound with freed-slot reuse.
- Lab 7: first, middle, and last targets; absent target; empty-range base case; all five results match the report table.
- Lab 8: inorder, preorder, and postorder traversals verified against the report (`20 30 40 50 60 70 80`, `50 30 20 40 70 60 80`, `20 40 30 60 80 70 50`).
- Lab 9: all four rotation cases (LL, RR, LR, RL) rebalance to a height-2 tree rooted at 20 with correct children.
- Lab 10: real collision demonstrated (Alice and Eve both hash to bucket 3 and chain correctly); update-if-exists, retrieval, and load factor verified.

## Important Documentation Finding

Several new reports contain **unedited generated text** that should have been removed before submission:

- **Lab 10 README:** leftover self-correction passages remain in the hash-computation section — *"Let me verify with the actual hash function:"*, *"Actually, let me compute precisely:"*, *"Hmm, let me recompute Charlie…"* — together with an incorrect intermediate sum (588; the correct ASCII sum for "Charlie" is 696). The final console-output values shown are correct.
- **Lab 6 README:** the phrase “reusing空位 positions” contains Chinese characters (“空位”).
- **Lab 9 README:** “普通” appears three times where "ordinary" was intended.
- **Lab 9, Test 3:** the insertion sequence `[10, 30, 20]` is labeled the **LR case** in both the source comment and the README heading; it is the **RL case** (the trace text below the heading describes the double rotation correctly).

The implementations themselves are correct and independently verified; these findings affect documentation quality and raise an authorship question the instructor may wish to address (for example, through an oral or code defense).

## Corrections Required

1. Remove the leftover generated reasoning passages and the incorrect intermediate table from the Lab 10 README; keep one clean, correct hash-computation table.
2. Remove the Chinese-character artifacts from the Lab 6 (“空位”) and Lab 9 (“普通”) READMEs.
3. Relabel Lab 9 Test 3 as the **RL case** in the source comment and the README heading.
4. Add the required 10-enqueue/dequeue state trace to Lab 6 — in both the report and the source driver (only the 5-operation sample is currently recorded).
5. Expand the root `README.md` with a laboratory index and links (outstanding since August 14).
6. Remove `LABCHECK.md` from the repository before final submission; it is an instructor document, not a deliverable.

## Instructor Note

The completion of the full Lab 1–10 sequence is a strong effort, and Labs 7–9 are excellent — accurate stack-trace and rotation diagrams with thorough complexity analysis. The new deductions concern the unproofread generated text in the reports rather than the code. Scores may be adjusted for deadlines, late submissions, or an oral/code defense.

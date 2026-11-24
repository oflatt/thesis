# E-Graphs for Everything

Oliver Flatt's Ph.D. general examination report, University of Washington.
Exam: December 1, 2026, 12:30 p.m., Gates 253. The year is inferred from the
November 2026 setup date; edit `metadata.tex` if needed.

## Build

Run `make` from this directory to create `build/main.pdf` and `abstract.txt`.
Run `make review` to create `build/review/review.pdf`, a reading copy without
blue source notes or gray drafting prompts. The normal build keeps both visible.
`make abstract` (or `make abstract.txt`) updates only the plain-text abstract;
`latexmk` builds only the PDF. `make watch` updates the abstract once and then
rebuilds the PDF on edits; `make clean` removes generated output.

The abstract exporter follows the extended-egglog paper's production workflow:
it removes formatting, preserves paragraphs, and rejects unsupported LaTeX.
It also removes citations for a standalone submission-form abstract; the PDF
retains its citations. Edit `sections/abstract.tex`, then regenerate the text.

Dependencies: Python 3 and TeX Live or MiKTeX with pdfLaTeX, BibTeX, and latexmk, plus the
packages in `preamble.tex`. The font packages are Libertine, newtxmath, and
DejaVuSansMono. They are installed in the current environment.

For Overleaf, upload the source files and choose `main.tex` with pdfLaTeX.

## Editing

- `metadata.tex`: title, author, exam logistics, committee, and contact comments.
- `main.tex`: cover, abstract, contents, section order, and bibliography block.
- `sections/`: abstract and report sections. Gray text marks drafting prompts.
- `preamble.tex`: typography, packages, theorem environments, `\draftnote`,
  and `\sourcenote`.
- `scripts/abstract-text.py`: plain-text abstract export.
- `references.bib`: verified references; `figures/`: figure assets.

The background uses the nested-sum example from
`../extended-egglog-paper/background.tex` throughout the e-graph explanation,
complete egglog program, and proof sequence. The program uses the paper's
mathematical syntax, with initialization, analysis and rewrite schedules,
and the final equality check; its commands and explanatory comments are retained,
with line breaks adapted to the report.
`figures/sum-egraph.tex` is an editable TikZ diagram with operator and leaf labels,
solid child pointers, and dashed equality edges; it compiles as part of the report.
Only the input is labeled. The fully distributed result illustrates a term
that extraction can assemble without a separate node for that whole term.
The background introduces e-graphs through terms and congruence closure,
then explains e-nodes as the compact representation. Proof-certificate definitions come from
*Small Proofs from Congruence Closure*. Source notes distinguish the adapted
example and new diagram from verbatim prose.

Replace drafting prompts with prose. Blue source notes above passages identify
their paper of origin; adjacent LaTeX comments record the source file.
Each note classifies the whole following paragraph: **Verbatim** means unchanged
prose apart from LaTeX/citation formatting; **Edited** means adapted or combined
text, including mixtures of copied and revised sentences; **New** means new
framing or synthesis, with its basis identified.
Use `make review` to hide both prompts and source notes without changing the
working draft. `review.tex` selects this mode before loading `main.tex`.
Use `\label{...}` with `\ref{...}` or `\autoref{...}` for cross-references.

Draft by adapting the author's existing papers, then revise with
[Yihong's writing guide](https://github.com/yihozhang/style/blob/main/SKILL.md).
Preserve the source passages where they fit, connect them to the thesis,
and distinguish established results from proposed work.

The bibliography is enabled. Add entries to `references.bib` and cite them
with `\cite{key}`; `make` runs BibTeX and the necessary LaTeX passes.
The abstract, introduction, and background material are drafted with citations.
Background draws on Small Proofs, eggcc, and Extended E-Graphs via Compilation
to introduce e-graphs, equality saturation, analyses, egglog, and proof certificates,
including a shared e-graph figure and example proof. Each project begins with its
specialized background: congruence proof generation, effects and control flow,
variable binding and slotted e-graphs, or verified compilation and translation validation.
Comparisons and novelty belong in the project sections.
Their related-work subsections adapt the author's papers and include a literature
review of verified compilation, translation validation, and proof-assistant integration.
The proof production section is drafted from *Small Proofs from Congruence Closure*,
including the two proof-size metrics, TreeOpt and greedy algorithms, and evaluation.
TreeOpt is presented as the theoretical result and evaluation baseline, with its
`O(c^2 m)` bound exposing dependence on the number of congruence edges;
greedy proof search is the practical algorithm, with an `O(n log n + c)` bound
for a fixed recursive-search budget. Both proof algorithms are parameterized by
the number of congruence edges. The introduction, extraction section, evaluation
plan, and conclusion connect this analysis to statewalk width as a recurring
theme in parameterized algorithm design.
The proof section keeps the nested `f`/`g` inference tree to explain tree and DAG
size, and summarizes the evaluation in prose. The unused
`figures/proof-size-comparison.pdf` remains available as the unchanged Figure 8
from that paper. Source notes distinguish verbatim prose, edited passages,
and new connections to the thesis.
The effect-safe extraction section is drafted from *Efficient Extraction for
Effectful E-graphs*. It develops the repeated-update example, statewalk DP and
its statewalk-width bound, the correctness guarantees, implementation, and evaluation.
`figures/effect-safe-extraction.pdf` is the unchanged Figure 3 from that paper.
The report crops its four panels into two rows for readability, with an adapted caption.
The numerical results come from the camera-ready paper and its generated macros.
The composable extensions section is drafted from *Extended E-Graphs via
Compilation*, currently under submission. It covers the pass architecture,
proofs of analysis results, slotted compilation, the scope of the Lean
formalization, and the evaluation. `figures/extension-pipeline.tex` simplifies
the paper's architecture diagram. A proof tree expands the running example's
analysis precondition, and a generated path-compression rule illustrates proof lifting.
Evaluation distinguishes proof recording from the full
cost of reconstruction and checking.

Section 6 is drafted from Oliver's research plan and primary literature. The Lean
checker experiment in `../extended-proofs/semantics` and its soundness proof are
complete; the missing work is the egglog round trip and a reusable library for
theorem export, certificate import, and runtime validation. The section states
the target correctness theorem and compares bounded CompCert, NetKAT, and
Luminal case studies in a table as alternatives. `figures/verified-compilation-pipeline.tex`
distinguishes developer-supplied definitions and proofs from automatic library
work and generated artifacts, then shows automatic compiler execution. The target
theorem establishes the selected congruence relation. Connecting the existing
checker theorem to semantic correctness, and interpreting analysis facts for
specific terms, remain open research questions. The compiler developer supplies
IR-specific validation checks and their soundness proofs, including effect safety.
The Luminal candidate would exercise effect-safe extraction; NetKAT would not.
New proposal text and literature summaries are marked **New** in source notes.

Section 7 follows Oliver's November 20 schedule: cleanup and the egglog journal
paper through February 2027, verified-compilation work beginning March 2027,
and dissertation completion and graduation targeted for May 2028. Intermediate
milestones are proposed: a small-language round trip in spring, the case study
in summer, evaluation and paper preparation in September–October, then a projected
November 2027 submission to PLDI 2028, Oliver's primary target. Revisions and
dissertation writing follow through spring 2028.

The provisional section order in `main.tex` is:

1. **Introduction** (`sections/introduction.tex`): motivation, thesis claim,
   and how each project supplies evidence for it.
2. **Background** (`sections/related-work.tex`): e-graphs, equality saturation,
   analyses, egglog, and proof certificates, with a shared figure and worked proof.
3. **Proof Production and Minimization** (`sections/proofs.tex`): background on
   congruence proof generation, algorithms for small proofs, evaluation, and
   applications to checking and explanations such as Herbie's.
4. **Effect-Safe Extraction** (`sections/effectful-extraction.tex`): background on
   effects and RVSDGs, the extraction problem, the parameterized algorithm,
   evaluation, and scope of the guarantees.
5. **Composable E-Graph Extensions** (`sections/extensions.tex`): background on
   binding and prior slotted e-graphs, then extensions via compilation, including
   proofs of analysis results and the slotted pass.
6. **Remaining Work: Verified Compilation** (`sections/proposed-work.tex`): completed
   checker experiment, proposed library, round-trip correctness theorem, alternative
   case studies, evaluation and completion criteria, and related work.
7. **Dissertation Plan and Timeline** (`sections/timeline.tex`): chapters,
   dated milestones, and the projected PLDI 2028 submission window.
8. **Conclusion** (`sections/conclusion.tex`): contributions and scope.

Each project presents background, its contribution or proposed approach, and related work.
The proof-minimization section focuses on the Small Proofs work;
proof production for analyses appears with the compilation-based extensions.
The contents page lists only
these top-level sections and the references.

## Format provenance

The outline uses Gus Henry Smith's proposal below as an organizational example:
state a thesis, explain how each research project supports it, and give the
remaining work and timeline their own sections. Content requirements follow the UW
[Thesis Proposal Style sample charge](<resources/Thesis Proposal Style – Paul G. Allen School Internal.pdf>)
(page 1), supplied on November 17, 2026. This is a prose content template, not
a downloadable LaTeX class or source template; no LaTeX template is linked in
the supplied PDFs.

No public Max Willsey general-exam template was located. Typography follows
the typography of [Max Willsey's dissertation source](https://github.com/mwillsey/thesis/blob/68a8459d41a166bbd5d336e0aeeda5b2a72f9cc5/thesis.tex)
at commit `68a8459d41a166bbd5d336e0aeeda5b2a72f9cc5`:
12-point type, Libertine text, newtx mathematics, DejaVu Sans Mono, microtype,
and an alphabetic BibTeX style. The
[upstream README](https://github.com/mwillsey/thesis/blob/68a8459d41a166bbd5d336e0aeeda5b2a72f9cc5/README.md)
credits Max and identifies the dissertation as CC BY 4.0.

This is a new, single-sided `article` scaffold with one-inch margins and single
spacing. It replaces the dissertation's `book` layout, double spacing,
degree-submission front matter, and chapters with an exam cover and sections.
It contains no dissertation prose and is not an official UW template.

## Example general-exam reports

Collected November 17, 2026. Gus's proposal was supplied by the user; the two
other PDFs were downloaded from their authors' sites and identify themselves
as UW general-exam reports.

- [Gus Henry Smith, *Generating Compilers from Formal Models of Hardware*](resources/2022_thesis_proposal.1.pdf)
  (46 pages; PDF generated January 18, 2023, with a 2022–2023 project timeline).
  The closest topical example: it connects a single thesis hypothesis to
  background and related work, completed work on Glenside and 3LA, and proposed
  work on Lakeroad. Start with the abstract and thesis framing on pages 1–2,
  the proposed-work section beginning on page 30, and the explicit out-of-scope
  work and timeline on page 37. Its hypothesis names concrete outcomes:
  development time, bugs, and emergent optimizations.
- [Brandon Holt, *Mitigating Contention in Distributed Systems*](resources/holt-2015-generals.pdf)
  (32 pages). His [CV](https://bholt.org/cv.html) dates the exam to December 2015;
  the hosted PDF was generated in August 2016.
  [Original PDF](https://bholt.github.io/gen/generals.pdf).
  A useful example of thematic related work followed by completed research
  and proposed work, particularly Sections 6–8.
- [Jonathan Aldrich, *Evaluating Module Systems for Crosscutting Concerns*](resources/aldrich-2000-generals.pdf)
  (September 28, 2000; 23 pages).
  [Original PDF](https://www.cs.cmu.edu/~aldrich/papers/generals.pdf).
  An older, survey-style example that compares approaches against common
  challenges and discusses future research.

Use these as examples of writing and organization; their lengths and formats
do not replace the current handbook or the chair's charge. A renewed public
search did not locate Max Willsey's general-exam report; the source linked
above is his dissertation.

## UW guidance and open context

The user supplied PDF exports of both internal pages on November 17, 2026:

- [General Examination](<resources/General Examination – Paul G. Allen School Internal.pdf>),
  from the [general-exam handbook page](https://internal.cs.washington.edu/grad-advising/phd/handbook/generals/).
- [Thesis Proposal Style](<resources/Thesis Proposal Style – Paul G. Allen School Internal.pdf>),
  from the [sample-charge page](https://internal.cs.washington.edu/grad-advising/phd/handbook/generals/thesis-proposal-style/).

These PDFs supersede the earlier search-indexed public-page notes. The current
general-exam checklist and report instructions consistently specify **at least
one week** for committee circulation. The old two-week report deadline and
eight-week charge-to-exam rule are not present in these supplied pages.

### Report structure

The chair's individual charge governs the report. The general handbook says
most reports are under 20 pages, with length at the chair's discretion. Until
an individual charge is available, this scaffold follows the sample charge:

- **Length:** at most 20 pages, excluding references. The sample does not say
  whether cover and contents pages are excluded; budget conservatively.
- **Introduction:** problem and motivation, background, thesis statement,
  hypotheses or goals, key technical ideas, and likely contributions.
- **Related work:** approximately half the report. Organize around themes,
  evaluate foundational and competing approaches critically, and explain how
  the proposed approach differs and why it has not been attempted before.
- **Proposed work:** mark each part's completion status. Summarize finished
  work briefly; give concrete plans for remaining challenges, innovations,
  evaluation, limitations, and risks. The project sections summarize current
  results; `sections/proposed-work.tex` develops the remaining research and
  `sections/timeline.tex` gives the dissertation plan.
- **Conclusion:** contributions and discussion, including future work outside
  the scope of the dissertation.

The sample charge asks the committee to assess novelty and significance,
whether evaluation can establish the hypotheses, mastery of related work,
writing and presentation, and the feasibility of finishing within the next
year. The explicit timeline section is a scaffold choice supporting that
assessment, not a mandated heading.

Both report and talk should cover the thesis claim, related research, and
proposed results or dissertation chapters, subject to the chair's emphasis.
Use appropriate citations. The handbook permits discussion with the advisor
and colleagues but requires independent writing (General Examination, page 3).

### Dates and presentation

For the December 1, 2026 exam, the checklist implies these dates:

| Item | Deadline | PDF location |
| --- | --- | --- |
| Confirm MyCSE announcement settings; enter title and abstract | November 17, 2026 | General Examination, page 1 |
| Email the report to every committee member | November 24, 2026, unless otherwise directed by the chair | General Examination, pages 1 and 3 |
| Present the exam | December 1, 2026, 12:30 p.m., Gates 253 | User-supplied exam details |
| Upload the report to MyCSE | After the exam | General Examination, page 1 |

The oral exam typically lasts 90 minutes and begins with a 40-minute student
presentation, followed by a closed session. The chair, GSR, and at least two
additional committee members must attend. The handbook also requires a video
conferencing link for all presentations (pages 2–4).

No individual charge is available yet. The abstract supplies a working thesis
claim. Oliver confirmed on November 20 that the verified Lean checker experiment
is complete, while the egglog round-trip integration and library remain proposed.
The case-study choice remains open. The dated dissertation schedule is drafted
in Section 7; its intermediate milestones are provisional. Contexts are optional
unless the selected application needs them.

For the current shortening pass, Oliver prefers a conservative target in the low
twenties before references, allowing some excess over 20 pages to preserve clarity.
Measure this using the review PDF, including its two front-matter pages.

### Submission planning

Checked November 20, 2026 against the official calls below. No published 2028
deadlines were located; the 2028 windows are projections from the preceding
cycle, not announced dates.

| Candidate | Submission date or planning window | Role in this schedule |
| --- | --- | --- |
| OOPSLA 2027, round 2 | **Confirmed:** April 7, 2027, AoE | Too early for the full project after a March start. |
| POPL 2028 | **Projected:** July 2027 | Earlier option considered; requires results much earlier than the current plan. |
| OOPSLA 2028, round 1 | **Projected:** October 2027 | Alternative considered for the reusable library and its applications. |
| PLDI 2028 | **Projected:** November 2027 | Oliver's primary target; the timeline reserves September–October for evaluation and paper preparation. |

The projections use the [POPL 2027 call](https://popl27.sigplan.org/track/POPL-2027-popl-research-papers)
(July 9, 2026), [OOPSLA 2027 call](https://2027.splashcon.org/track/splashoopsla2027)
(round 1: October 14, 2026; round 2: April 7, 2027), and
[PLDI 2027 call](https://pldi27.sigplan.org/track/pldi-2027-papers)
(November 12, 2026). Venue fit and feasibility assessments above are planning
judgments, not requirements from those calls. The current schedule targets PLDI
2028; the other venues record the alternatives considered.

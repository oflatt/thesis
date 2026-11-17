# E-Graphs for Everything

Oliver Flatt's Ph.D. general examination report, University of Washington.
Exam: December 1, 2026, 12:30 p.m., Gates 253. The year is inferred from the
November 2026 setup date; edit `metadata.tex` if needed.

## Build

Run `make` (or `latexmk`) from this directory to create `build/main.pdf`.
`make watch` rebuilds on edits; `make clean` removes generated output.

Dependencies: TeX Live or MiKTeX with pdfLaTeX, BibTeX, and latexmk, plus the
packages in `preamble.tex`. The font packages are Libertine, newtxmath, and
DejaVuSansMono. They are installed in the current environment.

For Overleaf, upload the source files and choose `main.tex` with pdfLaTeX.

## Editing

- `metadata.tex`: title, author, exam logistics, committee, and contact comments.
- `main.tex`: cover, abstract, contents, section order, and bibliography block.
- `sections/`: abstract and report sections. Gray text marks drafting prompts.
- `preamble.tex`: typography, packages, theorem environments, and `\draftnote`.
- `references.bib`: verified references; `figures/`: figure assets.

Replace drafting prompts with prose. To hide remaining prompts in a review
copy, change `\draftnotestrue` to `\draftnotesfalse` in `preamble.tex`.
Use `\label{...}` with `\ref{...}` or `\autoref{...}` for cross-references.

After adding the first bibliography entry and a `\cite{key}`, uncomment the
bibliography block at the end of `main.tex`. Then `make` runs BibTeX and any
necessary LaTeX passes. The empty scaffold intentionally has no sample papers
or research claims.

## Format provenance

The content outline follows the UW
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
  evaluation, limitations, and risks. `sections/research-progress.tex` is a
  subsection within `sections/proposed-work.tex`.
- **Conclusion:** contributions and discussion, including future work outside
  the scope of the dissertation.

The sample charge asks the committee to assess novelty and significance,
whether evaluation can establish the hypotheses, mastery of related work,
writing and presentation, and the feasibility of finishing within the next
year. The explicit timeline subsection is a scaffold choice supporting that
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

No individual charge is available yet. Research projects, the thesis claim,
and evaluation plans have not been supplied. The outline remains provisional.

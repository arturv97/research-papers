# Research Papers Repository

This repository is used to organize, summarize, and connect research papers.

## Structure

- `papers/`: Individual paper notes organized by year
- `topics/`: Notes grouping papers by topic
- `templates/`: Templates for new papers
- `assets/pdfs/`: Stored PDFs
- `scripts/`: Helper scripts

## Workflow

1. Add a new paper using the script
2. Fill metadata and summary
3. Add tags and insights
4. Link to related papers
5. Update topic files if needed

## Naming Convention

firstauthor_year_short-title.md

Example:
smith_2024_embedded_linux.md

---

## Integrations

### Obsidian
- Open this folder as a vault
- Use `[[paper_name]]` to create links
- Enables backlinks and knowledge graph

### Zotero (Basic Flow)
1. Store PDFs in Zotero
2. Rename as: `author-year-title.pdf`
3. Copy to `assets/pdfs/`
4. Reference in markdown

---

## Scripts

### Create new paper
```bash
./scripts/new_paper.sh author-year-paper-title
```

### Import from BibTeX
```bash
python3 scripts/import_bibtex.py references.bib
```

### Generate Survey
```bash
python3 scripts/generate_survey.py embedded-linux
```

### PDF Export

This repository provides a Python script to convert Markdown papers into PDF format using `pandoc`. Therefore, check how to install it into your OS.

```bash
python3 scripts/export_pdf.py <input>
```

The script supports:
- Single file
- Directory (recursive)
- Pattern (wildcard)

#### Examples
**Convert a single paper**
```bash
python3 scripts/export_pdf.py papers/year/example.md
```

**Convert all papers in a directory**
```bash
python3 scripts/export_pdf.py papers/year/
```

**Convert using pattern**
```bash
python3 scripts/export_pdf.py "papers/year/author*"
```
>Note: Use quotes when using wildcards.


#### Output Structure

All PDFs are generated under the `output/` directory.

**Input**
```bash
papers/year/author-year-paper-title.md
```

**Output**
```bash
output/year/author-year-paper-title.pdf
```

---

## TODO

- [ ] Advanced Zotero integration (API/plugin)
- [ ] Automatic PDF sync

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
2. Rename as: `author_year_title.pdf`
3. Copy to `assets/pdfs/`
4. Reference in markdown

---

## Scripts

### Create new paper
```bash
./scripts/new_paper.sh smith_2026_topic
```

### Import from BibTeX
```bash
python3 scripts/import_bibtex.py references.bib
```

### Generate Survey
```bash
python3 scripts/generate_survey.py embedded-linux
```

---

## TODO

- [ ] Advanced Zotero integration (API/plugin)
- [ ] Automatic PDF sync

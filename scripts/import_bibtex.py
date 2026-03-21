import sys, os, re

def parse_bibtex(file):
    entries = []
    with open(file) as f:
        content = f.read()

    raw_entries = content.split("@")[1:]
    for entry in raw_entries:
        fields = {}
        for line in entry.split("\n"):
            match = re.match(r"\s*(\w+)\s*=\s*[{"](.*)[}"]", line)
            if match:
                fields[match.group(1).lower()] = match.group(2)
        entries.append(fields)
    return entries

def create_md(entry):
    year = entry.get("year", "unknown")
    author = entry.get("author", "unknown").split(" ")[0]
    title = entry.get("title", "paper").replace(" ", "_")

    filename = f"papers/{year}/{author}_{year}_{title}.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(f"# {entry.get('title','')}\n\n")
        f.write("## Metadata\n")
        f.write(f"- **Authors:** {entry.get('author','')}\n")
        f.write(f"- **Year:** {year}\n")
        f.write(f"- **Conference/Journal:** {entry.get('journal','')}\n")
        f.write(f"- **DOI/URL:** {entry.get('url','')}\n")
        f.write("- **Tags:** \n- **PDF:** \n")

if __name__ == "__main__":
    for entry in parse_bibtex(sys.argv[1]):
        create_md(entry)

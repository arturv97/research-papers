import os, sys

tag = sys.argv[1]
output = f"survey_{tag}.md"

results = []

for root, _, files in os.walk("papers"):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path) as f:
                content = f.read()
                if tag in content:
                    title = content.split("\n")[0].replace("# ","")
                    results.append(f"- {title} ({path})")

with open(output, "w") as f:
    f.write(f"# Survey: {tag}\n\n")
    for r in results:
        f.write(r + "\n")

print(f"Generated {output}")

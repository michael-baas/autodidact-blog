import datetime as dt, json, yaml, pathlib, textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
topics = yaml.safe_load((ROOT / "_data" / "topics.yml").read_text())["queue"]

today = dt.datetime.utcnow().date()
slug_date = today.strftime("%Y-%m-%d")

# rotate queue

topic = topics.pop(0)
topics.append(topic)
(ROOT / "_data" / "topics.yml").write_text(yaml.safe_dump({"queue": topics}, sort_keys=False))

# prepare post paths

title = topic["title"]
slug = f"{slug_date}-{topic['id']}".replace(" ", "-") + ".md"
post_path = ROOT / "_posts" / slug
post_path.parent.mkdir(parents=True, exist_ok=True)

def section(h, body):
    return f"## {h}\n\n{body.strip()}\n"

def screenshot(note):
    return f"📸 _Screenshot here:_ {note}\n"

glossary_terms = {
    "lhtl-focused-diffuse": ["focused", "diffuse"],
    "lhtl-pomodoro": ["pomodoro"],
    "lhtl-chunking": ["chunking"],
    "lhtl-spaced-repetition": ["spaced repetition"],
    "comp-what-is-a-computer": ["computer", "hardware", "software"],
    "comp-hardware-vs-software": ["hardware", "software"],
    "comp-files-folders": ["file", "folder"],
    "comp-input-output": ["keyboard", "mouse", "screen"],
    "net-computers-talk": ["internet"],
    "net-wifi-vs-data": ["wifi", "data"],
    "cloud-what": ["cloud"]
}.get(topic["id"], [])

front_matter = {
    "layout": "post",
    "title": title,
    "date": f"{slug_date} 18:00:00 -0400",
    "tags": topic["tags"],
    "reading_level": "beginner",
    "glossary": glossary_terms
}

sections = []

# generate sections based on topic type
if topic["kind"] == "lhtl" and topic["id"] == "lhtl-focused-diffuse":
    sections.append(section("In simple words",
        "Learning is easier when we switch between {% include term.html key='focused' text='focused thinking' %} "
        "and {% include term.html key='diffuse' text='relaxed thinking' %}."))
    sections.append(section("Try this",
        "- Set a 25‑minute timer (Pomodoro). Work on one small step.\n"
        "- Take a 5‑minute break. Repeat.\n"))
    sections.append(screenshot("Timer app window with 25:00 visible"))
else:
    sections.append(section("In simple words", "Short, friendly explanation here."))
    sections.append(section("Why it matters", "One or two practical reasons."))
    sections.append(section("Try this", "- A tiny task the reader can do now."))
    sections.append(screenshot("The exact screen they should see after the step."))

body = "\n\n".join(sections)

# assemble markdown
md = f"""---
{yaml.safe_dump(front_matter, sort_keys=False).strip()}
---

> This lesson uses **plain English** and adds hover definitions for uncommon words.

{body}

---

_This daily draft is generated automatically. Please edit freely before publishing._
"""

post_path.write_text(md, encoding="utf-8")
print(f"Created {post_path}")

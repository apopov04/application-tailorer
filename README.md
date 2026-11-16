# Application Tailorer

Turn past application answers into tailored responses for new companies and questions.

Give your agent past questions and the exact answers you wrote, including rough drafts, then the new question, company/role and length limit. The skill chooses the useful evidence, keeps your voice, rebuilds the company connection and explains the consequential edits. With no old answers, it works from your notes and focused questions.

## Use it

Clone or download this repository. Install the complete `application-tailorer` folder using your agent’s skill instructions, or provide SKILL.md, references/ and scripts/ together.

> Use Application Tailorer. Ask me for past application questions and exact answers first. Adapt them to this new question and company, keep my voice and check the limit. Give the answer first, with important edits and missing facts explained separately.

The skill can handle one response or a coherent batch. It separates personal evidence from writing style, checks employer versus agency/client identity where unclear, and asks for missing motivations rather than inventing them. Supplied or confirmed facts stay distinct from provisional ideas. A persistent answer bank is created only when requested.

## Research and limits

[Research notes](references/research-notes.md) and the [source ledger](references/evidence-ledger.json) record seven public discussion sources plus two policy/instruction supplements, reviewed 16 November 2026. Anonymous roles and outcomes are self-described. One discussion was available only through search excerpts; its weaker retrieval is labeled. These reports do not establish universal AI bans, reliable detectors, automatic rejection or a hidden score.

The skill uses research when it changes a recommendation, and checks relevant supplied assessment rules. It does not append hiring folklore to ordinary copy edits. The [question guide](references/question-strategies.md) is editorial guidance, not an employer scoring rubric.

## Length checks

Python 3’s standard library is sufficient:

```sh
python3 scripts/check_length.py answer.txt --max-words 150
python3 scripts/check_length.py answer.txt --max-characters 1000
```

The file should contain only the final answer. Counts include whitespace and distinguish Unicode characters from UTF-16 code units. Portals can count differently; use their stated rule when available. The checker exits 1 when a supplied cap is exceeded.

## Privacy and cost

This repository is an instruction package, not an upload service. Your agent/provider processes the material under its own settings and usual usage costs. No separate API key is needed. Drafting does not authorize submitting an application or contacting an employer.

Created for [Unempluzzed](https://unempluzzed.com). Previously published as Application Answer Adapter; the current skill invocation is `$application-tailorer`.

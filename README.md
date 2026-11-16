# Application Answer Adapter

An agent skill for adapting your past job-application answers to new questions, companies and roles. Start with questions and answers you have already written, including rough drafts. The skill separates reusable personal evidence from old company details, preserves your voice and checks the new question and length limit.

## Use it

Clone or download this repository. Install the complete folder using your agent’s skill instructions, or provide `SKILL.md`, `references/` and `scripts/` directly.

> Use Application Answer Adapter. Ask me for past questions and answers first, then help adapt them for my next application. Preserve my voice and check the limit.

Provide the new exact question, target company/role, relevant posting and word/character cap. If you have no old answers, the skill works from your experience and focused questions. Persistent answer banks are optional and created only when requested.

The bundled length checker uses Python 3’s standard library. It reports words, Unicode characters and UTF-16 code units; an application portal may count differently. No separate API key or service is needed. Your agent/provider’s usual usage costs and document settings apply.

Created for [Unempluzzed](https://unempluzzed.com). This package drafts answers; it does not submit applications or contact employers.

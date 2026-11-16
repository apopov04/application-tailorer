# Application Tailorer comparison

Separate OpenAI builder, Anthropic builder and researcher, synthesized into a combined configuration.

| Version | Passed expectations |
| --- | --- |
| combined | 17/18 |
| published | 18/18 |
| openai-builder | 18/18 |
| anthropic-builder | 18/18 |

## Anonymous qualitative comparisons

- eval-0-intake: published, anthropic-builder. Both satisfy all intake requirements and provide a practical path when the applicant has no previous answers. B explicitly elicits a genuine company/work motivation and edit preference; D offers a shorter intake with a fallback. A and C also meet every expectation, but assume past answers are available and give no explicit fallback.
- eval-1-company-transfer: combined, published. All four satisfy every exact expectation and ground personal/company claims in the prompt. A and B have the smoothest plain-language role connections; A integrates them compactly and B separates them into easy sentences. C’s closing sentence is denser and D’s “through working with” slightly less natural. These are minor editorial differences, not substantive failures.
- eval-2-conflict-and-motivation: combined, openai-builder. C and D both make supported progress, preserve the resolved attribution, and ask one focused motivation question. C clearly distinguishes company facts from personal motivation; D most explicitly calibrates parser experience as an ingestion starting point and avoids implying validation expertise. A is also strong. B is useful and accurate, with a slightly narrower ingestion-only connection in the contribution passage. The preference reflects calibration and question fit, not length.
- eval-3-batch-and-length: anthropic-builder, published. A and D preserve the plain voice, answer distinct purposes, retain the coordinator’s responsibility, and keep the change note brief. D makes the candidate’s organization actions explicit; A’s direct factual example is also sufficient. B is sound but its note is unnecessarily long. C adds an unconfirmed causal result. Preference is based on factual scope and usable presentation, not answer length.

## Limits

Four cases per configuration; one sequential runner per configuration. Small qualitative comparison, not repeated independent trials.
Identical research access for all four configurations. This comparison tests instructions, not the effect of adding research access alone.
Both creator workflows were applied by separate Codex agents. No Claude-model comparison was run.
Per-case timing/token measurements unavailable; omitted rather than estimated.
Renamed from Application Answer Adapter to Application Tailorer after the frozen behavioral runs; final metadata and package validated separately.
anthropic-builder: 100.0% mean case pass rate.
combined: 93.8% mean case pass rate.
openai-builder: 100.0% mean case pass rate.
published: 100.0% mean case pass rate.

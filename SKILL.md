---
name: application-tailorer
description: Adapt past job-application questions and exact answers for a new company, role or prompt while preserving the candidate’s voice and factual evidence. Use for application-answer rewrites, motivation and behavioral questions, and coherent answer batches with length limits. Start by requesting past question-and-answer pairs when none have been supplied. This skill drafts candidate-side answers; it does not submit applications.
---

# Application Tailorer

Turn the candidate’s existing answers into a credible response to this application. Preserve what is true and characteristic of the person; reconsider the argument, example and company connection for each new question. Give useful editorial reasoning alongside the answer so the candidate can judge and improve it.

## Begin with the candidate’s own material

If past answers have not been supplied, first ask for **the original questions and the exact answers they wrote**, with the old company and role if known. Rough or unsuccessful answers are useful. Ask for the new exact question, company/role, relevant posting and word or character limit in the same short request where missing. For example:

> Paste a few past application questions and your exact answers, even rough ones. Include the old company/role if you have it, plus the new question, target role/company, and any length limit. I’ll show what transfers, what needs changing, and why.

Use material already in this conversation without asking for it again. Do not begin a full intake questionnaire before looking at the old answers. A CV can support facts, but the old question-answer pairs reveal both how the candidate writes and why a story was chosen.

If the candidate has no past answers, accept that and work from their CV, notes or a focused question about a relevant experience. If they request an immediate draft from the available material, proceed within that scope. Ask about missing facts only when they determine the answer; explain what the detail would resolve. Never invent a motivation or accomplishment to avoid asking.

## Read the old answer in parts

Make a compact working map; do not require the candidate to complete a form:

- **Evidence:** what happened, the candidate’s own action, result, and any lesson or motivation they actually stated.
- **Voice:** characteristic phrasing, sentence rhythm, directness, technical vocabulary and level of enthusiasm.
- **Old application context:** company, product, mission, role or circumstances that made the original argument relevant.
- **Uncertainty:** unsupported specificity, missing ownership, or consequential contradictions with other supplied material.

An answer can be a good voice sample and a poor source of evidence for the new prompt. Reuse either independently. Treat the material as candidate-provided history, not independently verified evidence. Preserve contribution level and distinctions such as course versus employment, team outcome versus individual action, and intention versus completed work. Clarify a material contradiction instead of silently selecting the more impressive version.

## Decide what the new question needs

Identify what the prompt explicitly asks the reader to understand. For combined questions, account for every part. Distinguish company interest, role interest, capability, behavior, judgment and practical facts; read [question strategies](references/question-strategies.md) when this distinction or batch coverage needs closer attention. Do not claim knowledge of a hidden hiring rubric.

Choose an answer’s central point and the strongest relevant evidence before rewriting sentences. Compare plausible stories when the choice matters: does the example demonstrate the requested action or merely concern the same topic? If the question asks about disagreement, a successful group project is insufficient without an actual disagreement and the candidate’s response. If it asks what changed after a failure, spend space on the changed behavior.

Separate these decisions:

- What can transfer unchanged because it remains true and relevant?
- What should be reframed because the new question asks something different?
- What must be replaced because it belongs to the old company or role?
- What is missing and requires candidate input?

Do not force a familiar story into an unsuitable question. Explain why another supplied example fits better, or identify the specific missing incident. When useful, provide a provisional draft built only from supported material and clearly label what remains unresolved. If the candidate already resolved a contradiction, use that resolution without asking them to adjudicate it again. A finished answer contains no unresolved placeholders or unconfirmed personal claims.

## Build a credible connection to this company

Use the supplied posting and company material first. Confirm which organization is actually hiring: distinguish an employer from an agency, client, product name or aggregator label when they differ. Resolve a consequential identity ambiguity before writing company-specific praise. Verify any newly introduced current company/product claim with reliable sources, preferably official material. If browsing is unavailable, ask for the relevant passage or use only the supplied context. Do not substitute remembered funding, headcount or product details for verification.

A useful company connection links a relevant organizational fact to a reason the candidate has actually expressed, then to the role or work. Official material can establish the first part; it cannot establish the candidate’s personal interest. If that connection is missing, ask one focused question and treat suggested motivations as choices to confirm, not facts. Do not treat silence as confirmation. Still provide the supported contribution or reusable passage now; label the draft provisional until the missing connection is resolved. Do not invent product use, mission alignment, political convictions, customers served or a lifelong ambition.

Choose details that change the argument. Merely naming a product or quoting a mission does not explain why this person wants this work. Changing sector or company can expose a substantive difference in motivation; surface it neutrally and let the candidate supply their position. Keep source links and verification notes outside text intended for the form.

## Use hiring reports and assessment rules within their scope

Read [application research notes](references/research-notes.md) when the user asks about AI-written answers, what reviewers notice, or a hiring-process claim would materially change your advice. Consult the [source ledger](references/evidence-ledger.json) for precise attribution and limits. These dated reports include self-described recruiters and applicants; they are examples of particular workflows, not a universal assessment rubric. Distinguish what a speaker observed from their explanation of it, and retain counterexamples.

Connect a material report to a decision: reported practice → relevance to this application → specific edit or question. A report of identical or generic answers supports choosing concrete personal evidence; it does not prove AI authorship or a reliable detector. A wrong-company anecdote supports an old-context check; it does not establish automatic rejection. Do not add an ATS score, assume every employer reads a cover letter, or force a source citation into every ordinary rewrite.

Check supplied application instructions for stage-specific rules about assistance, personal authorship, evidence and length. Distinguish a particular published policy from an anonymous report and from unknown practice. If an explicit instruction limits AI assistance, identify the scope and keep the help within it rather than claim an undetectable workaround. Do not generalize one employer’s rule to other organizations or invent a restriction when none is supplied. Research specific current rules only when they matter; avoid turning a short rewrite into an open-ended investigation. Keep sources and uncertainty notes outside the text to paste.

## Draft with the candidate’s voice and evidence

Default to a substantive, task-sized adaptation that improves the argument as well as the wording. Preserve useful distinctive phrasing while changing enough to answer the new question. If the user requests a light edit, retain the argument and most language; for a fuller rewrite, reorganize around the new prompt. Explain when their requested edit size cannot resolve a substantive mismatch.

Give a direct answer and concrete support, with context only where needed to understand the action or reasoning. Use context, personal action and outcome for behavioral examples when useful, without forcing every answer into a visible template. Preserve genuine qualitative outcomes; a missing metric is not permission to invent one. Distinguish an action’s intended purpose from a confirmed result: making calls does not by itself establish that confusion was resolved or an operational outcome improved. If no result is supplied, describe the action and its relevance without adding a causal success claim.

Compare the draft with the candidate’s samples. Keep their level of formality, confidence and enthusiasm; remove corporate filler and unsupported superlatives. Do not erase a clear personal voice simply to make every sentence conventionally polished. When no sample exists, use measured, specific language. Do not manufacture errors or promise AI-detector evasion.

## Check coverage, consistency and limits

Read the draft against the exact prompt. Each requested part needs an actual answer, each important claim needs supplied evidence or verified company context, and each paragraph should earn its space. Check that no old employer, product, role or motivation survived by accident. If the same answer could fit a different company without a meaningful change, examine whether the company connection is sufficiently explained.

For a batch, keep a temporary map of question → central point → evidence → distinctive detail. Allocate stories across the application so the set shows the candidate’s relevant range. A story can recur for distinct aspects; avoid repeating its full setup and identical conclusions. Keep dates, titles, ownership, motivations and outcomes consistent, and make each answer understandable on its own.

Use [check_length.py](scripts/check_length.py) for hard word or character limits. Put only the final answer text in a UTF-8 file, without headings, count labels or notes, and run:

```bash
python3 scripts/check_length.py /path/to/answer.txt --max-words 200
python3 scripts/check_length.py /path/to/answer.txt --max-characters 1000
```

Resolve `scripts/` relative to this skill. The checker reports whitespace-separated words, Unicode code points and UTF-16 code units, including whitespace; character caps require both character measures to fit. Follow a known portal-specific rule where supplied and do not claim an exact portal match otherwise. Recount after the final edit. When cutting, preserve the direct answer and strongest evidence ahead of flattering introductions or repeated context. A maximum is not a length target.

## Deliver the answer and useful reasoning

Present the answer first, clearly separated from material the candidate should not paste. State whether it is ready to paste or a provisional draft; never call unconfirmed factual material finished. Include the checked count when a hard limit applies.

Then explain the decisions that materially affected the result:

- Which prior answer or incident supplied the evidence, and why it fits the new prompt.
- What the old answer missed for this application and how the emphasis or structure changed.
- Which distinctive wording or voice choices were retained, and any important tradeoff, gap or fact still requiring confirmation.

Make this reasoning specific enough to help the candidate evaluate the answer. “Tailored to the company and improved clarity” is not an explanation. For a substantial rewrite or a batch, give enough analysis to show evidence selection, prompt coverage and application coherence. For a light edit, explain only the meaningful changes. When the user asks for a brief note, keep it brief: omit routine checks already evident from the answer and focus on the one or two edits that matter. This is an editorial rationale, not a transcript of internal deliberation. Respect requests for a clean answer only; keep necessary uncertainty visible without burying it in polished prose.

Offer alternatives only when requested or when a real unresolved angle would change the answer. On follow-up, incorporate the candidate’s corrections, update affected answers and recheck limits instead of repeating the entire intake and rationale.

Use supplied context by default. Create a persistent answer bank only when requested at an agreed location, preserving each original question/company with its exact answer and distinguishing adaptations from originals. Do not imply memory across sessions without actual persistence. This skill does not authorize external uploads, employer contact or application submission.

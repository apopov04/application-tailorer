---
name: application-answer-adapter
description: Reuse and tailor past job-application answers for a new company, role or question while preserving the candidate’s voice and evidence. Use for application-question rewrites, motivation answers, behavioral examples, short-form responses and coherent batches with word or character limits. Ask for past question-and-answer pairs before starting from scratch; this is candidate-side writing, not application submission.
---

# Application Answer Adapter

Help someone stop rewriting the same application from zero. Recover the useful personal evidence in answers they have already written, understand what the new question actually asks, and produce an answer that sounds like them and belongs in this application.

## Start with their existing answers

At the first useful opportunity, ask whether they have past **questions and the exact answers they wrote**, including the original company/role if known. Accept rough drafts, rejected applications and disconnected notes. Do not require a polished answer bank. If they already supplied these in the conversation, use them without asking again. If they have none, accept that and work from their CV, notes or a few focused questions. Do not repeatedly ask them to find old material.

Collect the new question exactly as shown, target company/role, the posting or relevant context, any word/character limit, and whether they want a light edit or a fuller rewrite. Bundle missing essentials into one short request. Candidate-specific facts in the conversation count as inputs. Do useful analysis with what is already available; do not fill the first response with a questionnaire.

When essential facts are missing, explain the specific detail that would unlock a credible answer. A clearly marked draft with one focused question can be more useful than refusing to begin. A submission-ready answer should not contain unresolved placeholders.

## Separate reusable evidence from the old application

Before adapting, build a compact working map: original question, what it was testing, candidate story or claim, actual contribution, outcome, voice, original-company details and uncertainties. Preserve contribution level, dates, numbers and ownership. Do not promote a group result into personal ownership, a course into employment, or a plan into a completed accomplishment.

Choose material for its relevance to the new question, rather than the superficial similarity of wording. A “why join us?” answer can contain a useful personal motivation but also a paragraph that belongs exclusively to the previous employer. Carry over the personal evidence; replace company-specific reasoning only when the inputs support the replacement.

Treat a previous answer as candidate-provided history, not independently verified evidence. If supplied answers contradict each other or the CV, ask about the consequential discrepancy. Do not silently choose a more impressive version. Strong phrasing can improve clarity without adding facts.

## Identify the question’s actual job

Read [question strategies](references/question-strategies.md) when questions differ in purpose or a batch risks repetitive answers. Distinguish motivation, company/product interest, role fit, behavioral evidence, values/judgment and practical constraints. Combined questions need each part answered. Avoid turning every response into a miniature cover letter.

For each new answer, decide what the reader needs to learn and choose the best evidence to make that clear. A familiar company name does not establish the candidate’s personal motivation. “Why this company?” and “Why this role?” overlap, but the former needs an actual connection to this organization and the latter needs evidence about the work.

If changing company or industry creates a substantive tension, surface it neutrally and ask the candidate what genuinely interests them. Do not invent personal convictions, political positions, product use, customers served, travel, mission alignment or childhood ambitions. The final answer should express motivations the candidate has supplied or confirmed.

## Add company context carefully

Prefer the candidate’s supplied posting and reliable context already available. Verify any new current company or product claim before using it, with browsing when available. Official sources can establish product descriptions and public role responsibilities; they do not establish what the candidate feels or what an employer secretly scores. If browsing is unavailable, use supported context and ask for a relevant passage instead of guessing.

Choose one or two facts that connect to the candidate’s experience or interests. Explain the connection rather than quoting the company’s mission back to it. Avoid generic praise that could survive replacing the employer name. Product announcements, funding and headcount change; do not rely on remembered details. Put fact-check links in a short note outside the answer unless the application asks for citations.

A rewrite from one defense company to another, for example, is not solved by swapping the names: the work, product, customers and candidate’s reasons may differ. Use the same principle across sectors without prescribing one ideological stance.

## Draft in the candidate’s voice

Use their existing answers as a style sample: sentence length, directness, vocabulary, level of enthusiasm and how they discuss their work. Preserve distinctive useful phrasing. Improve awkward structure and filler without replacing an ordinary person’s voice with corporate language. Default to a measured, specific tone when no sample exists. Do not manufacture mistakes to sound human or claim to evade an AI detector.

For a light edit, preserve the argument and most phrasing while fixing relevance, clarity and stale references. For a fuller rewrite, reorganize around the new question while retaining the personal evidence. If the old answer cannot support the new prompt, say what can be reused and ask for the missing example or motivation; do not force-fit it.

Lead with the answer, then give concrete support and a connection to the target work. Behavioral questions often benefit from context, personal action and outcome, but do not visibly force every response into a STAR template. A real qualitative result is useful; do not invent a percentage because the answer lacks a number.

## Check limits and the whole application

Use [check_length.py](scripts/check_length.py) when a hard word or character cap matters. Pass a UTF-8 file containing only the answer, without headings, quotation marks or change notes. The script counts whitespace-separated words, Unicode code points and UTF-16 code units, including whitespace. If the portal defines a different counting method, use that. For an unspecified character counter, keep both character counts within the cap and leave room when sensible; do not claim an exact portal match. Recount the final edited answer, not an earlier draft.

When cutting, preserve the direct answer and strongest personal evidence before flattering introductions or repeated context. A maximum is not a target to fill. Do not cut a response to an unexplained limit.

For a batch, map each question to its purpose and distribute evidence across the set. Reuse an example when it answers distinct aspects, but avoid repeating entire sentences or making all answers tell the same story. Keep dates, titles, outcomes, tone and motivations consistent. Answer each prompt independently enough that the employer can understand it.

## Deliver and iterate

Present the ready-to-paste answer first, clearly separated from commentary. Follow with a short change note: which past answer it draws on, how the emphasis changed, and any specific fact still awaiting confirmation. Keep sources and questions outside the text to paste. Provide multiple variants only when requested or when a real tone/angle choice needs resolution.

If a draft still contains uncertain factual material, label it as a draft and identify the unresolved part. Do not describe it as ready to submit. On follow-up, revise the chosen answer using the new facts, recheck the limit, and avoid repeating the whole analysis. If a user deliberately asks for hypothetical wording, keep it distinguishable from confirmed candidate history rather than silently merging it into the factual draft.

Use supplied context by default. Create a persistent answer bank only when requested, at a user-chosen location, with the original question/company and answer paired together. Do not claim to remember it across sessions unless the environment actually retains it. This skill does not authorize uploading documents elsewhere, contacting an employer or submitting an application.

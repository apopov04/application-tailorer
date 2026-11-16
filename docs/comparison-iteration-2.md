# Application Tailorer comparison

Separate OpenAI builder, Anthropic builder and researcher, synthesized into a combined configuration.

| Version | Passed expectations |
| --- | --- |
| combined | 18/18 |
| published | 18/18 |

## Anonymous qualitative comparisons

- eval-0-intake: published, combined. Both meet every intake expectation. A adds a helpful fallback when there are no old answers and asks for actual attraction; B provides the required intake directly. Neither difference establishes a material advantage for this prompt.
- eval-1-company-transfer: combined, published. Both preserve the same specific experience and plain opening, accurately retarget the motivation, and explain the substantive editing choices. Both ground the research discussion in the supplied anecdotes, separate observation from inferred AI attribution, and connect that evidence to keeping personal examples. The modest wording and note-length differences do not justify a winner.
- eval-2-conflict-and-motivation: combined, published. Tie: both satisfy all five expectations, preserve the confirmed contribution, make useful supported progress, and ask one focused motivation question while clearly marking the draft incomplete. The different passage lengths do not establish a quality advantage.
- eval-3-batch-and-length: published, combined. Tie. Both give distinct motivation and organization answers in the supplied plain voice, preserve the coordinator’s route ownership, and meet every stated expectation. Their wording differences do not establish a meaningful quality advantage.

## Limits

Four cases per configuration; one sequential runner per configuration. Small qualitative comparison, not repeated independent trials.
Identical research access for all four configurations. This comparison tests instructions, not the effect of adding research access alone.
Both creator workflows were applied by separate Codex agents. No Claude-model comparison was run.
This is a fresh combined/published regression comparison after the initial four-way comparison caught one unconfirmed outcome in the combined batch answer.
Per-case timing/token measurements unavailable; omitted rather than estimated.
Renamed from Application Answer Adapter to Application Tailorer after the frozen behavioral runs; final metadata and package validated separately.
combined: 100.0% mean case pass rate.
published: 100.0% mean case pass rate.

<img src="https://assets.carpedieminnovationsinc.com/sig/iridex.png" width="92" align="right" alt="iridex mark">

# iridex

**AI / ML development** — principal at [Carpe Diem Innovations Inc.](https://github.com/carpe-diem-innovations-inc)

Full-stack applied AI: local model deployment, training and fine-tuning, experimentation,
agentic tooling — skills, tools, pipelines — and analysis in whatever domain the problem lives
in. The constant across all of it: put agents and models to work to automate, improve, and
deliver the highest quality possible.

### Released

[**election-records-forensics-2026**](https://github.com/carpe-diem-innovations-inc/election-records-forensics-2026)
— reproducible document-release forensics: hash-anchored sources, CI re-derivation, tiered
claims, and a standing invitation to break it.

Reproduced on four machines besides continuous integration. Holding the processor constant
and crossing a Windows-to-Linux boundary produces byte-identical output; holding the
operating system constant and changing the processor makes the same two of sixteen OCR
files diverge, by the same amounts each time. The divergence tracks the processor family
rather than varying per run — and the perfect run is the weakest row of the set, which the
repository states rather than leaving a reader to assume.

[**doorman**](https://github.com/carpe-diem-innovations-inc/doorman)
— time-based one-time passwords on the Windows desktop: a padlock in the tray, click a code
to copy it. Secrets are held by the operating system's own protection API and never leave
the machine, and the program opens no network connection at all — a claim meant to be
checked by reading four short files rather than taken on trust. The one-time-password
standard has been open since 2011, so the generator is about twenty lines of the standard
library. Apache 2.0.

### Verification

[![verify](https://github.com/iridex-ai/iridex-ai/actions/workflows/verify.yml/badge.svg)](https://github.com/iridex-ai/iridex-ai/actions/workflows/verify.yml)

Every repository under this account and the parent organisation is verified before a push
lands, in three stages: it **works**, it is **safe**, and it works **elsewhere** — on a clean
runner rather than only on the author's machine. Nothing reaches a default branch without a
green result for that exact tree, and each repo carries a `.verify/receipt.json` recording
what was checked and where.

This page is no exception. Its check fetches every brand-asset URL the page embeds, and runs
weekly on a schedule as well as on push — a broken image here would be caused by something
outside this repo, so a push-only trigger would never find it.

```bash
python scripts/verify_profile.py
```

### Elsewhere

[Hugging Face](https://huggingface.co/iridex-ai) · [Kaggle](https://kaggle.com/iridexai) ·
[Weights & Biases](https://wandb.ai/profile/iridex-ai) · [LM Studio](https://lmstudio.ai/iridex-ai) ·
[ORCID](https://orcid.org/0009-0003-9784-3396)

Release signing key: `BA44 9C4B 93EE 08C3 C8C6 BB66 19B8 C479 4FA5 E399`
([keys.openpgp.org](https://keys.openpgp.org/search?q=BA449C4B93EE08C3C8C6BB6619B8C4794FA5E399))

Contact: iridex@carpedieminnovationsinc.com

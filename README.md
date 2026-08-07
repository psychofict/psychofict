<!--
  Profile README — © 2026 Ebenezer "Ebstar" Tarubinga · github.com/psychofict
  Design & layout licensed under CC BY 4.0 (see LICENSE).

  FACTS THAT AGE — verify before editing (last swept 2026-08-07):
  · Paper statuses: PixCon "preprint, under review" and FARCLUSS "Neural Networks, under
    review" — check arXiv / the journal before touching venue text.
  · Leaderboard ranks (#2 / #3, Pascal VOC / Cityscapes) — verify on the Papers with Code
    semi-supervised semantic segmentation leaderboards.
  · "four live government platforms" at Gractor — reconfirm the count before changing it.
  · Claude Code usage block — NEVER edit the numbers by hand; regenerate with
    scripts/refresh-stats.py (reads ~/.config/claude-token-tracker/history.db).
  · Stats cards / snake are self-hosted at grs-iota.vercel.app and the snake workflow in
    this repo — if an image breaks, check those first.
-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/psychofict/psychofict/main/assets/header-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/psychofict/psychofict/main/assets/header-light.svg" alt="Ebenezer Tarubinga — Production LLM Systems · Applied Computer Vision · Semantic Segmentation" />
</picture>

### I build AI systems that hold up in production — the unglamorous part where a demo becomes something a city actually runs on.

I'm the primary engineer on **four live government platforms** at
[Gractor](https://www.gractor.com), a smart-city AI company — RAG over **2.7M+ sensor
records at 98.8% accuracy**, tool-calling agents, and the evaluation harnesses that keep
them honest. Before that, my MSc at Korea University's
[Pattern Recognition & Machine Learning Lab](http://xai.korea.ac.kr/)
([Prof. Seong-Whan Lee](https://pure.korea.ac.kr/en/persons/seong-whan-lee), IEEE Fellow)
produced two first-author papers on semi-supervised semantic segmentation, ranked
**#2 and #3 globally** on the Pascal VOC and Cityscapes leaderboards — work I now
continue independently with **PixCon**.

My focus: reliable retrieval, calibrated uncertainty, and closing the gap between a
number that works in a paper and a system real users depend on.

[Portfolio](https://psychofict.github.io) · [Google Scholar](https://scholar.google.com/citations?user=W818y-gAAAAJ&hl=en) · [arXiv](https://arxiv.org/search/cs?searchtype=author&query=Tarubinga,+E) · [LinkedIn](https://www.linkedin.com/in/ebstar/) · [ebstar.co](https://ebstar.co) · [ebstarmusic@gmail.com](mailto:ebstarmusic@gmail.com)

<sub><b>STACK</b> — Python · PyTorch · CUDA · TypeScript · Next.js · FastAPI · PostgreSQL · Docker · Kubernetes · AWS</sub>

<br>

### 01 · SELECTED RESEARCH

| Year | Paper | Venue | Rank | Links |
|:----:|-------|:-----:|:----:|-------|
| 2026 | **PixCon** — Clean-Positive Contrastive Learning for Foundation-Model SSSS | Preprint (under review) | **#2** | [arXiv](https://arxiv.org/abs/2607.03068) · [Code](https://github.com/psychofict/PixCon) · [Project](https://psychofict.github.io/PixCon/) |
| 2026 | **FARCLUSS** — Fuzzy Adaptive Rebalancing & Contrastive Uncertainty Learning for SSSS | Neural Networks (under review) | **#2** | [arXiv](https://arxiv.org/abs/2506.11142) · [Code](https://github.com/psychofict/FARCLUSS) · [Project](https://psychofict.github.io/FARCLUSS/) |
| 2025 | **CW-BASS** — Confidence-Weighted Boundary-Aware Learning for SSSS | IJCNN (IEEE) | **#3** | [IEEE](https://ieeexplore.ieee.org/document/11227871/) · [arXiv](https://arxiv.org/abs/2502.15152) · [Code](https://github.com/psychofict/CW-BASS) · [Project](https://psychofict.github.io/CW-BASS/) |

<sub>SSSS = semi-supervised semantic segmentation. With ResNet-101 backbones, **CW-BASS**
and **FARCLUSS** were among the state of the art in 2025, ranking **#3 and #2 globally**
on Pascal VOC / Cityscapes (77.15% and 78.8% / 78.2% mIoU). **PixCon** (independent,
2026) carries the line onto foundation-model features (DINOv2-scale), reaching **#2**
while matching a strong UniMatch V2 baseline at lower cost. All three attack the same
problem — dense prediction from very few labels.</sub>

<br>

### 02 · SELECTED SOFTWARE

[**hwpkit**](https://github.com/psychofict/hwpkit) — read, fill & edit Korean HWP
(Hancom Office) documents in Python: text extraction for LLM/RAG, programmatic
form-filling, corruption-free binary rewrite. <sub>Python · OLE/CFB</sub>

[**claude_ai_usage_widget**](https://github.com/StaticB1/claude_ai_usage_widget) — live
system-tray widget for Claude Code plan limits (5h/7d) plus local token & cost analytics
per project, model, and tool. <sub>Python · GTK</sub>

[**claudehop**](https://github.com/psychofict/claudehop) — hop Claude Code between
multiple Claude accounts without logging in again; one file, stdlib only, Linux & macOS.
<sub>Python</sub>

[**tzohar-engine**](https://github.com/psychofict/tzohar-engine) — a framework for
personal & academic websites: typed section blocks, ORCID & BibTeX import, built with
Next.js. <sub>TypeScript · Next.js</sub>

<br>

### 03 · CLAUDE CODE USAGE

I build with agentic coding daily.

<!-- CLAUDE-STATS:START -->
| Tokens processed | Output generated | Sessions | Projects | Primary model | Since |
|---:|---:|---:|---:|:--|:--|
| **35.9 B** | 111 M | 516 | 74 | Opus 4.8 | May 2026 |

<sub>Local Claude Code telemetry via claude-token-tracker (processed = input + cache
writes/reads + output) · snapshot 2026-08-07 · regenerate with
<code>scripts/refresh-stats.py</code> — never edit these numbers by hand.</sub>
<!-- CLAUDE-STATS:END -->

<br>

### 04 · EXPERIENCE

**AI/ML Engineer** · [Gractor Co., Ltd.](https://www.gractor.com) · *Sept 2025 – present · Seoul*
<br>Primary engineer across four live government platforms. Built a RAG system over 2.7M+
IoT records at 98.8% eval accuracy, rebuilt a production agent from 94.9% → 100% (96/96)
with ~30% less code and ~12x faster startup, shipped a multi-provider LLM router with
circuit-breaker failover, and deployed YOLOv5 + OpenVINO edge inference on government
smart poles.

**Research Engineer (MSc)** · [Korea University, PRML Lab](http://xai.korea.ac.kr/) · *Sept 2023 – Feb 2026 · Seoul*
<br>Advised by Prof. Seong-Whan Lee (IEEE Fellow). First-author segmentation papers
(#2 & #3 globally); ~10K LOC of PyTorch multi-GPU training infrastructure; Korean patent
filed (autonomous-driving perception).

**AI Software Engineer** · GliT (GLITEC), EdTech · *Jan 2019 – Jan 2021 · Zimbabwe*
<br>Built two offline-first mobile learning products reaching 500+ students and 80,000+
learning sessions.

<br>

### 05 · EDUCATION & AWARDS

**MSc in Artificial Intelligence** · Korea University · 2023–2026 · GPA 3.78/4.0
<br>Global Korea Scholarship (sole Zimbabwe awardee) · BK21 Research Fellowship ·
Advisor: [Prof. Seong-Whan Lee](https://pure.korea.ac.kr/en/persons/seong-whan-lee)

**Awards** — GINCON Global Award 2025 (Korean National Assembly)

<br>

### 06 · GITHUB

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://grs-iota.vercel.app/api?username=psychofict&show_icons=true&count_private=true&include_all_commits=true&hide=contribs&hide_border=true&title_color=5EA1FF&icon_color=5EA1FF&text_color=9ca3af&bg_color=00000000&cb=4" />
    <img height="165" src="https://grs-iota.vercel.app/api?username=psychofict&show_icons=true&count_private=true&include_all_commits=true&hide=contribs&hide_border=true&title_color=0F62FE&icon_color=0F62FE&text_color=6b7280&bg_color=00000000&cb=4" alt="GitHub stats" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://grs-iota.vercel.app/api/top-langs/?username=psychofict&layout=compact&langs_count=8&hide_border=true&title_color=5EA1FF&text_color=9ca3af&bg_color=00000000&cb=4" />
    <img height="165" src="https://grs-iota.vercel.app/api/top-langs/?username=psychofict&layout=compact&langs_count=8&hide_border=true&title_color=0F62FE&text_color=6b7280&bg_color=00000000&cb=4" alt="Top languages" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/psychofict/psychofict/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/psychofict/psychofict/output/github-contribution-grid-snake.svg" />
    <img alt="contribution snake animation" src="https://raw.githubusercontent.com/psychofict/psychofict/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

<br>

---

<h3 align="center"><a href="mailto:ebstarmusic@gmail.com">Let's build something that ships.</a></h3>

<p align="center"><sub>Design © Ebenezer Tarubinga, licensed <a href="./LICENSE">CC BY 4.0</a> — reuse with attribution.</sub></p>

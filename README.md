<!--
  Profile README — © 2026 Ebenezer "Ebstar" Tarubinga · github.com/psychofict
  Design & layout licensed under CC BY 4.0 (see LICENSE).
  Reuse is welcome — please keep visible attribution to Ebenezer Tarubinga.
-->

<!-- ====================== HEADER BANNER ====================== -->
<a href="https://psychofict.github.io">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=190&section=header&text=Ebenezer%20Tarubinga&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI%2FML%20Engineer%20%C2%B7%20Production%20LLM%20Systems%20%C2%B7%20Computer-Vision%20Research&descSize=17&descAlignY=57" alt="Ebenezer Tarubinga" />
</a>

<!-- ====================== TYPING SUBTITLE ====================== -->
<p align="center">
  <a href="https://psychofict.github.io">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=1200&color=6AA6FF&center=true&vCenter=true&width=760&lines=AI%2FML+Engineer+%40+Gractor;Production+LLM+systems%3A+RAG+%C2%B7+agents+%C2%B7+evaluation;First-author+segmentation+researcher+(%232+%26+%233+globally);Research+to+production%2C+at+government+scale" alt="typing subtitle" />
  </a>
</p>

<!-- ====================== SOCIAL BADGES ====================== -->
<p align="center">
  <a href="https://psychofict.github.io"><img src="https://img.shields.io/badge/Portfolio-111111?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
  <a href="https://scholar.google.com/citations?user=W818y-gAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar" /></a>
  <a href="https://arxiv.org/search/cs?searchtype=author&query=Tarubinga,+E"><img src="https://img.shields.io/badge/arXiv-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv" /></a>
  <a href="https://www.linkedin.com/in/ebstar/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://ebstar.co"><img src="https://img.shields.io/badge/ebstar.co-1DA1F2?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" /></a>
  <a href="mailto:ebstarmusic@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=psychofict&label=Profile%20views&color=6AA6FF&style=flat-square" alt="profile views" />
  <img src="https://img.shields.io/badge/Based%20in-Seoul,%20Korea-6AA6FF?style=flat-square&logo=googlemaps&logoColor=white" alt="location" />
</p>

<!-- ====================== INTRO ====================== -->

**I build AI systems that hold up in production** — the unglamorous part where a demo becomes something a city actually runs on. I'm the primary engineer on **four live government platforms** at [Gractor](https://ebstar.co), a Series-A smart-city AI company: RAG over **2.7M+ sensor records at 98.8% accuracy**, tool-calling agents, and the evaluation harnesses that keep them honest.

Earlier, during my **MSc in AI at Korea University's [Pattern Recognition & Machine Learning Lab](https://xai.korea.ac.kr/)** (advised by [Prof. Seong-Whan Lee](https://pure.korea.ac.kr/en/persons/seong-whan-lee), IEEE Fellow), I published two first-author papers on **semi-supervised semantic segmentation**, ranked **#2 and #3 globally** on the Cityscapes and Pascal VOC leaderboards, work I now continue independently with **PixCon**.

My focus: reliable retrieval, calibrated uncertainty, and closing the gap between a number that works in a paper and a system real users depend on.

<!-- ====================== PUBLICATIONS ====================== -->
## &#128300; Publications

| Year | Paper | Venue | Rank | Links |
|:----:|-------|:-----:|:----:|-------|
| 2026 | **PixCon** &mdash; Clean-Positive Contrastive Learning for Foundation-Model SSSS | Preprint&nbsp;(under&nbsp;review) | **#2** | [arXiv](https://arxiv.org/abs/2607.03068) · [Code](https://github.com/psychofict/PixCon) · [Project](https://psychofict.github.io/PixCon/) |
| 2026 | **FARCLUSS** &mdash; Fuzzy Adaptive Rebalancing & Contrastive Uncertainty Learning for SSSS | Neural&nbsp;Networks&nbsp;(under&nbsp;review) | **#2** | [arXiv](https://arxiv.org/abs/2506.11142) · [Code](https://github.com/psychofict/FARCLUSS) · [Project](https://psychofict.github.io/FARCLUSS/) |
| 2025 | **CW-BASS** &mdash; Confidence-Weighted Boundary-Aware Learning for SSSS | IJCNN&nbsp;(IEEE) | **#3** | [IEEE](https://ieeexplore.ieee.org/document/11227871/) · [arXiv](https://arxiv.org/abs/2502.15152) · [Code](https://github.com/psychofict/CW-BASS) · [Project](https://psychofict.github.io/CW-BASS/) |

> With ResNet-101 backbones, **CW-BASS** and **FARCLUSS** were among the state of the art in semi-supervised segmentation in 2025, ranking **#3 and #2 globally** on Pascal VOC / Cityscapes (77.15% and 78.8% / 78.2% mIoU). **PixCon** (independent, 2026) carries the line onto foundation-model features (DINOv2-scale), reaching **#2** in semi-supervised segmentation, matching a strong UniMatch V2 baseline at lower cost. All three attack the same problem, dense prediction from very few labels: confidence-weighted boundaries (CW-BASS), fuzzy pseudo-labeling with contrastive rebalancing (FARCLUSS), and a clean-positive pixel memory bank (PixCon).

<!-- ====================== OPEN SOURCE ====================== -->
## &#128736;&#65039; Open Source

| Project | What it does | Stack |
|---------|--------------|-------|
| [**hwpkit**](https://github.com/psychofict/hwpkit) | Read, fill & edit Korean HWP (Hancom Office) docs in Python &mdash; text extraction for LLM/RAG, programmatic form-filling, and corruption-free binary rewrite | Python · OLE/CFB |
| [**Claude Usage Widget & Token Tracker**](https://github.com/StaticB1/claude_ai_usage_widget) | Live system-tray widget for Claude Code plan limits (5h/7d) + local token & cost analytics per project, model, and tool | Python · GTK · CLI |

<!-- ====================== CLAUDE CODE USAGE ====================== -->
**Claude Code usage** &mdash; I build with agentic coding daily.

<p>
  <img src="https://img.shields.io/badge/Claude_Code-30.3B_tokens_processed-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code tokens" />
</p>
<p>
  <img src="https://img.shields.io/badge/Output_generated-152M_tokens-CC785C?style=flat-square&logo=anthropic&logoColor=white" alt="output tokens" />
  <img src="https://img.shields.io/badge/Sessions-224-4B4B4B?style=flat-square" alt="sessions" />
  <img src="https://img.shields.io/badge/Projects-117-4B4B4B?style=flat-square" alt="projects" />
  <img src="https://img.shields.io/badge/Primary_model-Opus_4.8-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="primary model" />
  <img src="https://img.shields.io/badge/Since-May_2026-4B4B4B?style=flat-square" alt="since" />
</p>

<sub><i>Local Claude Code telemetry, snapshot updated Jul 2026.</i></sub>

<!-- ====================== TECH STACK ====================== -->
## &#129504; Tech Stack

**AI / LLM Systems**

<p>
  <img src="https://img.shields.io/badge/RAG_(hybrid_retrieval)-6AA6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/Agents_%26_Tool_Calling-6AA6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/Model_Context_Protocol-6AA6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/Evaluation_Harnesses-6AA6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/Prompt--Injection_Guardrails-6AA6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Anthropic_Claude-D97757?style=flat-square&logo=anthropic&logoColor=white" />
  <img src="https://img.shields.io/badge/HyperCLOVA_X-03C75A?style=flat-square&logo=naver&logoColor=white" />
</p>

**ML / Computer Vision**

<p>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white" />
  <img src="https://img.shields.io/badge/YOLOv5-00FFFF?style=flat-square&logo=yolo&logoColor=black" />
  <img src="https://img.shields.io/badge/OpenVINO-5218FA?style=flat-square&logo=intel&logoColor=white" />
  <img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" />
  <img src="https://img.shields.io/badge/W%26B-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black" />
</p>

**Backend & Data**

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeDB-02CAF9?style=flat-square&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/PostGIS-008BB9?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenSearch-005EB8?style=flat-square&logo=opensearch&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
</p>

**Frontend**

<p>
  <img src="https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/deck.gl-000000?style=flat-square&logo=deckgl&logoColor=white" />
  <img src="https://img.shields.io/badge/MapLibre-396CB2?style=flat-square&logo=maplibre&logoColor=white" />
  <img src="https://img.shields.io/badge/ECharts-AA344D?style=flat-square&logo=apacheecharts&logoColor=white" />
  <img src="https://img.shields.io/badge/Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" />
  <img src="https://img.shields.io/badge/Radix_UI-161618?style=flat-square&logo=radixui&logoColor=white" />
  <img src="https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white" />
  <img src="https://img.shields.io/badge/Zustand-433E38?style=flat-square" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white" />
</p>

**Infra / DevOps / IoT**

<p>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" />
  <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" />
  <img src="https://img.shields.io/badge/systemd-30D475?style=flat-square&logo=systemd&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/MQTT-660066?style=flat-square&logo=mqtt&logoColor=white" />
  <img src="https://img.shields.io/badge/ModBus_RTU-B0B0B0?style=flat-square" />
  <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" />
  <img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
</p>

**Languages**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" />
</p>

<!-- ====================== GITHUB STATS ====================== -->
## &#128202; GitHub Stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://grs-iota.vercel.app/api?username=psychofict&show_icons=true&count_private=true&include_all_commits=true&hide=contribs&hide_border=true&theme=tokyonight&title_color=6AA6FF&icon_color=6AA6FF&text_color=c9d1d9&bg_color=0d1117&cb=2" />
    <img height="165" src="https://grs-iota.vercel.app/api?username=psychofict&show_icons=true&count_private=true&include_all_commits=true&hide=contribs&hide_border=true&title_color=1F6FEB&icon_color=1F6FEB&cb=2" alt="GitHub stats" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://grs-iota.vercel.app/api/top-langs/?username=psychofict&layout=compact&langs_count=8&hide_border=true&theme=tokyonight&title_color=6AA6FF&text_color=c9d1d9&bg_color=0d1117&cb=2" />
    <img height="165" src="https://grs-iota.vercel.app/api/top-langs/?username=psychofict&layout=compact&langs_count=8&hide_border=true&title_color=1F6FEB&cb=2" alt="Top languages" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-kappa.vercel.app?user=psychofict&theme=tokyonight&hide_border=true&background=0D1117&ring=6AA6FF&fire=6AA6FF&currStreakLabel=6AA6FF&sideNums=c9d1d9&sideLabels=8b949e&dates=8b949e&stroke=0D1117&cb=3" />
    <img src="https://streak-kappa.vercel.app?user=psychofict&hide_border=true&ring=1F6FEB&fire=1F6FEB&currStreakLabel=1F6FEB&cb=3" alt="GitHub streak" />
  </picture>
</p>

<!-- ====================== CONTRIBUTION SNAKE ====================== -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/psychofict/psychofict/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/psychofict/psychofict/output/github-contribution-grid-snake.svg" />
    <img alt="contribution snake animation" src="https://raw.githubusercontent.com/psychofict/psychofict/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

<!-- ====================== EXPERIENCE ====================== -->
## &#128188; Experience

**AI/ML Engineer** · Gractor Co., Ltd. · *Sept 2025 – present · Seoul*
<br>Primary engineer across four live government platforms. Built a RAG system over 2.7M+ IoT records at 98.8% eval accuracy, rebuilt a production agent from 94.9% → 100% (96/96) with ~30% less code and ~12x faster startup, shipped a multi-provider LLM router with circuit-breaker failover, and deployed YOLOv5 + OpenVINO edge inference on government smart poles.

**Research Engineer (MSc)** · [Korea University](https://xai.korea.ac.kr/), PRML Lab · *Sept 2023 – Feb 2026 · Seoul*
<br>Advised by Prof. Seong-Whan Lee (IEEE Fellow). First-author segmentation papers (#2 & #3 globally); ~10K LOC of PyTorch multi-GPU training infrastructure; Korean patent filed (autonomous-driving perception).

**AI Software Engineer** · GliT (GLITEC), EdTech · *Jan 2019 – Jan 2021 · Zimbabwe*
<br>Built two offline-first mobile learning products reaching 500+ students and 80,000+ learning sessions.

## &#127891; Education &amp; Awards

**MSc in Artificial Intelligence** · Korea University · 2023–2026 · GPA 3.78/4.0
<br>Global Korea Scholarship (sole Zimbabwe awardee) · BK21 Research Fellowship · Advisor: [Prof. Seong-Whan Lee](https://pure.korea.ac.kr/en/persons/seong-whan-lee)

**Awards** — GINCON Global Award 2025 (Korean National Assembly)

<!-- ====================== FOOTER ====================== -->
<br>
<p align="center">
  <a href="mailto:ebstarmusic@gmail.com"><b>Let's build something that ships.</b></a>
</p>

<p align="center">
  <a href="https://github.com/psychofict"><img src="https://img.shields.io/badge/Design_%C2%A9_Ebenezer_Tarubinga-CC_BY_4.0-6AA6FF?style=flat-square" alt="Design licensed CC BY 4.0" /></a>
</p>
<p align="center"><sub>Like this profile? Reuse the design with attribution to <a href="https://github.com/psychofict">Ebenezer Tarubinga</a>. See <a href="./LICENSE">LICENSE</a>.</sub></p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer" alt="footer" />

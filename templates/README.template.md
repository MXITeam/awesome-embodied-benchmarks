# Awesome Embodied Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **categorized** list of benchmarks for robot learning and embodied AI — from classic simulation suites (Meta-World, RLBench, Habitat) to the newest VLA, humanoid, world-model-as-evaluator and safety benchmarks of 2025–2026.
>
> 一个系统整理、**分门别类**的机器人 / 具身智能 Benchmark 合集：覆盖经典仿真基准、真实世界评测、VLA 泛化与鲁棒性、人形机器人、导航、具身推理 (VLM)、世界模型评测、安全等方向，并持续追踪 2025–2026 的最新论文。

**Last updated: 2026-11** · Entries marked 🆕 appeared in 2026 · 🔥 = widely used / de-facto standard · `Sim` / `Real` / `Real2Sim` / `QA` = evaluation modality

> [!NOTE]
> **Citations** (from [Semantic Scholar](https://www.semanticscholar.org/), falling back to [OpenAlex](https://openalex.org/)) are refreshed **daily** by a [GitHub Action](.github/workflows/update-metrics.yml) · last refresh: **<!-- METRICS_UPDATED -->**.
> **GitHub ⭐** badges are rendered live by [shields.io](https://shields.io/) on every page view.
> Repos not listed by hand are auto-discovered from the paper's Hugging Face / arXiv page. `arXiv search` links mark papers whose arXiv ID has not been verified yet.
> PRs that fix links or add benchmarks are very welcome — edit [`data/benchmarks.yaml`](data/benchmarks.yaml), see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Contents

- [Leaderboard: Most Cited & Most Starred (引用/Star 排行)](#leaderboard-most-cited--most-starred-引用star-排行)
- [Taxonomy at a Glance (分类总览)](#taxonomy-at-a-glance-分类总览)
- [1. Tabletop & General Manipulation — Simulation (桌面/通用操作·仿真)](#1-tabletop--general-manipulation--simulation-桌面通用操作仿真)
- [2. VLA Generalization, Robustness & Benchmark Auditing (VLA 泛化/鲁棒性/评测可信度)](#2-vla-generalization-robustness--benchmark-auditing-vla-泛化鲁棒性评测可信度)
- [3. Long-Horizon, Memory & Compositional Tasks (长程/记忆/组合)](#3-long-horizon-memory--compositional-tasks-长程记忆组合)
- [4. Bimanual, Dexterous & Grasping (双臂/灵巧手/抓取)](#4-bimanual-dexterous--grasping-双臂灵巧手抓取)
- [5. Deformable, Tactile & Contact-Rich Manipulation (柔性物体/触觉/接触密集)](#5-deformable-tactile--contact-rich-manipulation-柔性物体触觉接触密集)
- [6. Real-World Manipulation Benchmarks & Evaluation Protocols (真实世界评测)](#6-real-world-manipulation-benchmarks--evaluation-protocols-真实世界评测)
- [7. Real-to-Sim, World-Model Evaluators & World-Model Benchmarks (Real2Sim/世界模型评测)](#7-real-to-sim-world-model-evaluators--world-model-benchmarks-real2sim世界模型评测)
- [8. Mobile Manipulation & Household Activities (移动操作/家庭任务)](#8-mobile-manipulation--household-activities-移动操作家庭任务)
- [9. Humanoid & Whole-Body Loco-Manipulation (人形/全身控制)](#9-humanoid--whole-body-loco-manipulation-人形全身控制)
- [10. Legged Locomotion & Continuous Control (足式运动/连续控制)](#10-legged-locomotion--continuous-control-足式运动连续控制)
- [11. Embodied Navigation — VLN / ObjectNav / Social (具身导航)](#11-embodied-navigation--vln--objectnav--social-具身导航)
- [12. Aerial / UAV Embodied Benchmarks (无人机)](#12-aerial--uav-embodied-benchmarks-无人机)
- [13. Embodied Reasoning, Spatial Understanding & Planning for (M)LLMs (具身推理/空间理解/规划)](#13-embodied-reasoning-spatial-understanding--planning-for-mllms-具身推理空间理解规划)
- [14. Multi-Agent & Human-Robot Collaboration (多智能体/人机协作)](#14-multi-agent--human-robot-collaboration-多智能体人机协作)
- [15. Safety, Security & Trustworthiness (安全/对抗/可信)](#15-safety-security--trustworthiness-安全对抗可信)
- [16. Simulation Platforms & Unified Benchmark Frameworks (仿真平台/统一框架)](#16-simulation-platforms--unified-benchmark-frameworks-仿真平台统一框架)
- [17. Companion Datasets Often Used for Evaluation (常用于评测的数据集)](#17-companion-datasets-often-used-for-evaluation-常用于评测的数据集)
- [18. Competitions & Challenges (竞赛)](#18-competitions--challenges-竞赛)
- [19. Surveys on Robot Benchmarks & Evaluation (综述)](#19-surveys-on-robot-benchmarks--evaluation-综述)
- [Trends & Takeaways (趋势总结)](#trends--takeaways-趋势总结)
- [How to Pick a Benchmark (选型建议)](#how-to-pick-a-benchmark-选型建议)

---

## Leaderboard: Most Cited & Most Starred (引用/Star 排行)

Auto-generated top 20 (each benchmark / repo counted once).

<!-- TOP_LISTS -->

---

## Taxonomy at a Glance (分类总览)

```
Robot / Embodied AI Benchmarks
├── What is evaluated (能力维度)
│   ├── Low-level control ── manipulation (tabletop, bimanual, dexterous, deformable, tactile)
│   │                     └─ locomotion (legged, humanoid whole-body), aerial
│   ├── Generalization & robustness ── visual / layout / language / embodiment / camera perturbations
│   ├── Long-horizon & memory ── multi-stage tasks, household activities, memory-dependent tasks
│   ├── Navigation ── PointNav, ObjectNav, VLN, social, indoor-to-outdoor
│   ├── Reasoning & planning (VLM/LLM "brain") ── spatial QA, affordance, pointing, task planning, failure analysis
│   ├── Collaboration ── multi-robot, human-robot
│   └── Safety & trust ── hazard awareness, jailbreaks, adversarial inputs, governance
└── How it is evaluated (评测方式)
    ├── Sim         ── fully simulated closed-loop rollouts
    ├── Real        ── physical robots (single-site, distributed, autonomous-reset)
    ├── Real2Sim    ── digital twins / Gaussian splats / green-screen matched to real setups
    ├── World model ── learned video/world models as evaluators
    └── QA          ── offline question answering / pointing over robot-centric images & videos
```

---

## 1. Tabletop & General Manipulation — Simulation (桌面/通用操作·仿真)

Classic and widely used simulated manipulation suites. 经典的仿真操作基准，多数 VLA/模仿学习论文都会在这里报分。

<!-- TABLE:t01 -->

---

## 2. VLA Generalization, Robustness & Benchmark Auditing (VLA 泛化/鲁棒性/评测可信度)

LIBERO / SIMPLER 等分数接近饱和后，社区开始系统性地扰动、审计和"去记忆化"这些基准。

<!-- TABLE:t02 -->

---

## 3. Long-Horizon, Memory & Compositional Tasks (长程/记忆/组合)

<!-- TABLE:t03 -->

---

## 4. Bimanual, Dexterous & Grasping (双臂/灵巧手/抓取)

<!-- TABLE:t04 -->

---

## 5. Deformable, Tactile & Contact-Rich Manipulation (柔性物体/触觉/接触密集)

### 5.1 Deformable objects (cloth, rope, fluids, plasticine)

<!-- TABLE:t05 -->

### 5.2 Tactile & contact-rich

<!-- TABLE:t06 -->

---

## 6. Real-World Manipulation Benchmarks & Evaluation Protocols (真实世界评测)

<!-- TABLE:t07 -->

---

## 7. Real-to-Sim, World-Model Evaluators & World-Model Benchmarks (Real2Sim/世界模型评测)

真实评测昂贵，2024 起出现两条替代路线：(a) 与真实场景对齐的仿真 (SIMPLER, Gaussian splat)；(b) 用视频世界模型直接"推演"策略。核心指标是与真实成功率的 Pearson 相关性和排序一致性 (MMRV)。本节也收录评测世界模型本身的基准 (EWMBench, WorldArena, World-in-World 等)。

<!-- TABLE:t08 -->

---

## 8. Mobile Manipulation & Household Activities (移动操作/家庭任务)

<!-- TABLE:t09 -->

---

## 9. Humanoid & Whole-Body Loco-Manipulation (人形/全身控制)

<!-- TABLE:t10 -->

---

## 10. Legged Locomotion & Continuous Control (足式运动/连续控制)

<!-- TABLE:t11 -->

---

## 11. Embodied Navigation — VLN / ObjectNav / Social (具身导航)

<!-- TABLE:t12 -->

---

## 12. Aerial / UAV Embodied Benchmarks (无人机)

<!-- TABLE:t13 -->

---

## 13. Embodied Reasoning, Spatial Understanding & Planning for (M)LLMs (具身推理/空间理解/规划)

评测"机器人大脑"——VLM/LLM 在具身场景下的感知、空间推理、指点、可供性、任务规划与失败分析。

### 13.1 Embodied QA, spatial reasoning & pointing

<!-- TABLE:t14 -->

### 13.2 Task planning & agentic evaluation

<!-- TABLE:t15 -->

---

## 14. Multi-Agent & Human-Robot Collaboration (多智能体/人机协作)

<!-- TABLE:t16 -->

---

## 15. Safety, Security & Trustworthiness (安全/对抗/可信)

<!-- TABLE:t17 -->

---

## 16. Simulation Platforms & Unified Benchmark Frameworks (仿真平台/统一框架)

Not benchmarks per se, but most benchmarks above are built on them.

<!-- TABLE:t18 -->

---

## 17. Companion Datasets Often Used for Evaluation (常用于评测的数据集)

<!-- TABLE:t19 -->

---

## 18. Competitions & Challenges (竞赛)

- **LeHome Challenge** (ICRA 2026) — household garment manipulation: Isaac Sim round (62 teams) + real-robot final. [Website](https://lehome-challenge.github.io/)
- **RSS 2026 Post-Training for Robotics Challenge** — standardized real-robot bimanual benchmark. [Website](https://posttraining-for-robotics.github.io/)
- **AgiBot World Challenge** (ICRA 2026) — sim track on GenieSim 3.0 + real-robot finals (incl. supermarket mobile manipulation). [Report](https://www.therobotreport.com/agibot-holds-world-challenge-2026-see-how-ai-models-perform-real-tasks/)
- **RoboChallenge** (2025–) — always-on online real-robot evaluation (Table30). [Website](https://robochallenge.ai/)
- **RoboDojo Leaderboard** (2026–) — sim + remote real-robot leaderboard. [Website](https://robodojo-benchmark.com/)
- **BEHAVIOR Challenge** (NeurIPS 2025) — 50 long-horizon household tasks in OmniGibson. [Website](https://behavior.stanford.edu/challenge/)
- **Habitat Navigation / Rearrangement Challenges** (CVPR 2019–2023). [Website](https://aihabitat.org/challenge/)
- **ManiSkill Challenge** (2021–2022). [Website](https://www.maniskill.ai/)
- **Real Robot Challenge** (2020–2022, TriFinger dexterous). [Website](https://real-robot-challenge.com/)
- **ICRA Cloth Competition** (2024–2026). 
- **MARS Challenge** (NeurIPS 2025 SpaVLE workshop) — multi-agent embodied planning.
- **ManiSkill-ViTac Challenge** (2024–2026) — tactile & visuo-tactile manipulation. [arXiv:2411.12503](https://arxiv.org/abs/2411.12503)
- **Robotic Grasping and Manipulation Competition (RGMC)** (IROS/ICRA, 2016–) — in-hand, picking & assembly tracks.
- **AIJ Contest — Embodied AI track** (2024) — run on Kitchen-R.
- **Amazon Picking/Robotics Challenge** (2015–2017) — warehouse pick-and-place.

---

## 19. Surveys on Robot Benchmarks & Evaluation (综述)

<!-- TABLE:t20 -->

Related awesome lists: [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) · [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam)

---

## Trends & Takeaways (趋势总结)

1. **Saturation → perturbation.** LIBERO/SIMPLER/CALVIN numbers are near ceiling for strong VLAs. 2025–26 work (LIBERO-PRO/Plus/MAX, STRONG-VLA, RoboSPA) shows that small camera, init-state or wording changes can collapse success — *report perturbed suites, not just the original*.
2. **Benchmarks themselves are being audited.** Shortcut solvability, few-trial noise and demo-source leakage ([2609.37771](https://arxiv.org/abs/2609.37771)) mean you should report confidence intervals and number of trials.
3. **Real-world evaluation is scaling** via distribution (RoboArena, RoboColosseum — 124 sites), always-on online fleets (RoboChallenge), unified sim+real suites (RoboDojo), automation (AutoEval) and low-cost replication (VLA-REPLICA). RoboColosseum finds policy rankings barely transfer across embodiments — evaluate on *your* robot.
4. **Cheaper proxies for real robots:** Real2Sim (SIMPLER → PolaRiS → 3DGS verification) and world-model evaluators (WorldGym, dWorldEval, WMBench, RoboWorld). The key metric is rank correlation with real success.
5. **Beyond success rate:** memory (RoboMME), compositionality (ATOM-Bench), safety (SafeVLA-Bench, SoftVTBench), and behavior quality (RoboEval).
6. **The "brain" is evaluated separately from the "body":** ERQA, RoboBench, Embodied3DBench, ERQA-Plus test VLM reasoning offline; ERIQ reports this correlates with downstream VLA generalization.
7. **New embodiments get their own suites:** humanoids (SIMPLE, CoHuB, LHM-Humanoid), dexterous hands (DexJoCo, POMDAR), UAVs (OpenFly, UAV-ON), tactile (UniVTAC, RobOmni).

## How to Pick a Benchmark (选型建议)

<!-- TABLE:t21 -->

---

## Contributing

PRs welcome! Add entries to [`data/benchmarks.yaml`](data/benchmarks.yaml) — **do not edit `README.md` directly**, it is generated from [`templates/README.template.md`](templates/README.template.md). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) To the extent possible under law, the contributors have waived all copyright and related rights to this work.

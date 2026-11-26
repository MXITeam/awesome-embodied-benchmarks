# Awesome Embodied Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **categorized** list of benchmarks for robot learning and embodied AI — from classic simulation suites (Meta-World, RLBench, Habitat) to the newest VLA, humanoid, world-model-as-evaluator and safety benchmarks of 2025–2026.
>
> 一个系统整理、**分门别类**的机器人 / 具身智能 Benchmark 合集：覆盖经典仿真基准、真实世界评测、VLA 泛化与鲁棒性、人形机器人、导航、具身推理 (VLM)、世界模型评测、安全等方向，并持续追踪 2025–2026 的最新论文。

**Last updated: 2026-11** · Entries marked 🆕 appeared in 2026 · 🔥 = widely used / de-facto standard · `Sim` / `Real` / `Real2Sim` / `QA` = evaluation modality

> [!NOTE]
> **Citations** (from [Semantic Scholar](https://www.semanticscholar.org/), falling back to [OpenAlex](https://openalex.org/)) are refreshed **daily** by a [GitHub Action](.github/workflows/update-metrics.yml) · last refresh: **2026-11-25 13:01 UTC**.
> **GitHub ⭐** badges are rendered live by [shields.io](https://shields.io/) on every page view.
> Repos not listed by hand are auto-discovered from the paper's Hugging Face / arXiv page. `arXiv search` links mark papers whose arXiv ID has not been verified yet.
> **Code** and **Data** link to what the authors have released. *Data* means what the benchmark tests on: tasks, scenes, questions or demonstrations. *Tasks in code*: code found, but no separate data files. *Same-name dataset (unverified)*: a Hugging Face dataset with the same name, uploader not checked. *Announced*: the paper says it is or will be released, with no link found. *Not found* does not mean closed. Links were matched by script and only a sample was checked by hand. So far, of 1,797 rows checked by 2026-11-25, 872 have code, 778 have data or test files, 706 have both, and nothing was found for 548.
> PRs that fix links or add benchmarks are very welcome — edit [`data/benchmarks.yaml`](data/benchmarks.yaml), see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Benchmarks by section

Each section has its own page with the full table and direct links to code and data.

| Section | Benchmarks | With code | With data | Nothing found |
|---|---|---|---|---|
| [1. Tabletop & General Manipulation — Simulation (桌面/通用操作·仿真)](benchmarks/01-tabletop-manipulation.md) | 146 | 96 | 84 | 27 |
| [2. VLA Generalization, Robustness & Benchmark Auditing (VLA 泛化/鲁棒性/评测可信度)](benchmarks/02-vla-robustness.md) | 132 | 70 | 61 | 36 |
| [3. Long-Horizon, Memory & Compositional Tasks (长程/记忆/组合)](benchmarks/03-long-horizon-memory.md) | 89 | 42 | 45 | 23 |
| [4. Bimanual, Dexterous & Grasping (双臂/灵巧手/抓取)](benchmarks/04-bimanual-dexterous-grasping.md) | 104 | 48 | 40 | 43 |
| [5. Deformable, Tactile & Contact-Rich Manipulation (柔性物体/触觉/接触密集)](benchmarks/05-deformable-tactile-contact.md) | 93 | 45 | 41 | 31 |
| [6. Real-World Manipulation Benchmarks & Evaluation Protocols (真实世界评测)](benchmarks/06-real-world-manipulation.md) | 72 | 24 | 21 | 32 |
| [7. Real-to-Sim, World-Model Evaluators & World-Model Benchmarks (Real2Sim/世界模型评测)](benchmarks/07-real2sim-world-models.md) | 93 | 52 | 54 | 14 |
| [8. Mobile Manipulation & Household Activities (移动操作/家庭任务)](benchmarks/08-mobile-manipulation-household.md) | 78 | 34 | 27 | 35 |
| [9. Humanoid & Whole-Body Loco-Manipulation (人形/全身控制)](benchmarks/09-humanoid.md) | 55 | 18 | 18 | 23 |
| [10. Legged Locomotion & Continuous Control (足式运动/连续控制)](benchmarks/10-locomotion-control.md) | 40 | 22 | 12 | 16 |
| [11. Embodied Navigation — VLN / ObjectNav / Social (具身导航)](benchmarks/11-navigation.md) | 264 | 116 | 94 | 90 |
| [12. Aerial / UAV Embodied Benchmarks (无人机)](benchmarks/12-aerial.md) | 92 | 48 | 42 | 27 |
| [13. Embodied Reasoning, Spatial Understanding & Planning for (M)LLMs (具身推理/空间理解/规划)](benchmarks/13-embodied-reasoning-planning.md) | 297 | 161 | 160 | 63 |
| [14. Multi-Agent & Human-Robot Collaboration (多智能体/人机协作)](benchmarks/14-multi-agent-hri.md) | 140 | 49 | 37 | 56 |
| [15. Safety, Security & Trustworthiness (安全/对抗/可信)](benchmarks/15-safety.md) | 102 | 47 | 42 | 32 |
| **Total** | **1,797** | **872** | **778** | **548** |

**Widely used (🔥)**

| Benchmark | Section | Year / Venue | Highlights | Code | Data |
|---|---|---|---|---|---|
| 🔥 **Meta-World** | [1](benchmarks/01-tabletop-manipulation.md) | 2019 / CoRL | 50 Sawyer tasks; multi-task & meta-RL (ML1/ML10/ML45, MT10/MT50) | [Code](https://github.com/Farama-Foundation/Metaworld) | [In repo](https://github.com/Farama-Foundation/Metaworld) |
| 🔥 **RLBench** | [1](benchmarks/01-tabletop-manipulation.md) | 2019 / RA-L | 100 hand-designed tasks with demos; standard for keyframe/3D policies (PerAct, RVT) | [Code](https://github.com/stepjam/RLBench) | [In repo](https://github.com/stepjam/RLBench) |
| 🔥 **CALVIN** | [1](benchmarks/01-tabletop-manipulation.md) | 2021 / RA-L | Language-conditioned long-horizon chains (5 tasks in a row), ABC→D split | [Code](https://github.com/mees/calvin) | [Download](http://calvin.cs.uni-freiburg.de/scene_info_fix/task_ABCD_D_scene_info.zip) |
| 🔥 **LIBERO** | [1](benchmarks/01-tabletop-manipulation.md) | 2023 / NeurIPS D&B | 130 tasks; Spatial / Object / Goal / Long suites; lifelong learning; the most-reported VLA benchmark | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) | [Download script](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| 🔥 **RoboCasa** | [1](benchmarks/01-tabletop-manipulation.md) | 2024 / RSS | Large-scale kitchen scenes, 100 tasks, generative assets | [Code](https://github.com/robocasa/robocasa) | [Download script](https://github.com/robocasa/robocasa) |
| 🆕🔥 **RoboDojo** | [1](benchmarks/01-tabletop-manipulation.md) | 2026 / ECCV | 42 sim + 18 real tasks; Generalization / Precision / Long-Horizon / Memory / Open; 30 policies on a live leaderboard; best policy 8.8% sim success vs 76% teleop | [Code](https://github.com/RoboDojo-Benchmark/RoboDojo) | [Download script](https://github.com/RoboDojo-Benchmark/RoboDojo) |
| 🔥 **RoboTwin 2.0** | [4](benchmarks/04-bimanual-dexterous-grasping.md) | 2025 / ICML'26 | 50 dual-arm tasks, 731 objects, 5 embodiments, 5-axis domain randomization, 100k+ trajectories | [Code](https://github.com/robotwin-Platform/robotwin) | [Download](https://huggingface.co/datasets/TianxingChen/RoboTwin2.0/tree/main/dataset) |
| 🔥 **AutoEval** | [6](benchmarks/06-real-world-manipulation.md) | 2025 / CoRL | 24/7 evaluation with learned success detection & auto-reset on WidowX/Bridge | [Code](https://github.com/zhouzypaul/auto_eval) | Tasks in code |
| 🔥 **RoboArena** | [6](benchmarks/06-real-world-manipulation.md) | 2025 / CoRL | Crowd-sourced, double-blind pairwise comparisons on DROID across 7 institutions | [Code](https://github.com/robo-arena/roboarena) | [Download](https://huggingface.co/datasets/RoboArena/DataDump_08-05-2025) |
| 🔥 **RoboChallenge (Table30)** | [6](benchmarks/06-real-world-manipulation.md) | 2025 | Large-scale online real-robot eval; 30 tabletop tasks on UR5/Franka/ALOHA/ARX-5; remote action-queue API | [Code](https://github.com/RoboChallenge/RoboChallengeInference) | [Download](https://huggingface.co/datasets/RoboChallenge/Table30) |
| 🆕🔥 **RoboColosseum** | [6](benchmarks/06-real-world-manipulation.md) | 2026 | 124 sites, 4 embodiments, 5,699 pairwise comparisons; rankings don't transfer across robots (Kendall W = 0.24) | [Code](https://github.com/RoboColosseum/robocolosseum-client) | Tasks in code |
| 🔥 **SIMPLER** | [7](benchmarks/07-real2sim-world-models.md) | 2024 / CoRL | Visual-matching / variant-aggregation sims for Google Robot & WidowX; MMRV metric | [Code](https://github.com/simpler-env/SimplerEnv) | [In repo](https://github.com/simpler-env/ManiSkill2_real2sim) |
| 🔥 **ALFRED** | [8](benchmarks/08-mobile-manipulation-household.md) | 2020 / CVPR | Instruction following for household tasks | [Code](https://github.com/askforalfred/alfred) | [Download script](https://github.com/askforalfred/alfred) |
| 🔥 **BEHAVIOR-1K** | [8](benchmarks/08-mobile-manipulation-household.md) | 2022 / CoRL (arXiv 2024) | 1,000 activities, 50 scenes, realistic physics | [Code](https://github.com/StanfordVL/BEHAVIOR-1K) | [Download](https://huggingface.co/datasets/behavior-1k/2025-challenge-demos) |
| 🔥 **HumanoidBench** | [9](benchmarks/09-humanoid.md) | 2024 / RSS | 27 whole-body locomotion + manipulation tasks on Unitree H1 with hands | [Code](https://github.com/carlosferrazza/humanoid-bench) | [In repo](https://github.com/carlosferrazza/humanoid-bench) |
| 🔥 **DeepMind Control Suite** | [10](benchmarks/10-locomotion-control.md) | 2018 | Standard continuous-control RL tasks | [Code](https://github.com/deepmind/dm_control) | [In repo](https://github.com/deepmind/dm_control) |
| 🔥 **Room-to-Room (R2R)** | [11](benchmarks/11-navigation.md) | 2018 / CVPR | Vision-and-language navigation on discrete graphs | [Code](https://github.com/peteanderson80/Matterport3DSimulator) | [Download script](https://github.com/peteanderson80/Matterport3DSimulator) |
| 🔥 **Habitat** (PointNav/ObjectNav) | [11](benchmarks/11-navigation.md) | 2019 / ICCV | Fast embodied simulator + navigation challenges | [Code](https://github.com/facebookresearch/habitat-lab) | [In repo](https://github.com/facebookresearch/habitat-lab) |
| 🔥 **ERQA** (Gemini Robotics) | [13](benchmarks/13-embodied-reasoning-planning.md) | 2025 | 400 MCQs: spatial, trajectory, action, state, multi-view reasoning | [Code](https://github.com/embodiedreasoning/ERQA) | [In repo](https://github.com/embodiedreasoning/ERQA) |
| 🔥 **EmbodiedBench** | [13](benchmarks/13-embodied-reasoning-planning.md) | 2025 / ICML | 1,128 tasks in 4 envs; MLLMs strong at high-level, weak at low-level | [Code](https://github.com/EmbodiedBench/EmbodiedBench) | [Download](https://huggingface.co/datasets/EmbodiedBench/EB-ALFRED) |

## Also on this page

- [Leaderboard: Most Cited & Most Starred (引用/Star 排行)](#leaderboard-most-cited--most-starred-引用star-排行)
- [Taxonomy at a Glance (分类总览)](#taxonomy-at-a-glance-分类总览)
- [16. Simulation Platforms & Unified Benchmark Frameworks (仿真平台/统一框架)](#16-simulation-platforms--unified-benchmark-frameworks-仿真平台统一框架)
- [17. Companion Datasets Often Used for Evaluation (常用于评测的数据集)](#17-companion-datasets-often-used-for-evaluation-常用于评测的数据集)
- [18. Competitions & Challenges (竞赛)](#18-competitions--challenges-竞赛)
- [19. Surveys on Robot Benchmarks & Evaluation (综述)](#19-surveys-on-robot-benchmarks--evaluation-综述)
- [Trends & Takeaways (趋势总结)](#trends--takeaways-趋势总结)
- [How to Pick a Benchmark (选型建议)](#how-to-pick-a-benchmark-选型建议)

---

## Leaderboard: Most Cited & Most Starred (引用/Star 排行)

Auto-generated top 20 (each benchmark / repo counted once).

| # | Most cited | Citations | Most starred | Stars |
|---|---|---|---|---|
| 1 | LIBERO | [2,417](https://www.semanticscholar.org/paper/98cfd7b1b29453c4e82536f5afdc6ddc58bbb1b3) | [MuJoCo / MuJoCo Playground](https://github.com/google-deepmind/mujoco) | 18,480 |
| 2 | Habitat | [2,323](https://www.semanticscholar.org/paper/b4a35e548de27b6924e5f2ee41d37238a5c4a1d5) | [Gymnasium MuJoCo](https://github.com/Farama-Foundation/Gymnasium) | 12,856 |
| 3 | Room-to-Room (R2R) | [2,148](https://www.semanticscholar.org/paper/c37c23b12e00168833eccff8025a830ce27c5abc) | [NVIDIA Isaac Sim / Isaac Lab](https://github.com/isaac-sim/IsaacLab) | 8,722 |
| 4 | D4RL — Franka Kitchen | [2,040](https://www.semanticscholar.org/paper/cd4db2d18d96fc1380f6cf379ead49c5492d8d50) | [DeepMind Control Suite](https://github.com/google-deepmind/dm_control) | 4,732 |
| 5 | Meta-World | [1,962](https://www.semanticscholar.org/paper/0bc855f84668b35cb65618d996d09f6e434d28c9) | [Habitat-Sim / Habitat-Lab](https://github.com/facebookresearch/habitat-sim) | 3,845 |
| 6 | ALFWorld | [1,610](https://www.semanticscholar.org/paper/398a0625e8707a0b41ac58eaec51e8feb87dd7cb) | [Habitat 2.0 — Home Assistant Benchmark](https://github.com/facebookresearch/habitat-lab) | 3,194 |
| 7 | DeepMind Control Suite | [1,608](https://www.semanticscholar.org/paper/a9a3ed69c94a3e1c08ef1f833d9199f57736238b) | [RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin) | 3,081 |
| 8 | DROID | [1,421](https://www.semanticscholar.org/paper/ee5070fe52fd17da9a89d3f342fb07cc9ae51afe) | [robosuite](https://github.com/ARISE-Initiative/robosuite) | 2,723 |
| 9 | Open X-Embodiment | [1,317](https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f) | [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) | 2,571 |
| 10 | ALFRED | [1,312](https://www.semanticscholar.org/paper/f4cf4246f3882aa6337e9c05d5675a3b8463a32e) | [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment) | 2,104 |
| 11 | RLBench | [1,243](https://www.semanticscholar.org/paper/a2fdfda785b3a2a0178d174daa515377c531f222) | [Meta-World](https://github.com/Farama-Foundation/Metaworld) | 1,909 |
| 12 | RoboMimic | [1,225](https://www.semanticscholar.org/paper/3032844d6ac6882ccb03e7a2c22a0026b210ac05) | [RoboCasa](https://github.com/robocasa/robocasa) | 1,888 |
| 13 | BridgeData V2 | [1,025](https://www.semanticscholar.org/paper/6a375be82efc01ec4ed73334655935a56ba82d38) | [RoboVerse](https://github.com/RoboVerseOrg/RoboVerse) | 1,882 |
| 14 | GraspNet-1Billion | [978](https://www.semanticscholar.org/paper/f76c9834a249a97ebcaf225a216c6076032af99c) | [RLBench](https://github.com/stepjam/RLBench) | 1,839 |
| 15 | VSI-Bench | [965](https://www.semanticscholar.org/paper/376461a2c049f6fa51a4303853fdc672e4d07a0d) | [AI2-THOR / ProcTHOR](https://github.com/allenai/ai2thor) | 1,832 |
| 16 | CALVIN | [962](https://www.semanticscholar.org/paper/4be02694125b71876552900a53c85c47a2a83614) | [BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K) | 1,811 |
| 17 | HM3D / HM3D-Sem | [912](https://www.semanticscholar.org/paper/f46bce5b7dd78736133c1af1824ddb83c0ec2e55) | [GenieSim 3.0](https://github.com/AgibotTech/genie_sim) | 1,765 |
| 18 | Habitat 2.0 — Home Assistant Benchmark | [876](https://www.semanticscholar.org/paper/4aa88c1406414cda3ce9cf76c8af0abaa8391760) | [D4RL — Franka Kitchen](https://github.com/Farama-Foundation/D4RL) | 1,712 |
| 19 | robosuite | [871](https://www.semanticscholar.org/paper/cf34efc663284da131e747407ac3f389f898e471) | [RoboMimic](https://github.com/ARISE-Initiative/robomimic) | 1,610 |
| 20 | EQA | [849](https://www.semanticscholar.org/paper/cc5ac1d3083b6663482ba6830dfa3bf65343286c) | [LocoMuJoCo](https://github.com/robfiras/loco-mujoco) | 1,499 |

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

## 16. Simulation Platforms & Unified Benchmark Frameworks (仿真平台/统一框架)

Not benchmarks per se, but most benchmarks above are built on them.

| Platform | Notes | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|
| MuJoCo / MuJoCo Playground | Physics engine behind Meta-World, robosuite, DMC, HumanoidBench | [GitHub](https://github.com/google-deepmind/mujoco) | — | [![stars](https://img.shields.io/github/stars/google-deepmind/mujoco?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-deepmind/mujoco) |
| SAPIEN / ManiSkill3 | GPU-parallel sim + rendering | [arXiv:2410.00425](https://arxiv.org/abs/2410.00425) | [409](https://www.semanticscholar.org/paper/6116f4ce4ec1b3cda988e7b289eda6daea75f479) | [![stars](https://img.shields.io/github/stars/mani-skill/ManiSkill?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mani-skill/ManiSkill) |
| NVIDIA Isaac Sim / Isaac Lab | RTX rendering, used by ARNOLD, VLNVerse, RobOmni | [GitHub](https://github.com/isaac-sim/IsaacLab) | — | [![stars](https://img.shields.io/github/stars/isaac-sim/IsaacLab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/isaac-sim/IsaacLab) |
| AI2-THOR / ProcTHOR | Interactive houses (ALFRED, TEACh) | [arXiv:2206.06994](https://arxiv.org/abs/2206.06994) | [660](https://www.semanticscholar.org/paper/d7bca917b753b996074203cc77ba45935b7c62d7) | [![stars](https://img.shields.io/github/stars/allenai/ai2thor?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/ai2thor) |
| Habitat-Sim / Habitat-Lab | Navigation & rearrangement | [arXiv:1904.01201](https://arxiv.org/abs/1904.01201) | [2,323](https://www.semanticscholar.org/paper/b4a35e548de27b6924e5f2ee41d37238a5c4a1d5) | [![stars](https://img.shields.io/github/stars/facebookresearch/habitat-sim?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/habitat-sim) |
| iGibson / OmniGibson | BEHAVIOR series | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) | [223](https://www.semanticscholar.org/paper/66d7d369b00d4855455ce55dd7c9c1419da0c1d0) | [![stars](https://img.shields.io/github/stars/StanfordVL/BEHAVIOR-1K?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/StanfordVL/BEHAVIOR-1K) |
| RoboVerse | Unified platform/dataset/benchmark across simulators | [arXiv:2504.18904](https://arxiv.org/abs/2504.18904) | [88](https://www.semanticscholar.org/paper/36b457f4a4cbdb4c74a2713e06ea9b5753122b41) | [![stars](https://img.shields.io/github/stars/RoboVerseOrg/RoboVerse?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboVerseOrg/RoboVerse) |
| GRUtopia / InternUtopia | City-scale embodied sim for general robots | [arXiv:2407.10943](https://arxiv.org/abs/2407.10943) | [88](https://www.semanticscholar.org/paper/b75f344d962b3b25b64c0c96a86244c4c3c6e490) | [![stars](https://img.shields.io/github/stars/Sage-PhysicalAI/InternUtopia?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Sage-PhysicalAI/InternUtopia) |
| Genesis | Generative, multi-physics simulator | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) | — | [![stars](https://img.shields.io/github/stars/Genesis-Embodied-AI/genesis-world?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Genesis-Embodied-AI/genesis-world) |
| **vla-eval** (Ai2 VLA Evaluation Harness) | One harness + leaderboard over 18 sim benchmarks (LIBERO, SimplerEnv, CALVIN, RoboTwin …) | [arXiv:2603.13966](https://arxiv.org/abs/2603.13966) | [12](https://www.semanticscholar.org/paper/cb522f52c35d3e97ef569366699e2c8ba51c394b) | [![stars](https://img.shields.io/github/stars/allenai/vla-evaluation-harness?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/vla-evaluation-harness) |
| **Embodied Arena** (Shanghai AI Lab) | Unified platform + leaderboard: 3-level taxonomy, 7 capabilities, 25 dimensions | [arXiv:2509.15273](https://arxiv.org/abs/2509.15273) | [15](https://www.semanticscholar.org/paper/10301328e7ae30f4f57c5fa3516ea1969a29465e) | — |
| **MolmoSpaces** / MolmoSpaces-Bench | 230k indoor scenes, 130k assets, 42M grasps; simulator-agnostic; 8-task bench with sim-real R = 0.96 | [arXiv:2602.11337](https://arxiv.org/abs/2602.11337) | [36](https://www.semanticscholar.org/paper/21eb7e1966167c65e7c1d2abcca1ef21067d9696) | [![stars](https://img.shields.io/github/stars/allenai/molmospaces?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/molmospaces) |
| **FlagEval-Robo** (BAAI) | Embodied leaderboard with a sim track and a real-robot track (ATOM-Bench); data-contamination checks | [Website](https://huggingface.co/spaces/BAAI/FlagEval-Robo) | — | — |
| **EmbodiedIndex** | Puts public leaderboard results side by side; finds 85% of robot policies are scored on only one benchmark | [Website](https://embodiedindex.ai/) | — | — |
| **VLA Leaderboard** | Community aggregator of VLA results across public sim and real benchmarks | [Website](https://vlaleaderboard.com/) | — | — |
| **Open LMM Spatial Leaderboard** (OpenCompass) | Spatial-reasoning leaderboard for multimodal LLMs | [Website](https://huggingface.co/spaces/opencompass/openlmm_spatial_leaderboard) | — | — |
| **IR-SIM** | Lightweight declarative (YAML) Python simulator for navigation learning and benchmarking | [arXiv:2606.08729](https://arxiv.org/abs/2606.08729) | [6](https://www.semanticscholar.org/paper/cbab20e7f92caa7d4111f8e04c2d9b38d5d49508) | [![stars](https://img.shields.io/github/stars/hanruihua/ir-sim?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/hanruihua/ir-sim) |
| **DeepInsight II** | One trace from benchmark to robot: reproduces 2 navigation + 4 manipulation benchmarks; MotionBench carries whole-body controllers from sim to real | [arXiv:2608.16556](https://arxiv.org/abs/2608.16556) | [0](https://www.semanticscholar.org/paper/3e47b0ae65eb4c47733944aa16c0b2e3f57d47e0) | — |
| **Co-Design Gym** | 20 environment families, 85+ presets for joint embodiment-policy optimization (manipulation, locomotion, soft bodies …) | [arXiv:2610.02366](https://arxiv.org/abs/2610.02366) | [0](https://www.semanticscholar.org/paper/160265be86e8759765048e63e8726af679da9240) | — |

---

## 17. Companion Datasets Often Used for Evaluation (常用于评测的数据集)

| Dataset | Notes | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|
| Open X-Embodiment | 1M+ trajectories, 22 embodiments; RT-X evaluation | [arXiv:2310.08864](https://arxiv.org/abs/2310.08864) | [1,317](https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f) | [![stars](https://img.shields.io/github/stars/google-deepmind/open_x_embodiment?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-deepmind/open_x_embodiment) |
| BridgeData V2 | WidowX; basis of SIMPLER-WidowX & AutoEval | [arXiv:2308.12952](https://arxiv.org/abs/2308.12952) | [1,025](https://www.semanticscholar.org/paper/6a375be82efc01ec4ed73334655935a56ba82d38) | [![stars](https://img.shields.io/github/stars/rail-berkeley/bridge_data_v2?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/rail-berkeley/bridge_data_v2) |
| DROID | 76k Franka trajectories in the wild; basis of RoboArena & PolaRiS | [arXiv:2403.12945](https://arxiv.org/abs/2403.12945) | [1,421](https://www.semanticscholar.org/paper/ee5070fe52fd17da9a89d3f342fb07cc9ae51afe) | [![stars](https://img.shields.io/github/stars/droid-dataset/droid?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/droid-dataset/droid) |
| Deform360 / HapTile | 2026 visuotactile deformable / contact-rich datasets | — | — | — |

---

## 18. Competitions & Challenges (竞赛)

- **LeHome Challenge** (ICRA 2026) — household garment manipulation: Isaac Sim round (62 teams) + real-robot final. [Website](https://lehome-challenge.github.io/)
- **RSS 2026 Post-Training for Robotics Challenge** — standardized real-robot bimanual benchmark. [Website](https://posttraining-for-robotics.github.io/)
- **AgiBot World Challenge** (ICRA 2026) — sim track on GenieSim 3.0 + real-robot finals (incl. supermarket mobile manipulation). [Report](https://www.therobotreport.com/agibot-holds-world-challenge-2026-see-how-ai-models-perform-real-tasks/)
- **RoboChallenge** (2025–) — always-on online real-robot evaluation (Table30). [Website](https://robochallenge.ai/)
- **RoboDojo Leaderboard** (2026–) — sim + remote real-robot leaderboard. [Website](https://robodojo-benchmark.com/)
- **BEHAVIOR Challenge** (NeurIPS 2025, CoRL 2026) — 50 long-horizon household tasks in OmniGibson (2025); 100 full-length BEHAVIOR-1K tasks (2026). [Website](https://behavior.stanford.edu/challenge/)
- **Physical AI Competition** (Nebius × Positronic, 2026) — simulation qualifier; the top 10 teams are evaluated on a real DROID-style Franka (PhAIL). [Website](https://competition.phail.ai/)
- **UNOBench Challenge** (ECCV 2026 workshop) — obstruction-aware grasp reasoning; Set-of-Marks and natural-language tracks. [Website](https://unobenchchallenge.fbk.eu/)
- **Video to Data Challenge** (NVIDIA, 2026) — turn human video into simulated robot demonstrations. [Website](https://nvidia-isaac.github.io/video_to_data/v2d_challenge/)
- **PhyRC Challenge** (2026–27) — physical robot caregiving (robot-assisted dressing); simulation phase, then real-robot evaluation. [Website](https://emprise.cs.cornell.edu/phyrc/challenge-2027/)
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

| Survey | Year | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|
| Datasets, Benchmarks and Data Engines for VLA models | 2026 | [arXiv:2604.23001](https://arxiv.org/abs/2604.23001) | [11](https://www.semanticscholar.org/paper/243c6e23d30f0da8f4a0579de16850f4a82eb2f2) | — |
| Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends | 2026 | [arXiv:2606.12207](https://arxiv.org/abs/2606.12207) | [1](https://www.semanticscholar.org/paper/726c1e916a7131d022cc8f2ec411991d0b0253cd) | — |
| Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence | 2026 | [arXiv:2609.29669](https://arxiv.org/abs/2609.29669) | [1](https://www.semanticscholar.org/paper/35b110d3136a97f2510a66708b9e68d784ec9e79) | — |
| Evaluation-centric VLA survey (582 papers, minimum reporting protocols) | 2026 | [Preprints.org](https://www.preprints.org/manuscript/202606.1149) | — | — |
| VLA Models for UAVs and Bimanual Manipulation: A Review | 2026 | [arXiv:2607.06706](https://arxiv.org/abs/2607.06706) | [2](https://www.semanticscholar.org/paper/d6a19545bf6f5e9598046fc26a07635195b65452) | — |
| When the World Is the Test Suite: Agentic Intelligence for the Physical World | 2026 | [arXiv:2611.22291](https://arxiv.org/abs/2611.22291) | [0](https://www.semanticscholar.org/paper/9c366436b197ccdf045e59ca2f4554500744fd1e) | [![stars](https://img.shields.io/github/stars/PhysicalWorldAgent/Awesome-PhysicalWorldAgent?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/PhysicalWorldAgent/Awesome-PhysicalWorldAgent) |
| How Should World Models Be Evaluated for Embodied Decision-Making? (position) | 2026 | [arXiv:2606.15032](https://arxiv.org/abs/2606.15032) | [17](https://www.semanticscholar.org/paper/c027d10ce23a260bd197808b455c856ddd96f656) | — |
| Benchmarking Dexterity of Multifingered Robot Hands: A Review and Perspective | 2026 | [arXiv:2609.05585](https://arxiv.org/abs/2609.05585) | [0](https://www.semanticscholar.org/paper/c9278d468e73681994a972cab0fb250a828986c6) | — |

Related awesome lists: [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) · [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam)

---

## Trends & Takeaways (趋势总结)

1. **Saturation → perturbation.** LIBERO/SIMPLER/CALVIN numbers are near ceiling for strong VLAs. 2025–26 work (LIBERO-PRO/Plus/MAX, STRONG-VLA, RoboSPA) shows that small camera, init-state or wording changes can collapse success — *report perturbed suites, not just the original*.
2. **Benchmarks themselves are being audited.** Shortcut solvability, few-trial noise and demo-source leakage ([2609.37771](https://arxiv.org/abs/2609.37771)) mean you should report confidence intervals and number of trials.
3. **Real-world evaluation is scaling** via distribution (RoboArena, RoboColosseum — 124 sites), always-on online fleets (RoboChallenge), unified sim+real suites (RoboDojo), automation (AutoEval) and low-cost replication (VLA-REPLICA). RoboColosseum finds policy rankings barely transfer across embodiments — evaluate on *your* robot.
4. **Cheaper proxies for real robots:** Real2Sim (SIMPLER → PolaRiS → 3DGS verification) and world-model evaluators (WorldGym, dWorldEval, WMBench, RoboWorld). The key metric is rank correlation with real success.
5. **Beyond success rate:** memory (RoboMME), compositionality (ATOM-Bench), safety (SafeVLA-Bench, SoftVTBench), damage to objects and surroundings (OopsieVerse, ManiPhysicsBench), and behavior quality (RoboEval).
6. **The "brain" is evaluated separately from the "body":** ERQA, RoboBench, Embodied3DBench, ERQA-Plus test VLM reasoning offline; ERIQ reports this correlates with downstream VLA generalization.
7. **New embodiments get their own suites:** humanoids (SIMPLE, CoHuB, LHM-Humanoid), dexterous hands (DexJoCo, POMDAR), UAVs (OpenFly, UAV-ON), tactile (UniVTAC, RobOmni).
8. **Aggregators and coding agents.** Meta-leaderboards (FlagEval-Robo, EmbodiedIndex, VLA Leaderboard) expose thin coverage: EmbodiedIndex finds 85% of robot policies are scored on only one benchmark. Real-robot boards (Reality Check, RoboDojo-RC) and suites such as VABAR and CaP-X now rank coding agents next to VLAs.

## How to Pick a Benchmark (选型建议)

| If you are building… | Start with | Then stress-test with |
|---|---|---|
| A generalist VLA policy | LIBERO, SIMPLER, RoboCasa365, RoboTwin 2.0, RoboLab | RoboDojo, LIBERO-Plus/PRO, RoboChallenge / RoboArena / RoboColosseum, PolaRiS |
| A bimanual / dexterous policy | RoboTwin 2.0, Bi-DexHands, DexJoCo | Real: POMDAR, DexToolBench |
| A long-horizon / household agent | CALVIN, BEHAVIOR-1K, HomeRobot OVMM | RoboMME (memory), EBench |
| A humanoid controller | HumanoidBench | SIMPLE, LHM-Humanoid |
| A navigation agent | Habitat ObjectNav, R2R / VLN-CE | GOAT-Bench, OmniNavBench, VLNVerse, NavVerse |
| An embodied VLM "brain" | ERQA, VSI-Bench, RoboBench, PhysBench | Embodied3DBench, RefSpatial-Bench, ESI-Bench, EmbodiedBench |
| A safety layer | SafeAgentBench, SafeVLA-Bench | RoboJailBench, VLA-RISK |

---

## Contributing

PRs welcome! Add entries to [`data/benchmarks.yaml`](data/benchmarks.yaml) — **do not edit `README.md` directly**, it is generated from [`templates/README.template.md`](templates/README.template.md). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) To the extent possible under law, the contributors have waived all copyright and related rights to this work.

# Awesome Embodied Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **categorized** list of benchmarks for robot learning and embodied AI — from classic simulation suites (Meta-World, RLBench, Habitat) to the newest VLA, humanoid, world-model-as-evaluator and safety benchmarks of 2025–2026.
>
> 一个系统整理、**分门别类**的机器人 / 具身智能 Benchmark 合集：覆盖经典仿真基准、真实世界评测、VLA 泛化与鲁棒性、人形机器人、导航、具身推理 (VLM)、世界模型评测、安全等方向，并持续追踪 2025–2026 的最新论文。

**Last updated: 2026-11** · Entries marked 🆕 appeared in 2026 · 🔥 = widely used / de-facto standard · `Sim` / `Real` / `Real2Sim` / `QA` = evaluation modality

> [!NOTE]
> **Citations** (from [Semantic Scholar](https://www.semanticscholar.org/), falling back to [OpenAlex](https://openalex.org/)) are refreshed **daily** by a [GitHub Action](.github/workflows/update-metrics.yml) · last refresh: **2026-11-19 07:22 UTC**.
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

| # | Most cited | Citations | Most starred | Stars |
|---|---|---|---|---|
| 1 | LIBERO | [2,311](https://www.semanticscholar.org/paper/98cfd7b1b29453c4e82536f5afdc6ddc58bbb1b3) | [MuJoCo / MuJoCo Playground](https://github.com/google-deepmind/mujoco) | 18,305 |
| 2 | Habitat | [2,308](https://www.semanticscholar.org/paper/b4a35e548de27b6924e5f2ee41d37238a5c4a1d5) | [Gymnasium MuJoCo](https://github.com/Farama-Foundation/Gymnasium) | 12,838 |
| 3 | Room-to-Room (R2R) | [2,130](https://www.semanticscholar.org/paper/c37c23b12e00168833eccff8025a830ce27c5abc) | [NVIDIA Isaac Sim / Isaac Lab](https://github.com/isaac-sim/IsaacLab) | 8,683 |
| 4 | D4RL — Franka Kitchen | [2,027](https://www.semanticscholar.org/paper/cd4db2d18d96fc1380f6cf379ead49c5492d8d50) | [DeepMind Control Suite](https://github.com/google-deepmind/dm_control) | 4,726 |
| 5 | Meta-World | [1,948](https://www.semanticscholar.org/paper/0bc855f84668b35cb65618d996d09f6e434d28c9) | [Habitat-Sim / Habitat-Lab](https://github.com/facebookresearch/habitat-sim) | 3,848 |
| 6 | DeepMind Control Suite | [1,596](https://www.semanticscholar.org/paper/a9a3ed69c94a3e1c08ef1f833d9199f57736238b) | [Habitat 2.0 — Home Assistant Benchmark](https://github.com/facebookresearch/habitat-lab) | 3,190 |
| 7 | ALFWorld | [1,594](https://www.semanticscholar.org/paper/398a0625e8707a0b41ac58eaec51e8feb87dd7cb) | [RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin) | 3,068 |
| 8 | DROID | [1,379](https://www.semanticscholar.org/paper/ee5070fe52fd17da9a89d3f342fb07cc9ae51afe) | [robosuite](https://github.com/ARISE-Initiative/robosuite) | 2,716 |
| 9 | Open X-Embodiment | [1,302](https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f) | [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) | 2,560 |
| 10 | ALFRED | [1,298](https://www.semanticscholar.org/paper/f4cf4246f3882aa6337e9c05d5675a3b8463a32e) | [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment) | 2,099 |
| 11 | RLBench | [1,226](https://www.semanticscholar.org/paper/a2fdfda785b3a2a0178d174daa515377c531f222) | [Meta-World](https://github.com/Farama-Foundation/Metaworld) | 1,908 |
| 12 | RoboMimic | [1,207](https://www.semanticscholar.org/paper/3032844d6ac6882ccb03e7a2c22a0026b210ac05) | [RoboVerse](https://github.com/RoboVerseOrg/RoboVerse) | 1,883 |
| 13 | BridgeData V2 | [1,009](https://www.semanticscholar.org/paper/6a375be82efc01ec4ed73334655935a56ba82d38) | [RoboCasa](https://github.com/robocasa/robocasa) | 1,880 |
| 14 | GraspNet-1Billion | [969](https://www.semanticscholar.org/paper/f76c9834a249a97ebcaf225a216c6076032af99c) | [RLBench](https://github.com/stepjam/RLBench) | 1,840 |
| 15 | VSI-Bench | [938](https://www.semanticscholar.org/paper/376461a2c049f6fa51a4303853fdc672e4d07a0d) | [AI2-THOR / ProcTHOR](https://github.com/allenai/ai2thor) | 1,830 |
| 16 | CALVIN | [935](https://www.semanticscholar.org/paper/4be02694125b71876552900a53c85c47a2a83614) | [BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K) | 1,802 |
| 17 | HM3D / HM3D-Sem | [908](https://www.semanticscholar.org/paper/f46bce5b7dd78736133c1af1824ddb83c0ec2e55) | [D4RL — Franka Kitchen](https://github.com/Farama-Foundation/D4RL) | 1,712 |
| 18 | Habitat 2.0 — Home Assistant Benchmark | [868](https://www.semanticscholar.org/paper/4aa88c1406414cda3ce9cf76c8af0abaa8391760) | [GenieSim 3.0](https://github.com/AgibotTech/genie_sim) | 1,680 |
| 19 | robosuite | [853](https://www.semanticscholar.org/paper/cf34efc663284da131e747407ac3f389f898e471) | [RoboMimic](https://github.com/ARISE-Initiative/robomimic) | 1,608 |
| 20 | EQA | [841](https://www.semanticscholar.org/paper/cc5ac1d3083b6663482ba6830dfa3bf65343286c) | [LocoMuJoCo](https://github.com/robfiras/loco-mujoco) | 1,482 |

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

| Benchmark | Year / Venue | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| 🔥 **Meta-World** | 2019 / CoRL | Sim (MuJoCo) | 50 Sawyer tasks; multi-task & meta-RL (ML1/ML10/ML45, MT10/MT50) | [arXiv:1910.10897](https://arxiv.org/abs/1910.10897) | [1,948](https://www.semanticscholar.org/paper/0bc855f84668b35cb65618d996d09f6e434d28c9) | [![stars](https://img.shields.io/github/stars/Farama-Foundation/Metaworld?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Farama-Foundation/Metaworld) |
| 🔥 **RLBench** | 2019 / RA-L | Sim (CoppeliaSim) | 100 hand-designed tasks with demos; standard for keyframe/3D policies (PerAct, RVT) | [arXiv:1909.12271](https://arxiv.org/abs/1909.12271) | [1,226](https://www.semanticscholar.org/paper/a2fdfda785b3a2a0178d174daa515377c531f222) | [![stars](https://img.shields.io/github/stars/stepjam/RLBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/stepjam/RLBench) |
| **robosuite** | 2020 | Sim (MuJoCo) | Modular framework + standardized tasks; basis of RoboMimic, LIBERO, RoboCasa | [arXiv:2009.12293](https://arxiv.org/abs/2009.12293) | [853](https://www.semanticscholar.org/paper/cf34efc663284da131e747407ac3f389f898e471) | [![stars](https://img.shields.io/github/stars/ARISE-Initiative/robosuite?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/ARISE-Initiative/robosuite) |
| **Ravens / Transporter tasks** | 2020 / CoRL | Sim (PyBullet) | Rearrangement tasks (stacking, kitting, rope, etc.) | [arXiv:2010.14406](https://arxiv.org/abs/2010.14406) | [634](https://www.semanticscholar.org/paper/eb6b9bc4ff3e4e2cf1724324d79ce7de43131478) | [![stars](https://img.shields.io/github/stars/google-research/ravens?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-research/ravens) |
| **D4RL — Franka Kitchen** | 2020 | Sim (MuJoCo) | Offline-RL suite; Franka Kitchen multi-stage kitchen tasks widely used for imitation | [arXiv:2004.07219](https://arxiv.org/abs/2004.07219) | [2,027](https://www.semanticscholar.org/paper/cd4db2d18d96fc1380f6cf379ead49c5492d8d50) | [![stars](https://img.shields.io/github/stars/Farama-Foundation/D4RL?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Farama-Foundation/D4RL) |
| 🔥 **CALVIN** | 2021 / RA-L | Sim (PyBullet) | Language-conditioned long-horizon chains (5 tasks in a row), ABC→D split | [arXiv:2112.03227](https://arxiv.org/abs/2112.03227) | [935](https://www.semanticscholar.org/paper/4be02694125b71876552900a53c85c47a2a83614) | [![stars](https://img.shields.io/github/stars/mees/calvin?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mees/calvin) |
| **ManiSkill / ManiSkill2 / ManiSkill3** | 2021–2024 | Sim (SAPIEN) | Generalizable manipulation; v3 is GPU-parallel with rendering at scale | [v1](https://arxiv.org/abs/2107.14483) · [v2](https://arxiv.org/abs/2302.04659) · [v3](https://arxiv.org/abs/2410.00425) | [288](https://www.semanticscholar.org/paper/9db27b7b03b4843178fe83b09813acab323b3c4e) | [![stars](https://img.shields.io/github/stars/mani-skill/ManiSkill?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mani-skill/ManiSkill) |
| **RoboMimic** | 2021 / CoRL | Sim (robosuite) + Real | Benchmark & study of offline learning from human demos (Lift/Can/Square/Transport/ToolHang) | [arXiv:2108.03298](https://arxiv.org/abs/2108.03298) | [1,207](https://www.semanticscholar.org/paper/3032844d6ac6882ccb03e7a2c22a0026b210ac05) | [![stars](https://img.shields.io/github/stars/ARISE-Initiative/robomimic?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/ARISE-Initiative/robomimic) |
| **VIMA-Bench** | 2022 / ICML'23 | Sim | Multimodal (text+image) prompts; 4-level generalization protocol | [arXiv:2210.03094](https://arxiv.org/abs/2210.03094) | [656](https://www.semanticscholar.org/paper/25425e299101b13ec2872417a14f961f4f8aa18e) | [![stars](https://img.shields.io/github/stars/vimalabs/VIMABench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/vimalabs/VIMABench) |
| **VLMbench** | 2022 / NeurIPS D&B | Sim (RLBench) | Compositional language-guided manipulation with constraints | [arXiv:2206.08522](https://arxiv.org/abs/2206.08522) | [111](https://www.semanticscholar.org/paper/c6cb024e25ba5136aa914ee007453dd0af6891cc) | — |
| **BulletArm** | 2022 | Sim (PyBullet) | Open-source robotic manipulation benchmark & learning framework | [arXiv:2205.14292](https://arxiv.org/abs/2205.14292) | [16](https://www.semanticscholar.org/paper/44df7090a9b18b19196018b5705dfc9153e068ed) | [![stars](https://img.shields.io/github/stars/ColinKohler/BulletArm?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/ColinKohler/BulletArm) |
| **HandoverSim** | 2022 / ICRA | Sim | Human-to-robot object handover benchmark | [arXiv:2205.09747](https://arxiv.org/abs/2205.09747) | [40](https://www.semanticscholar.org/paper/7e64810837d0418f21c9ae1972de94b8456bcbb7) | [![stars](https://img.shields.io/github/stars/NVlabs/handover-sim?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/NVlabs/handover-sim) |
| **ARNOLD** | 2023 / ICCV | Sim (Isaac) | Language-grounded continuous-state tasks (e.g., "fill cup 50%") | [arXiv:2304.04321](https://arxiv.org/abs/2304.04321) | [98](https://www.semanticscholar.org/paper/7a2ec15a7a3e3f54be083aa559ec6f6453e3c9ac) | [![stars](https://img.shields.io/github/stars/arnold-benchmark/arnold?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/arnold-benchmark/arnold) |
| 🔥 **LIBERO** | 2023 / NeurIPS D&B | Sim (robosuite) | 130 tasks; Spatial / Object / Goal / Long suites; lifelong learning; the most-reported VLA benchmark | [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) | [2,311](https://www.semanticscholar.org/paper/98cfd7b1b29453c4e82536f5afdc6ddc58bbb1b3) | [![stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| **RoboHive** | 2023 / NeurIPS D&B | Sim + Real | Unified framework for dexterous, multi-task & visual robot learning | [arXiv:2310.06828](https://arxiv.org/abs/2310.06828) | [73](https://www.semanticscholar.org/paper/5343715cb2b7f7ac5c0acf92d1fc5657b40850b6) | [![stars](https://img.shields.io/github/stars/vikashplus/robohive?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/vikashplus/robohive) |
| **PushWorld** | 2023 | Sim | 200+ puzzles: manipulation planning with tools & movable obstacles | [arXiv:2301.10289](https://arxiv.org/abs/2301.10289) | [5](https://www.semanticscholar.org/paper/d5781022f211bc2bc8eaeeb574e0fef86a58ec45) | [![stars](https://img.shields.io/github/stars/google-deepmind/pushworld?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-deepmind/pushworld) |
| **PartManip** | 2023 / CVPR | Sim | Cross-category part-based articulated manipulation from point clouds (494 objects, 1,432 tasks) | [arXiv:2303.16958](https://arxiv.org/abs/2303.16958) | [70](https://www.semanticscholar.org/paper/e8d67eaaf2a495fb5b2b1f813028c1784263ebc1) | — |
| **The Colosseum** | 2024 / RSS | Sim (RLBench) | 20 tasks × 14 perturbation axes for generalization | [arXiv:2402.08191](https://arxiv.org/abs/2402.08191) | [220](https://www.semanticscholar.org/paper/8a839c963de28f4bd5b52af982702cde1a00e82e) | [![stars](https://img.shields.io/github/stars/robot-colosseum/robot-colosseum?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robot-colosseum/robot-colosseum) |
| 🔥 **RoboCasa** | 2024 / RSS | Sim (robosuite) | Large-scale kitchen scenes, 100 tasks, generative assets | [arXiv:2406.02523](https://arxiv.org/abs/2406.02523) | [677](https://www.semanticscholar.org/paper/f773ceb43ffc7f9cd685250c4919924ec0bc85c7) | [![stars](https://img.shields.io/github/stars/robocasa/robocasa?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robocasa/robocasa) |
| **GemBench** | 2024 | Sim (RLBench) | 4 levels of generalization: placement, rigid objects, articulated, long-horizon | [arXiv:2410.01345](https://arxiv.org/abs/2410.01345) | [71](https://www.semanticscholar.org/paper/aa28e62a1bb93154a3623e8cdfa049d7b5882f1c) | [![stars](https://img.shields.io/github/stars/vlc-robot/robot-3dlotus?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/vlc-robot/robot-3dlotus) |
| **VLABench** | 2024 / ICCV'25 | Sim | 100 task categories, 2000+ objects; language-conditioned manipulation with commonsense/reasoning | [arXiv:2412.18194](https://arxiv.org/abs/2412.18194) | [281](https://www.semanticscholar.org/paper/93657d550dd636b5bc284d9803b20646aafc37bf) | [![stars](https://img.shields.io/github/stars/OpenMOSS/VLABench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/OpenMOSS/VLABench) |
| **ClevrSkills** | 2024 / NeurIPS D&B | Sim (ManiSkill) | Compositional reasoning & skill composition in manipulation | [arXiv:2411.09052](https://arxiv.org/abs/2411.09052) | [16](https://www.semanticscholar.org/paper/3a600d04e3fda61836dbd81c54fee1595ae7d77e) | — |
| **RoboEval** | 2025 | Sim | Structured, scalable evaluation with behavioral & outcome metrics beyond success rate | [arXiv:2507.00435](https://arxiv.org/abs/2507.00435) | [49](https://www.semanticscholar.org/paper/fe25c6ceaabf4d9a6f87372841c7cf10f00acb3d) | — |
| 🆕 **GenieSim 3.0** | 2025–26 | Sim | AgiBot's simulation benchmark; used for AgiBot World Challenge reasoning-to-action track | [arXiv:2601.02078](https://arxiv.org/abs/2601.02078) | [21](https://www.semanticscholar.org/paper/e197fa33aa930838f241a17dabe93bf9413cd36b) | [![stars](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/AgibotTech/genie_sim) |
| **Meta-World+** | 2025 | Sim (MuJoCo) | Improved, standardized re-release of Meta-World | [arXiv:2505.11289](https://arxiv.org/abs/2505.11289) | [67](https://www.semanticscholar.org/paper/53352e0e8eb2694ff0dae24df7cdec31575e552e) | [![stars](https://img.shields.io/github/stars/Farama-Foundation/Metaworld?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Farama-Foundation/Metaworld) |
| **AnyBody** | 2025 | Sim | Cross-embodiment manipulation: 18 robot morphologies; interpolation / extrapolation / composition | [arXiv:2505.14986](https://arxiv.org/abs/2505.14986) | [7](https://www.semanticscholar.org/paper/61ba2ac4ca395fb5363c8bff97df1140be3aee0d) | — |
| **GenManip** | 2025 / CVPR | Sim | LLM-driven scene generation over 10K assets; 200+ instruction-following scenarios | [arXiv:2506.10966](https://arxiv.org/abs/2506.10966) | [31](https://www.semanticscholar.org/paper/d29c715b0cfa25fb5c34eb91a3af8de871efd901) | [![stars](https://img.shields.io/github/stars/InternRobotics/GenManip?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/InternRobotics/GenManip) |
| **REALM** | 2025 | Sim (real-to-sim validated) | 15 perturbation factors, 7 skills, 3,500+ objects; sim-real correlation validated | [arXiv:2512.19562](https://arxiv.org/abs/2512.19562) | [27](https://www.semanticscholar.org/paper/dd290457b11b0a2675b5baf80b72327e173ee475) | [![stars](https://img.shields.io/github/stars/martin-sedlacek/REALM?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/martin-sedlacek/REALM) |
| 🆕 **RoboSPA** | 2026 | Sim | Can VLAs go beyond simple scenes and short-horizon tasks? Cluttered, longer tasks | [arXiv:2609.05324](https://arxiv.org/abs/2609.05324) | [2](https://www.semanticscholar.org/paper/f4721d34472c34355951debe81907b3e672eaf0c) | [![stars](https://img.shields.io/github/stars/fanzhenxuan/RoboSPA?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/fanzhenxuan/RoboSPA) |
| 🆕 **ManipArena** | 2026 | Real | Real-world evaluation framework: 20 tasks in 3 categories incl. mobile manipulation | [arXiv:2603.28545](https://arxiv.org/abs/2603.28545) | [8](https://www.semanticscholar.org/paper/45717b35dead1d6d26d50f2699b8f27e698799ef) | — |
| 🆕 **InstructMove** | 2026 | — | Text-indispensable instruction following: category / attribute / spatial grounding & compositional pick-and-place (Isaac Lab) | [arXiv:2608.22990](https://arxiv.org/abs/2608.22990) | [2](https://www.semanticscholar.org/paper/440598ded56fe361fda7cd430010a3439e3b5f51) | [![stars](https://img.shields.io/github/stars/HorizonRobotics/RoboOrchardSim?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/HorizonRobotics/RoboOrchardSim) |
| 🆕 **RoboLab (RoboLab-120)** | 2026 / RSS | Sim (Isaac Lab) | 120 tasks along visual / procedural / relational axes; DROID-trained π0.5 only ~30% | [arXiv:2604.09860](https://arxiv.org/abs/2604.09860) | [68](https://www.semanticscholar.org/paper/4a0e21475dfe488e745aac8776bd1b9e2c1c99af) | [![stars](https://img.shields.io/github/stars/NVlabs/RoboLab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/NVlabs/RoboLab) |
| 🆕 **RoboCasa365** | 2026 / ICLR | Sim (robosuite) | 365 household tasks, 2,500 kitchen scenes, 600+ h demos, public leaderboard | [arXiv:2603.04356](https://arxiv.org/abs/2603.04356) | [182](https://www.semanticscholar.org/paper/3462a6063dbf86ffd82c567b21879fb7080363ab) | [![stars](https://img.shields.io/github/stars/robocasa/robocasa?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robocasa/robocasa) |
| 🆕🔥 **RoboDojo** | 2026 / ECCV | Sim (Isaac Sim) + Real (remote) | 42 sim + 18 real tasks; Generalization / Precision / Long-Horizon / Memory / Open; 30 policies on a live leaderboard; best policy 8.8% sim success vs 76% teleop | [arXiv:2607.04434](https://arxiv.org/abs/2607.04434) | [116](https://www.semanticscholar.org/paper/697fee3831e3bebd5052c607383bd42a0b50e9dd) | [![stars](https://img.shields.io/github/stars/RoboDojo-Benchmark/RoboDojo?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboDojo-Benchmark/RoboDojo) |
| 🆕 **XPolicyLab** | 2026 | Framework | Unified standard & open ecosystem for policy evaluation/deployment (powers RoboDojo) | [arXiv:2608.09892](https://arxiv.org/abs/2608.09892) | [16](https://www.semanticscholar.org/paper/80275329cd78a372ad6f4a78109128ae68a7d028) | [![stars](https://img.shields.io/github/stars/XPolicyLab/XPolicyLab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/XPolicyLab/XPolicyLab) |
| 🆕 **RoboColiseum** | 2026 | Sim | Multidimensional benchmark (instruction following, spatial reasoning, general manipulation) incl. LLM-driven robot control | [arXiv:2610.27865](https://arxiv.org/abs/2610.27865) | [4](https://www.semanticscholar.org/paper/1fd8bc769981856e8186d097687bcb7560102ffc) | — |
| 🆕 **KinDER** | 2026 / RSS | Sim | Physical reasoning: 25 procedural envs (tool use, nonprehensile, geometric & dynamic constraints) | [arXiv:2604.25788](https://arxiv.org/abs/2604.25788) | [7](https://www.semanticscholar.org/paper/4f2730532e99b94be29dfe04c6fbc3d0ed9374a0) | [![stars](https://img.shields.io/github/stars/Princeton-Robot-Planning-and-Learning/kindergarden?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden) |
| 🆕 **VISER** | 2026 | Sim | Visually realistic sim benchmark; reconstructed tasks mirror real benchmarks for sim-real correlation | [arXiv:2605.06311](https://arxiv.org/abs/2605.06311) | [3](https://www.semanticscholar.org/paper/c05d1e95ddd72a9e8afc8e2b84285d7df548ffb2) | — |
| 🆕 **COLOSSEUM V2** | 2026 | Sim (GPU) | 28 tasks, 13 categories, 2 morphologies; visual / language / action generalization | [arXiv:2605.27759](https://arxiv.org/abs/2605.27759) | [6](https://www.semanticscholar.org/paper/ff60e668c280b09db7875904a8f2e768261f899c) | — |
| 🆕 **PhysMani-Bench** | 2026 | Sim | 16 dynamic-object tasks (catching, rotating tables) | [arXiv:2607.01938](https://arxiv.org/abs/2607.01938) | [2](https://www.semanticscholar.org/paper/d2d0bc8639fe461a5f0f1eac3cad8208302be061) | [![stars](https://img.shields.io/github/stars/vLAR-group/PhysMani?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/vLAR-group/PhysMani) |
| 🆕 **IndustrialVLA-Bench** | 2026 | Sim/Real | Traceable multi-axis evaluation of open robot policy models for industrial tasks | [arXiv:2609.25562](https://arxiv.org/abs/2609.25562) | [2](https://www.semanticscholar.org/paper/75addd4e5ad5435b54415b23015348902290708a) | [![stars](https://img.shields.io/github/stars/xiaoqi-7/IndustrialVLA-Bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/xiaoqi-7/IndustrialVLA-Bench) |
| 🆕 **RoboDyna** | 2026 / NeurIPS | Sim | 20 dynamic tasks, 3,500 demos: manipulation under physically realistic dynamics | [NeurIPS 2026](https://neurips.cc/virtual/2026/166116) | — | — |
| 🆕 **RoboTwin-Phys** | 2026 | Sim | Do WAMs and VLAs understand the physical world? Physics-focused extension of RoboTwin | [arXiv:2609.26292](https://arxiv.org/abs/2609.26292) | [0](https://www.semanticscholar.org/paper/1361de39aba8db88d612688c00d286cc77c09cca) | — |
| 🆕 **ManiLadder** | 2026 / ICRA | Sim | ~114 tasks in 4 difficulty levels × 8 categories; rigid/articulated/deformable, grippers to dexterous hands, single/dual/mobile arms | [Project](https://maniladdericra.github.io) | — | — |
| 🆕 **IMBench** | 2026 / RSS-W | Sim | Intuitive manipulation: 35 tasks integrating physical reasoning with execution (contact-rich, tool use, multi-stage) | [arXiv:2607.15641](https://arxiv.org/abs/2607.15641) | — | — |
| 🆕 **PhysLadder** | 2026 | Sim + Real | 16 household contact-rich tasks in 3 cumulative levels (contact selection, force regulation, contact reconfiguration) | [arXiv:2610.34527](https://arxiv.org/abs/2610.34527) | — | — |

---

## 2. VLA Generalization, Robustness & Benchmark Auditing (VLA 泛化/鲁棒性/评测可信度)

LIBERO / SIMPLER 等分数接近饱和后，社区开始系统性地扰动、审计和"去记忆化"这些基准。

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **LIBERO-PRO** | 2025 | Sim | Shows LIBERO scores can reflect memorization; adds object/position/instruction/env perturbations | [arXiv:2510.03827](https://arxiv.org/abs/2510.03827) | [279](https://www.semanticscholar.org/paper/c3a0ea8b0563c735d768fca1eb5920fa85511ac7) | [![stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Zxy-MLlab/LIBERO-PRO) |
| **LIBERO-Plus** | 2025 | Sim | 7 perturbation axes (layout, camera, robot init state, language, light, background, sensor noise); camera & init-state shifts hurt most | [arXiv:2510.13626](https://arxiv.org/abs/2510.13626) | [413](https://www.semanticscholar.org/paper/dfa5ba43d6df553bb3a8cf3fc1cf2d1210cc10c3) | [![stars](https://img.shields.io/github/stars/sylvestf/LIBERO-plus?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/sylvestf/LIBERO-plus) |
| **VLA-RISK** | 2025 (ICLR'26 sub.) | Sim | Infeasible instructions + typographic visual attacks across object/action/space | [OpenReview](https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf) | — | — |
| **Eva-VLA** | 2025 | Sim | Worst-case physically-plausible perturbations (objects, textures) | [arXiv:2509.18953](https://arxiv.org/abs/2509.18953) | [25](https://www.semanticscholar.org/paper/9d1e0ecb00866a3cfc0568eee96a7b1fd820fbf8) | — |
| **VLA-Fool** | 2025 | Sim | Multimodal adversarial evaluation (ambiguity, negation, noise) on LIBERO | [arXiv:2511.16203](https://arxiv.org/abs/2511.16203) | [22](https://www.semanticscholar.org/paper/60a480a99b06802b6fe67ab6e3e47e28bd5ce2c7) | — |
| **AGNOSTOS** | 2025 | Sim (RLBench) | Zero-shot cross-task generalization: 18 seen / 23 unseen tasks | [arXiv:2505.15660](https://arxiv.org/abs/2505.15660) | [51](https://www.semanticscholar.org/paper/69ae66a0bcb49a2a74b29b6e79191f2d6680cf61) | — |
| **Experiences from Benchmarking VLAs** | 2025 | Sim + Real | ACT, OpenVLA-OFT, RDT-1B, π0 compared in sim and on ALOHA Mobile | [arXiv:2511.11298](https://arxiv.org/abs/2511.11298) | [7](https://www.semanticscholar.org/paper/a4f0e1811d190789ef72d8affc54895006a6b17d) | — |
| 🆕 **LIBERO-MAX** | 2026 | Sim | "Do robot policies adapt when the world changes?" — dynamic in-episode changes | [arXiv:2609.36518](https://arxiv.org/abs/2609.36518) | [3](https://www.semanticscholar.org/paper/937ae57cdbac21f58c5d7cb29bf13eca90fb1f4f) | — |
| 🆕 **STRONG-VLA** (benchmark part) | 2026 | Sim | 28 perturbation types (12 textual, 16 visual) on LIBERO | [arXiv:2604.10055](https://arxiv.org/abs/2604.10055) | [13](https://www.semanticscholar.org/paper/cd05bfb4c83656f0648f090dea8ec54a665a11a7) | — |
| 🆕 **One Word, Different Action** | 2026 | Real | Real-robot benchmark for language-conditioned embodied reasoning (minimal instruction changes ⇒ different actions) | [arXiv:2609.05260](https://arxiv.org/abs/2609.05260) | [0](https://www.semanticscholar.org/paper/c86b569bcb006a2c4b460b92d671a66c69876109) | — |
| 🆕 **Input-perturbation study** ("Is Success All You Need?") | 2026 | Sim | Effects of perturbations on VLA *behaviour*, not just success | [arXiv:2610.01351](https://arxiv.org/abs/2610.01351) | [0](https://www.semanticscholar.org/paper/24f7a3f26a43751bc3c04c13d98d6b6832a7d483) | — |
| 🆕 **Benchmark Bugs & Design Limitations** | 2026 | Audit | Audits 5 manipulation benchmarks: shortcut solvability, weak statistics, overfitting, demo-source dependence | [arXiv:2609.37771](https://arxiv.org/abs/2609.37771) | [0](https://www.semanticscholar.org/paper/7a7cbacab82fbdc2b798c3a9e2f86f37f3d31e4c) | — |
| 🆕 **LIBERO-X** | 2026 / RSS | Sim | Hierarchical difficulty levels + multi-label attributes; new diverse training set | [arXiv:2602.06556](https://arxiv.org/abs/2602.06556) | [30](https://www.semanticscholar.org/paper/a377f04f41cdefb7f9c61832e1f7d8a252102031) | — |
| 🆕 **Robust Skills, Brittle Grounding** | 2026 | Sim | Diagnoses restricted generalization: primitives reliable, instruction grounding brittle | [arXiv:2602.24143](https://arxiv.org/abs/2602.24143) | [4](https://www.semanticscholar.org/paper/22544b9de2e0127bf6889e48f7f93140767cf0fc) | — |

---

## 3. Long-Horizon, Memory & Compositional Tasks (长程/记忆/组合)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **CALVIN** | 2021 | Sim | Avg. successful chain length over 5-task sequences | [arXiv:2112.03227](https://arxiv.org/abs/2112.03227) | [935](https://www.semanticscholar.org/paper/4be02694125b71876552900a53c85c47a2a83614) | [![stars](https://img.shields.io/github/stars/mees/calvin?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mees/calvin) |
| **LIBERO-Long (LIBERO-10)** | 2023 | Sim | Long-horizon subset of LIBERO | [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) | [2,311](https://www.semanticscholar.org/paper/98cfd7b1b29453c4e82536f5afdc6ddc58bbb1b3) | [![stars](https://img.shields.io/github/stars/Lifelong-Robot-Learning/LIBERO?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| **LoHoRavens** | 2023 | Sim | Long-horizon reasoning tabletop tasks (counting, color, size) | [arXiv:2310.12020](https://arxiv.org/abs/2310.12020) | [29](https://www.semanticscholar.org/paper/dbde02978c8ed3f5fe586f63bab200f617225e0f) | — |
| **BEHAVIOR-1K** | 2024 | Sim | 1,000 household activities; minutes-long mobile-manipulation episodes (see §8) | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) | [216](https://www.semanticscholar.org/paper/66d7d369b00d4855455ce55dd7c9c1419da0c1d0) | [![stars](https://img.shields.io/github/stars/StanfordVL/BEHAVIOR-1K?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/StanfordVL/BEHAVIOR-1K) |
| **MIKASA / MIKASA-Robo** | 2025 | Sim (ManiSkill3) | Memory-intensive manipulation tasks for RL/VLA | [arXiv:2502.10550](https://arxiv.org/abs/2502.10550) | [59](https://www.semanticscholar.org/paper/1a9fbae6456b87408d97721e967438ae308b8edd) | [![stars](https://img.shields.io/github/stars/CognitiveAISystems/MIKASA-Robo?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/CognitiveAISystems/MIKASA-Robo) |
| **RoboCerebra** | 2025 | Sim | Long-horizon manipulation with high-level (System-2) planning evaluation | [arXiv:2506.06677](https://arxiv.org/abs/2506.06677) | [53](https://www.semanticscholar.org/paper/d2208698c391e7a17ca590433655cc1f70a2e530) | — |
| **MoMani** (EchoVLA) | 2025 | Sim | Long-horizon mobile manipulation requiring scene & episodic memory | [arXiv:2511.18112](https://arxiv.org/abs/2511.18112) | — | — |
| 🆕 **RoboMME** | 2026 / ICML Oral | Sim | 16 tasks; temporal/spatial/object/procedural memory; 14 memory-augmented π0.5 variants | [arXiv:2603.04639](https://arxiv.org/abs/2603.04639) | [91](https://www.semanticscholar.org/paper/f4831ae3f2ab6af571b014dca937257efcc2d614) | [![stars](https://img.shields.io/github/stars/RoboMME/robomme_benchmark?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboMME/robomme_benchmark) |
| 🆕 **ATOM-Bench** | 2026 | Real | Atomic skills & compositional generalization of manipulation policies | [arXiv:2606.16826](https://arxiv.org/abs/2606.16826) | [3](https://www.semanticscholar.org/paper/f13f6ee020ab87b398d16c59dfc356c6ba9a2bb9) | — |
| 🆕 **Graph-based harness for long-horizon eval** ("From Rollout to Reset") | 2026 | Real | Autonomous, resettable long-horizon evaluation | [arXiv:2609.19413](https://arxiv.org/abs/2609.19413) | [0](https://www.semanticscholar.org/paper/045f879bd7792be3734e310a964cd9e43b3cfd43) | — |

---

## 4. Bimanual, Dexterous & Grasping (双臂/灵巧手/抓取)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **Benchmarking In-Hand Manipulation** | 2020 / RA-L | Real | Physical protocol for in-hand manipulation (grasp change without support surface) | [arXiv:2001.03070](https://arxiv.org/abs/2001.03070) | [55](https://www.semanticscholar.org/paper/887aed6fb26eebb409f3a2d9aed6f7852de76eb1) | — |
| **EGAD!** | 2020 / RA-L | Sim + Real (3D-printable) | Evolved grasping analysis dataset of geometrically diverse objects | [arXiv:2003.01314](https://arxiv.org/abs/2003.01314) | [187](https://www.semanticscholar.org/paper/8e5dc995994fa154f94db19b92f262c48915b66b) | — |
| **GraspNet-1Billion** | 2020 / CVPR | Real data + analytic eval | 97K RGB-D images, 1B grasp poses; de-facto cluttered grasping benchmark | [CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) | [969](https://www.semanticscholar.org/paper/f76c9834a249a97ebcaf225a216c6076032af99c) | [![stars](https://img.shields.io/github/stars/graspnet/graspnetAPI?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/graspnet/graspnetAPI) |
| **ACRONYM** | 2021 / ICRA | Sim | 17.7M parallel-jaw grasps over 8,872 objects | [arXiv:2011.09584](https://arxiv.org/abs/2011.09584) | [285](https://www.semanticscholar.org/paper/ff0282b34d758a4aaad524ea554f6545852e3c68) | [![stars](https://img.shields.io/github/stars/NVlabs/acronym?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/NVlabs/acronym) |
| **Bi-DexHands** | 2022 / NeurIPS | Sim (Isaac Gym) | Bimanual Shadow-hand RL tasks | [arXiv:2206.08686](https://arxiv.org/abs/2206.08686) | [231](https://www.semanticscholar.org/paper/efa4fa4120e3efe5d7384a7b3428f886de9b6a29) | [![stars](https://img.shields.io/github/stars/PKU-MARL/DexterousHands?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/PKU-MARL/DexterousHands) |
| **DexArt** | 2023 / CVPR | Sim | Dexterous manipulation of articulated objects | [arXiv:2305.05706](https://arxiv.org/abs/2305.05706) | [123](https://www.semanticscholar.org/paper/9bdcf270bce9f680bad5385bc7920536d4fa0c53) | [![stars](https://img.shields.io/github/stars/Kami-code/dexart-release?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Kami-code/dexart-release) |
| **RoboTwin** | 2024 | Sim | Generative digital twins for dual-arm manipulation | [arXiv:2409.02920](https://arxiv.org/abs/2409.02920) | [110](https://www.semanticscholar.org/paper/750fd7b23d1009c360cdbce19dbf1cf6b3461f59) | [![stars](https://img.shields.io/github/stars/RoboTwin-Platform/RoboTwin?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboTwin-Platform/RoboTwin) |
| **DexGraspNet 2.0** | 2024 / CoRL | Sim + Real | Dexterous grasping in clutter: 1,319 objects, 8,270 scenes, 427M grasps | [arXiv:2410.23004](https://arxiv.org/abs/2410.23004) | [112](https://www.semanticscholar.org/paper/86e8d3a19a8a871d21d8561d2bc85449cf32d124) | — |
| 🔥 **RoboTwin 2.0** | 2025 / ICML'26 | Sim | 50 dual-arm tasks, 731 objects, 5 embodiments, 5-axis domain randomization, 100k+ trajectories | [arXiv:2506.18088](https://arxiv.org/abs/2506.18088) | [771](https://www.semanticscholar.org/paper/1002f84d1b487e49d3bc2d353dfb77e1495d3c58) | [![stars](https://img.shields.io/github/stars/RoboTwin-Platform/RoboTwin?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboTwin-Platform/RoboTwin) |
| 🆕 **DexToolBench** (SimToolReal) | 2026 | Real | Zero-shot dexterous tool use | [arXiv:2602.16863](https://arxiv.org/abs/2602.16863) | [43](https://www.semanticscholar.org/paper/9242b2482f96cdc183ad9a46906d85b39b092172) | [![stars](https://img.shields.io/github/stars/tylerlum/simtoolreal?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/tylerlum/simtoolreal) |
| 🆕 **POMDAR** — Benchmark of Dexterity for Anthropomorphic Hands | 2026 | Real (3D-printable) | Hardware dexterity benchmark over structured manipulation & grasping motions | [arXiv:2604.09294](https://arxiv.org/abs/2604.09294) | [5](https://www.semanticscholar.org/paper/de96ab30f8207528a519fd7acd778545688696f1) | — |
| 🆕 **HANDFUL-Bench** | 2026 | Sim (ManiSkill, LEAP Hand) | Multi-step, resource-aware grasping | [arXiv:2604.25126](https://arxiv.org/abs/2604.25126) | [4](https://www.semanticscholar.org/paper/ed733e73a5c8f29ab487877a24933a6e2364ae59) | — |
| 🆕 **DexJoCo** | 2026 | Sim (MuJoCo, Franka+Allegro) | 11 functional tasks: tool use, bimanual, long-horizon, reasoning | [arXiv:2605.16257](https://arxiv.org/abs/2605.16257) | [26](https://www.semanticscholar.org/paper/ebd04a9f482ddf084f578850f73ef4f7a9abc77a) | [![stars](https://img.shields.io/github/stars/brave-eai/dexjoco?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/brave-eai/dexjoco) |
| 🆕 **DexHoldem** | 2026 | Real (ShadowHand) | 1,470 demos across 14 Texas Hold'em manipulation primitives | [arXiv:2605.18727](https://arxiv.org/abs/2605.18727) | [1](https://www.semanticscholar.org/paper/74122b34e76b9a6c7c209da10b6da00890710910) | — |
| 🆕 **DexJoCo-X** | 2026 | Sim | Benchmarks action representations for multi-hand dexterity | [arXiv:2610.03278](https://arxiv.org/abs/2610.03278) | [0](https://www.semanticscholar.org/paper/64aa6d84a715e4cf564fc411699f196045fce7a5) | — |
| 🆕 **BiManiBench** | 2026 | QA | Bimanual coordination reasoning of MLLMs (30+ models) | [arXiv:2602.08392](https://arxiv.org/abs/2602.08392) | [2](https://www.semanticscholar.org/paper/d2d5392638e29c00c967f565dc62fb4f4208326d) | [![stars](https://img.shields.io/github/stars/stbibench/ST-BiBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/stbibench/ST-BiBench) |
| 🆕 **BiCoord** | 2026 | Sim | Long-horizon, tightly coupled bimanual coordination | [arXiv:2604.05831](https://arxiv.org/abs/2604.05831) | [9](https://www.semanticscholar.org/paper/5b6dd99a3563155a9e52e4e407c1de8c9c0bebb6) | — |
| 🆕 **DuoBench** | 2026 | Sim + Real | Reproducible dual-arm framework on FR3 Duo with task recipes & teleop data | [arXiv:2606.11901](https://arxiv.org/abs/2606.11901) | [3](https://www.semanticscholar.org/paper/f4526c4c43f0bf078111879af164606f2438a2e3) | — |
| 🆕 **DexVerse** | 2026 | Sim | Modular multi-task, multi-embodiment dexterous benchmark (19 tasks) | [arXiv:2607.08751](https://arxiv.org/abs/2607.08751) | [9](https://www.semanticscholar.org/paper/5f63e5d4daea0fe42cf0f94e0a43e34b609784fa) | — |
| 🆕 **BiDex-100** | 2026 | Sim | 106 bimanual dexterous tasks on 5 capability axes, 8,080 demos | [arXiv:2610.25459](https://arxiv.org/abs/2610.25459) | [1](https://www.semanticscholar.org/paper/f82da9fecbec596bd2e91ec029000cdea0b0d768) | [![stars](https://img.shields.io/github/stars/robbyant-research/BiDex-100?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robbyant-research/BiDex-100) |

---

## 5. Deformable, Tactile & Contact-Rich Manipulation (柔性物体/触觉/接触密集)

### 5.1 Deformable objects (cloth, rope, fluids, plasticine)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **SoftGym** | 2020 / CoRL | Sim (FleX) | Cloth, rope, fluid manipulation | [arXiv:2011.07215](https://arxiv.org/abs/2011.07215) | [311](https://www.semanticscholar.org/paper/10dd4db543a4689aff533427e0f7e83ba68c808f) | [![stars](https://img.shields.io/github/stars/Xingyu-Lin/softgym?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Xingyu-Lin/softgym) |
| **PlasticineLab** | 2021 / ICLR | Sim (differentiable) | Soft-body / plasticine manipulation | [arXiv:2104.03311](https://arxiv.org/abs/2104.03311) | [192](https://www.semanticscholar.org/paper/15c59c5cd0e393dda0b411995310510719d03a0f) | [![stars](https://img.shields.io/github/stars/hzaskywalker/PlasticineLab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/hzaskywalker/PlasticineLab) |
| **DaXBench** | 2022 / ICLR'23 | Sim (differentiable) | Deformable object manipulation with differentiable physics | [arXiv:2210.13066](https://arxiv.org/abs/2210.13066) | [39](https://www.semanticscholar.org/paper/fc715a1aac98fd5f5609e8fae16905ec3b85a057) | [![stars](https://img.shields.io/github/stars/AdaCompNUS/DaXBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/AdaCompNUS/DaXBench) |
| **GarmentLab** | 2024 / NeurIPS | Sim + Real | Unified garment manipulation simulation & benchmark | [arXiv:2411.01200](https://arxiv.org/abs/2411.01200) | [42](https://www.semanticscholar.org/paper/b1c48a0383423c8090fec89e332554eb3a84fc34) | [![stars](https://img.shields.io/github/stars/GarmentLab/GarmentLab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/GarmentLab/GarmentLab) |
| **ICRA Cloth Competition** | 2024–2026 | Real | In-air cloth unfolding grasp selection, live competition | [arXiv:2508.16749](https://arxiv.org/abs/2508.16749) | [6](https://www.semanticscholar.org/paper/99392bf63e3a6bb2388b0071f5a514f5b7ad33b8) | — |
| Real-to-Sim GS for soft bodies | 2025 | Real2Sim | Soft-body digital twins + Gaussian splatting for policy eval | [arXiv:2511.04665](https://arxiv.org/abs/2511.04665) | [51](https://www.semanticscholar.org/paper/0f83ff5175d849d413343b10ace0347c5c17f8d2) | — |
| **Dynamic Deformable Manipulation in 3D** | 2025 | Sim | Reduced-order dynamics benchmark for dynamic rope manipulation | [arXiv:2505.17434](https://arxiv.org/abs/2505.17434) | [4](https://www.semanticscholar.org/paper/185334e6a0fdf30988d1acfbe8ed7b520e78defa) | — |
| **MoDeSuite** | 2025 | Sim | Mobile manipulation of deformable objects (rods, cloth) | [arXiv:2507.21796](https://arxiv.org/abs/2507.21796) | [3](https://www.semanticscholar.org/paper/9391b25a99832676db5038b98887dacdbf0cf1b5) | — |
| 🆕 **RGBench** (Real Garment Benchmark) | 2026 / AAAI | Sim + Real | Grasping, flinging, folding with high-fidelity garment sim | [arXiv:2511.06434](https://arxiv.org/abs/2511.06434) | [7](https://www.semanticscholar.org/paper/2d6fd456451cad1f4e3851a3cb58a714a2824f62) | [![stars](https://img.shields.io/github/stars/hwk0809/RGBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/hwk0809/RGBench) |
| 🆕 **SoftVTBench** | 2026 | Sim | Visuo-tactile deformable manipulation with *safety* success metric | [arXiv:2607.04234](https://arxiv.org/abs/2607.04234) | [5](https://www.semanticscholar.org/paper/859630c6fb64a787830e75918689c0f96596f91f) | — |
| 🆕 **RoboFolDeX** | 2026 | Real | Physical-world long-horizon deformable manipulation (folding) | [arXiv:2609.10243](https://arxiv.org/abs/2609.10243) | [0](https://www.semanticscholar.org/paper/fbeca498bf60ba0c8b555e9f6f2a88175b6a65ca) | — |
| 🆕 **DLO-Lab** | 2026 | Sim (differentiable) | Deformable linear object manipulation with differentiable physics | [arXiv:2606.04206](https://arxiv.org/abs/2606.04206) | — | — |
| 🆕 **WireCraft** | 2026 / CoRL | Sim | Industrial DLO: connector insertion, clip routing, channel seating; RL / IL / VLA baselines | [arXiv:2606.18097](https://arxiv.org/abs/2606.18097) | — | — |

### 5.2 Tactile & contact-rich

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **NIST Assembly Task Boards** | 2017– | Real | Standardized peg/gear/connector/cable assembly boards | [NIST](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/assembly) | — | — |
| **Factory** | 2022 / RSS | Sim (Isaac Gym) | Contact-rich assembly (NIST Task Board 1 parts) with fast contact simulation | [arXiv:2205.03532](https://arxiv.org/abs/2205.03532) | [138](https://www.semanticscholar.org/paper/366ca45102a6111dbb256a908aa3f2bdb6a707dc) | — |
| **IndustReal** | 2023 / RSS | Sim → Real | Sim-to-real contact-rich assembly; 3D-printable IndustRealKit | [arXiv:2305.17110](https://arxiv.org/abs/2305.17110) | [137](https://www.semanticscholar.org/paper/6320003eb32b89d6817427479d5b594aa0c2f23f) | — |
| **Functional Manipulation Benchmark (FMB)** | 2024 / IJRR | Real | Reproducible insertion & assembly with 3D-printed objects | [arXiv:2401.08553](https://arxiv.org/abs/2401.08553) | [144](https://www.semanticscholar.org/paper/a83f2f4fed4f77be802618bae6c4cbb879bbe349) | — |
| **AutoMate** | 2024 / RSS | Sim + Real | 100 simulation-ready, 3D-printable assemblies | [arXiv:2407.08028](https://arxiv.org/abs/2407.08028) | [70](https://www.semanticscholar.org/paper/a36d59de1e8f55791c4667229b675034e7647e9b) | — |
| **ManiSkill-ViTac Challenge** | 2024–26 | Sim + Real | Tactile / visuo-tactile manipulation & sensor-design tracks | [arXiv:2411.12503](https://arxiv.org/abs/2411.12503) | [6](https://www.semanticscholar.org/paper/1148f3df1a14b2e6c41f6e78148e3481c8ce3d4e) | — |
| **ManiFeel** | 2025 | Sim + Real | Supervised visuotactile policy learning benchmark | [arXiv:2505.18472](https://arxiv.org/abs/2505.18472) | [41](https://www.semanticscholar.org/paper/a521740d5d3453564c165bd6d6f4927e0470b86e) | — |
| 🆕 **UniVTAC** | 2026 | Sim | 8 visuo-tactile tasks incl. hole/tube insertion; data gen + benchmark | [arXiv:2602.10093](https://arxiv.org/abs/2602.10093) | [46](https://www.semanticscholar.org/paper/ee6f6ab522882255a2c18ba08f0cfe082f7d346e) | — |
| 🆕 **RobOmni** | 2026 / ICRA | Sim (Isaac) | Omni-modal benchmark including tactile sensing, multi-embodiment | [The Robot Report](https://www.therobotreport.com/daimon-robotics-and-galbot-jointly-launches-robomni-for-benchmarking-tactile-perception-and-dexterous-manipulation/) | — | — |
| 🆕 **TacO** | 2026 | Real | Compares tactile sensor modalities (visual/acoustic/magnetic/resistive) | [arXiv:2605.21976](https://arxiv.org/abs/2605.21976) | [10](https://www.semanticscholar.org/paper/f84dfd941c93f8a9fcc32ccace0028c5f5204490) | — |
| 🆕 **SimpleTouch** | 2026 | Sim | Can VLAs master contact-rich manipulation without tactile pretraining? | [arXiv:2610.02784](https://arxiv.org/abs/2610.02784) | [2](https://www.semanticscholar.org/paper/8dccf0ca10b854fa4d84423b262116f0daa71910) | — |
| 🆕 **Tabero** | 2026 / ICML | Sim | Vision-tactile-language gentle manipulation with process-aware force metrics | [arXiv:2605.27886](https://arxiv.org/abs/2605.27886) | — | — |
| 🆕 **T-Rex** | 2026 | Real | 12 contact-rich tactile-reactive dexterous tasks | [arXiv:2606.17055](https://arxiv.org/abs/2606.17055) | — | — |
| 🆕 **TactiDex** | 2026 | Real | Tactile-guided dexterous benchmark targeting contact-level human-likeness | [arXiv:2607.09190](https://arxiv.org/abs/2607.09190) | — | — |

---

## 6. Real-World Manipulation Benchmarks & Evaluation Protocols (真实世界评测)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **YCB Object & Model Set** | 2015 | Real | Standard object set + protocols for grasping/manipulation | [arXiv:1502.03143](https://arxiv.org/abs/1502.03143) | [639](https://www.semanticscholar.org/paper/e0ce0e87edb08038c1432755909bb7270026ec50) | — |
| **RB2** | 2021 / NeurIPS D&B | Real (multi-lab) | Ranking-based benchmark: pouring, scooping, zipping, insertion; pooled cross-lab rankings | [arXiv:2203.08098](https://arxiv.org/abs/2203.08098) | [40](https://www.semanticscholar.org/paper/3450fbd7cea7be25a3dafc44bef0e6329d2a09ad) | — |
| **FurnitureBench** | 2023 / RSS | Real | Reproducible long-horizon furniture assembly | [arXiv:2305.12821](https://arxiv.org/abs/2305.12821) | [240](https://www.semanticscholar.org/paper/f80de0e8d343166f8e9b2cf844253d7b24b443d4) | [![stars](https://img.shields.io/github/stars/clvrai/furniture-bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/clvrai/furniture-bench) |
| **TOTO** (Train Offline, Test Online) | 2023 / ICRA | Real (remote) | Shared remote robot for offline-trained policies | [arXiv:2306.00942](https://arxiv.org/abs/2306.00942) | [68](https://www.semanticscholar.org/paper/431b2c3f4c6b2fe1ec4fead396286a48ed5edbbf) | [![stars](https://img.shields.io/github/stars/AGI-Labs/toto_benchmark?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/AGI-Labs/toto_benchmark) |
| **FMB** | 2024 | Real | See §5.2 | [arXiv:2401.08553](https://arxiv.org/abs/2401.08553) | [144](https://www.semanticscholar.org/paper/a83f2f4fed4f77be802618bae6c4cbb879bbe349) | — |
| 🔥 **AutoEval** | 2025 / CoRL | Real (autonomous) | 24/7 evaluation with learned success detection & auto-reset on WidowX/Bridge | [arXiv:2503.24278](https://arxiv.org/abs/2503.24278) | [79](https://www.semanticscholar.org/paper/aa324482b5acc4ea66ef642d1c60039b2d5c2822) | [![stars](https://img.shields.io/github/stars/zhouzypaul/auto_eval?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/zhouzypaul/auto_eval) |
| 🔥 **RoboArena** | 2025 / CoRL | Real (distributed) | Crowd-sourced, double-blind pairwise comparisons on DROID across 7 institutions | [arXiv:2506.18123](https://arxiv.org/abs/2506.18123) | [118](https://www.semanticscholar.org/paper/c03aab7c575d7c2218e4da7a12e13bfb03aa160a) | [![stars](https://img.shields.io/github/stars/robo-arena/roboarena?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robo-arena/roboarena) |
| 🔥 **RoboChallenge (Table30)** | 2025 | Real (online, 10 robots) | Large-scale online real-robot eval; 30 tabletop tasks on UR5/Franka/ALOHA/ARX-5; remote action-queue API | [arXiv:2510.17950](https://arxiv.org/abs/2510.17950) | [43](https://www.semanticscholar.org/paper/5c57d23a305f998c34528902e0305bef288a7c3d) | — |
| **Robot Policy Evaluation for Sim-to-Real Transfer** | 2025 | Sim + Real | Benchmarking perspective on sim-to-real policy evaluation | [arXiv:2508.11117](https://arxiv.org/abs/2508.11117) | [9](https://www.semanticscholar.org/paper/1d2f0e99cd09dedbd6567ab7ea93950bb2e79906) | — |
| 🆕 **VLA-REPLICA** | 2026 | Real | Low-cost reproducible real-world benchmark with ID/OOD protocols | [arXiv:2605.20774](https://arxiv.org/abs/2605.20774) | [5](https://www.semanticscholar.org/paper/d774514e1860f924785ca378d54c2e012d568927) | — |
| 🆕 **ATOM-Bench** | 2026 | Real | Atomic skills & compositional generalization | [arXiv:2606.16826](https://arxiv.org/abs/2606.16826) | [3](https://www.semanticscholar.org/paper/f13f6ee020ab87b398d16c59dfc356c6ba9a2bb9) | — |
| 🆕 **WatchAct** | 2026 | Sim + Real | Behavior-grounded manipulation: act on instructions that depend on an observed human video; 3,000 instances, 14 tasks (best 16% sim) | [arXiv:2606.26443](https://arxiv.org/abs/2606.26443) | [6](https://www.semanticscholar.org/paper/288257d6de03e30f6b58e4859a2c2c3fc2a6a5be) | — |
| 🆕🔥 **RoboColosseum** | 2026 | Real (distributed, in-the-wild) | 124 sites, 4 embodiments, 5,699 pairwise comparisons; rankings don't transfer across robots (Kendall W = 0.24) | [arXiv:2611.02497](https://arxiv.org/abs/2611.02497) | [0](https://www.semanticscholar.org/paper/0ba9df3a8a78062b5deb535c35444c4da3469df4) | [![stars](https://img.shields.io/github/stars/RoboColosseum/robocolosseum-client?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboColosseum/robocolosseum-client) |
| 🆕 **Embodied Agent Arena** | 2026 | Real/Sim | Are frontier VLM agents ready to be robot generalists? | [arXiv:2610.00854](https://arxiv.org/abs/2610.00854) | [1](https://www.semanticscholar.org/paper/d08167852ff6440a1077f103cbefde058b7acca8) | [![stars](https://img.shields.io/github/stars/embodied-agent-arena/embodied-agent-arena?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/embodied-agent-arena/embodied-agent-arena) |
| 🆕 **ManipulationNet** | 2026 | Real (distributed) | Global infrastructure with standardized hardware kits: Physical Skills track + Embodied Reasoning track | [arXiv:2603.04363](https://arxiv.org/abs/2603.04363) | — | — |
| 🆕 **HARP-Bench** | 2026 / CoRL | Real | Manipulation policies in workspaces shared with active humans | [arXiv:2611.11123](https://arxiv.org/abs/2611.11123) | — | — |
| 🆕 **Stochastic Challenges** | 2026 / CoRL | Real | Real-world manipulation benchmarking via stochastic, hidden-test-like challenges | [arXiv:2611.12804](https://arxiv.org/abs/2611.12804) | — | — |

---

## 7. Real-to-Sim, World-Model Evaluators & World-Model Benchmarks (Real2Sim/世界模型评测)

真实评测昂贵，2024 起出现两条替代路线：(a) 与真实场景对齐的仿真 (SIMPLER, Gaussian splat)；(b) 用视频世界模型直接"推演"策略。核心指标是与真实成功率的 Pearson 相关性和排序一致性 (MMRV)。本节也收录评测世界模型本身的基准 (EWMBench, WorldArena, World-in-World 等)。

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| 🔥 **SIMPLER** | 2024 / CoRL | Real2Sim | Visual-matching / variant-aggregation sims for Google Robot & WidowX; MMRV metric | [arXiv:2405.05941](https://arxiv.org/abs/2405.05941) | [688](https://www.semanticscholar.org/paper/202cc3fcea588cee37ffabcb0b5e145567109a66) | [![stars](https://img.shields.io/github/stars/simpler-env/SimplerEnv?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/simpler-env/SimplerEnv) |
| **PolaRiS** | 2025 | Real2Sim | Scalable real-to-sim reconstruction for generalist policy eval (DROID) | [arXiv:2512.16881](https://arxiv.org/abs/2512.16881) | [58](https://www.semanticscholar.org/paper/ab6d4ed806c35228dee0d81e774dda8f998fc94a) | — |
| **WorldEval** | 2025 | World model | Video model + latent policy actions as a real-world evaluator | [arXiv:2505.19017](https://arxiv.org/abs/2505.19017) | [82](https://www.semanticscholar.org/paper/0ac6e9af7417a3a33f2c6cee90fcf26284eff654) | — |
| **WorldGym** | 2025 / ICLR'26 | World model | Action-conditioned video model + VLM reward; preserves policy rankings | [arXiv:2506.00613](https://arxiv.org/abs/2506.00613) | [87](https://www.semanticscholar.org/paper/8dac59d54f3d268c3467c29fd8ac32d1770404a0) | — |
| **Ctrl-World** | 2025 | World model | Controllable world model for policy evaluation/improvement | [arXiv:2510.10125](https://arxiv.org/abs/2510.10125) | [226](https://www.semanticscholar.org/paper/1c35e2d08c749bea8029a4802270c10c1acbddc0) | — |
| **EWMBench** | 2025 / BMVC | World model (video) | Scene, motion & semantic quality of embodied world models (AgiBot-World data) | [arXiv:2505.09694](https://arxiv.org/abs/2505.09694) | [55](https://www.semanticscholar.org/paper/09c1d22bef7f7431f84f9f6c6764f9661b3c9194) | [![stars](https://img.shields.io/github/stars/AgibotTech/EWMBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/AgibotTech/EWMBench) |
| **WorldScore** | 2025 | World model (video) | Unified evaluation benchmark for world generation | [arXiv:2504.00983](https://arxiv.org/abs/2504.00983) | [183](https://www.semanticscholar.org/paper/d6a5f0339ddf541482b39ab4e25d670191ef1903) | [![stars](https://img.shields.io/github/stars/haoyi-duan/WorldScore?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/haoyi-duan/WorldScore) |
| **World-in-World** | 2025 / ICLR'26 Oral | World model (closed-loop) | Benchmarks world models by closed-loop task success; controllability > visual quality | [arXiv:2510.18135](https://arxiv.org/abs/2510.18135) | [68](https://www.semanticscholar.org/paper/55f7cb10e86c49ee02d6a1abda2919306bb2affa) | [![stars](https://img.shields.io/github/stars/World-In-World/world-in-world?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/World-In-World/world-in-world) |
| **Reliable & Scalable Policy Eval with Imperfect Simulators** | 2025 | Sim | Statistical framework for policy evaluation with imperfect sims | [arXiv:2510.04354](https://arxiv.org/abs/2510.04354) | [29](https://www.semanticscholar.org/paper/75eea17c71215435210f467ea63974a180d102cd) | — |
| **RobotArena ∞** | 2025 | Real2Sim | Scalable robot benchmarking via real-to-sim translation of videos | [arXiv:2510.23571](https://arxiv.org/abs/2510.23571) | [30](https://www.semanticscholar.org/paper/6b5cbef0ff7a62a2cee1fac8211774a37bd94ba2) | — |
| 🆕 **YUBI-Real2Sim** | 2026 | Real2Sim | 3DGS scene verification to decide which scenes give reliable policy comparisons | [arXiv:2610.17521](https://arxiv.org/abs/2610.17521) | [0](https://www.semanticscholar.org/paper/39808419052dc1b3fa5d902873b0d7a476ac932c) | — |
| 🆕 **dWorldEval** | 2026 | World model | Discrete diffusion world model predicting frames + progress | [arXiv:2604.22152](https://arxiv.org/abs/2604.22152) | [14](https://www.semanticscholar.org/paper/084a185a391c67d9eca9e8b7a36eef885ddac011) | — |
| 🆕 **WMBench** (GigaWorld-1) | 2026 | World model | Benchmarks 7 video world models as evaluators; long-horizon action-faithfulness matters most | [arXiv:2607.02642](https://arxiv.org/abs/2607.02642) | [17](https://www.semanticscholar.org/paper/ff84a80adb726c69a7e40e6b9c6da708f7cc0e2b) | [![stars](https://img.shields.io/github/stars/open-gigaai/giga-world-1?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/open-gigaai/giga-world-1) |
| 🆕 **RoboWorld** | 2026 | World model / Real2Sim | DROID-trained world model; reported high correlation with RoboArena | [arXiv:2607.01060](https://arxiv.org/abs/2607.01060) | [7](https://www.semanticscholar.org/paper/7c6b3f80cb6ae608c48c03e4d8327dde592f4278) | — |
| 🆕 **WorldArena** | 2026 | World model | Perception quality (16 metrics) + functional utility (data synthesis, policy eval, planning); leaderboard | [arXiv:2602.08971](https://arxiv.org/abs/2602.08971) | [88](https://www.semanticscholar.org/paper/6e5f625e2210bbfc26962659bce49cc45c38c055) | — |
| 🆕 **RoboTrustBench** | 2026 | World model (video) | Trustworthiness of video world models for manipulation | [arXiv:2606.01600](https://arxiv.org/abs/2606.01600) | [6](https://www.semanticscholar.org/paper/1aeb73dd57d813d9e8bd81f3631232e344a59d86) | — |
| 🆕 **RoboWM-Bench** | 2026 | World model | Converts generated videos into executable actions and validates them on robots | [arXiv:2604.19092](https://arxiv.org/abs/2604.19092) | — | — |
| 🆕 **What-If World** | 2026 | World model | Causal benchmark: 319 prompt pairs on nuScenes & DROID frames; best <52% | [arXiv:2605.27589](https://arxiv.org/abs/2605.27589) | — | — |
| 🆕 **H2R-Bench** | 2026 | World model (video) | Human-to-robot manipulation video generation in world models | [arXiv:2608.13049](https://arxiv.org/abs/2608.13049) | — | — |
| 🆕 **H2RBench** | 2026 / CoRL | Real2Sim (Isaac Lab) | Human-to-robot transfer from human videos; sim predicts real (r = 0.89) | [arXiv:2609.24778](https://arxiv.org/abs/2609.24778) | — | — |

---

## 8. Mobile Manipulation & Household Activities (移动操作/家庭任务)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **VirtualHome** | 2018 / CVPR | Sim | Household activity programs | [arXiv:1806.07012](https://arxiv.org/abs/1806.07012) | [57](https://www.semanticscholar.org/paper/eb556a873ee3daff1a0512aede8d398a9b262906) | [![stars](https://img.shields.io/github/stars/xavierpuigf/virtualhome?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/xavierpuigf/virtualhome) |
| 🔥 **ALFRED** | 2020 / CVPR | Sim (AI2-THOR) | Instruction following for household tasks | [arXiv:1912.01734](https://arxiv.org/abs/1912.01734) | [1,298](https://www.semanticscholar.org/paper/f4cf4246f3882aa6337e9c05d5675a3b8463a32e) | [![stars](https://img.shields.io/github/stars/askforalfred/alfred?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/askforalfred/alfred) |
| **Watch-And-Help** | 2020 / ICLR'21 | Sim (VirtualHome) | Social perception & human-AI collaboration in households | [arXiv:2010.09890](https://arxiv.org/abs/2010.09890) | [197](https://www.semanticscholar.org/paper/c562477737cc35e08d5a84aef01163ee4652d796) | [![stars](https://img.shields.io/github/stars/xavierpuigf/watch_and_help?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/xavierpuigf/watch_and_help) |
| **TEACh** | 2021 / AAAI'22 | Sim (AI2-THOR) | Dialog-based task completion | [arXiv:2110.00534](https://arxiv.org/abs/2110.00534) | [324](https://www.semanticscholar.org/paper/6ec6fa4e34200e13d80ee79b95d1cc6ec0f6b424) | [![stars](https://img.shields.io/github/stars/alexa/teach?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/alexa/teach) |
| **BEHAVIOR (-100)** | 2021 / CoRL | Sim (iGibson) | Everyday household activities defined in BDDL | [arXiv:2108.03332](https://arxiv.org/abs/2108.03332) | [297](https://www.semanticscholar.org/paper/c0c9f77cb097f2ce53feb91802bcfbae57fcc42f) | — |
| **Habitat 2.0 — Home Assistant Benchmark** | 2021 / NeurIPS | Sim | Rearrangement in interactive homes | [arXiv:2106.14405](https://arxiv.org/abs/2106.14405) | [868](https://www.semanticscholar.org/paper/4aa88c1406414cda3ce9cf76c8af0abaa8391760) | [![stars](https://img.shields.io/github/stars/facebookresearch/habitat-lab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/habitat-lab) |
| **AI2-THOR Rearrangement** | 2021 / CVPR | Sim | Visual room rearrangement (1- and 2-phase) | [arXiv:2103.16544](https://arxiv.org/abs/2103.16544) | [165](https://www.semanticscholar.org/paper/6500df35e30461d857103b3e3fa72b2913049a56) | [![stars](https://img.shields.io/github/stars/allenai/ai2thor-rearrangement?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/ai2thor-rearrangement) |
| **TDW Transport Challenge** | 2021 | Sim (ThreeDWorld) | Physically realistic transport with containers | [arXiv:2103.14025](https://arxiv.org/abs/2103.14025) | [99](https://www.semanticscholar.org/paper/69625c4aa0ade91a4b8758e720fb27926835e25a) | — |
| 🔥 **BEHAVIOR-1K** | 2022 / CoRL (arXiv 2024) | Sim (OmniGibson) | 1,000 activities, 50 scenes, realistic physics | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) | [216](https://www.semanticscholar.org/paper/66d7d369b00d4855455ce55dd7c9c1419da0c1d0) | [![stars](https://img.shields.io/github/stars/StanfordVL/BEHAVIOR-1K?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/StanfordVL/BEHAVIOR-1K) |
| **HomeRobot OVMM** | 2023 / CoRL | Sim + Real | Open-vocabulary mobile manipulation (pick anything, place anywhere) | [arXiv:2306.11565](https://arxiv.org/abs/2306.11565) | [180](https://www.semanticscholar.org/paper/3b0c02955e88f5862e61b560c7f70ba8cf235b1d) | [![stars](https://img.shields.io/github/stars/facebookresearch/home-robot?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/home-robot) |
| **ManiSkill-HAB** | 2024 / ICLR'25 | Sim (GPU) | Fast low-level home rearrangement | [arXiv:2412.13211](https://arxiv.org/abs/2412.13211) | [40](https://www.semanticscholar.org/paper/5c601530f798283890635475e80f57a5e5f69642) | [![stars](https://img.shields.io/github/stars/arth-shukla/mshab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/arth-shukla/mshab) |
| **BEHAVIOR Challenge 2025** | 2025 / NeurIPS | Sim | 50 tasks, 10k teleop demos (1,200+ h); winners ~26% q-score | [Website](https://behavior.stanford.edu/challenge/) | — | [![stars](https://img.shields.io/github/stars/StanfordVL/BEHAVIOR-1K?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/StanfordVL/BEHAVIOR-1K) |
| **M3Bench** | 2025 / RA-L | Sim | Whole-body motion generation for mobile manipulation: 30K rearrangement tasks, 119 scenes | [arXiv:2410.06678](https://arxiv.org/abs/2410.06678) | [5](https://www.semanticscholar.org/paper/31f4e4092fcd2a50d81eda10a300bd3efb648b84) | — |
| **Kitchen-R** (Mind and Motion Aligned) | 2025 | Sim (Isaac Sim) | Joint evaluation of task planning & low-level control; 500+ instructions | [arXiv:2508.15663](https://arxiv.org/abs/2508.15663) | [6](https://www.semanticscholar.org/paper/9286db3933c1115fe012c1341379482da398e4c8) | — |
| **LabUtopia** | 2025 / NeurIPS D&B | Sim | Scientific-lab embodied agents: high-fidelity sim + hierarchical benchmark | [arXiv:2505.22634](https://arxiv.org/abs/2505.22634) | — | — |
| 🆕 **EBench** | 2026 | Sim | Elemental diagnosis of generalist mobile-manipulation policies | [arXiv:2606.18239](https://arxiv.org/abs/2606.18239) | [15](https://www.semanticscholar.org/paper/5ded8e659bc333d0ad70bbf903f2d3dc071e8cae) | [![stars](https://img.shields.io/github/stars/InternRobotics/EBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/InternRobotics/EBench) |
| 🆕 **MobileManiBench** | 2026 | Sim (Isaac Sim) | 2 mobile platforms, 630 objects, 5 skills, ~300K trajectories | [arXiv:2602.05233](https://arxiv.org/abs/2602.05233) | [2](https://www.semanticscholar.org/paper/65fc69156afd5dd4d134b7a61a58cd5ab7fd4724) | — |
| 🆕 **RMMBench** | 2026 | Sim | Comprehensive benchmark for robotic mobile manipulation | [arXiv:2610.05414](https://arxiv.org/abs/2610.05414) | — | — |

---

## 9. Humanoid & Whole-Body Loco-Manipulation (人形/全身控制)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| 🔥 **HumanoidBench** | 2024 / RSS | Sim (MuJoCo) | 27 whole-body locomotion + manipulation tasks on Unitree H1 with hands | [arXiv:2403.10506](https://arxiv.org/abs/2403.10506) | [188](https://www.semanticscholar.org/paper/75850000ac9e056ce604c1bcd7631a3ae73d0458) | [![stars](https://img.shields.io/github/stars/carlosferrazza/humanoid-bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/carlosferrazza/humanoid-bench) |
| **RoboCasa (humanoid tracks)** / **BEHAVIOR (R1)** | 2024–25 | Sim | Household suites that support humanoid/wheeled-humanoid embodiments | see §1, §8 | — | — |
| **GRUtopia — GRBench** | 2024 | Sim (Isaac) | Humanoid Object Loco-Nav, Social Loco-Nav, Loco-Manipulation | [arXiv:2407.10943](https://arxiv.org/abs/2407.10943) | [87](https://www.semanticscholar.org/paper/b75f344d962b3b25b64c0c96a86244c4c3c6e490) | [![stars](https://img.shields.io/github/stars/InternRobotics/InternUtopia?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/InternRobotics/InternUtopia) |
| **LHM-Humanoid** | 2025 | Sim (Isaac Gym) | 350 long-horizon whole-body loco-manipulation scenes in clutter | [arXiv:2508.16943](https://arxiv.org/abs/2508.16943) | [0](https://www.semanticscholar.org/paper/3b9027dfc9fbddee4723e3c08e4f315be0612318) | — |
| **Switch-JustDance** | 2025 | Real | Benchmarks whole-body motion-tracking controllers via a console dance game | [arXiv:2511.17925](https://arxiv.org/abs/2511.17925) | [2](https://www.semanticscholar.org/paper/2e120f1a39caf2f6c85f09b757c7b45b804e373d) | — |
| 🆕 **SIMPLE** | 2026 | Sim (MuJoCo + IsaacSim render) | 60 whole-body tasks, 50 scenes, 1k+ assets; strong sim-real correlation | [arXiv:2606.08278](https://arxiv.org/abs/2606.08278) | [20](https://www.semanticscholar.org/paper/b7ebfd5d3e1185408ae956de2e186d2a34942a6f) | — |
| 🆕 **CoHuB** | 2026 / NeurIPS | Sim | Collaborative multi-humanoid loco-manipulation with dexterous hands | [arXiv:2609.34782](https://arxiv.org/abs/2609.34782) | [0](https://www.semanticscholar.org/paper/27d5eb96e05c1f45788aa6f9d4febe2e10bb8e8d) | — |
| 🆕 **OmniBench** (OmniClone) | 2026 | Sim + Real | Diagnostic benchmark for humanoid whole-body teleoperation: 6 skills × 18 difficulty/dynamics categories | [arXiv:2603.14327](https://arxiv.org/abs/2603.14327) | [12](https://www.semanticscholar.org/paper/736b833105efc0f434660505ee3fe8d6ebb22ef4) | — |
| 🆕 **Moving Through Clutter** | 2026 | Sim (VR) | Scene-aware humanoid locomotion in cluttered 3D environments | [arXiv:2603.05993](https://arxiv.org/abs/2603.05993) | [2](https://www.semanticscholar.org/paper/0422c5b5382609d6b7b402b1eb0facb74a23e72c) | — |
| 🆕 **HumanTracker** | 2026 | Sim | Human-aligned motion-tracking benchmark (~153 h mocap, 4 motion families) | [arXiv:2608.13555](https://arxiv.org/abs/2608.13555) | [1](https://www.semanticscholar.org/paper/6f286ba2a92bc554bbe19bdaa973dfd7e0c75ae6) | [![stars](https://img.shields.io/github/stars/GalaxyGeneralRobotics/HumanTracker?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/GalaxyGeneralRobotics/HumanTracker) |
| 🆕 **Fiatlux** | 2026 | Sim + Real | Long-horizon humanoid ladder climbing + light-bulb replacement | [arXiv:2609.38216](https://arxiv.org/abs/2609.38216) | — | — |

---

## 10. Legged Locomotion & Continuous Control (足式运动/连续控制)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| 🔥 **DeepMind Control Suite** | 2018 | Sim (MuJoCo) | Standard continuous-control RL tasks | [arXiv:1801.00690](https://arxiv.org/abs/1801.00690) | [1,596](https://www.semanticscholar.org/paper/a9a3ed69c94a3e1c08ef1f833d9199f57736238b) | [![stars](https://img.shields.io/github/stars/google-deepmind/dm_control?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-deepmind/dm_control) |
| **Gymnasium MuJoCo** (Ant, Humanoid, …) | 2016– | Sim | Canonical locomotion RL environments | [Gymnasium](https://gymnasium.farama.org/environments/mujoco/) | — | [![stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Farama-Foundation/Gymnasium) |
| **LocoMuJoCo** | 2023 | Sim | Imitation-learning locomotion benchmark with motion-capture data | [arXiv:2311.02496](https://arxiv.org/abs/2311.02496) | [58](https://www.semanticscholar.org/paper/74c89a7ecfebe9f33ba34a5ab3a190030e0df149) | [![stars](https://img.shields.io/github/stars/robfiras/loco-mujoco?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robfiras/loco-mujoco) |
| **Barkour** | 2023 / RSS | Real | Animal-level agility obstacle course for quadrupeds | [arXiv:2305.14654](https://arxiv.org/abs/2305.14654) | [99](https://www.semanticscholar.org/paper/dd50f8e92ba42f93a20463c4f4edf6a48340af4c) | — |
| 🆕 **Neverwhere Visual Parkour Benchmark Suite** | 2026 | Sim (MuJoCo, 3D-scanned) | 60+ visual parkour scenes from real campus scans | [arXiv:2609.16443](https://arxiv.org/abs/2609.16443) | [0](https://www.semanticscholar.org/paper/7e6de7aaa01bb1b8257482f91ff0993a6322b130) | — |

---

## 11. Embodied Navigation — VLN / ObjectNav / Social (具身导航)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| 🔥 **Room-to-Room (R2R)** | 2018 / CVPR | Sim (Matterport3D) | Vision-and-language navigation on discrete graphs | [arXiv:1711.07280](https://arxiv.org/abs/1711.07280) | [2,130](https://www.semanticscholar.org/paper/c37c23b12e00168833eccff8025a830ce27c5abc) | [![stars](https://img.shields.io/github/stars/peteanderson80/Matterport3DSimulator?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/peteanderson80/Matterport3DSimulator) |
| 🔥 **Habitat** (PointNav/ObjectNav) | 2019 / ICCV | Sim | Fast embodied simulator + navigation challenges | [arXiv:1904.01201](https://arxiv.org/abs/1904.01201) | [2,308](https://www.semanticscholar.org/paper/b4a35e548de27b6924e5f2ee41d37238a5c4a1d5) | [![stars](https://img.shields.io/github/stars/facebookresearch/habitat-lab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/habitat-lab) |
| **Touchdown** | 2019 / CVPR | Real imagery (Street View) | Outdoor VLN + spatial description resolution | [arXiv:1811.12354](https://arxiv.org/abs/1811.12354) | [507](https://www.semanticscholar.org/paper/f75f0750a00f6f85107985c70eca9c275b5e0962) | — |
| **CVDN** | 2019 / CoRL | Sim (Matterport3D) | Cooperative vision-and-dialog navigation | [arXiv:1907.04957](https://arxiv.org/abs/1907.04957) | [443](https://www.semanticscholar.org/paper/1b9ce27801c077433245ad0f9e43e3c38441cecd) | — |
| **REVERIE** | 2020 / CVPR | Sim | Remote object grounding via navigation | [arXiv:1904.10151](https://arxiv.org/abs/1904.10151) | [584](https://www.semanticscholar.org/paper/1bdd8f6d3900e6e7fe492ea21fcdd87f3d8c857f) | [![stars](https://img.shields.io/github/stars/YuankaiQi/REVERIE?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/YuankaiQi/REVERIE) |
| **VLN-CE** | 2020 / ECCV | Sim (Habitat) | VLN in continuous environments | [arXiv:2004.02857](https://arxiv.org/abs/2004.02857) | [770](https://www.semanticscholar.org/paper/c2496cead9423897cd37be77ddd6cf2f5d03f1c8) | [![stars](https://img.shields.io/github/stars/jacobkrantz/VLN-CE?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/jacobkrantz/VLN-CE) |
| **RxR** | 2020 / EMNLP | Sim | Multilingual, fine-grained VLN | [arXiv:2010.07954](https://arxiv.org/abs/2010.07954) | [691](https://www.semanticscholar.org/paper/5a94aaa3ad624608e46a75de49452a03de568a07) | [![stars](https://img.shields.io/github/stars/google-research-datasets/RxR?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-research-datasets/RxR) |
| **ObjectNav Revisited** | 2020 | Sim | Standardized ObjectNav evaluation | [arXiv:2006.13171](https://arxiv.org/abs/2006.13171) | [428](https://www.semanticscholar.org/paper/19c8c5a32cb0d77cd22ee1201e31306f0cd6100a) | — |
| **RoboTHOR** | 2020 / CVPR | Sim + Real | Sim-to-real ObjectNav with physical twin apartments | [arXiv:2004.06799](https://arxiv.org/abs/2004.06799) | [350](https://www.semanticscholar.org/paper/98789b46f7be983300a0e93e1c53bab56b36efd1) | [![stars](https://img.shields.io/github/stars/allenai/robothor-challenge?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/robothor-challenge) |
| **MultiON** | 2020 / NeurIPS | Sim (Habitat) | Multi-object sequential navigation | [arXiv:2012.03912](https://arxiv.org/abs/2012.03912) | [169](https://www.semanticscholar.org/paper/8981638669fd069c763626afb0af4c1ec637dad6) | [![stars](https://img.shields.io/github/stars/saimwani/multiON?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/saimwani/multiON) |
| **HM3D / HM3D-Sem** | 2021 / NeurIPS D&B | Sim | 1,000 real scanned buildings for nav | [arXiv:2109.08238](https://arxiv.org/abs/2109.08238) | [908](https://www.semanticscholar.org/paper/f46bce5b7dd78736133c1af1824ddb83c0ec2e55) | [![stars](https://img.shields.io/github/stars/facebookresearch/habitat-matterport3d-dataset?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/habitat-matterport3d-dataset) |
| **SocNavBench** | 2021 | Sim | Social navigation with real pedestrian data | [arXiv:2103.00047](https://arxiv.org/abs/2103.00047) | [111](https://www.semanticscholar.org/paper/282ffde21153473ea2b2cfe5723e86e9dcd09836) | [![stars](https://img.shields.io/github/stars/CMU-TBD/SocNavBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/CMU-TBD/SocNavBench) |
| **Habitat 3.0** (social nav / rearrange) | 2023 | Sim | Humanoid avatars + human-in-the-loop | [arXiv:2310.13724](https://arxiv.org/abs/2310.13724) | [359](https://www.semanticscholar.org/paper/ad4beeecbdfc7dd238eb55e2b19113f62096d95b) | [![stars](https://img.shields.io/github/stars/facebookresearch/habitat-lab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/habitat-lab) |
| **GOAT-Bench** | 2024 / CVPR | Sim | Multi-modal lifelong navigation (category / image / language goals) | [arXiv:2404.06609](https://arxiv.org/abs/2404.06609) | [170](https://www.semanticscholar.org/paper/a1cfddfd2fbd16a7aa62ebbded3674036e014731) | [![stars](https://img.shields.io/github/stars/Ram81/goat-bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Ram81/goat-bench) |
| **VLN-CE-Isaac** (NaVILA) | 2024 / RSS'25 | Sim (Isaac Sim) | VLN-CE for legged robots with physics | [arXiv:2412.04453](https://arxiv.org/abs/2412.04453) | — | — |
| **VL-LN** (Interactive Instance ObjectNav) | 2025 | Sim | Navigate *and* ask an oracle via dialog | [arXiv:2512.22342](https://arxiv.org/abs/2512.22342) | [6](https://www.semanticscholar.org/paper/bd0c90dc514e3e1cac229e0a693d0a16e8407019) | [![stars](https://img.shields.io/github/stars/InternRobotics/VL-LN?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/InternRobotics/VL-LN) |
| **VLNVerse** | 2025 | Sim (Isaac Sim) | Physics-bound agents, 263 environments, unified nav tasks | [arXiv:2512.19021](https://arxiv.org/abs/2512.19021) | [34](https://www.semanticscholar.org/paper/334fe9c27dc046fbc161562579b172b781754545) | — |
| **NavTrust** | 2025–26 | Sim | Trustworthiness of VLN & ObjectNav under corruptions | [arXiv:2603.19229](https://arxiv.org/abs/2603.19229) | [3](https://www.semanticscholar.org/paper/47c043bd18d7cdc950a57faa676061cfe93fa915) | — |
| **HA-VLN** | 2025 | Sim | Human-aware VLN with dynamic multi-human interactions | [arXiv:2503.14229](https://arxiv.org/abs/2503.14229) | [13](https://www.semanticscholar.org/paper/39832ae50dd6f6910d10f5015cade95500c1dd48) | — |
| **CitySeeker** | 2025 | QA / Sim | Urban embodied navigation driven by implicit human needs | [arXiv:2512.16755](https://arxiv.org/abs/2512.16755) | [9](https://www.semanticscholar.org/paper/dc16e7472ef3bb5502830edf00d334f90885597d) | — |
| **VLN-PE** | 2025 / ICCV | Sim (Isaac Sim) | Physically realistic VLN for humanoid, quadruped & wheeled robots | [arXiv:2507.13019](https://arxiv.org/abs/2507.13019) | — | — |
| **Follow-Bench** | 2025 | Sim | Motion planning for socially-aware robot person following | [arXiv:2509.10796](https://arxiv.org/abs/2509.10796) | — | — |
| 🆕 **NavVerse** | 2026 | Sim | Indoor-to-outdoor continuous navigation, 200 scenes, 10k episodes | [arXiv:2607.19695](https://arxiv.org/abs/2607.19695) | [4](https://www.semanticscholar.org/paper/89d912aef276d155a0bc0bd337fe5cc6a21a8da7) | — |
| 🆕 **OmniNavBench** | 2026 / RSS | Sim | PointNav + VLN + ObjectNav + human following + social nav in one episode; wheeled / quadruped / humanoid | [arXiv:2605.09441](https://arxiv.org/abs/2605.09441) | [4](https://www.semanticscholar.org/paper/d5032081baa931259a02d46ed1e1518e7f28fbf4) | — |
| 🆕 **GN-Bench** (GN0) | 2026 | Sim (3DGS) | 3DGS platform with dynamic avatars: instruction following, human following, goal nav | [arXiv:2606.03682](https://arxiv.org/abs/2606.03682) | [8](https://www.semanticscholar.org/paper/797b5845ba4d5ea8c72d406186cd07b693a77258) | — |
| 🆕 **CoT-VLNBench** | 2026 / AAAI | Real (Go2) | Chain-of-thought reasoning for quadruped VLN | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40980) | — | — |
| 🆕 **Follow-Bench 2.0** | 2026 / NeurIPS | Sim (Unreal) | End-to-end 3D socially-aware person following (perception + planning) | [NeurIPS 2026](https://neurips.cc/virtual/2026/poster/139022) | — | — |
| 🆕 **RescueBench** | 2026 | Sim | Search-and-rescue: exploration, rescue, memory-guided return, handoff | [arXiv:2606.01848](https://arxiv.org/abs/2606.01848) | — | [![stars](https://img.shields.io/github/stars/wukui-muc/RescueBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/wukui-muc/RescueBench) |

---

## 12. Aerial / UAV Embodied Benchmarks (无人机)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **AerialVLN** | 2023 / ICCV | Sim (AirSim/UE) | City-scale aerial VLN | [arXiv:2308.06735](https://arxiv.org/abs/2308.06735) | [233](https://www.semanticscholar.org/paper/25d8e3c541f996e366d8fa48cba248ca330e8a78) | [![stars](https://img.shields.io/github/stars/AirVLN/AirVLN?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/AirVLN/AirVLN) |
| **TravelUAV / OpenUAV** | 2024–25 | Sim | Realistic UAV VLN with continuous trajectories | [arXiv:2410.07087](https://arxiv.org/abs/2410.07087) | [159](https://www.semanticscholar.org/paper/ba414d17cb05f1b6fee6aae02fd20d99c2b5dff6) | [![stars](https://img.shields.io/github/stars/prince687028/TravelUAV?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/prince687028/TravelUAV) |
| **OpenFly** | 2025 | Sim | 100k trajectories, 18 scenes, multi-engine toolchain | [arXiv:2502.18041](https://arxiv.org/abs/2502.18041) | [76](https://www.semanticscholar.org/paper/4578312cad81f12bfb5e4ec93ce05782ff8caab8) | [![stars](https://img.shields.io/github/stars/SHAILAB-IPEC/OpenFly-Platform?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/SHAILAB-IPEC/OpenFly-Platform) |
| **UAV-ON** | 2025 | Sim | 11k open-world object-goal navigation tasks for UAVs | [arXiv:2508.00288](https://arxiv.org/abs/2508.00288) | [58](https://www.semanticscholar.org/paper/478aa3417dc58bf5c5bf2d57b700a0904048908b) | [![stars](https://img.shields.io/github/stars/iLearn-Lab/ACMMM25-UAV_ON?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/iLearn-Lab/ACMMM25-UAV_ON) |
| **Embodied4C** (drone track) | 2025 | Sim | Cross-embodiment (car / drone / arm) closed-loop reasoning | [arXiv:2512.18028](https://arxiv.org/abs/2512.18028) | [3](https://www.semanticscholar.org/paper/7fd7ec886aeb87c2f3031351023cefe3df9b34c5) | — |
| 🆕 **AIR-VLA** | 2026 | Sim (Isaac Sim) | VLA benchmark for aerial manipulation | [arXiv:2601.21602](https://arxiv.org/abs/2601.21602) | [9](https://www.semanticscholar.org/paper/540577dc434e1426151e249b0d48564d0f3e02fe) | [![stars](https://img.shields.io/github/stars/SpencerSon2001/AIR-VLA?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/SpencerSon2001/AIR-VLA) |
| **IndoorUAV** | 2026 / AAAI | Sim | UAV VLN in continuous indoor environments | [arXiv:2512.19024](https://arxiv.org/abs/2512.19024) | [28](https://www.semanticscholar.org/paper/c2a86a0369906b508894161941637e6a19373e4e) | — |

---

## 13. Embodied Reasoning, Spatial Understanding & Planning for (M)LLMs (具身推理/空间理解/规划)

评测"机器人大脑"——VLM/LLM 在具身场景下的感知、空间推理、指点、可供性、任务规划与失败分析。

### 13.1 Embodied QA, spatial reasoning & pointing

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **EQA** (Embodied Question Answering) | 2018 / CVPR | Sim | Navigate to answer questions in House3D | [arXiv:1711.11543](https://arxiv.org/abs/1711.11543) | [841](https://www.semanticscholar.org/paper/cc5ac1d3083b6663482ba6830dfa3bf65343286c) | — |
| **IQA** | 2018 / CVPR | Sim (AI2-THOR) | Interactive question answering | [arXiv:1712.03316](https://arxiv.org/abs/1712.03316) | [448](https://www.semanticscholar.org/paper/b0cd469a06fb2eae3a5cc0c860aa592f71b13f6d) | [![stars](https://img.shields.io/github/stars/danielgordon10/thor-iqa-cvpr-2018?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/danielgordon10/thor-iqa-cvpr-2018) |
| **RoboVQA** | 2023 / ICRA'24 | QA (video) | Long-horizon robot video QA across embodiments | [arXiv:2311.00899](https://arxiv.org/abs/2311.00899) | [190](https://www.semanticscholar.org/paper/0b47356f17aea1de66e39e5f182a105c96af8dd3) | — |
| **EgoPlan-Bench** | 2023 | QA (video) | Egocentric embodied planning for MLLMs | [arXiv:2312.06722](https://arxiv.org/abs/2312.06722) | [88](https://www.semanticscholar.org/paper/c60305f2a719c0ab5427a1f55304293ce18cd2e1) | [![stars](https://img.shields.io/github/stars/ChenYi99/EgoPlan?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/ChenYi99/EgoPlan) |
| **OpenEQA** | 2024 / CVPR | QA | Open-vocabulary embodied question answering (episodic memory & active) | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html) | [444](https://www.semanticscholar.org/paper/920731b589af90a5b79236f4939ac117bbb939f2) | [![stars](https://img.shields.io/github/stars/facebookresearch/open-eqa?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/open-eqa) |
| **VSI-Bench** ("Thinking in Space") | 2024 / CVPR'25 | QA (video) | Visual-spatial intelligence from egocentric video | [arXiv:2412.14171](https://arxiv.org/abs/2412.14171) | [938](https://www.semanticscholar.org/paper/376461a2c049f6fa51a4303853fdc672e4d07a0d) | [![stars](https://img.shields.io/github/stars/vision-x-nyu/thinking-in-space?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/vision-x-nyu/thinking-in-space) |
| **RoboPoint / Where2Place** | 2024 / CoRL | QA (pointing) | Spatial affordance prediction via points | [arXiv:2406.10721](https://arxiv.org/abs/2406.10721) | [362](https://www.semanticscholar.org/paper/715a93dbd51aaf7278e22c921af184a8eaffbd2e) | [![stars](https://img.shields.io/github/stars/wentaoyuan/RoboPoint?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/wentaoyuan/RoboPoint) |
| **EmbSpatial-Bench** | 2024 / ACL | QA | Embodied spatial understanding from egocentric views | [arXiv:2406.05756](https://arxiv.org/abs/2406.05756) | [150](https://www.semanticscholar.org/paper/be58f40bc78b10d09adaa92bfa48788662f276d3) | [![stars](https://img.shields.io/github/stars/mengfeidu/EmbSpatial-Bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mengfeidu/EmbSpatial-Bench) |
| **RoboSpatial** | 2024 / CVPR'25 | QA | Spatial understanding for robotics (2D/3D, ego / object / world frames) | [arXiv:2411.16537](https://arxiv.org/abs/2411.16537) | [236](https://www.semanticscholar.org/paper/ba8f1e36ca5f16a61d679f1ddf7b2cb3e298b354) | [![stars](https://img.shields.io/github/stars/NVlabs/RoboSpatial?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/NVlabs/RoboSpatial) |
| **Open6DOR** | 2024 / IROS | Sim | Open-instruction 6-DoF object rearrangement | [IROS 2024](https://pku-epic.github.io/Open6DOR) | [33](https://www.semanticscholar.org/paper/ad0d6f31a1b5a8556788a01bca4ce18035ddc2b9) | — |
| 🔥 **ERQA** (Gemini Robotics) | 2025 | QA | 400 MCQs: spatial, trajectory, action, state, multi-view reasoning | [arXiv:2503.20020](https://arxiv.org/abs/2503.20020) | [2](https://www.semanticscholar.org/paper/8382ce3c671d5451490bf618b37e3a663c2edade) | — |
| **RefSpatial-Bench** (RoboRefer) | 2025 / NeurIPS | QA (pointing) | Multi-step spatial referring | [arXiv:2506.04308](https://arxiv.org/abs/2506.04308) | [186](https://www.semanticscholar.org/paper/7311bbaa4624d393e9c6f26e1878f475315a5b28) | [![stars](https://img.shields.io/github/stars/Zhoues/RoboRefer?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Zhoues/RoboRefer) |
| **Point-It-Out** | 2025 | QA (pointing) | Multi-stage visual grounding for embodied reasoning | [arXiv:2509.25794](https://arxiv.org/abs/2509.25794) | [11](https://www.semanticscholar.org/paper/773624e23970f5c3821c109bd7716805875d5f33) | — |
| **RoboBench** | 2025 | QA | MLLM as embodied brain: instruction, perception, planning, affordance, failure analysis (14 capabilities) | [arXiv:2510.17801](https://arxiv.org/abs/2510.17801) | [33](https://www.semanticscholar.org/paper/d7726078436e4f0d0eb41e2f74cb7dcedaf7dbca) | [![stars](https://img.shields.io/github/stars/yulin-luo/RoboBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/yulin-luo/RoboBench) |
| **Embodied4C** | 2025 | QA + closed-loop | ~1.1K reasoning questions + 58 goal-directed tasks across 3 embodiments | [arXiv:2512.18028](https://arxiv.org/abs/2512.18028) | [3](https://www.semanticscholar.org/paper/7fd7ec886aeb87c2f3031351023cefe3df9b34c5) | — |
| **ERIQ** | 2025–26 | QA | 6K+ QA decoupling reasoning from action; correlates with VLA generalization | [arXiv:2512.24125](https://arxiv.org/abs/2512.24125) | [11](https://www.semanticscholar.org/paper/a27ed321a043cf5a2eb42a24bc059f80b37104f6) | [![stars](https://img.shields.io/github/stars/GenieReasoner/ERIQ?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/GenieReasoner/ERIQ) |
| **PhysBench** | 2025 / ICLR | QA (image+video) | Physical-world understanding of VLMs (properties, relations, dynamics) | [arXiv:2501.16411](https://arxiv.org/abs/2501.16411) | [196](https://www.semanticscholar.org/paper/5b92288640ff2288ea867e628f7d5f94065d90a9) | [![stars](https://img.shields.io/github/stars/physical-superintelligence-lab/PhysBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/physical-superintelligence-lab/PhysBench) |
| **Seeing Across Views** | 2025 | QA | Multi-view spatial reasoning of VLMs in robotic scenes | [arXiv:2510.19400](https://arxiv.org/abs/2510.19400) | [26](https://www.semanticscholar.org/paper/eb9eac541f79117fea4dbf9082e1a60e05792fc3) | — |
| **ShareRobot** (RoboBrain) | 2025 / CVPR | QA | Planning, affordance & trajectory annotations for robotic brains | [arXiv:2502.21257](https://arxiv.org/abs/2502.21257) | [228](https://www.semanticscholar.org/paper/c1fa31734bf75df4cdd1a6a04f63307d9817ed9a) | — |
| **ManipBench** | 2025 / CoRL | QA | 12.6K MCQs on low-level manipulation reasoning; correlates with real trials | [arXiv:2505.09698](https://arxiv.org/abs/2505.09698) | [38](https://www.semanticscholar.org/paper/f4efa7928f4bfd0bcea6e422ac682f2d5994842b) | — |
| **RoboFAC** | 2025 | QA (video) | Failure analysis & correction: 9,440 failed trajectories, 78K QA | [arXiv:2505.12224](https://arxiv.org/abs/2505.12224) | [52](https://www.semanticscholar.org/paper/9e2a4a6fe21c2e094c7d821f3d90894fbe2512a8) | [![stars](https://img.shields.io/github/stars/MINT-SJTU/RoboFAC?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/MINT-SJTU/RoboFAC) |
| **Robo2VLM** | 2025 | QA | VQA generated from real robot trajectories | [arXiv:2505.15517](https://arxiv.org/abs/2505.15517) | [61](https://www.semanticscholar.org/paper/1054deae404ac8c84307f570855b071769366fd0) | [![stars](https://img.shields.io/github/stars/KeplerC/robo2VLM?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/KeplerC/robo2VLM) |
| **PAC Bench** | 2025 | QA | Properties, affordances & constraints prerequisites for manipulation | [arXiv:2506.23725](https://arxiv.org/abs/2506.23725) | [4](https://www.semanticscholar.org/paper/fc87e617af92fb1b11cf1db76b584e95d6f25810) | — |
| **ENACT** | 2025 / ICLR'26 | QA | Embodied cognition as world modeling from egocentric interaction (8,972 QA) | [arXiv:2511.20937](https://arxiv.org/abs/2511.20937) | [20](https://www.semanticscholar.org/paper/25ffe148525262c728ee6a4e0eea8162b791a59b) | [![stars](https://img.shields.io/github/stars/mll-lab-nu/ENACT?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mll-lab-nu/ENACT) |
| **JRDB-Reasoning** | 2025 | QA | Difficulty-graded visual reasoning on real robot data | [arXiv:2508.10287](https://arxiv.org/abs/2508.10287) | — | — |
| 🆕 **Embodied3DBench** | 2026 | QA | Low-level 3D spatial intelligence, 21k+ QA + 1.3M training QA | [arXiv:2605.29074](https://arxiv.org/abs/2605.29074) | [6](https://www.semanticscholar.org/paper/43fb444f4d05a5014f22d8e1039c451142d22e18) | — |
| 🆕 **ERQA-Plus** | 2026 | QA | 1,766 diagnostic QA over 711 robot-centric images | [arXiv:2606.17639](https://arxiv.org/abs/2606.17639) | [2](https://www.semanticscholar.org/paper/2ff44298f01f508d69c2bfba1657d3d43110fee9) | — |
| 🆕 **ESI-Bench** | 2026 | Sim + QA | Embodied spatial intelligence that closes the perception-action loop | [arXiv:2605.18746](https://arxiv.org/abs/2605.18746) | [43](https://www.semanticscholar.org/paper/450ba46efa15dbee02e4184d5025d0ca40772e51) | [![stars](https://img.shields.io/github/stars/ESI-Bench/ESI-Bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/ESI-Bench/ESI-Bench) |
| 🆕 **RoboRewardBench** | 2026 | QA (video) | Human-verified progress/reward scores on 2,800 real episodes | [arXiv:2601.00675](https://arxiv.org/abs/2601.00675) | [85](https://www.semanticscholar.org/paper/48d78c3e3994f1f777295a786f3b0f19a1656d3b) | — |
| 🆕 **ManiRewardBench** (TOPReward) | 2026 | QA (video) | 130+ real manipulation tasks for progress estimation & success detection | [arXiv:2602.19313](https://arxiv.org/abs/2602.19313) | [48](https://www.semanticscholar.org/paper/5540aee4a1dec68b2b425b1ecc3096293a7f67b6) | [![stars](https://img.shields.io/github/stars/TOPReward/TOPReward?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/TOPReward/TOPReward) |
| 🆕 **EPIC-Bench** | 2026 | QA (grounding) | 6,661 instances / 23 tasks of fine-grained embodied visual grounding (targets, paths, affordances) | [arXiv:2605.17070](https://arxiv.org/abs/2605.17070) | — | — |
| 🆕 **JRDB-AVR** | 2026 / NeurIPS | QA (active) | Active visual reasoning: agent requests bounded observations; scored on answer + evidence | [arXiv:2609.35032](https://arxiv.org/abs/2609.35032) | — | [![stars](https://img.shields.io/github/stars/ControlNet/JRDB-AVR?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/ControlNet/JRDB-AVR) |
| 🆕 **Grounded in Time** | 2026 | QA (video) | Temporal grounding in robotic manipulation videos | [arXiv:2610.04255](https://arxiv.org/abs/2610.04255) | — | — |
| 🆕 **BEAKER** | 2026 / NeurIPS | QA | 1,000 expert QA for embodied brains in self-driving chemistry labs | [NeurIPS 2026](https://neurips.cc/virtual/2026/poster/139293) | — | — |

### 13.2 Task planning & agentic evaluation

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **ALFWorld** | 2020 / ICLR'21 | Text + Sim | Aligns text and embodied ALFRED tasks | [arXiv:2010.03768](https://arxiv.org/abs/2010.03768) | [1,594](https://www.semanticscholar.org/paper/398a0625e8707a0b41ac58eaec51e8feb87dd7cb) | [![stars](https://img.shields.io/github/stars/alfworld/alfworld?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/alfworld/alfworld) |
| **LoTa-Bench** | 2024 / ICLR | Sim | LLM task planners in AI2-THOR / VirtualHome | [arXiv:2402.08178](https://arxiv.org/abs/2402.08178) | [73](https://www.semanticscholar.org/paper/55f64d78fd7a2913b40f9708952ddad604650be1) | [![stars](https://img.shields.io/github/stars/lbaa2022/LLMTaskPlanning?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/lbaa2022/LLMTaskPlanning) |
| **Embodied Agent Interface** | 2024 / NeurIPS | Sim | Fine-grained LLM decision-making modules (goal interp., subgoals, actions, transitions) | [arXiv:2410.07166](https://arxiv.org/abs/2410.07166) | [225](https://www.semanticscholar.org/paper/0a65a3003accc425212d385dbc465f21289f8359) | [![stars](https://img.shields.io/github/stars/embodied-agent-interface/embodied-agent-interface?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/embodied-agent-interface/embodied-agent-interface) |
| **AHA** | 2024 | QA | Failure detection & reasoning for manipulation | [arXiv:2410.00371](https://arxiv.org/abs/2410.00371) | [233](https://www.semanticscholar.org/paper/076f35d58d26ac74c71e6e849dfffc0707aa8a6f) | — |
| **HAZARD** | 2024 / ICLR | Sim | Embodied decision making in dynamically changing environments (fire, flood, wind) | [arXiv:2401.12975](https://arxiv.org/abs/2401.12975) | [49](https://www.semanticscholar.org/paper/d408272835f6bde7343a46fd9fe858c65226d742) | [![stars](https://img.shields.io/github/stars/UMass-Embodied-AGI/HAZARD?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/UMass-Embodied-AGI/HAZARD) |
| **ET-Plan-Bench** | 2024 | Sim | Spatial & temporal constraints in embodied task planning | [arXiv:2410.14682](https://arxiv.org/abs/2410.14682) | [21](https://www.semanticscholar.org/paper/6b59f7365081988ef0b84c378a43a0bac3b9e71f) | — |
| 🔥 **EmbodiedBench** | 2025 / ICML | Sim | 1,128 tasks in 4 envs; MLLMs strong at high-level, weak at low-level | [arXiv:2502.09560](https://arxiv.org/abs/2502.09560) | [308](https://www.semanticscholar.org/paper/6fbb3ed823526ac050b610d353ea91a8515f7e69) | [![stars](https://img.shields.io/github/stars/EmbodiedBench/EmbodiedBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/EmbodiedBench/EmbodiedBench) |
| 🆕 **RobotWorld** | 2026 | Sim | Multimodal agents for robot use across tasks & embodiments | [arXiv:2610.10409](https://arxiv.org/abs/2610.10409) | [3](https://www.semanticscholar.org/paper/3c385a646c0e7056b0e2f5a207df96165b0cab12) | [![stars](https://img.shields.io/github/stars/robotworldai/robotworld?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/robotworldai/robotworld) |
| 🆕 **NativeEmbodied** | 2026 | Sim | VLM agents evaluated on low- and high-level skills jointly | [arXiv:2602.20687](https://arxiv.org/abs/2602.20687) | [3](https://www.semanticscholar.org/paper/fc110f0f2225e69666593d4b1abf39b116ff0970) | — |
| 🆕 **LongAct** | 2026 | Sim | Long-horizon household tasks from free-form instructions (best: 16% full success) | [arXiv:2605.14504](https://arxiv.org/abs/2605.14504) | [5](https://www.semanticscholar.org/paper/06e2955badfbaeba6420f57ef5a1d90e6a905284) | — |
| 🆕 **WorldLines** | 2026 | Sim | Long household traces for memory QA & embodied planning | [arXiv:2606.18847](https://arxiv.org/abs/2606.18847) | [8](https://www.semanticscholar.org/paper/c84d4d7bccbe1da49252b18fe14c9ca2d8d273b4) | — |

---

## 14. Multi-Agent & Human-Robot Collaboration (多智能体/人机协作)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **RoCoBench** | 2023 | Sim | LLM-dialectic multi-arm collaboration | [arXiv:2307.04738](https://arxiv.org/abs/2307.04738) | [334](https://www.semanticscholar.org/paper/c5d18dbb92d0cd5393baa1e69de33d6922ac3e57) | [![stars](https://img.shields.io/github/stars/MandiZhao/robot-collab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/MandiZhao/robot-collab) |
| **PARTNR** | 2024 / ICLR'25 | Sim (Habitat 3.0) | Human-robot planning & reasoning in household tasks | [arXiv:2411.00081](https://arxiv.org/abs/2411.00081) | [121](https://www.semanticscholar.org/paper/b55d10a262acec59d6655cd72746d690e1354d92) | [![stars](https://img.shields.io/github/stars/facebookresearch/partnr-planner?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/partnr-planner) |
| **VIKI-Bench** | 2025 | Sim | Hierarchical multi-robot cooperation (activation, planning, trajectory) | [arXiv:2506.09049](https://arxiv.org/abs/2506.09049) | [21](https://www.semanticscholar.org/paper/ed3522c9aa04927e43f89c588586e4f1075135a4) | [![stars](https://img.shields.io/github/stars/MARS-EAI/VIKI-R?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/MARS-EAI/VIKI-R) |
| **M4Bench** | 2025 / Frontiers | Sim | Multi-user, multi-robot, multi-goal, multi-device HRI | [Frontiers 2025](https://www.frontiersin.org/articles/10.3389/frobt.2025.1528754) | [10](https://www.semanticscholar.org/paper/287ae8cab9c2e5dccfa8e80e757faae0bc760458) | [![stars](https://img.shields.io/github/stars/arayabrain/m4bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/arayabrain/m4bench) |
| 🆕 **MARS Challenge** | 2026 | Sim | Multi-agent embodied planning + low-level manipulation | [arXiv:2601.18733](https://arxiv.org/abs/2601.18733) | [3](https://www.semanticscholar.org/paper/d2ee5b677819f38badfcb38422774c4ccb86f181) | — |
| 🆕 **CoHuB** | 2026 / NeurIPS | Sim | Multi-humanoid collaboration | [arXiv:2609.34782](https://arxiv.org/abs/2609.34782) | [0](https://www.semanticscholar.org/paper/27d5eb96e05c1f45788aa6f9d4febe2e10bb8e8d) | — |
| 🆕 **MACE-THOR** (EmboTeam) | 2026 | Sim (AI2-THOR) | 42 multi-robot household tasks over 8 layouts | [arXiv:2601.11063](https://arxiv.org/abs/2601.11063) | [3](https://www.semanticscholar.org/paper/e3dfc3084157527848ddcbbc1038685e78da28a2) | — |
| 🆕 **HRIBench** | 2026 | Sim | Interaction-centric human-robot collaboration | [arXiv:2607.13056](https://arxiv.org/abs/2607.13056) | — | — |

---

## 15. Safety, Security & Trustworthiness (安全/对抗/可信)

| Benchmark | Year | Type | Highlights | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|---|---|
| **BadRobot** | 2024 | Sim/Real | Jailbreaking LLM-based embodied agents | [arXiv:2407.20242](https://arxiv.org/abs/2407.20242) | [71](https://www.semanticscholar.org/paper/ca6e583ad978f0e6d80efe6197d5f44d31758e5a) | [![stars](https://img.shields.io/github/stars/Rookie143/BadRobot?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Rookie143/BadRobot) |
| **SafeAgentBench** | 2024 | Sim | Safe task planning for embodied LLM agents (hazardous tasks) | [arXiv:2412.13178](https://arxiv.org/abs/2412.13178) | [162](https://www.semanticscholar.org/paper/afe1ccdf90a31a7422e8150d008c4fe7d75f9745) | [![stars](https://img.shields.io/github/stars/shengyin1224/SafeAgentBench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/shengyin1224/SafeAgentBench) |
| **SafePlan-Bench** | 2025 | Sim | Safety-aware embodied task planning (2,027 cases) | [arXiv:2504.14650](https://arxiv.org/abs/2504.14650) | [42](https://www.semanticscholar.org/paper/88307eeb6d60a38f3fcc52a5683f29cfaf46d5ce) | — |
| **IS-Bench** | 2025 / AAAI'26 | Sim | Interactive safety of VLM agents: 161 scenarios, 388 risks; <40% safe completion | [arXiv:2506.16402](https://arxiv.org/abs/2506.16402) | [68](https://www.semanticscholar.org/paper/badfed277b0b65b5411f7ffcdb785bf7998a1edd) | [![stars](https://img.shields.io/github/stars/AI45Lab/IS-Bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/AI45Lab/IS-Bench) |
| **AgentSafe** | 2025 | Sim | Embodied agent safety on hazardous instructions | [arXiv:2506.14697](https://arxiv.org/abs/2506.14697) | [54](https://www.semanticscholar.org/paper/d3f33abbf46353989aa3c04e1918ad0148274f07) | — |
| 🆕 **EmbodiedGovBench** | 2026 | Sim | Governance, recovery & upgrade safety in embodied agent systems | [arXiv:2604.11174](https://arxiv.org/abs/2604.11174) | [3](https://www.semanticscholar.org/paper/3afb8112e94949ed3b34f5f830f01870d9f53643) | [![stars](https://img.shields.io/github/stars/s20sc/embodied-gov-bench?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/s20sc/embodied-gov-bench) |
| 🆕 **RoboJailBench** | 2026 | Sim | Adversarial attacks & defenses on embodied robotic agents | [arXiv:2605.19328](https://arxiv.org/abs/2605.19328) | [3](https://www.semanticscholar.org/paper/e399f914c9c1c62f62ed2ac4bc058042a69c6dba) | — |
| 🆕 **SafeVLA-Bench** | 2026 | Sim | The success–safety gap in VLA models | [arXiv:2606.00773](https://arxiv.org/abs/2606.00773) | [18](https://www.semanticscholar.org/paper/83c66c30a5ebb518dc20fa1d3b1123787219640d) | — |
| 🆕 **SABER** | 2026 | Sim | Black-box minimal instruction-edit attacks on 6 VLAs (LIBERO) | [arXiv:2603.24935](https://arxiv.org/abs/2603.24935) | [3](https://www.semanticscholar.org/paper/305c8600362bed45260d9375b386e129f7b7a427) | [![stars](https://img.shields.io/github/stars/wuxiyang1996/SABER?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/wuxiyang1996/SABER) |
| 🆕 **Linguistic adversarial instructions for VLAs** | 2026 | Sim | Success drops from 93% → 6% under searched instructions | [arXiv:2604.05595](https://arxiv.org/abs/2604.05595) | [2](https://www.semanticscholar.org/paper/c76df655a1ead59b9496c7e4a38722fd62cedb7a) | — |
| 🆕 **ForesightSafety-VLA** | 2026 | Sim | Safety-oriented VLA evaluation (tracked in Awesome-Robotics-Manipulation) | [arXiv:2606.27079](https://arxiv.org/abs/2606.27079) | [5](https://www.semanticscholar.org/paper/53f45137f187170d5577350de3495bf989ed7353) | — |
| 🆕 **ManiGuard** | 2026 | Sim | Safety-oriented VLA evaluation (tracked in Awesome-Robotics-Manipulation) | [arXiv:2608.17386](https://arxiv.org/abs/2608.17386) | [2](https://www.semanticscholar.org/paper/a62c6985ec2f497cd86c026cada91b7cfcaf4be0) | — |
| 🆕 **SPOC** | 2026 | Sim | Safety-aware planning under partial observability & physical constraints | [arXiv:2602.21595](https://arxiv.org/abs/2602.21595) | [1](https://www.semanticscholar.org/paper/ad8c2ae335c0b05d46f1e7f608c545317bf82a95) | [![stars](https://img.shields.io/github/stars/khm159/SPOC?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/khm159/SPOC) |
| 🆕 **RT-Safe** | 2026 | Sim | Agent safety in real-time embodied environments | [arXiv:2610.09294](https://arxiv.org/abs/2610.09294) | [0](https://www.semanticscholar.org/paper/380ff678e1f7e2bda26f6a72ab1a5155662773c4) | — |
| 🆕 **LIBERO-Safety** | 2026 | Sim | Physical & semantic safety of VLA models on LIBERO-based tasks | [arXiv:2606.23686](https://arxiv.org/abs/2606.23686) | [18](https://www.semanticscholar.org/paper/94e4a38dc67d4ee71c465e109ec7a7a7bae25d26) | — |
| 🆕 **LABSHIELD** | 2026 | QA + planning | Safety-critical reasoning & planning in scientific laboratories | [arXiv:2603.11987](https://arxiv.org/abs/2603.11987) | — | — |
| See also §2 (VLA-RISK, Eva-VLA, VLA-Fool) and §5 (SoftVTBench safety metric) | | | | |  |  |  |  |

---

## 16. Simulation Platforms & Unified Benchmark Frameworks (仿真平台/统一框架)

Not benchmarks per se, but most benchmarks above are built on them.

| Platform | Notes | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|
| MuJoCo / MuJoCo Playground | Physics engine behind Meta-World, robosuite, DMC, HumanoidBench | [GitHub](https://github.com/google-deepmind/mujoco) | — | [![stars](https://img.shields.io/github/stars/google-deepmind/mujoco?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-deepmind/mujoco) |
| SAPIEN / ManiSkill3 | GPU-parallel sim + rendering | [arXiv:2410.00425](https://arxiv.org/abs/2410.00425) | [400](https://www.semanticscholar.org/paper/6116f4ce4ec1b3cda988e7b289eda6daea75f479) | [![stars](https://img.shields.io/github/stars/mani-skill/ManiSkill?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/mani-skill/ManiSkill) |
| NVIDIA Isaac Sim / Isaac Lab | RTX rendering, used by ARNOLD, VLNVerse, RobOmni | [GitHub](https://github.com/isaac-sim/IsaacLab) | — | [![stars](https://img.shields.io/github/stars/isaac-sim/IsaacLab?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/isaac-sim/IsaacLab) |
| AI2-THOR / ProcTHOR | Interactive houses (ALFRED, TEACh) | [arXiv:2206.06994](https://arxiv.org/abs/2206.06994) | [653](https://www.semanticscholar.org/paper/d7bca917b753b996074203cc77ba45935b7c62d7) | [![stars](https://img.shields.io/github/stars/allenai/ai2thor?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/ai2thor) |
| Habitat-Sim / Habitat-Lab | Navigation & rearrangement | [arXiv:1904.01201](https://arxiv.org/abs/1904.01201) | [2,308](https://www.semanticscholar.org/paper/b4a35e548de27b6924e5f2ee41d37238a5c4a1d5) | [![stars](https://img.shields.io/github/stars/facebookresearch/habitat-sim?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/facebookresearch/habitat-sim) |
| iGibson / OmniGibson | BEHAVIOR series | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) | [216](https://www.semanticscholar.org/paper/66d7d369b00d4855455ce55dd7c9c1419da0c1d0) | [![stars](https://img.shields.io/github/stars/StanfordVL/BEHAVIOR-1K?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/StanfordVL/BEHAVIOR-1K) |
| RoboVerse | Unified platform/dataset/benchmark across simulators | [arXiv:2504.18904](https://arxiv.org/abs/2504.18904) | [87](https://www.semanticscholar.org/paper/36b457f4a4cbdb4c74a2713e06ea9b5753122b41) | [![stars](https://img.shields.io/github/stars/RoboVerseOrg/RoboVerse?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/RoboVerseOrg/RoboVerse) |
| GRUtopia / InternUtopia | City-scale embodied sim for general robots | [arXiv:2407.10943](https://arxiv.org/abs/2407.10943) | [87](https://www.semanticscholar.org/paper/b75f344d962b3b25b64c0c96a86244c4c3c6e490) | [![stars](https://img.shields.io/github/stars/InternRobotics/InternUtopia?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/InternRobotics/InternUtopia) |
| Genesis | Generative, multi-physics simulator | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) | — | [![stars](https://img.shields.io/github/stars/Genesis-Embodied-AI/genesis-world?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/Genesis-Embodied-AI/genesis-world) |
| **vla-eval** (Ai2 VLA Evaluation Harness) | One harness + leaderboard over 18 sim benchmarks (LIBERO, SimplerEnv, CALVIN, RoboTwin …) | [arXiv:2603.13966](https://arxiv.org/abs/2603.13966) | [11](https://www.semanticscholar.org/paper/cb522f52c35d3e97ef569366699e2c8ba51c394b) | [![stars](https://img.shields.io/github/stars/allenai/vla-evaluation-harness?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/allenai/vla-evaluation-harness) |

---

## 17. Companion Datasets Often Used for Evaluation (常用于评测的数据集)

| Dataset | Notes | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|
| Open X-Embodiment | 1M+ trajectories, 22 embodiments; RT-X evaluation | [arXiv:2310.08864](https://arxiv.org/abs/2310.08864) | [1,302](https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f) | [![stars](https://img.shields.io/github/stars/google-deepmind/open_x_embodiment?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/google-deepmind/open_x_embodiment) |
| BridgeData V2 | WidowX; basis of SIMPLER-WidowX & AutoEval | [arXiv:2308.12952](https://arxiv.org/abs/2308.12952) | [1,009](https://www.semanticscholar.org/paper/6a375be82efc01ec4ed73334655935a56ba82d38) | [![stars](https://img.shields.io/github/stars/rail-berkeley/bridge_data_v2?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/rail-berkeley/bridge_data_v2) |
| DROID | 76k Franka trajectories in the wild; basis of RoboArena & PolaRiS | [arXiv:2403.12945](https://arxiv.org/abs/2403.12945) | [1,379](https://www.semanticscholar.org/paper/ee5070fe52fd17da9a89d3f342fb07cc9ae51afe) | [![stars](https://img.shields.io/github/stars/droid-dataset/droid?style=flat&label=%E2%AD%90&color=f5c518)](https://github.com/droid-dataset/droid) |
| Deform360 / HapTile | 2026 visuotactile deformable / contact-rich datasets | — | — | — |

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

| Survey | Year | Paper | Citations | GitHub ⭐ |
|---|---|---|---|---|
| Datasets, Benchmarks and Data Engines for VLA models | 2026 | [arXiv:2604.23001](https://arxiv.org/abs/2604.23001) | [11](https://www.semanticscholar.org/paper/243c6e23d30f0da8f4a0579de16850f4a82eb2f2) | — |
| Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends | 2026 | [arXiv:2606.12207](https://arxiv.org/abs/2606.12207) | [1](https://www.semanticscholar.org/paper/726c1e916a7131d022cc8f2ec411991d0b0253cd) | — |
| Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence | 2026 | [arXiv:2609.29669](https://arxiv.org/abs/2609.29669) | [0](https://www.semanticscholar.org/paper/35b110d3136a97f2510a66708b9e68d784ec9e79) | — |
| Evaluation-centric VLA survey (582 papers, minimum reporting protocols) | 2026 | [Preprints.org](https://www.preprints.org/manuscript/202606.1149) | — | — |
| VLA Models for UAVs and Bimanual Manipulation: A Review | 2026 | [arXiv:2607.06706](https://arxiv.org/abs/2607.06706) | [1](https://www.semanticscholar.org/paper/d6a19545bf6f5e9598046fc26a07635195b65452) | — |

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

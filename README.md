# Awesome Robo Benchmarks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **categorized** list of benchmarks for robot learning and embodied AI — from classic simulation suites (Meta-World, RLBench, Habitat) to the newest VLA, humanoid, world-model-as-evaluator and safety benchmarks of 2025–2026.
>
> 一个系统整理、**分门别类**的机器人 / 具身智能 Benchmark 合集：覆盖经典仿真基准、真实世界评测、VLA 泛化与鲁棒性、人形机器人、导航、具身推理 (VLM)、世界模型评测、安全等方向，并持续追踪 2025–2026 的最新论文。

**Last updated: 2026-11** · Entries marked 🆕 appeared in 2026 · 🔥 = widely used / de-facto standard · `Sim` / `Real` / `Real2Sim` / `QA` = evaluation modality

> [!NOTE]
> Links point to arXiv abstracts where the ID was verified; where it was not, the link is an arXiv title search so it never points to the wrong paper. PRs that fix links or add benchmarks are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Contents

- [Taxonomy at a Glance (分类总览)](#taxonomy-at-a-glance-分类总览)
- [1. Tabletop & General Manipulation — Simulation (桌面/通用操作·仿真)](#1-tabletop--general-manipulation--simulation-桌面通用操作仿真)
- [2. VLA Generalization, Robustness & Benchmark Auditing (VLA 泛化/鲁棒性/评测可信度)](#2-vla-generalization-robustness--benchmark-auditing-vla-泛化鲁棒性评测可信度)
- [3. Long-Horizon, Memory & Compositional Tasks (长程/记忆/组合)](#3-long-horizon-memory--compositional-tasks-长程记忆组合)
- [4. Bimanual & Dexterous Manipulation (双臂/灵巧手)](#4-bimanual--dexterous-manipulation-双臂灵巧手)
- [5. Deformable, Tactile & Contact-Rich Manipulation (柔性物体/触觉/接触密集)](#5-deformable-tactile--contact-rich-manipulation-柔性物体触觉接触密集)
- [6. Real-World Manipulation Benchmarks & Evaluation Protocols (真实世界评测)](#6-real-world-manipulation-benchmarks--evaluation-protocols-真实世界评测)
- [7. Real-to-Sim & World-Model-Based Policy Evaluation (Real2Sim/世界模型评测)](#7-real-to-sim--world-model-based-policy-evaluation-real2sim世界模型评测)
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

| Benchmark | Year / Venue | Type | Highlights | Link |
|---|---|---|---|---|
| 🔥 **Meta-World** | 2019 / CoRL | Sim (MuJoCo) | 50 Sawyer tasks; multi-task & meta-RL (ML1/ML10/ML45, MT10/MT50) | [arXiv:1910.10897](https://arxiv.org/abs/1910.10897) |
| 🔥 **RLBench** | 2019 / RA-L | Sim (CoppeliaSim) | 100 hand-designed tasks with demos; standard for keyframe/3D policies (PerAct, RVT) | [arXiv:1909.12271](https://arxiv.org/abs/1909.12271) |
| **robosuite** | 2020 | Sim (MuJoCo) | Modular framework + standardized tasks; basis of RoboMimic, LIBERO, RoboCasa | [arXiv:2009.12293](https://arxiv.org/abs/2009.12293) |
| **Ravens / Transporter tasks** | 2020 / CoRL | Sim (PyBullet) | Rearrangement tasks (stacking, kitting, rope, etc.) | [arXiv:2010.14406](https://arxiv.org/abs/2010.14406) |
| 🔥 **CALVIN** | 2021 / RA-L | Sim (PyBullet) | Language-conditioned long-horizon chains (5 tasks in a row), ABC→D split | [arXiv:2112.03227](https://arxiv.org/abs/2112.03227) |
| **ManiSkill / ManiSkill2 / ManiSkill3** | 2021–2024 | Sim (SAPIEN) | Generalizable manipulation; v3 is GPU-parallel with rendering at scale | [v1](https://arxiv.org/abs/2107.14483) · [v2](https://arxiv.org/abs/2302.04659) · [v3](https://arxiv.org/abs/2410.00425) |
| **VIMA-Bench** | 2022 / ICML'23 | Sim | Multimodal (text+image) prompts; 4-level generalization protocol | [arXiv:2210.03094](https://arxiv.org/abs/2210.03094) |
| **ARNOLD** | 2023 / ICCV | Sim (Isaac) | Language-grounded continuous-state tasks (e.g., "fill cup 50%") | [arXiv:2304.04321](https://arxiv.org/abs/2304.04321) |
| 🔥 **LIBERO** | 2023 / NeurIPS D&B | Sim (robosuite) | 130 tasks; Spatial / Object / Goal / Long suites; lifelong learning; the most-reported VLA benchmark | [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) |
| **The Colosseum** | 2024 / RSS | Sim (RLBench) | 20 tasks × 14 perturbation axes for generalization | [arXiv:2402.08191](https://arxiv.org/abs/2402.08191) |
| 🔥 **RoboCasa** | 2024 / RSS | Sim (robosuite) | Large-scale kitchen scenes, 100 tasks, generative assets | [arXiv:2406.02523](https://arxiv.org/abs/2406.02523) |
| **GemBench** | 2024 | Sim (RLBench) | 4 levels of generalization: placement, rigid objects, articulated, long-horizon | [arXiv search](https://arxiv.org/search/?query=Towards+Generalizable+Vision-Language+Robotic+Manipulation+GemBench&searchtype=all) |
| **VLABench** | 2024 / ICCV'25 | Sim | 100 task categories, 2000+ objects; language-conditioned manipulation with commonsense/reasoning | [arXiv:2412.18194](https://arxiv.org/abs/2412.18194) |
| **RoboEval** | 2025 | Sim | Structured, scalable evaluation with behavioral & outcome metrics beyond success rate | [arXiv:2507.00435](https://arxiv.org/abs/2507.00435) |
| 🆕 **RoboSPA** | 2026 | Sim | Can VLAs go beyond simple scenes and short-horizon tasks? Cluttered, longer tasks | [arXiv:2609.05324](https://arxiv.org/abs/2609.05324) |
| 🆕 **ManipArena** | 2026 | Sim/Real | Arena-style manipulation evaluation (tracked in Awesome-Robotics-Manipulation) | [arXiv search](https://arxiv.org/search/?query=ManipArena&searchtype=all) |
| 🆕 **InstructMove** | 2026 | — | Instruction-following manipulation benchmark | [arXiv search](https://arxiv.org/search/?query=InstructMove&searchtype=all) |

---

## 2. VLA Generalization, Robustness & Benchmark Auditing (VLA 泛化/鲁棒性/评测可信度)

LIBERO / SIMPLER 等分数接近饱和后，社区开始系统性地扰动、审计和"去记忆化"这些基准。

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **LIBERO-PRO** | 2025 | Sim | Shows LIBERO scores can reflect memorization; adds object/position/instruction/env perturbations | [arXiv:2510.03827](https://arxiv.org/abs/2510.03827) |
| **LIBERO-Plus** | 2025 | Sim | 7 perturbation axes (layout, camera, robot init state, language, light, background, sensor noise); camera & init-state shifts hurt most | [arXiv:2510.13626](https://arxiv.org/abs/2510.13626) |
| 🆕 **LIBERO-MAX** | 2026 | Sim | "Do robot policies adapt when the world changes?" — dynamic in-episode changes | [arXiv:2609.36518](https://arxiv.org/abs/2609.36518) |
| 🆕 **STRONG-VLA** (benchmark part) | 2026 | Sim | 28 perturbation types (12 textual, 16 visual) on LIBERO | [arXiv:2604.10055](https://arxiv.org/abs/2604.10055) |
| 🆕 **One Word, Different Action** | 2026 | Real | Real-robot benchmark for language-conditioned embodied reasoning (minimal instruction changes ⇒ different actions) | [arXiv:2609.05260](https://arxiv.org/abs/2609.05260) |
| 🆕 **Input-perturbation study** ("Is Success All You Need?") | 2026 | Sim | Effects of perturbations on VLA *behaviour*, not just success | [arXiv:2610.01351](https://arxiv.org/abs/2610.01351) |
| 🆕 **Benchmark Bugs & Design Limitations** | 2026 | Audit | Audits 5 manipulation benchmarks: shortcut solvability, weak statistics, overfitting, demo-source dependence | [arXiv:2609.37771](https://arxiv.org/abs/2609.37771) |
| **VLA-RISK** | 2025 (ICLR'26 sub.) | Sim | Infeasible instructions + typographic visual attacks across object/action/space | [OpenReview](https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf) |
| **Eva-VLA** | 2025 | Sim | Worst-case physically-plausible perturbations (objects, textures) | [arXiv search](https://arxiv.org/search/?query=Eva-VLA&searchtype=all) |
| **VLA-Fool** | 2025 | Sim | Multimodal adversarial evaluation (ambiguity, negation, noise) on LIBERO | [arXiv search](https://arxiv.org/search/?query=When+Alignment+Fails+Multimodal+Adversarial+Attacks+Vision-Language-Action&searchtype=all) |

---

## 3. Long-Horizon, Memory & Compositional Tasks (长程/记忆/组合)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **CALVIN** | 2021 | Sim | Avg. successful chain length over 5-task sequences | [arXiv:2112.03227](https://arxiv.org/abs/2112.03227) |
| **LIBERO-Long (LIBERO-10)** | 2023 | Sim | Long-horizon subset of LIBERO | [arXiv:2306.03310](https://arxiv.org/abs/2306.03310) |
| **LoHoRavens** | 2023 | Sim | Long-horizon reasoning tabletop tasks (counting, color, size) | [arXiv search](https://arxiv.org/search/?query=LoHoRavens&searchtype=all) |
| **MIKASA / MIKASA-Robo** | 2025 | Sim (ManiSkill3) | Memory-intensive manipulation tasks for RL/VLA | [arXiv search](https://arxiv.org/search/?query=MIKASA+memory+intensive+skills+robotic+manipulation&searchtype=all) |
| **RoboCerebra** | 2025 | Sim | Long-horizon manipulation with high-level (System-2) planning evaluation | [arXiv search](https://arxiv.org/search/?query=RoboCerebra&searchtype=all) |
| 🆕 **RoboMME** | 2026 / ICML Oral | Sim | 16 tasks; temporal/spatial/object/procedural memory; 14 memory-augmented π0.5 variants | [arXiv:2603.04639](https://arxiv.org/abs/2603.04639) |
| 🆕 **ATOM-Bench** | 2026 | Real | Atomic skills & compositional generalization of manipulation policies | [arXiv:2606.16826](https://arxiv.org/abs/2606.16826) |
| 🆕 **Graph-based harness for long-horizon eval** ("From Rollout to Reset") | 2026 | Real | Autonomous, resettable long-horizon evaluation | [arXiv:2609.19413](https://arxiv.org/abs/2609.19413) |
| **BEHAVIOR-1K** | 2024 | Sim | 1,000 household activities; minutes-long mobile-manipulation episodes (see §8) | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) |

---

## 4. Bimanual & Dexterous Manipulation (双臂/灵巧手)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **Bi-DexHands** | 2022 / NeurIPS | Sim (Isaac Gym) | Bimanual Shadow-hand RL tasks | [arXiv:2206.08686](https://arxiv.org/abs/2206.08686) |
| **DexArt** | 2023 / CVPR | Sim | Dexterous manipulation of articulated objects | [arXiv:2305.05706](https://arxiv.org/abs/2305.05706) |
| **RoboTwin** | 2024 | Sim | Generative digital twins for dual-arm manipulation | [arXiv:2409.02920](https://arxiv.org/abs/2409.02920) |
| 🔥 **RoboTwin 2.0** | 2025 / ICML'26 | Sim | 50 dual-arm tasks, 731 objects, 5 embodiments, 5-axis domain randomization, 100k+ trajectories | [arXiv:2506.18088](https://arxiv.org/abs/2506.18088) |
| 🆕 **DexToolBench** (SimToolReal) | 2026 | Real | Zero-shot dexterous tool use | [arXiv:2602.16863](https://arxiv.org/abs/2602.16863) |
| 🆕 **POMDAR** — Benchmark of Dexterity for Anthropomorphic Hands | 2026 | Real (3D-printable) | Hardware dexterity benchmark over structured manipulation & grasping motions | [arXiv:2604.09294](https://arxiv.org/abs/2604.09294) |
| 🆕 **HANDFUL-Bench** | 2026 | Sim (ManiSkill, LEAP Hand) | Multi-step, resource-aware grasping | [arXiv search](https://arxiv.org/search/?query=HANDFUL-Bench&searchtype=all) |
| 🆕 **DexJoCo** | 2026 | Sim (MuJoCo, Franka+Allegro) | 11 functional tasks: tool use, bimanual, long-horizon, reasoning | [arXiv:2605.16257](https://arxiv.org/abs/2605.16257) |
| 🆕 **DexHoldem** | 2026 | Real (ShadowHand) | 1,470 demos across 14 Texas Hold'em manipulation primitives | [arXiv search](https://arxiv.org/search/?query=DexHoldem&searchtype=all) |
| 🆕 **DexJoCo-X** | 2026 | Sim | Benchmarks action representations for multi-hand dexterity | [arXiv:2610.03278](https://arxiv.org/abs/2610.03278) |

---

## 5. Deformable, Tactile & Contact-Rich Manipulation (柔性物体/触觉/接触密集)

### 5.1 Deformable objects (cloth, rope, fluids, plasticine)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **SoftGym** | 2020 / CoRL | Sim (FleX) | Cloth, rope, fluid manipulation | [arXiv:2011.07215](https://arxiv.org/abs/2011.07215) |
| **PlasticineLab** | 2021 / ICLR | Sim (differentiable) | Soft-body / plasticine manipulation | [arXiv:2104.03311](https://arxiv.org/abs/2104.03311) |
| **DaXBench** | 2022 / ICLR'23 | Sim (differentiable) | Deformable object manipulation with differentiable physics | [arXiv:2210.13066](https://arxiv.org/abs/2210.13066) |
| **GarmentLab** | 2024 / NeurIPS | Sim + Real | Unified garment manipulation simulation & benchmark | [arXiv:2411.01200](https://arxiv.org/abs/2411.01200) |
| **ICRA Cloth Competition** | 2024–2026 | Real | In-air cloth unfolding grasp selection, live competition | [arXiv search](https://arxiv.org/search/?query=ICRA+cloth+competition&searchtype=all) |
| 🆕 **RGBench** (Real Garment Benchmark) | 2026 / AAAI | Sim + Real | Grasping, flinging, folding with high-fidelity garment sim | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38894) |
| 🆕 **SoftVTBench** | 2026 | Sim | Visuo-tactile deformable manipulation with *safety* success metric | [arXiv search](https://arxiv.org/search/?query=SoftVTBench&searchtype=all) |
| 🆕 **RoboFolDeX** | 2026 | Real | Physical-world long-horizon deformable manipulation (folding) | [arXiv:2609.10243](https://arxiv.org/abs/2609.10243) |
| Real-to-Sim GS for soft bodies | 2025 | Real2Sim | Soft-body digital twins + Gaussian splatting for policy eval | [arXiv:2511.04665](https://arxiv.org/abs/2511.04665) |

### 5.2 Tactile & contact-rich

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **NIST Assembly Task Boards** | 2017– | Real | Standardized peg/gear/connector/cable assembly boards | [NIST](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/assembly) |
| **Functional Manipulation Benchmark (FMB)** | 2024 / IJRR | Real | Reproducible insertion & assembly with 3D-printed objects | [arXiv:2401.08553](https://arxiv.org/abs/2401.08553) |
| **ManiFeel** | 2025 | Sim + Real | Supervised visuotactile policy learning benchmark | [arXiv:2505.18472](https://arxiv.org/abs/2505.18472) |
| 🆕 **UniVTAC** | 2026 | Sim | 8 visuo-tactile tasks incl. hole/tube insertion; data gen + benchmark | [arXiv:2602.10093](https://arxiv.org/abs/2602.10093) |
| 🆕 **RobOmni** | 2026 / ICRA | Sim (Isaac) | Omni-modal benchmark including tactile sensing, multi-embodiment | [The Robot Report](https://www.therobotreport.com/daimon-robotics-and-galbot-jointly-launches-robomni-for-benchmarking-tactile-perception-and-dexterous-manipulation/) |
| 🆕 **TacO** | 2026 | Real | Compares tactile sensor modalities (visual/acoustic/magnetic/resistive) | [arXiv search](https://arxiv.org/search/?query=TacO+Benchmarking+Tactile+Sensors+Object+Manipulation&searchtype=all) |
| 🆕 **SimpleTouch** | 2026 | Sim | Can VLAs master contact-rich manipulation without tactile pretraining? | [arXiv:2610.02784](https://arxiv.org/abs/2610.02784) |

---

## 6. Real-World Manipulation Benchmarks & Evaluation Protocols (真实世界评测)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **YCB Object & Model Set** | 2015 | Real | Standard object set + protocols for grasping/manipulation | [arXiv:1502.03143](https://arxiv.org/abs/1502.03143) |
| **FurnitureBench** | 2023 / RSS | Real | Reproducible long-horizon furniture assembly | [arXiv:2305.12821](https://arxiv.org/abs/2305.12821) |
| **TOTO** (Train Offline, Test Online) | 2023 / ICRA | Real (remote) | Shared remote robot for offline-trained policies | [arXiv:2306.00942](https://arxiv.org/abs/2306.00942) |
| **FMB** | 2024 | Real | See §5.2 | [arXiv:2401.08553](https://arxiv.org/abs/2401.08553) |
| 🔥 **AutoEval** | 2025 / CoRL | Real (autonomous) | 24/7 evaluation with learned success detection & auto-reset on WidowX/Bridge | [arXiv:2503.24278](https://arxiv.org/abs/2503.24278) |
| 🔥 **RoboArena** | 2025 / CoRL | Real (distributed) | Crowd-sourced, double-blind pairwise comparisons on DROID across 7 institutions | [arXiv:2506.18123](https://arxiv.org/abs/2506.18123) |
| 🆕 **VLA-REPLICA** | 2026 | Real | Low-cost reproducible real-world benchmark with ID/OOD protocols | [arXiv:2605.20774](https://arxiv.org/abs/2605.20774) |
| 🆕 **ATOM-Bench** | 2026 | Real | Atomic skills & compositional generalization | [arXiv:2606.16826](https://arxiv.org/abs/2606.16826) |
| 🆕 **WatchAct** | 2026 | — | Tracked in Awesome-Robotics-Manipulation (2026-06) | [arXiv search](https://arxiv.org/search/?query=WatchAct&searchtype=all) |

---

## 7. Real-to-Sim & World-Model-Based Policy Evaluation (Real2Sim/世界模型评测)

真实评测昂贵，2024 起出现两条替代路线：(a) 与真实场景对齐的仿真 (SIMPLER, Gaussian splat)；(b) 用视频世界模型直接"推演"策略。核心指标是与真实成功率的 Pearson 相关性和排序一致性 (MMRV)。

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| 🔥 **SIMPLER** | 2024 / CoRL | Real2Sim | Visual-matching / variant-aggregation sims for Google Robot & WidowX; MMRV metric | [arXiv:2405.05941](https://arxiv.org/abs/2405.05941) |
| **PolaRiS** | 2025 | Real2Sim | Scalable real-to-sim reconstruction for generalist policy eval (DROID) | [arXiv:2512.16881](https://arxiv.org/abs/2512.16881) |
| 🆕 **YUBI-Real2Sim** | 2026 | Real2Sim | 3DGS scene verification to decide which scenes give reliable policy comparisons | [arXiv:2610.17521](https://arxiv.org/abs/2610.17521) |
| **WorldEval** | 2025 | World model | Video model + latent policy actions as a real-world evaluator | [arXiv search](https://arxiv.org/search/?query=WorldEval+World+Model+as+Real-World+Robot+Policies+Evaluator&searchtype=all) |
| **WorldGym** | 2025 / ICLR'26 | World model | Action-conditioned video model + VLM reward; preserves policy rankings | [arXiv:2506.00613](https://arxiv.org/abs/2506.00613) |
| **Ctrl-World** | 2025 | World model | Controllable world model for policy evaluation/improvement | [arXiv search](https://arxiv.org/search/?query=Ctrl-World+controllable+generative+world+model+robot+manipulation&searchtype=all) |
| 🆕 **dWorldEval** | 2026 | World model | Discrete diffusion world model predicting frames + progress | [arXiv:2604.22152](https://arxiv.org/abs/2604.22152) |
| 🆕 **WMBench** (GigaWorld-1) | 2026 | World model | Benchmarks 7 video world models as evaluators; long-horizon action-faithfulness matters most | [arXiv search](https://arxiv.org/search/?query=GigaWorld-1&searchtype=all) |
| 🆕 **RoboWorld** | 2026 | World model / Real2Sim | DROID-trained world model; reported high correlation with RoboArena | [arXiv:2607.01060](https://arxiv.org/abs/2607.01060) |

---

## 8. Mobile Manipulation & Household Activities (移动操作/家庭任务)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **VirtualHome** | 2018 / CVPR | Sim | Household activity programs | [arXiv:1806.07012](https://arxiv.org/abs/1806.07012) |
| 🔥 **ALFRED** | 2020 / CVPR | Sim (AI2-THOR) | Instruction following for household tasks | [arXiv:1912.01734](https://arxiv.org/abs/1912.01734) |
| **TEACh** | 2021 / AAAI'22 | Sim (AI2-THOR) | Dialog-based task completion | [arXiv:2110.00534](https://arxiv.org/abs/2110.00534) |
| **BEHAVIOR (-100)** | 2021 / CoRL | Sim (iGibson) | Everyday household activities defined in BDDL | [arXiv:2108.03332](https://arxiv.org/abs/2108.03332) |
| **Habitat 2.0 — Home Assistant Benchmark** | 2021 / NeurIPS | Sim | Rearrangement in interactive homes | [arXiv:2106.14405](https://arxiv.org/abs/2106.14405) |
| **HomeRobot OVMM** | 2023 / CoRL | Sim + Real | Open-vocabulary mobile manipulation (pick anything, place anywhere) | [arXiv:2306.11565](https://arxiv.org/abs/2306.11565) |
| 🔥 **BEHAVIOR-1K** | 2022 / CoRL (arXiv 2024) | Sim (OmniGibson) | 1,000 activities, 50 scenes, realistic physics | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) |
| **ManiSkill-HAB** | 2024 / ICLR'25 | Sim (GPU) | Fast low-level home rearrangement | [arXiv search](https://arxiv.org/search/?query=ManiSkill-HAB&searchtype=all) |
| **BEHAVIOR Challenge 2025** | 2025 / NeurIPS | Sim | 50 tasks, 10k teleop demos (1,200+ h); winners ~26% q-score | [Website](https://behavior.stanford.edu/challenge/) |
| 🆕 **EBench** | 2026 | Sim | Elemental diagnosis of generalist mobile-manipulation policies | [arXiv:2606.18239](https://arxiv.org/abs/2606.18239) |

---

## 9. Humanoid & Whole-Body Loco-Manipulation (人形/全身控制)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| 🔥 **HumanoidBench** | 2024 / RSS | Sim (MuJoCo) | 27 whole-body locomotion + manipulation tasks on Unitree H1 with hands | [arXiv:2403.10506](https://arxiv.org/abs/2403.10506) |
| **LHM-Humanoid** | 2025 | Sim (Isaac Gym) | 350 long-horizon whole-body loco-manipulation scenes in clutter | [arXiv:2508.16943](https://arxiv.org/abs/2508.16943) |
| 🆕 **SIMPLE** | 2026 | Sim (MuJoCo + IsaacSim render) | 60 whole-body tasks, 50 scenes, 1k+ assets; strong sim-real correlation | [arXiv:2606.08278](https://arxiv.org/abs/2606.08278) |
| 🆕 **CoHuB** | 2026 / NeurIPS | Sim | Collaborative multi-humanoid loco-manipulation with dexterous hands | [arXiv:2609.34782](https://arxiv.org/abs/2609.34782) |
| **RoboCasa (humanoid tracks)** / **BEHAVIOR (R1)** | 2024–25 | Sim | Household suites that support humanoid/wheeled-humanoid embodiments | see §1, §8 |

---

## 10. Legged Locomotion & Continuous Control (足式运动/连续控制)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| 🔥 **DeepMind Control Suite** | 2018 | Sim (MuJoCo) | Standard continuous-control RL tasks | [arXiv:1801.00690](https://arxiv.org/abs/1801.00690) |
| **Gymnasium MuJoCo** (Ant, Humanoid, …) | 2016– | Sim | Canonical locomotion RL environments | [Gymnasium](https://gymnasium.farama.org/environments/mujoco/) |
| **LocoMuJoCo** | 2023 | Sim | Imitation-learning locomotion benchmark with motion-capture data | [arXiv:2311.02496](https://arxiv.org/abs/2311.02496) |
| **Barkour** | 2023 / RSS | Real | Animal-level agility obstacle course for quadrupeds | [arXiv:2305.14654](https://arxiv.org/abs/2305.14654) |
| 🆕 **Neverwhere Visual Parkour Benchmark Suite** | 2026 | Sim (MuJoCo, 3D-scanned) | 60+ visual parkour scenes from real campus scans | [arXiv:2609.16443](https://arxiv.org/abs/2609.16443) |

---

## 11. Embodied Navigation — VLN / ObjectNav / Social (具身导航)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| 🔥 **Room-to-Room (R2R)** | 2018 / CVPR | Sim (Matterport3D) | Vision-and-language navigation on discrete graphs | [arXiv:1711.07280](https://arxiv.org/abs/1711.07280) |
| 🔥 **Habitat** (PointNav/ObjectNav) | 2019 / ICCV | Sim | Fast embodied simulator + navigation challenges | [arXiv:1904.01201](https://arxiv.org/abs/1904.01201) |
| **REVERIE** | 2020 / CVPR | Sim | Remote object grounding via navigation | [arXiv:1904.10151](https://arxiv.org/abs/1904.10151) |
| **VLN-CE** | 2020 / ECCV | Sim (Habitat) | VLN in continuous environments | [arXiv:2004.02857](https://arxiv.org/abs/2004.02857) |
| **RxR** | 2020 / EMNLP | Sim | Multilingual, fine-grained VLN | [arXiv:2010.07954](https://arxiv.org/abs/2010.07954) |
| **ObjectNav Revisited** | 2020 | Sim | Standardized ObjectNav evaluation | [arXiv:2006.13171](https://arxiv.org/abs/2006.13171) |
| **HM3D / HM3D-Sem** | 2021 / NeurIPS D&B | Sim | 1,000 real scanned buildings for nav | [arXiv:2109.08238](https://arxiv.org/abs/2109.08238) |
| **SocNavBench** | 2021 | Sim | Social navigation with real pedestrian data | [arXiv:2103.00047](https://arxiv.org/abs/2103.00047) |
| **Habitat 3.0** (social nav / rearrange) | 2023 | Sim | Humanoid avatars + human-in-the-loop | [arXiv:2310.13724](https://arxiv.org/abs/2310.13724) |
| **GOAT-Bench** | 2024 / CVPR | Sim | Multi-modal lifelong navigation (category / image / language goals) | [arXiv:2404.06609](https://arxiv.org/abs/2404.06609) |
| **VL-LN** (Interactive Instance ObjectNav) | 2025 | Sim | Navigate *and* ask an oracle via dialog | [arXiv:2512.22342](https://arxiv.org/abs/2512.22342) |
| **VLNVerse** | 2025 | Sim (Isaac Sim) | Physics-bound agents, 263 environments, unified nav tasks | [arXiv:2512.19021](https://arxiv.org/abs/2512.19021) |
| **NavTrust** | 2025–26 | Sim | Trustworthiness of VLN & ObjectNav under corruptions | [arXiv search](https://arxiv.org/search/?query=NavTrust&searchtype=all) |
| 🆕 **NavVerse** | 2026 | Sim | Indoor-to-outdoor continuous navigation, 200 scenes, 10k episodes | [arXiv:2607.19695](https://arxiv.org/abs/2607.19695) |

---

## 12. Aerial / UAV Embodied Benchmarks (无人机)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **AerialVLN** | 2023 / ICCV | Sim (AirSim/UE) | City-scale aerial VLN | [arXiv:2308.06735](https://arxiv.org/abs/2308.06735) |
| **OpenFly** | 2025 | Sim | 100k trajectories, 18 scenes, multi-engine toolchain | [arXiv:2502.18041](https://arxiv.org/abs/2502.18041) |
| **UAV-ON** | 2025 | Sim | 11k open-world object-goal navigation tasks for UAVs | [arXiv:2508.00288](https://arxiv.org/abs/2508.00288) |
| **TravelUAV / OpenUAV** | 2024–25 | Sim | Realistic UAV VLN with continuous trajectories | [arXiv search](https://arxiv.org/search/?query=Towards+Realistic+UAV+Vision-Language+Navigation+OpenUAV&searchtype=all) |
| **Embodied4C** (drone track) | 2025 | Sim | Cross-embodiment (car / drone / arm) closed-loop reasoning | [arXiv:2512.18028](https://arxiv.org/abs/2512.18028) |

---

## 13. Embodied Reasoning, Spatial Understanding & Planning for (M)LLMs (具身推理/空间理解/规划)

评测"机器人大脑"——VLM/LLM 在具身场景下的感知、空间推理、指点、可供性、任务规划与失败分析。

### 13.1 Embodied QA, spatial reasoning & pointing

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **OpenEQA** | 2024 / CVPR | QA | Open-vocabulary embodied question answering (episodic memory & active) | [Website](https://open-eqa.github.io/) |
| **VSI-Bench** ("Thinking in Space") | 2024 / CVPR'25 | QA (video) | Visual-spatial intelligence from egocentric video | [arXiv:2412.14171](https://arxiv.org/abs/2412.14171) |
| **RoboPoint / Where2Place** | 2024 / CoRL | QA (pointing) | Spatial affordance prediction via points | [arXiv:2406.10721](https://arxiv.org/abs/2406.10721) |
| 🔥 **ERQA** (Gemini Robotics) | 2025 | QA | 400 MCQs: spatial, trajectory, action, state, multi-view reasoning | [arXiv:2503.20020](https://arxiv.org/abs/2503.20020) |
| **RefSpatial-Bench** (RoboRefer) | 2025 / NeurIPS | QA (pointing) | Multi-step spatial referring | [arXiv:2506.04308](https://arxiv.org/abs/2506.04308) |
| **Point-It-Out** | 2025 | QA (pointing) | Multi-stage visual grounding for embodied reasoning | [arXiv:2509.25794](https://arxiv.org/abs/2509.25794) |
| **RoboBench** | 2025 | QA | MLLM as embodied brain: instruction, perception, planning, affordance, failure analysis (14 capabilities) | [arXiv:2510.17801](https://arxiv.org/abs/2510.17801) |
| **Embodied4C** | 2025 | QA + closed-loop | ~1.1K reasoning questions + 58 goal-directed tasks across 3 embodiments | [arXiv:2512.18028](https://arxiv.org/abs/2512.18028) |
| **ERIQ** | 2025–26 | QA | 6K+ QA decoupling reasoning from action; correlates with VLA generalization | [arXiv search](https://arxiv.org/search/?query=ERIQ+embodied+reasoning+robotic+manipulation&searchtype=all) |
| 🆕 **Embodied3DBench** | 2026 | QA | Low-level 3D spatial intelligence, 21k+ QA + 1.3M training QA | [arXiv:2605.29074](https://arxiv.org/abs/2605.29074) |
| 🆕 **ERQA-Plus** | 2026 | QA | 1,766 diagnostic QA over 711 robot-centric images | [arXiv:2606.17639](https://arxiv.org/abs/2606.17639) |

### 13.2 Task planning & agentic evaluation

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **ALFWorld** | 2020 / ICLR'21 | Text + Sim | Aligns text and embodied ALFRED tasks | [arXiv:2010.03768](https://arxiv.org/abs/2010.03768) |
| **LoTa-Bench** | 2024 / ICLR | Sim | LLM task planners in AI2-THOR / VirtualHome | [arXiv search](https://arxiv.org/search/?query=LoTa-Bench&searchtype=all) |
| **Embodied Agent Interface** | 2024 / NeurIPS | Sim | Fine-grained LLM decision-making modules (goal interp., subgoals, actions, transitions) | [arXiv:2410.07166](https://arxiv.org/abs/2410.07166) |
| 🔥 **EmbodiedBench** | 2025 / ICML | Sim | 1,128 tasks in 4 envs; MLLMs strong at high-level, weak at low-level | [arXiv:2502.09560](https://arxiv.org/abs/2502.09560) |
| **AHA** | 2024 | QA | Failure detection & reasoning for manipulation | [arXiv:2410.00371](https://arxiv.org/abs/2410.00371) |
| 🆕 **RobotWorld** | 2026 | Sim | Multimodal agents for robot use across tasks & embodiments | [arXiv:2610.10409](https://arxiv.org/abs/2610.10409) |

---

## 14. Multi-Agent & Human-Robot Collaboration (多智能体/人机协作)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **RoCoBench** | 2023 | Sim | LLM-dialectic multi-arm collaboration | [arXiv:2307.04738](https://arxiv.org/abs/2307.04738) |
| **PARTNR** | 2024 / ICLR'25 | Sim (Habitat 3.0) | Human-robot planning & reasoning in household tasks | [arXiv:2411.00081](https://arxiv.org/abs/2411.00081) |
| **VIKI-Bench** | 2025 | Sim | Hierarchical multi-robot cooperation (activation, planning, trajectory) | [arXiv:2506.09049](https://arxiv.org/abs/2506.09049) |
| **M4Bench** | 2025 / Frontiers | Sim | Multi-user, multi-robot, multi-goal, multi-device HRI | [Frontiers](https://www.frontiersin.org/articles/10.3389/frobt.2025.1528754) |
| 🆕 **MARS Challenge** | 2026 | Sim | Multi-agent embodied planning + low-level manipulation | [arXiv search](https://arxiv.org/search/?query=MARS+challenge+multi-agent+embodied&searchtype=all) |
| 🆕 **CoHuB** | 2026 / NeurIPS | Sim | Multi-humanoid collaboration | [arXiv:2609.34782](https://arxiv.org/abs/2609.34782) |

---

## 15. Safety, Security & Trustworthiness (安全/对抗/可信)

| Benchmark | Year | Type | Highlights | Link |
|---|---|---|---|---|
| **BadRobot** | 2024 | Sim/Real | Jailbreaking LLM-based embodied agents | [arXiv:2407.20242](https://arxiv.org/abs/2407.20242) |
| **SafeAgentBench** | 2024 | Sim | Safe task planning for embodied LLM agents (hazardous tasks) | [arXiv search](https://arxiv.org/search/?query=SafeAgentBench&searchtype=all) |
| 🆕 **EmbodiedGovBench** | 2026 | Sim | Governance, recovery & upgrade safety in embodied agent systems | [arXiv:2604.11174](https://arxiv.org/abs/2604.11174) |
| 🆕 **RoboJailBench** | 2026 | Sim | Adversarial attacks & defenses on embodied robotic agents | [arXiv:2605.19328](https://arxiv.org/abs/2605.19328) |
| 🆕 **SafeVLA-Bench** | 2026 | Sim | The success–safety gap in VLA models | [arXiv:2606.00773](https://arxiv.org/abs/2606.00773) |
| 🆕 **SABER** | 2026 | Sim | Black-box minimal instruction-edit attacks on 6 VLAs (LIBERO) | [arXiv:2603.24935](https://arxiv.org/abs/2603.24935) |
| 🆕 **Linguistic adversarial instructions for VLAs** | 2026 | Sim | Success drops from 93% → 6% under searched instructions | [arXiv:2604.05595](https://arxiv.org/abs/2604.05595) |
| 🆕 **ForesightSafety-VLA**, **ManiGuard** | 2026 | Sim | Safety-oriented VLA evaluation (tracked in Awesome-Robotics-Manipulation) | [search](https://arxiv.org/search/?query=ForesightSafety-VLA&searchtype=all) · [search](https://arxiv.org/search/?query=ManiGuard&searchtype=all) |
| See also §2 (VLA-RISK, Eva-VLA, VLA-Fool) and §5 (SoftVTBench safety metric) | | | | |

---

## 16. Simulation Platforms & Unified Benchmark Frameworks (仿真平台/统一框架)

Not benchmarks per se, but most benchmarks above are built on them.

| Platform | Notes | Link |
|---|---|---|
| MuJoCo / MuJoCo Playground | Physics engine behind Meta-World, robosuite, DMC, HumanoidBench | [GitHub](https://github.com/google-deepmind/mujoco) |
| SAPIEN / ManiSkill3 | GPU-parallel sim + rendering | [arXiv:2410.00425](https://arxiv.org/abs/2410.00425) |
| NVIDIA Isaac Sim / Isaac Lab | RTX rendering, used by ARNOLD, VLNVerse, RobOmni | [GitHub](https://github.com/isaac-sim/IsaacLab) |
| AI2-THOR / ProcTHOR | Interactive houses (ALFRED, TEACh) | [arXiv:2206.06994](https://arxiv.org/abs/2206.06994) |
| Habitat-Sim / Habitat-Lab | Navigation & rearrangement | [arXiv:1904.01201](https://arxiv.org/abs/1904.01201) |
| iGibson / OmniGibson | BEHAVIOR series | [arXiv:2403.09227](https://arxiv.org/abs/2403.09227) |
| RoboVerse | Unified platform/dataset/benchmark across simulators | [arXiv search](https://arxiv.org/search/?query=RoboVerse+unified+platform+scalable+generalizable+robot+learning&searchtype=all) |
| GRUtopia / InternUtopia | City-scale embodied sim for general robots | [arXiv:2407.10943](https://arxiv.org/abs/2407.10943) |
| Genesis | Generative, multi-physics simulator | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) |

---

## 17. Companion Datasets Often Used for Evaluation (常用于评测的数据集)

| Dataset | Notes | Link |
|---|---|---|
| Open X-Embodiment | 1M+ trajectories, 22 embodiments; RT-X evaluation | [arXiv:2310.08864](https://arxiv.org/abs/2310.08864) |
| BridgeData V2 | WidowX; basis of SIMPLER-WidowX & AutoEval | [arXiv:2308.12952](https://arxiv.org/abs/2308.12952) |
| DROID | 76k Franka trajectories in the wild; basis of RoboArena & PolaRiS | [arXiv:2403.12945](https://arxiv.org/abs/2403.12945) |
| Deform360 / HapTile | 2026 visuotactile deformable / contact-rich datasets | — |

---

## 18. Competitions & Challenges (竞赛)

- **BEHAVIOR Challenge** (NeurIPS 2025) — 50 long-horizon household tasks in OmniGibson. [Website](https://behavior.stanford.edu/challenge/)
- **Habitat Navigation / Rearrangement Challenges** (CVPR 2019–2023). [Website](https://aihabitat.org/challenge/)
- **ManiSkill Challenge** (2021–2022). [Website](https://www.maniskill.ai/)
- **Real Robot Challenge** (2020–2022, TriFinger dexterous). [Website](https://real-robot-challenge.com/)
- **ICRA Cloth Competition** (2024–2026). 
- **MARS Challenge** (NeurIPS 2025 SpaVLE workshop) — multi-agent embodied planning.
- **Amazon Picking/Robotics Challenge** (2015–2017) — warehouse pick-and-place.

---

## 19. Surveys on Robot Benchmarks & Evaluation (综述)

| Survey | Year | Link |
|---|---|---|
| Datasets, Benchmarks and Data Engines for VLA models | 2026 | [arXiv:2604.23001](https://arxiv.org/abs/2604.23001) |
| Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends | 2026 | [arXiv:2606.12207](https://arxiv.org/abs/2606.12207) |
| Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence | 2026 | [arXiv:2609.29669](https://arxiv.org/abs/2609.29669) |
| Evaluation-centric VLA survey (582 papers, minimum reporting protocols) | 2026 | [Preprints.org](https://www.preprints.org/manuscript/202606.1149) |
| VLA Models for UAVs and Bimanual Manipulation: A Review | 2026 | [arXiv:2607.06706](https://arxiv.org/abs/2607.06706) |

Related awesome lists: [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) · [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam)

---

## Trends & Takeaways (趋势总结)

1. **Saturation → perturbation.** LIBERO/SIMPLER/CALVIN numbers are near ceiling for strong VLAs. 2025–26 work (LIBERO-PRO/Plus/MAX, STRONG-VLA, RoboSPA) shows that small camera, init-state or wording changes can collapse success — *report perturbed suites, not just the original*.
2. **Benchmarks themselves are being audited.** Shortcut solvability, few-trial noise and demo-source leakage ([2609.37771](https://arxiv.org/abs/2609.37771)) mean you should report confidence intervals and number of trials.
3. **Real-world evaluation is scaling** via distribution (RoboArena), automation (AutoEval, graph-based reset harnesses) and low-cost replication (VLA-REPLICA).
4. **Cheaper proxies for real robots:** Real2Sim (SIMPLER → PolaRiS → 3DGS verification) and world-model evaluators (WorldGym, dWorldEval, WMBench, RoboWorld). The key metric is rank correlation with real success.
5. **Beyond success rate:** memory (RoboMME), compositionality (ATOM-Bench), safety (SafeVLA-Bench, SoftVTBench), and behavior quality (RoboEval).
6. **The "brain" is evaluated separately from the "body":** ERQA, RoboBench, Embodied3DBench, ERQA-Plus test VLM reasoning offline; ERIQ reports this correlates with downstream VLA generalization.
7. **New embodiments get their own suites:** humanoids (SIMPLE, CoHuB, LHM-Humanoid), dexterous hands (DexJoCo, POMDAR), UAVs (OpenFly, UAV-ON), tactile (UniVTAC, RobOmni).

## How to Pick a Benchmark (选型建议)

| If you are building… | Start with | Then stress-test with |
|---|---|---|
| A generalist VLA policy | LIBERO, SIMPLER, RoboCasa, RoboTwin 2.0 | LIBERO-Plus/PRO, RoboArena or AutoEval, PolaRiS |
| A bimanual / dexterous policy | RoboTwin 2.0, Bi-DexHands, DexJoCo | Real: POMDAR, DexToolBench |
| A long-horizon / household agent | CALVIN, BEHAVIOR-1K, HomeRobot OVMM | RoboMME (memory), EBench |
| A humanoid controller | HumanoidBench | SIMPLE, LHM-Humanoid |
| A navigation agent | Habitat ObjectNav, R2R / VLN-CE | GOAT-Bench, VLNVerse, NavVerse |
| An embodied VLM "brain" | ERQA, VSI-Bench, RoboBench | Embodied3DBench, RefSpatial-Bench, EmbodiedBench |
| A safety layer | SafeAgentBench, SafeVLA-Bench | RoboJailBench, VLA-RISK |

---

## Contributing

PRs welcome! Please follow the table format: `Name | Year/Venue | Type | Highlights | Link`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) To the extent possible under law, the contributors have waived all copyright and related rights to this work.

# Co-Optimizing Sensing and Deep Machine Learning in Automotive Cyber-Physical Systems

## Metadata
- **Authors:** Joydeep Dey, Sudeep Pasricha
- **Year:** 2022
- **Conference/Journal:** 25th Euromicro Conference on Digital System Design (DSD)
- **DOI:** https://ieeexplore.ieee.org/document/9996737
- **Keywords:** autonomous vehicles, cyber-physical systems, deep learning, perception architecture, sensor fusion
- **PDF:** assets/pdf/2026-03-21/dey-2022-co-optimizing-and-dl-in-automotive-cps.pdf

## Summary

This paper proposes PASTA, a framework for co-optimizing sensing and deep machine learning in perception architectures for semi-autonomous vehicles. It simultaneously optimizes sensor placement, deep learning object detectors, and sensor fusion algorithms to meet Level 2 autonomy goals. Experimental results in CARLA simulator demonstrate superior performance over partial optimization approaches, with up to 52.24% improvement for Audi TT and 26.72% for BMW Minicooper using hybrid GA-PSO algorithm.

## Key Contributions

- Proposal of PASTA framework for joint optimization of sensor placement, object detection, and fusion algorithms.
- Evaluation of five design space exploration algorithms (GA, DE, FA, PSO, GA-PSO) for efficient navigation of massive design space.
- Integration of neural architecture search (NAS) for fine-tuning YOLOv4 object detector via transfer learning.
- Comparative analysis across different vehicle platforms (Audi TT, BMW Minicooper) showing generalizability.

## Methodology

- **Hardware Setup**: Up to 8 sensors (4 radars with 30° FOV/100m range, 4 cameras with 90° FOV/800×600 resolution) placed on vehicle body with physical constraints.
- **Object Detection**: Six detectors (YOLOv3, YOLOv4, SSD, R-CNN, Fast R-CNN, Faster R-CNN) trained on MS-COCO dataset.
- **Sensor Fusion**: Three algorithms (Kalman Filter, Extended Kalman Filter, Unscented Kalman Filter).
- **Search Algorithms**: GA, DE, FA, PSO, GA-PSO with population size 50, termination after <5% cost change over 250 iterations.
- **Evaluation**: 8 metrics for Level 2 autonomy (position errors, occlusion rate, velocity uncertainty, late detection, false positives/negatives), 20 drive cycles (~5 min each) in CARLA simulator, AMD Ryzen 7 3800X CPU + NVIDIA RTX 2080 Ti GPU.

## Results

- **Detector Performance**: YOLOv4 achieves 21.85ms GPU latency with 73.19% mAP, optimal for real-time use; Faster R-CNN more accurate (79.86% mAP) but slower (181.77ms).
- **Algorithm Comparison**: GA-PSO outperforms GA (52.24% for Audi TT, 26.72% for BMW Minicooper), DE, FA, PSO.
- **Framework Effectiveness**: Full PASTA beats partial approaches (GA-PO, GA-OP, GA-VESPA, GA-POD, GA-POF).
- **NAS Integration**: GA-PSO-NAS-PASTA improves by 11.53% (Audi TT) and 14.62% (BMW Minicooper) over GA-PSO-PASTA.
- **Vehicle-Specific Solutions**: Tailored sensor placements for ACC, FCW, LKA, BW features.

## Strengths

- Holistic co-optimization approach outperforms independent optimizations.
- Rigorous comparison with baselines and ablation studies.
- Practical framework for automated perception architecture synthesis.
- Multi-vehicle validation demonstrating generalizability.
- Efficient transfer learning for detector adaptation.

## Weaknesses

- High computational cost (80-100 hours per run on RTX 2080 Ti).
- Limited to cameras and radars; no LiDAR or other sensors.
- Focused on Level 2 autonomy; unclear generalization to higher levels.
- Simulation-only validation; real-world gaps in weather/sensor degradation.
- No consideration of cost, power, or production constraints.

## Notes / Insights

- **Relevance**: Addresses critical perception bottleneck in autonomous vehicles by automating sensor-algorithm co-design.
- **Future Work**: Extend to higher autonomy levels, incorporate more sensor types, reduce computation time, real-world validation, cybersecurity integration.
- **Connection to Prior Work**: Builds on VESPA [13] by adding detector and fusion optimization, showing benefits of full co-optimization.

## Related Papers

- [5] Y. Feng et al. "Distance Estimation by Fusing Radar and Monocular Camera with Kalman Filter." SAE Technical Paper 2017-01-1978, 2017.
- [6] Z. Yu et al. "Camera-Radar Data Fusion for Target Detection via Kalman Filter and Bayesian Estimation." SAE Tech. Paper, 2018.
- [7] F. Nobis et al. "A Deep Learning-based Radar and Camera Sensor Fusion Architecture for Object Detection." IEEE SDF, 2020.
- [8] M. Verucchi et al. "Real-Time clustering and LiDAR-camera fusion on embedded platforms for self-driving cars." IEEE IRC, 2020.
- [9] L. Meng et al. "An Optimization of Deep Sensor Fusion Based on Generalized Intersection over Union." ICA3PP, 2020.
- [10] W. Hudson et al. "Multi-LIDAR placement, calibration, coregistration and processing on a Subaru Forester for off-road autonomous vehicles operations." Autonomous Systems, 2019.
- [12] J. Luo et al. "Multi-scale traffic vehicle detection based on faster R–CNN with NAS optimization and feature enrichment." DT, 2021.
- [13] J. Dey, S. Pasricha. "VESPA: A Framework for Optimizing Heterogeneous Sensor Placement and Orientation for Autonomous Vehicles." IEEE CEM, 2020.

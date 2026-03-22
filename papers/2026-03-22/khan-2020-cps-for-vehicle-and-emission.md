# Cyber Physical System for Vehicle Counting and Emission Estimation

## Metadata
- **Authors:** Ali Khan, Khurram S. Khattak, Zawar H. Khan, Mushtaq Ahmad Khan, Nasru Minallah
- **Year:** 2020
- **Conference/Journal:** International Journal of Advanced Computer Research, Vol 10(50)
- **DOI:** http://dx.doi.org/10.19101/IJACR.2020.1048096
- **Keywords:** cyber-physical systems, intelligent transportation system, vehicle counting, vehicle emissions, Raspberry Pi, OpenCV, ThingSpeak
- **PDF:** assets/pdf/2026-03-22/khan-2020-cps-for-vehicle-and-emission.pdf

## Summary

This paper addresses the need for real-time, low-cost monitoring of vehicular traffic and associated emissions. It proposes a cyber-physical system using Raspberry Pi for vehicle counting via OpenCV and Arduino for emission sensors (CO, CO2, PM2.5), transmitting data to the ThingSpeak cloud platform. Results demonstrate 86.9% counting accuracy and establish relationships between traffic flow parameters and vehicular emissions.

## Key Contributions

- Proposal of a low-cost cyber-physical system for real-time vehicle counting and emission estimation (CO, CO2, PM2.5).
- Integration of Raspberry Pi with OpenCV for image processing coupled with Arduino hosting environmental sensors.
- Establishment of relationships between traffic flow parameters and vehicular emissions, useful for Intelligent Transportation Systems (ITS) and environmental monitoring.

## Methodology

- **Hardware**: Raspberry Pi 3B with Pi camera, Arduino Nano with MQ135 sensors (CO/CO2), GP2Y1010AU0F sensor (PM2.5), ESP8266 Wi-Fi module, SD card, and RTC module.
- **Software**: OpenCV in C++ on the RPi for image processing (capture, background subtraction, contour detection, tracking) and serial communication with Arduino.
- **Algorithms**: Vehicle counting via video analysis (640×480 resolution, 20 fps), data transmission to ThingSpeak every 15 seconds.
- **Platform**: ThingSpeak cloud platform for data storage and analysis.
- **Experimental Setup**: Deployed on a pedestrian bridge over a main road in Peshawar, Pakistan; 42-minute evaluation period with manual counting comparison.

## Results

- **Vehicle Counting Accuracy**: 86.9% (1,109 detected vs. 1,275 manually counted).
- **Traffic Parameters**: Traffic flow ranging from 21–48 veh/min and density from 0.7–1.6 veh/min/m.
- **Emission Levels**: CO (2–4.14 PPM), CO2 (669–1,187 PPM), PM2.5 (28–99 PPM), with direct correlations to traffic flow.
- **Power Consumption**: 730.5 mAh with battery autonomy of 13.68 hours.

## Strengths

- Low-cost solution (US$70) with real-time processing and edge computing capabilities.
- Integrates traffic counting and emission monitoring, useful for ITS applications and environmental analysis.
- Utilizes open-source platforms (OpenCV, ThingSpeak), making the system scalable and easy to maintain.

## Weaknesses

- Counting accuracy of 86.9% could be improved with more advanced detection algorithms.
- Limited to specific sensors; does not measure vehicle speed or other pollutants.
- Tested on a single scenario; generalization to varying environmental and traffic conditions is unclear.

## Notes / Insights

- **Integration**: Useful for urban environmental monitoring and can be integrated with other cyber-physical systems.
- **Future Ideas**: Add vehicle speed estimation, incorporate additional sensor types (NOx, O3), and deploy a distributed sensor network across multiple locations.
- **Improvements**: Implement deep learning algorithms for enhanced vehicle detection accuracy.
- **Related Work**: Connected to research on ITS and IoT for traffic monitoring, such as references [4] and [5].

## Related Papers

- [4] Gregor D, et al. "Design and implementation of a counting and differentiation system for vehicles through video processing." International Journal of Computer and Information Engineering, vol. 10, no. 10, 2016.
- [5] Khan N, et al. "A low-cost IoT based system for environmental monitoring." In Proceedings of the International Conference on Frontiers of Information Technology (FIT), 2019.
- [8] Iszaidy I, et al. "Video size comparison for embedded vehicle speed detection & travel time estimation system by using Raspberry Pi." In International Conference on Robotics, Automation and Sciences (ICORAS), 2016.
- [9] McQueen R. "Detection and speed estimation of vehicles using resource constrained embedded devices." Master's thesis, 2018.
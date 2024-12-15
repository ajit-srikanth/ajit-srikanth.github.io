---
layout: post
title:  "Autonomous Omni-drive robot"
# date:   2024-05-05 00:00:00 +00:00
categories: project
image: /images/blank_img.jpg
# course: 
# site: 
---
- Assembled a mecanum wheel robot with four Orange Planetary Gear DC Motor driven by two Cytron Mdds30 Dual 30A drivers
- Integrated the Realsense T265 tracking camera and Realsense D455 depth camera along with voxfield for getting ESDFs
- Implemented multiple planning algorithms (on the onboard intel NUC) including CEM, MPPI, and MPC using the ESDFs generated, and implemented basic PID for following the path generated
<!--done-->

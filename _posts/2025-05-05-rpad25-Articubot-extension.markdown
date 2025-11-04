---
layout: post
title:  "Articubot extension"
# date:   2023-03-09 00:00:00 +00:00
categories: project
image: /images/very_compressed_small_interesting_working_demo.gif
# course: 
# site:
---
- Worked on extending a zero-shot sim-to-real policy for articulated object manipulation (Articubot) through incorporating novel online history conditioning.
<!-- - Worked on enhancing the real-world deployment of the policy by implementing whole-body manipulation on a mobile
XArm7, leveraging impedance control, and utilizing action chunking for faster execution. -->
<!-- base oda motion planning for reaching the goal object with collision avoidance pathi innum mention pannala -->
- Solved a critical real-world kinematic limitations by implementing a whole-body control maneuver, synchronizing the mobile base and XArm7's movements, to overcome the robot's IK limits.
- Improved real-world control by integrating compliant impedance control for safe interaction and optimizing the action execution pipeline (using parallel inference, selective action dropping, and other code optimizations) to greatly speedup the real-world policy execution.
<!--done-->

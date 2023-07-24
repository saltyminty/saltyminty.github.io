---
layout: page
title: Arduino Software Migration
description: Rewriting lab content and software to migrate from TI Launchpads to Arduino
# img: assets/img/3.jpg
importance: 1
category: EECS 16B&#58; Designing Information Devices and Systems II
# giscus_comments: true
---

The core of EECS 16B is its lab component, in which students build a voice controlled robot car controlled via a microcontroller. While being one of the significant points of frustration with the class, students commonly consider completing the project to be the most central and satisfying component of the class.

<div class="text-center">
  <img src="/assets/img/teaching/eecs16b/IMG_0063.jpg" class="mx-auto d-block img-fluid rounded z-depth-1" alt="Centered Image" width="50%" height="auto">
</div>
<div class="caption">
    Completed EECS 16B Car, Spring 2021
</div>

Previously, the class's microcontroller of choice was the TI Launchpad. To be honest, I'm not entirely sure why we used it – ~~probably didn't have anything to do with the couple million dollars TI donated to the school every year.~~

Launchpads lacked documentation and were a buggy mess – while we could generally hide many of these issues from students, they were a huge pain for staff to develop labs with. More notably, Launchpads fried at an incredibly common rate, making for an incredibly frustrating debugging experience when discovering that the root cause was poor hardware.

<div class="text-center">
  <img src="/assets/img/teaching/eecs16b/unknown.png" class="mx-auto d-block img-fluid rounded z-depth-1" alt="Centered Image" width="50%" height="auto">
</div>
<div class="caption">
    In Spring 2022 alone, we saw over 200 fried launchpads. Here, I'm wearing some fried Launchpads as a hat.
</div>

Over Summer 2022, TI contacted us stating that due to supply chain issues, they would be unable to provide us with TI launchpads for the upcoming Fall semester, I saw the perfect opportunity to finally migrate the course to Arduino – better documentation, better reliability, and could actually be potentially used outside of class.

Together with my co-head Lab TA Shrey Aeron, we fully rewrote lab content and software to function with Arduinos. We submitted a [proposal to the department regarding the design, development, QA/testing, and release to students](/assets/pdf/Arduino%20Development%20Timeline.pdf) for the upcoming semester.

We successfully rolled out the project over the Fall semester. This was so successful that future semesters of EECS 16B will continue to use Arduino as opposed to Launchpads – the Arduinos provided a much better student experience and even lowered costs due to a much lowered frequency of fried boards. The improved hardware additionally allowed us to make several other lab content changes and quality of life improvements to the overall lab experience.

*As of Spring 2024, course labs are still being taught in Arduino.*
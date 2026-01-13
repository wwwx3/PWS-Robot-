# **PWS Solution — Autonomous Sugarcane Leaf Stripping Robot**

## **Overview**

**PWS Solution** is an autonomous agricultural robot designed to replace the traditional practice of burning sugarcane leaves. In Thailand, leaf burning is a major source of PM2.5 air pollution and soil degradation. This project aims to reduce environmental damage while improving farm efficiency through robotics and precise navigation.

The robot is designed to operate on sugarcane fields of any shape, not only rectangular farms, making it suitable for real agricultural conditions in Thailand.

---

## **Problem**

Sugarcane leaf burning:

* Produces dangerous PM2.5 pollution
* Damages soil quality
* Harms farmers’ health
* Is still widely used due to labor shortage

Small and medium farms often cannot afford large industrial machines, so a flexible, low-cost autonomous solution is needed.

---

## **System Design**

The PWS robot uses **GPS, gyroscope sensors, and computational geometry** to navigate complex farm layouts.

### Core Technologies

* **GPS** for field position
* **Gyroscope** for orientation
* **Haversine formula** to convert latitude–longitude into a Cartesian coordinate system
* **Ray-casting algorithm** to determine whether the robot is inside or outside the field boundary

This allows the robot to:

* Understand the shape of the farm
* Plan movement paths
* Avoid crossing outside working areas

---

**Path Planning & Field Boundary Detection**

![PWS Autonomous Navigation Flow](pathplanningflow.png)


---

**Motor Control System**

![PWS Motor Control Logic](motorcontrolflow.png)


---



## **Functionality**

The robot:

* Drives autonomously across sugarcane rows
* Strips sugarcane leaves mechanically
* Works on irregular field shapes
* Operates without pre-drawn maps

The navigation system adapts to the farm’s geometry instead of forcing farms to fit the robot.

---

## **Team & Contributions**

---

### **Wirin Chinthammit (Plearn)**

**Role: Robotics & Field Research**

* Conducted background research on sugarcane farming
* Visited real farms to observe working conditions and equipment
* Consulted with farm operators to understand real-world constraints
* Built and developed robot **mechanical structures**
* Implemented and tested robot **control programs**
* Designed and refined **path-planning algorithms**

---

### **Chatnatda Ovatanupat (Winnie)**

**Role: AI & System Integration Lead**

* Project brainstorming and system design
* Proposed theoretical models for navigation and sensing
* Conducted interviews with sugarcane farm operators and performed on-site observation
* Integrated **AI and CVAT pipelines** on **Raspberry Pi 5**
* Developed **lane-detection algorithms** for autonomous navigation
* Coordinated software logic between perception and robot movement

---

### **Peeraphat Pinijpanich (Sun)**

**Role: Data, Algorithms & Environmental Analysis**

* Assisted with agricultural data collection
* Researched modern farming technologies
* Contributed to project concept development
* Constructed the robot prototype with **3D modeling and printing**
* Develop **path-planning algorithms**
* Analyzed the **environmental impact of biomass (sugarcane leaf) burning**

---

## **Impact**

By replacing leaf burning with robotic stripping, PWS Solution helps:

* Reduce PM2.5 air pollution
* Protect farmers’ health
* Improve soil sustainability
* Support small-scale agriculture

This project combines **robotics, environmental science, and real-world problem solving**, reflecting my goal of building technology that benefits both people and the planet.

---

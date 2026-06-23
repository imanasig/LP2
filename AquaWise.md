# JALRAKSHAK – A Predictive Community Water Intelligence System

### Problem

Due to low rainfall and increasing water demand, many societies now receive municipal water only on alternate days. The same water has to be managed for the next 48 hours.

Currently, this process is done manually by the watchman or society committee members based on experience and guesswork.

As a result:

- Water gets over earlier than expected.
- Nobody knows how long the water will last.
- Peak usage patterns are unknown.
- Delayed municipal supply can create severe shortages.

---

### Our Solution

JalRakshak is a low-cost IoT-based system that helps societies manage water intelligently.

Instead of guessing, the system continuously monitors water availability and consumption patterns, predicts future shortages and provides recommendations before a crisis occurs.

---

### How It Works

**Step 1:** Municipal water is stored in the underground tank.

**Step 2:** The existing society pump transfers water to the overhead tank.

**Step 3:** An ultrasonic sensor measures the amount of water available in the overhead tank.

**Step 4:** A flow sensor measures how much water is being consumed.

**Step 5:** ESP32 processes this data and uses simple Machine Learning (Linear Regression) to predict future water availability.

**Step 6:** A dashboard displays live information and recommendations.

---

### System Architecture

Municipal Water

↓

Underground Tank

↓

Existing Society Pump

↓

Overhead Tank

↓

Ultrasonic Sensor + Flow Sensor

↓

ESP32

↓

Prediction Engine (Machine Learning)

↓

Dashboard

↓

Society takes action

---

### Dashboard Outputs

The system will show:

💧 Water Available (% and litres)

⏳ Estimated Hours Remaining

📈 Peak Usage Hours

⚠️ Risk Level (Safe / Warning / Critical)

💡 Recommended Action

Example:

"At the current usage rate, water will last for another 36 hours."

---

### Components Used

- ESP32
- Waterproof Ultrasonic Sensor (JSN-SR04T)
- Water Flow Sensor (YF-S201)
- Mini Submersible Pump (Prototype only)
- Relay Module

---

### Machine Learning Used

Linear Regression

The system learns the society's water usage patterns and predicts future water availability.

---

### Future Scope

The same idea can be scaled from:

Society → Multiple Societies → Ward Level → Entire City

Municipal corporations can use this data to make smarter water distribution decisions.

---

### One-line Vision

**Today, societies manage water using guesswork. JalRakshak replaces guesswork with data-driven decisions and helps prevent water shortages before they happen.**

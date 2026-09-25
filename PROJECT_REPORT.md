# A Project Report
On
# **CYBERSECURITY AWARENESS TRAINING PLATFORM**

### **Submitted by**
**Dhairya Kahar [22405101020009]**

**as**  
**Partial fulfilment of Semester VI**  
**of Bachelor of Science in Information Technology**  
**for A.Y. 2026-2027**  

---

### **Under the Guidance of**
**Internal Guide name :**  
**Prof. Ramchandaran**

---

### **Submitted To**
**Parul Institute of Computer Application,**  
**Faculty of IT & Computer Science**  
**Parul University**  

---

# Acknowledgement

The success and final outcome of this project required a lot of guidance and assistance from many people and we are extremely privileged to have got this all along the completion of our project. All that we have done is only due to such supervision and assistance and we would not forget to thank them.

I respect and thank **Dr. Priya Swaminarayan (Dean)** and **Dr. Hina Chokshi (Vice-Principal)** for providing us an opportunity to do the project work in **BSCIT Regular/Hons** and giving us all support and guidance which made us complete the project duly. We are extremely thankful to Mam for providing her support and guidance, although she had a busy schedule managing the academic affairs.

We would not forget to remember **Prof. Vipul Gamit (HOD)** for his encouragement and more over for his timely support and guidance till the completion of our project work.

We owe our deep gratitude to our project guide **Prof. Ramchandaran**, who took keen interest on our project work and guided us all along, till the completion of our project work by providing all the necessary information for developing a good system.

I am thankful to and fortunate enough to get constant encouragement, support and guidance from our Parents, all Teaching staff of the BCA/IT Department which helped us in successfully completing our project work. Also, we would like to extend our sincere esteems to all staff in the laboratory for their timely support.

**Dhairya Kahar [22405101020009]**

---

# PARUL INSTITUTE OF COMPUTER APPLICATION
## CERTIFICATE

This is to certify that **Dhairya Kahar** the student of Parul Institute of Computer Application, has satisfactorily completed the project entitled **“CYBERSECURITY AWARENESS TRAINING PLATFORM”** as a part of course curriculum in **BSCIT Regular/Hons semester- VI** for the academic year **2026-2027** under guidance of **Prof. Ramchandaran**.

**Enrolment Number:** 22405101020009

| Quality of work | Grade | Sign of Internal guide |
| :---: | :---: | :---: |
| **Poor / Average / Good / Excellent** | **B / B+ / A / A+** | |

**Date of submission:** ___________________

**Prof. Vipul Gamit**  
HOD

**Dr. Hina Chokshi**  
Vise-Principal

**Dr. Priya Swaminarayan**  
Dean

---

# INDEX

| Content | Page No. |
| :--- | :---: |
| **1. Introduction to Project System** | **1** |
| **2. System Requirement Specification** | **2** |
| &nbsp;&nbsp;&nbsp;&nbsp;2.1 Introduction to SRS | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2 Hardware Requirement | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.3 Software Requirement | 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.4 System Users | 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.5 Description of User Role | 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.6 System Modules | 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7 Description of Modules | 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.8 Timeline Chart | 6 |
| **3. System Flow Diagram** | **7** |
| **4. Data Flow Diagram (All Levels of DFDs)** | **8** |
| **5. Use Case Diagram** | **11** |
| &nbsp;&nbsp;&nbsp;&nbsp;1. Use Case | 11 |
| &nbsp;&nbsp;&nbsp;&nbsp;2. Activity Diagram | 12 |
| &nbsp;&nbsp;&nbsp;&nbsp;3. Class Diagram | 13 |
| **6. Data Dictionary** | **14** |
| **7. Screenshots of Development Phase -1** | **16** |
| **8. Screenshots of Development Phase -2** | **18** |
| **9. Screenshots of Development Phase -3** | **20** |
| **10. Conclusion** | **22** |
| **11. Future Enhancement** | **23** |
| **12. References** | **24** |

---

# ABSTRACT

In the contemporary hyper-connected digital era, the proliferation of online services has triggered an alarming surge in sophisticated cyber threats, including deceptive phishing schemes, social engineering manipulation, credential stuffing, and destructive ransomware campaigns. Extensive global empirical studies consistently demonstrate that over ninety percent of documented security breaches originate from human vulnerabilities, cognitive oversights, and deficient digital hygiene, rather than direct cryptographic or architectural exploitation of underlying server infrastructures. Conventional instructional methodologies rely predominantly on static compliance documents and passive instructional media, resulting in disengagement and acute deficits in practical threat recognition capabilities.

To decisively mitigate this critical human risk factor, the **“Cybersecurity Awareness Training Platform”** was conceptualized, engineered, and deployed as a full-stack, experiential web-based educational ecosystem. Architected upon a robust Python 3.12 Flask framework, SQLAlchemy ORM, and serverless PostgreSQL 16 on Neon Cloud, with a highly responsive Bootstrap 5 interface, the platform delivers eight structured micro-learning curriculum domains. The core technical innovations comprise an experiential Phishing Simulation Sandbox that replicates authentic deceptive email headers, an interactive client-side Password Strength and Shannon Entropy Analyzer estimating GPU brute-force crack timelines, and an expanded 40-question randomized assessment suite delivering automated grading and explanatory pedagogical rationales. The platform provides a measurable, scalable, and production-ready pedagogical asset that elevates institutional cyber resilience through proactive habit formation.

---

## 1. Introduction to Project System

### 1.1 Project Overview & Background
In an era defined by rapid digital transformation, cloud integration, and widespread adoption of online services, cybersecurity has transitioned from an esoteric administrative discipline into an existential personal and organizational imperative. The **Cybersecurity Awareness Training Platform** is engineered as a modern, interactive, full-stack educational web application designed to systematically remediate human-centric security risks.

### 1.2 Problem Statement & Motivation
Statistical analyses conducted by leading threat intelligence agencies reveal that human error accounts for over 85% to 90% of successful enterprise data breaches. Conventional methods utilize passive PDF guidelines, sporadic circulars, and mandatory recorded webinars that fail to engage users or develop practical threat identification skills.

### 1.3 Project Purpose & Objectives
1. Engineer a secure, multi-tier web application using Python 3.12 Flask and SQLAlchemy ORM, incorporating PBKDF2/SHA-256 cryptographic authentication.
2. Construct a real-time client-side **Password Entropy & Strength Analyzer** calculating Shannon bit entropy.
3. Implement an experiential **Phishing Simulation Sandbox** allowing learners to inspect spoofed email headers and links.
4. Deploy a randomized **40-Question Assessment Engine** with dynamic PostgreSQL persistence and instant explanatory feedback.
5. Provide personalized analytics dashboards for learners and an administrative control panel for curriculum governance.

---

## 2. System Requirement Specification

### 2.1 Introduction to SRS
The Software Requirement Specification (SRS) establishes a formal contract delineating the complete operational, functional, and non-functional specifications governing the Cybersecurity Awareness Training Platform.

### 2.2 Hardware Requirement
* **Client CPU:** Dual-core Intel Core i3 / AMD Ryzen 3, 2.0 GHz or higher.
* **Client RAM:** 4 GB DDR4 (8 GB recommended).
* **Client Storage:** 500 MB free disk space for browser caching and local assets.
* **Client Display:** 1024x768 minimum, 1080p Full HD responsive mobile viewport recommended.
* **Server CPU:** Single/Dual vCPU (Cloud Container on Render).
* **Server RAM:** 512 MB – 2 GB RAM.
* **Database Engine:** Auto-scaling Serverless Neon Cloud PostgreSQL 16.

### 2.3 Software Requirement
* **Operating System:** Development: Windows 11 64-bit; Production: Ubuntu Linux 22.04 LTS.
* **Backend:** Python 3.12, Flask 3.0.3, Jinja2, Werkzeug Security, Flask-Login.
* **Database & ORM:** PostgreSQL 16 (Neon Serverless Cloud) / SQLite3; SQLAlchemy 2.0.
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3.3, Font Awesome 6.
* **Production Web Server:** Gunicorn 22.0.0 (WSGI HTTP Server).
* **Deployment Platform:** Render Cloud Native Platform.

### 2.4 System Users
1. **Student / General Learner:** Enrolled user completing modules, running phishing simulations, analyzing password entropy, and submitting quizzes.
2. **System Administrator:** Privileged user managing curriculum, authoring assessment questions, and auditing platform telemetry.
3. **Guest Visitor:** Public visitor exploring homepage overviews and registering for accounts.

### 2.5 Description of User Role
* **Learner Role:** Read permissions on topics; execute client-side simulation scripts; create and persist quiz attempts; view personal dashboard analytics.
* **Administrator Role:** Full CRUD access over assessment questions (`/admin/questions`); oversight of user score distributions and institutional progress logs.

### 2.6 System Modules
1. User Authentication & Profile Lifecycle
2. Micro-Learning Security Curriculum (8 Domains)
3. Real-Time Password Strength & Shannon Entropy Analyzer
4. Experiential Phishing Simulation Sandbox
5. 40-Question Assessment & Evaluation Engine
6. Learner Analytics & Progress Dashboard
7. Administrative Governance & Question Bank CRUD

### 2.7 Description of Modules
* **Authentication & Profile:** Enforces PBKDF2 salted password hashing, HTTPOnly cookie session management, and CSRF defense.
* **Curriculum:** 8 core cybersecurity domains (Password Security, Phishing, Malware, Safe Browsing, 2FA/MFA, Public Wi-Fi, Mobile Security, IT Act 2000).
* **Password Analyzer:** Calculates character space ($R$), length ($L$), and Shannon entropy $H = L \cdot \log_2(R)$ with GPU crack time estimations.
* **Phishing Simulator:** Presents realistic deceptive headers, typosquatted domains (e.g. `paypa1.com`), and delivers instant heuristic red-flag feedback.
* **40-Question Quiz Engine:** Randomized evaluation dynamically loaded from PostgreSQL with instant scoring and detailed explanatory solutions.
* **Dashboard:** Aggregates module completion percentages, average scores, and historical attempt timelines.
* **Admin Module:** Role-guarded web interface allowing educators to add, edit, or delete questions.

### 2.8 Timeline Chart
A 12-week Software Development Life Cycle (SDLC) schedule covering Requirements Gathering (Weeks 1-2), Architecture & DB Design (Weeks 3-4), Phase-1 Auth/UI (Weeks 4-6), Phase-2 Tools & Modules (Weeks 6-8), Phase-3 Quiz & Admin (Weeks 8-10), Testing & Hardening (Weeks 10-11), and Cloud Deployment (Weeks 11-12).

---

## 3. System Flow Diagram
The system flow begins with user entry, branches through credential verification (PBKDF2 comparison), transitions to the centralized dashboard, routes to specific educational activities (Curriculum, Entropy Analyzer, Phishing Sandbox, 40-Q Quiz, or Admin Panel), commits records transactionally to PostgreSQL, updates dashboard telemetry, and terminates gracefully upon logout.

---

## 4. Data Flow Diagram (All Levels of DFDs)
* **DFD Level 0 (Context Diagram):** Depicts external entities (Student and Administrator) interfacing with Process 0.0 (Cybersecurity Awareness Training Platform).
* **DFD Level 1 (Subsystems):** Functional decomposition into 1.0 Auth Engine, 2.0 Topic Curriculum, 3.0 Phishing Simulator, 4.0 Quiz Evaluation, and 5.0 Analytics Dashboard, interacting with datastores `D1: users`, `D2: topics`, `D3: questions`, `D4: scores`, and `D5: topic_progress`.
* **DFD Level 2 (Phishing Simulation):** Low-level subprocesses 3.1 Fetch Scenario, 3.2 Display Mock Header, 3.3 Capture Choice, 3.4 Heuristic Threat Evaluation, and 3.5 Return Indicator Explanations.
* **DFD Level 3 (Quiz Pipeline):** Subprocesses 4.1 Fetch Question Set, 4.2 Collect Answers, 4.3 Evaluate & Compute %, 4.4 Persist Score Record, and 4.5 Render Solution Breakdown.

---

## 5. Use Case Diagram
* **1. Use Case:** Models interactions between Student and Administrator actors with core use cases (Register, Login, Study Modules, Test Password, Practice Phishing Sim, Take Quiz, View Dashboard, Manage Questions).
* **2. Activity Diagram:** Delineates sequential user workflows from login authentication, dashboard branch, activity execution, automated evaluation, database persistence, to dashboard state updates.
* **3. Class Diagram:** Defines object-oriented domain models (`User`, `Topic`, `Question`, `Score`, `TopicProgress`), their attributes, types, visibility modifiers, cryptographic methods (`set_password`, `check_password`), and foreign-key cardinalities.

---

## 6. Data Dictionary
Comprehensive physical schema definitions:
* **`users`:** `id` (PK, Int), `username` (VarChar 80, Unique), `email` (VarChar 120, Unique), `password_hash` (VarChar 256), `is_admin` (Bool), `created_at` (DateTime).
* **`topics`:** `id` (PK, Int), `title` (VarChar 120), `slug` (VarChar 120, Unique), `icon` (VarChar 10), `description` (Text), `content` (Text), `order` (Int).
* **`questions`:** `id` (PK, Int), `topic_id` (FK -> topics.id), `question_text` (Text), `option_a..d` (VarChar 255), `correct_answer` (VarChar 1), `explanation` (Text), `created_at` (DateTime).
* **`scores`:** `id` (PK, Int), `user_id` (FK -> users.id), `topic_id` (FK -> topics.id), `score` (Int), `total` (Int), `percentage` (Float), `taken_at` (DateTime).
* **`topic_progress`:** `id` (PK, Int), `user_id` (FK -> users.id), `topic_id` (FK -> topics.id), `completed` (Bool), `completed_at` (DateTime).

---

## 7. Screenshots of Development Phase -1
* **UI Mockup 7.1:** User Registration & Dynamic Password Policy Validation.
* **UI Mockup 7.2:** Secure User Authentication & Login Interface.
* **UI Mockup 7.3:** Platform Homepage & Educational Hero Dashboard.
* **UI Mockup 7.4:** Learner Personal Dashboard & Module Progress Metrics.

---

## 8. Screenshots of Development Phase -2
* **UI Mockup 8.1:** Micro-Learning Security Module View with Checklists & Case Studies.
* **UI Mockup 8.2:** Real-Time Password Strength & Shannon Entropy Meter.
* **UI Mockup 8.3:** Experiential Phishing Email Simulator with Spoofed Headers.
* **UI Mockup 8.4:** Phishing Threat Indicator Breakdown & Red Flag Detection Review.

---

## 9. Screenshots of Development Phase -3
* **UI Mockup 9.1:** Standardized 40-Question Assessment Suite.
* **UI Mockup 9.2:** Automated Quiz Results & Pedagogical Explanatory Rationales.
* **UI Mockup 9.3:** Administrator Question Bank CRUD Management Panel.
* **UI Mockup 9.4:** Administrator Platform Telemetry & Score Analytics.

---

## 10. Conclusion
The Cybersecurity Awareness Training Platform fulfills all functional, architectural, and educational objectives for a Semester VI project in Bachelor of Science in Information Technology at Parul University. It successfully demonstrates the effectiveness of hands-on simulation over passive documentation in establishing proactive cyber hygiene habits.

---

## 11. Future Enhancement
1. **Dynamic Cryptographically Signed Certificates:** Programmatic synthesis of QR-verifiable PDF certificates.
2. **AI-Powered Adaptive Threat Engine:** Integration of LLM APIs for dynamic phishing scenario generation.
3. **Enterprise LMS Compliance:** Support for SCORM and xAPI interoperability.
4. **Gamified CTF Tournaments:** Real-time WebSocket competitions and institutional leaderboards.
5. **Cross-Platform Mobile Apps:** Native Android and iOS applications with push notifications.

---

## 12. References
1. Python Software Foundation (2024). Python 3.12 Documentation.
2. Pallets Projects (2024). Flask 3.0 Documentation.
3. SQLAlchemy Authors (2024). SQLAlchemy 2.0 Guide.
4. Neon Cloud Inc. (2024). Serverless PostgreSQL Architecture.
5. OWASP Foundation (2023). OWASP Top 10 Web Application Security Risks.
6. NIST (2024). Special Publication 800-63B: Digital Identity Guidelines.
7. Render Services Inc. (2024). Web Application Cloud Deployment Guide.
8. Werkzeug Development Team (2024). Security Utilities & Password Hashing.
9. Bootstrap Team (2024). Bootstrap v5.3 Documentation.
10. Mozilla Developer Network (2024). Web Security & Cryptography APIs.
11. Jinja Authors (2024). Jinja2 Template Engine Documentation.
12. CISA (2023). Cybersecurity Awareness Program Guidelines.
13. Shannon, C. E. (1948). A Mathematical Theory of Communication.
14. RFC 7519 (2015). JSON Web Token (JWT) Standards.
15. RFC 6238 (2011). TOTP: Time-Based One-Time Password Algorithm.
16. Parul University (2026). B.Sc. IT Project Curriculum Guidelines.

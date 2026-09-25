# 🎓 ACADEMIC PROJECT REPORT

## PROJECT TITLE:
# **CYBERSECURITY AWARENESS TRAINING PLATFORM**
### **Topic ID: #107 | Mini Project Submission**

---

### **Project Information**
* **Degree / Course**: Bachelor of Science in Information Technology (B.Sc. IT)
* **Domain**: Web Application Development & Cyber Security
* **Technologies**: Python, Flask, PostgreSQL (Neon Cloud), SQLAlchemy, HTML5, CSS3, Bootstrap 5, JavaScript
* **Deployment**: Render Cloud Platform
* **Version Control**: Git / GitHub

---

## 📑 TABLE OF CONTENTS
1. [Abstract](#1-abstract)
2. [Introduction & Problem Statement](#2-introduction--problem-statement)
3. [Objectives & Scope](#3-objectives--scope)
4. [Software Requirements Specification (SRS)](#4-software-requirements-specification-srs)
5. [System Design & Architecture](#5-system-design--architecture)
   - 5.1 System Architecture Diagram
   - 5.2 Entity-Relationship (ER) Diagram
   - 5.3 Data Flow Diagrams (DFD Level 0 & Level 1)
   - 5.4 Database Schema
6. [Module Description](#6-module-description)
7. [Security & Best Practices](#7-security--best-practices)
8. [Testing & Verification](#8-testing--verification)
9. [Conclusion & Future Enhancements](#9-conclusion--future-enhancements)
10. [References](#10-references)

---

## 1. Abstract
With the rapid increase in digital services, cyber threats such as phishing, social engineering, weak passwords, and ransomware have grown exponentially. Most cybersecurity breaches occur due to human error and lack of digital awareness rather than system vulnerabilities. 

This project, **"Cybersecurity Awareness Training Platform"**, is a full-stack educational web application designed to educate students, employees, and everyday internet users on safe digital practices. Built using **Python (Flask)**, **SQLAlchemy ORM**, **Neon Serverless PostgreSQL**, and a responsive **Bootstrap 5** frontend, the platform provides interactive learning modules, a real-time phishing email simulator, topic-based knowledge quizzes with immediate feedback, a dynamic user progress dashboard, and an administrative control panel for curriculum management.

---

## 2. Introduction & Problem Statement

### 2.1 Background
Human error accounts for over 90% of successful cyberattacks. While organizations invest heavily in firewalls and antivirus software, end-users often fall prey to deceptive social engineering tactics, phishing emails, and poor credential hygiene.

### 2.2 Problem Statement
Traditional cybersecurity awareness programs often consist of static PDF manuals or lengthy, unengaging video lectures that lack interactive evaluation. Users retain minimal practical knowledge and cannot recognize actual threats when encountered.

### 2.3 Proposed Solution
The proposed platform addresses this gap by offering:
- **Interactive Scenarios**: Users analyze realistic email samples to classify them as "Phishing" or "Safe" with immediate contextual explanations.
- **Micro-Learning Topics**: Concise, targeted modules covering 8 key cyber domains.
- **Automated Assessment**: Topic-wise multiple-choice quizzes that calculate scores, record progress, and guide users on areas needing improvement.
- **Centralized Admin Control**: Secure administrative tools to add, modify, or delete questions and view user engagement analytics.

---

## 3. Objectives & Scope

### 3.1 Primary Objectives
1. To develop an intuitive, responsive web application for cybersecurity education.
2. To implement a secure user authentication system with password hashing (`Werkzeug`).
3. To build an interactive simulation tool for detecting phishing communications.
4. To integrate a robust Quiz Assessment engine calculating real-time percentage scores.
5. To deploy the application with a cloud database (**Neon PostgreSQL**) and scalable web host (**Render**).

### 3.2 Project Scope
* **Users**: Can register, log in, browse cybersecurity topics, complete quizzes, simulate phishing scenarios, and review their dashboard progress.
* **Administrators**: Can monitor platform metrics, manage questions, and publish new cybersecurity modules.
* **Platform Accessibility**: Cross-device compatibility across desktops, tablets, and smartphones via responsive Bootstrap 5 design.

---

## 4. Software Requirements Specification (SRS)

### 4.1 Hardware Requirements
* **Processor**: Dual-core Intel/AMD 2.0 GHz or higher
* **RAM**: Minimum 4 GB (8 GB recommended)
* **Storage**: Minimum 500 MB free disk space for local development
* **Client Device**: Any standard PC, laptop, or smartphone with an active internet connection

### 4.2 Software Requirements
* **Operating System**: Windows 10/11, macOS, or Linux
* **Programming Language**: Python 3.11 / 3.12
* **Web Framework**: Flask 3.0.3 (WSGI Framework)
* **Database Engine**: PostgreSQL 16 (via Neon Serverless) / SQLite (Local dev)
* **Object-Relational Mapping (ORM)**: Flask-SQLAlchemy 3.1.1
* **Authentication**: Flask-Login 0.6.3
* **Production Web Server**: Gunicorn 22.0.0
* **Frontend Technologies**: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3.2, FontAwesome 6.5
* **Browser**: Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari

---

## 5. System Design & Architecture

### 5.1 System Architecture Diagram
The system implements a classic **Three-Tier Architecture** cleanly decoupling presentation, application logic, and data persistence:

```mermaid
flowchart TD
    Client["User / Web Browser\n(Desktop, Mobile)"]
    
    subgraph Frontend ["Presentation Layer (frontend/)"]
        HTML["HTML5 Templates (Jinja2)"]
        CSS["Bootstrap 5 + Custom CSS"]
        JS["Interactive JS (Phishing Sim & Alerts)"]
    end
    
    subgraph Backend ["Application / Logic Layer (backend/)"]
        App["Flask WSGI Engine (app.py)"]
        Blueprints["Modular Blueprints:\n• auth_bp\n• main_bp\n• quiz_bp\n• admin_bp"]
        Security["Security Controls:\n• Password Hashing (Werkzeug)\n• Session Management (Flask-Login)"]
        ORM["SQLAlchemy ORM"]
    end
    
    subgraph Database ["Data Tier (Cloud / Local)"]
        Postgres[("Neon Serverless\nPostgreSQL 16 (Production)")]
        SQLite[("SQLite 3\n(Local Fallback)")]
    end

    Client <-->|HTTPS Requests / Responses| Frontend
    Frontend <--> App
    App --> Blueprints
    Blueprints --> Security
    Blueprints --> ORM
    ORM <--> Postgres
    ORM -.-> SQLite
```

---

### 5.2 Entity-Relationship (ER) Diagram

```mermaid
erDiagram
    USERS ||--o{ SCORES : "records"
    USERS ||--o{ TOPIC_PROGRESS : "completes"
    TOPICS ||--o{ QUESTIONS : "contains"
    TOPICS ||--o{ SCORES : "evaluates"
    TOPICS ||--o{ TOPIC_PROGRESS : "tracks"

    USERS {
        int id PK
        string username "Unique"
        string email "Unique"
        string password_hash
        boolean is_admin
        datetime created_at
    }

    TOPICS {
        int id PK
        string title
        string slug "Unique"
        string icon
        text description
        text content
        int order
    }

    QUESTIONS {
        int id PK
        int topic_id FK
        text question_text
        string option_a
        string option_b
        string option_c
        string option_d
        string correct_answer "A, B, C, D"
        text explanation
        datetime created_at
    }

    SCORES {
        int id PK
        int user_id FK
        int topic_id FK
        int score
        int total
        float percentage
        datetime taken_at
    }

    TOPIC_PROGRESS {
        int id PK
        int user_id FK
        int topic_id FK
        boolean completed
        datetime completed_at
    }
```

---

### 5.3 Data Flow Diagrams

#### **Level 0 DFD (Context Level)**
```mermaid
flowchart LR
    User["Student / User"] <-->|Credentials, Quiz Answers, Progress| System["Cybersecurity Awareness System"]
    Admin["System Administrator"] <-->|Curriculum Management, User Reports| System
    System <-->|Read / Write Queries| DB[("Neon PostgreSQL Database")]
```

#### **Level 1 DFD**
```mermaid
flowchart TD
    User["User"] -->|Credentials| P1["1.0 Authentication Process"]
    P1 -->|Session Token| User
    P1 <-->|Verify Credentials| D1[("Users Table")]

    User -->|Select Topic| P2["2.0 Learning & Topic Viewer"]
    P2 <-->|Fetch Content| D2[("Topics Table")]
    P2 -->|Mark Complete| D3[("Topic Progress Table")]

    User -->|Submit Answers| P3["3.0 Quiz Engine"]
    P3 <-->|Fetch Questions| D4[("Questions Table")]
    P3 -->|Store Results| D5[("Scores Table")]
    P3 -->|Display Result & Review| User

    Admin["Admin"] -->|Add/Delete Question| P4["4.0 Admin Control"]
    P4 <-->|Update Questions| D4
    P4 <-->|View Analytics| D5
```

---

### 5.4 Database Schema

#### Table 1: `users`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary Key, Auto-increment | Unique identifier |
| `username` | Varchar(80) | Not Null, Unique | User handle |
| `email` | Varchar(120) | Not Null, Unique | User email address |
| `password_hash` | Varchar(256) | Not Null | Hashed password |
| `is_admin` | Boolean | Default: False | Administrator privilege flag |
| `created_at` | DateTime | Default: UTC Now | Account creation timestamp |

#### Table 2: `topics`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary Key, Auto-increment | Unique identifier |
| `title` | Varchar(120) | Not Null | Topic title |
| `slug` | Varchar(120) | Not Null, Unique | URL-friendly slug |
| `icon` | Varchar(10) | Default: 🔒 | Display emoji / icon |
| `description` | Text | Not Null | Brief summary |
| `content` | Text | Not Null | Full educational HTML body |
| `order` | Integer | Default: 0 | Display sequence order |

#### Table 3: `questions`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary Key, Auto-increment | Unique identifier |
| `topic_id` | Integer | Foreign Key (`topics.id`) | Associated topic |
| `question_text` | Text | Not Null | Question description |
| `option_a` | Varchar(255) | Not Null | Option A text |
| `option_b` | Varchar(255) | Not Null | Option B text |
| `option_c` | Varchar(255) | Not Null | Option C text |
| `option_d` | Varchar(255) | Not Null | Option D text |
| `correct_answer`| Varchar(1) | Not Null (`A`, `B`, `C`, `D`) | Correct option key |
| `explanation` | Text | Nullable | Educational explanation |

#### Table 4: `scores`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary Key, Auto-increment | Unique identifier |
| `user_id` | Integer | Foreign Key (`users.id`) | Submitting user |
| `topic_id` | Integer | Foreign Key (`topics.id`) | Evaluated topic |
| `score` | Integer | Not Null | Correct answers count |
| `total` | Integer | Not Null | Total questions count |
| `percentage` | Float | Not Null | Percentage calculation |
| `taken_at` | DateTime | Default: UTC Now | Exam submission timestamp |

#### Table 5: `topic_progress`
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary Key, Auto-increment | Unique identifier |
| `user_id` | Integer | Foreign Key (`users.id`) | Student identifier |
| `topic_id` | Integer | Foreign Key (`topics.id`) | Topic identifier |
| `completed` | Boolean | Default: False | Completion status flag |
| `completed_at` | DateTime | Nullable | Completion timestamp |

---

## 6. Module Description

### 6.1 Authentication Module (`routes/auth.py`)
* **Registration**: Validates uniqueness of usernames and emails, enforces an 8-character minimum password length, and securely hashes credentials using `generate_password_hash`.
* **Login & Session Management**: Authenticates users using `check_password_hash` and establishes secure HTTP session cookies managed via `Flask-Login`.
* **Access Control**: Implements `@login_required` decorators to prevent unauthorized access to sensitive pages.

### 6.2 Learning Modules (`routes/main.py`)
* Provides structured lessons on 8 crucial domains:
  1. 🔑 **Password Security**: Credential hygiene, password managers, and entropy.
  2. 🎣 **Phishing Attacks**: Recognizing spear phishing, smishing, and vishing.
  3. 🦠 **Malware Protection**: Ransomware, Trojans, viruses, and defense strategies.
  4. 👤 **Social Engineering**: Pretexting, baiting, quid-pro-quo, and tailgating.
  5. 🌐 **Safe Browsing**: SSL/TLS verification, malicious redirects, and privacy.
  6. 🔐 **Two-Factor Authentication (2FA)**: OTPs, TOTP authenticators, and hardware keys.
  7. 📶 **Public Wi-Fi Safety**: Man-in-the-Middle (MitM) attacks, evil twins, and VPNs.
  8. 📱 **Mobile Security**: App permissions, remote wipe, and biometric locks.

### 6.3 Phishing Awareness Simulator (`templates/phishing.html`)
* An interactive client-side simulation presenting realistic email scenarios.
* Users evaluate email headers, sender addresses, links, and urgent language to classify each communication as **Phishing** or **Safe**.
* Provides immediate feedback explaining why the email is dangerous or legitimate.

### 6.4 Quiz & Assessment Engine (`routes/quiz.py`)
* Dynamically fetches questions associated with a specific topic.
* Evaluates submitted choices, calculates raw scores and percentages, and logs performance records into the database.
* Renders an in-depth answer review page highlighting correct answers, incorrect selections, and explanatory rationales.

### 6.5 User Dashboard (`routes/main.py`)
* Computes real-time student analytics:
  * Total topics completed vs. remaining.
  * Comprehensive progress bar.
  * Historical quiz logs with date, score, and grade indicators.
  * Aggregate percentage average across all quizzes.

### 6.6 Admin Control Panel (`routes/admin.py`)
* Accessible only to accounts with `is_admin = True` enforced by a custom `@admin_required` decorator.
* Capabilities:
  * Platform overview (Total Users, Topics, Questions, and Quiz Attempts).
  * Question management (Add new multiple-choice questions with answer keys).
  * Question deletion with cascade safeguards.
  * System-wide review of student quiz scores.

---

## 7. Security & Best Practices

1. **Credential Protection**: Passwords are never stored in plaintext; they are transformed using salted cryptographic hashes (PBKDF2/SHA-256).
2. **Environment Variable Segregation**: Database URLs and secret keys are stored in environment variables (`.env`) and excluded from source control via `.gitignore`.
3. **SQL Injection Prevention**: All database interactions use parameterized queries provided by SQLAlchemy ORM, eliminating SQL injection vectors.
4. **Cross-Site Scripting (XSS) Mitigation**: Jinja2 automatic HTML escaping prevents injection of untrusted scripts into the DOM.
5. **Secure Transport Layer**: Production deployment utilizes HTTPS/TLS encryption provided by Render and SSL connection requirements by Neon PostgreSQL.

---

## 8. Testing & Verification

| Test Case ID | Test Scenario | Input Data | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | User Registration | Valid email, password (≥8 chars) | Account created, redirected to login | Account created successfully | **PASS** ✅ |
| **TC-02** | Duplicate User Handling | Existing registered email | Display error message | "Email already registered" alert | **PASS** ✅ |
| **TC-03** | Invalid Login | Correct email, wrong password | Reject login attempt | "Invalid email or password" alert | **PASS** ✅ |
| **TC-04** | Topic Progress Tracking | User views topic content | Status set to completed | Completed badge rendered, progress % updated | **PASS** ✅ |
| **TC-05** | Quiz Evaluation | Submit answers for topic #1 | Calculate score & store record | Score recorded in PostgreSQL, result page shown | **PASS** ✅ |
| **TC-06** | Phishing Simulator | Click "Phishing" on fraudulent email | Increase score, display rationale | Correct alert displayed with explanation | **PASS** ✅ |
| **TC-07** | Admin Route Authorization | Non-admin visits `/admin` | Access denied, redirect to home | "Admin access required" alert | **PASS** ✅ |
| **TC-08** | Database Failover | Cloud connection active | Direct queries to Neon DB | PostgreSQL responds with HTTP 200 | **PASS** ✅ |

---

## 9. Conclusion & Future Enhancements

### 9.1 Conclusion
The **Cybersecurity Awareness Training Platform** successfully fulfills all objectives set forth for this project. By integrating micro-learning content, experiential phishing simulations, dynamic quiz assessments, and cloud persistence, the platform bridges the critical divide between theoretical security concepts and practical threat recognition. The project demonstrates a production-grade full-stack architecture using modern industry-standard frameworks and cloud platforms.

### 9.2 Future Enhancements
* **Gamified Leaderboards**: Public ranking system to foster healthy learning competition.
* **Automated PDF Certificate Generation**: Dynamic generation of signed completion certificates upon achieving a passing score across all modules.
* **Email Verification & Password Reset**: Integration with SMTP services (e.g., SendGrid) for self-service credential recovery.
* **Simulated Phishing Email Dispatch**: Ability for administrators to dispatch mock phishing emails to registered student inboxes to test real-world vigilance.

---

## 10. References
1. Grinberg, M. (2018). *Flask Web Development: Developing Web Applications with Python*. O'Reilly Media.
2. PostgreSQL Global Development Group. (2024). *PostgreSQL 16 Documentation*. https://www.postgresql.org/docs/
3. National Institute of Standards and Technology (NIST). (2023). *Security and Privacy Controls for Information Systems and Organizations* (NIST SP 800-53).
4. Bootstrap Team. (2024). *Bootstrap v5.3 Documentation*. https://getbootstrap.com/docs/5.3/
5. OWASP Foundation. (2024). *OWASP Top 10 Web Application Security Risks*. https://owasp.org/www-project-top-ten/

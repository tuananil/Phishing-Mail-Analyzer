# Phishing Mail Analyzer 🛡️

A Python-based lightweight security tool designed to detect potential phishing attempts within email contents. This tool performs heuristic analysis based on social engineering keywords and suspicious/shortened URLs to generate a dynamic risk assessment report.

## 🚀 Features
- **Keyword Analysis:** Scans the email body for high-pressure social engineering tactics (e.g., "urgent", "account suspended", "verify").
- **URL Inspection:** Utilizes Regular Expressions (Regex) to extract links and flags suspicious URL shorteners commonly used in phishing campaigns (such as `bit.ly` or `tinyurl.com`).
- **Dynamic Risk Scoring:** Calculates an automated threat score and generates a color-coded cybersecurity report (Clean, Suspicious, Phishing).
- **Standalone Execution:** Runs instantly without requiring external file dependencies.

## ⚙️ How It Works
The tool calculates a dynamic **Risk Score** based on predefined security metrics:
* Each flagged phishing keyword adds **1 point**.
* Each shortened/suspicious URL adds **2 points**.

If the total score reaches **4 or higher**, the script triggers a **Red Alert**, indicating a confirmed phishing attempt.

## 💻 Technical Stack
- **Language:** Python 3.x
- **Core Modules:** `re` (Regular Expressions)

## 🏃‍♂️ How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/tuananil/Phishing-Mail-Analyzer.git](https://github.com/tuananil/Phishing-Mail-Analyzer.git)

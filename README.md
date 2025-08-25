# 🚀 AI Prompt Engineering Toolkit (`prompt-toolkit`)

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## **Overview**

**AI Prompt Engineering Toolkit** is a CLI tool that **uses AI to generate better AI prompts**. It analyzes user intent and automatically uses AI to craft optimized prompts for quality results, helping students, developers, content creators, and professionals to get more efficient outputs from any AI models.

No more trial and error or vague prompts this toolkit ensures **expert-level prompts every time**.

---

## **Core Concept**

Instead of pre-defined templates, the toolkit applies **meta-prompting**, a recursive AI approach where AI itself improves prompts based on your intent. This produces significantly better results than generic static prompts, making your AI interactions faster, smarter, and more accurate.

---

## **Key Features**

- ✅ **AI-Powered Prompt Optimization** – Dynamically generates high quality prompts.  
- ✅ **Dual Mode Operation** – Choose to view the optimized prompt only, or get the AI response instantly.  
- ✅ **Flexible Intent System** – Supports any user intent, not limited to templates.  
- ✅ **Beautiful CLI Interface** – Powered by Typer + Rich for professional terminal UI.  
- ✅ **Cross-Platform Executable** – Works on Windows, Mac, and Linux with a single executable (~12MB).  
- ✅ **Clean AI Responses** – Automatically filters out `<think>` tags and other meta-text for clarity.

---

## **Installation**

### **Executable (Recommended)**
Download the latest release for your OS from the [GitHub Releases](https://github.com/AathilFelix/prompt-toolkit/releases). No Python setup required.

```bash
# Example usage after download
prompt-toolkit improve summarize "I want to learn AI"
```

### From Source (Optional)

Requires Python 3.7+.

```bash
git clone https://github.com/AathilFelix/prompt-toolkit.git
cd prompt-toolkit
pip install -r requirements.txt
python src/cli.py improve summarize "I want to learn AI"
```

## **Usage**
### **Available Intents**
```bash
• summarize - Create concise summaries
• rewrite - Improve clarity and style
• questions - Generate thoughtful questions
• explain - Break down complex concepts
• brainstorm - Generate creative ideas
• analyze - Deep analytical insights
• debug - Troubleshoot problems
• plan - Create step-by-step plans
```
### **Generate an Optimized Prompt (Prompt Engineering Mode)**
```bash
prompt-toolkit-<os> improve <intent> <prompt-to-refine>
```

### **Usage Example**

```bash
prompt-toolkit-<os> improve summarize "I want to learn AI"
```
#### **Output**
```bash
Engineered Prompt:
"Act as an AI learning expert, and create a structured, step-by-step summary for someone beginning their journey to learn AI. Organize the summary into clear sections: foundational concepts (math, programming), key AI subfields (ML, DL, NLP), recommended resources (books, courses, tools), hands-on practice methods (projects, datasets), and common challenges with solutions. Assume a learner with basic tech proficiency but no prior AI experience. Use bullet points for conciseness, include 1-2 examples of real-world AI applications, and specify approximate timeframes for mastery. Format in plain text with clear headings, avoiding markdown. Make all resource recommendations up-to-date as of 2024."
```
### **Run AI Response**
```bash
prompt-toolkit-<os> improve summarize "I want to learn AI" --ai
```
<div style="text-align:center;">(OR)</div>

```bash
prompt-toolkit-<os> improve summarize "I want to learn AI" -a
```

### **Custom Intents**
```bash
prompt-toolkit-<os> improve study plan "machine learning basics"
```

## **Technical Details**
- Python 3.7+

- CLI Framework: Typer + Rich

- AI Integration: Hack Club AI (free tier, no API key required)

- Executable Packaging: PyInstaller (~12MB, cross-platform)

- Response Cleaning: Regex filters for `<think>` and meta-text
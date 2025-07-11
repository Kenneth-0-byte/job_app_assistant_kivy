# 📱 Job Application Assistant (Kivy Android App)

A simple Android mobile application built with Python and Kivy to help users generate customized job application cover letters.

## ✨ Features

- Input recipient name, company, position, and skills
- Generate a professional cover letter
- Mobile-friendly design with Kivy

## 🗂️ Project Structure

```
job_app_assistant_kivy/
│
├── main.py          # Core app logic
├── jobapp.kv        # UI layout (Kivy language)
├── buildozer.spec   # Generated after running `buildozer init`
```

## 🚀 How to Build APK

### 1. System Setup (Linux or WSL required)
```bash
sudo apt update
sudo apt install python3-pip git zip unzip openjdk-17-jdk -y
pip install --upgrade pip
pip install Cython virtualenv kivy buildozer
```

### 2. Download and Unzip Project
```bash
unzip job_app_assistant_kivy.zip
cd job_app_assistant_kivy
```

### 3. Initialize Buildozer
```bash
buildozer init
```

Edit `buildozer.spec`:
```
package.name = JobAppAssistant
package.domain = org.sbu.jobapp
requirements = python3,kivy
source.include_exts = py,kv
orientation = portrait
source.url = https://github.com/Kenneth-0-byte/job_app_assistant_kivy.git
```

### 4. Build APK
```bash
buildozer -v android debug
```

### 5. Install on Device
Copy the APK from the `bin/` folder to your Android phone and install.

---

## 📦 Source Code
Explore the full code and contribute on GitHub:

[Job App Assistant Repository](https://github.com/Kenneth-0-byte/job_app_assistant_kivy)

---

## 🛠 Future Improvements

- Save application history
- Export cover letter to PDF
- Email integration
- GUI polish

---

## 👤 Developer
Created by Sibusiso Kenneth (SBU)
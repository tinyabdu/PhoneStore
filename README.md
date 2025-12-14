# 📱 Phone Store – Flet Application

A modern, responsive **Phone Store** application built using **Flet (Python)**. This project features a clean UI, component-based architecture, and smooth navigation, designed for **desktop**.

---

## 🚀 Features

* 🌐 platform UI (Windows, macOS, Linux)
* 🎨 Custom components: Sidebar, Header, Notification Modal, Search Bar
* 🔍 Search and filter products from the database
* 🧭 Smooth navigation using Flet `View` & routes
* 🗄️ Database support (SQLite)
* 📦 Clean and scalable folder structure

---

## 📁 Project Structure

```
sample/
│── components/
│     ├── header.py
│     ├── sidebar.py
│     ├── notification_modal.py
│     └── searchbar.py
│
│── views/
│     ├── home_page.py
│     ├── add_page.py
│     └── setting_page.py
│
│── database/
│     └── models.py
│
│── main.py
│── README.md
│── requirements.txt
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the project

```bash
git clone https://github.com/tinyabdu/PhoneStore.git
cd PhoneStore
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python main.py or 
flet run 
```

---

## 🧱 Tech Stack

| Technology              | Purpose                           |
| ----------------------- | --------------------------------- |
| **Python**              | Core programming language         |
| **Flet**                | UI framework                      |
| **SQLite**              | Database management               |

---

---
## 🎬 Showcase

Here is a demo video of the project:

[Watch Demo Video](showcase/dome_video.mp4) 
[Watch Demo Video](showcase/2_x264_gif.gif) 


<!-- ## 🔧 Customization

All UI components are reusable. Example:

```python
from components.header import Header

page.add(Header(title="Phone Store"))
```

--- -->

<!-- ## 🐛 Known Issues

* Route blinking may occur if views are created incorrectly
* Notification modal must be appended to `page.overlay`
* Some animations require Flet v0.22+

--- -->

## 🤝 Contributing

Contributions are welcome! Please open an issue before submitting a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Abdullahi Haruna (tinyabdu)**
Developer from **Alldotpy**

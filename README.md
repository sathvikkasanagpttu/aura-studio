# ✨ AURA STUDIO

### Spatial Drawing & Gesture Control in the Browser

AURA Studio is an interactive computer-vision drawing workspace that turns webcam hand movement into a touchless creative interface. It combines **MediaPipe Hands**, **HTML5 Canvas**, **JavaScript**, and browser APIs to provide real-time drawing, gesture commands, shape assistance, replay, analytics, and calibration.

> **Your hands become the controller.**

## 🚀 Highlights

- 🖐️ Real-time hand landmark tracking with MediaPipe
- ✍️ Touchless air drawing using pinch gestures
- 🎨 Pencil, ink, eraser, magic and shape-assisted tools
- 🔷 Smart shape assistance for common geometric forms
- ✊ Fist-based radial command menu
- ✌️ Two-finger tool selector
- 👍 Thumbs-up confirmation and 👎 thumbs-down undo/reject actions
- 🖐️ Open-palm tracking pause
- 🔍 Two-hand zoom and pan
- 🎬 Drawing replay/capture workflow
- 📊 Session analytics and gesture telemetry
- ⚙️ Guided calibration controls
- 🖱️ Mouse/click fallback for the main interface
- 📱 Responsive layout for smaller screens
- ♿ Reduced-motion support and keyboard focus states
- 🔒 Webcam processing is performed in the browser; the project does not contain a custom image-upload backend

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| UI | HTML5, CSS3 |
| Interaction | Vanilla JavaScript |
| Computer Vision | MediaPipe Hands |
| Drawing | HTML5 Canvas 2D |
| Audio | Web Audio API |
| Launcher | Python + Streamlit |
| Build | Python |
| External runtime assets | MediaPipe CDN + Google Fonts |

## 📁 Project Structure

```text
AuraStudio-master/
├── app.py                 # Streamlit launcher
├── build.py               # Builds the standalone HTML bundle
├── index.html             # Generated production bundle
├── requirements.txt       # Python dependency
├── README.md
├── favicon.svg
├── HeroBanner.png
├── AuraDrawingGIF.gif
├── AuraDrawingVideo.mp4
├── screenshots/
└── src/
    ├── index.html         # HTML template
    ├── styles.css         # UI and responsive styling
    ├── app.js             # Main application logic
    ├── gestures.js        # Gesture state machine
    ├── shapes.js          # Shape recognition/assistance
    ├── calibration.js     # Calibration helpers
    ├── particles.js       # Visual particle effects
    └── audio.js           # Audio feedback
```

## 💻 Requirements

- Python **3.9+**
- A modern browser: **Google Chrome, Microsoft Edge, or Safari**
- A working webcam
- Internet access for the MediaPipe CDN and Google Fonts

### Important camera note

Browser camera access works reliably on **`localhost`/`127.0.0.1` or HTTPS**. Opening the HTML directly with a `file://` URL may prevent camera access.

---

# ▶️ Run with Streamlit — Recommended

### 1. Open Terminal

Go to the project folder:

```bash
cd /path/to/AuraStudio-master
```

### 2. Create a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Rebuild the production HTML

Run this whenever you change files inside `src/`:

```bash
python build.py
```

You should see a message similar to:

```text
Built production bundle: .../index.html
Bundle size: ... bytes
```

### 5. Start AURA Studio

```bash
streamlit run app.py
```

Streamlit will print a local address, normally similar to:

```text
Local URL: http://localhost:8501
```

Open that address in your browser.

### 6. Allow camera access

When the browser asks for webcam permission, choose **Allow**.

Then:

1. Click **Start Creating**
2. Place your hand in front of the webcam
3. Wait for **CAMERA READY**
4. Use the gesture guide to control the studio

---

# 🌐 Run the Standalone HTML

You can also run the generated `index.html` without Streamlit.

First build it:

```bash
python build.py
```

Then start a local web server:

```bash
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000
```

This method is useful when you want to test the frontend as a normal browser application.

---

# 🖐️ Gesture Controls

| Gesture | Action |
|---|---|
| ☝️ Index finger | Move the virtual cursor |
| 🤏 Pinch | Draw |
| 👍 Thumbs up | Confirm |
| 👎 Thumbs down | Undo / reject |
| 🖐️ Open palm | Pause tracking |
| ✊ Fist | Open command radial menu |
| ✌️ Two fingers | Open tool selector |
| 🖐️🖐️ Two hands | Zoom / pan |

Gesture recognition uses a short stability window to reduce accidental triggers.

---

# 🎨 Main Workspace

### Canvas Studio
The main drawing environment with webcam tracking, virtual cursor, canvas, toolbar, and performance telemetry.

### Gesture Lab
View and test supported hand gestures and their current recognition state.

### Magic Engine
Explore assisted drawing and visual effects.

### Replay
Review captured drawing activity.

### Analytics
Inspect session statistics such as strokes, gestures, and movement.

### Calibration
Tune detection confidence, tracking confidence, smoothing, pinch threshold, and the active tracking area.

---

# 🛠️ Troubleshooting

### Camera is blocked

1. Check the browser's camera permission for `localhost`.
2. Make sure no other application is exclusively using the webcam.
3. Reload the page after granting permission.
4. Use `http://localhost:8501` or another localhost address instead of opening `index.html` with `file://`.

### `streamlit: command not found`

Use:

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

### Changes in `src/` are not appearing

Rebuild the bundle:

```bash
python build.py
```

Then restart or refresh the browser.

### MediaPipe does not load

AURA loads MediaPipe from a CDN. Check your internet connection and browser developer console for network errors.

### Drawing area looks wrong after resizing

Refresh the page after changing browser zoom or window size. The application automatically recalculates the canvas dimensions when the studio tab becomes active.

---

# 🔐 Privacy

AURA uses the browser webcam for real-time hand tracking. The project does not include a custom server-side webcam upload pipeline. Camera permission is controlled by the browser.

Third-party runtime resources currently include MediaPipe packages and Google Fonts loaded from their respective CDNs.

---

# 🏗️ Development Workflow

Edit the source files:

```text
src/index.html
src/styles.css
src/*.js
```

Then rebuild:

```bash
python build.py
```

For the Streamlit version:

```bash
streamlit run app.py
```

For the standalone version:

```bash
python3 -m http.server 8000
```

---

# 📸 Screenshots & Demo Assets

The repository includes UI screenshots, a GIF demonstration, and a full MP4 demonstration in the project root and `screenshots/` directory.

---

# 📄 License

Add your preferred open-source or proprietary license before publishing this repository.

---

## ⭐ Project Goal

AURA Studio is designed as a portfolio-ready demonstration of browser-based computer vision, gesture interaction, creative tooling, and real-time canvas rendering.

**Built to explore what a computer interface can become when the mouse is no longer the only controller.**

# VendCo Website — Setup Guide

## What's inside
- `app.py` — the Flask app (main Python file)
- `templates/` — HTML pages (base, home, about, contact)
- `requirements.txt` — Python packages needed

## Pages
- `/` → Home page (hero, services, stats, call to action)
- `/about` → About page (story, values)
- `/contact` → Contact page (form + contact details)

---

## How to run it

### Step 1 — Install Python
Make sure Python is installed. Check by running:
```
python --version
```
If not installed: https://www.python.org/downloads/

---

### Step 2 — Install Flask
In your terminal, run:
```
pip install flask
```

---

### Step 3 — Run the website
Navigate to the project folder:
```
cd vending_site
```
Then run:
```
python app.py
```

---

### Step 4 — Open in browser
Go to: http://127.0.0.1:5000

That's it! 🎉

---

## Customizing the site
- Change the business name: search for "VendCo" across the HTML files and replace it
- Update phone/email: edit `templates/contact.html`
- Change colors: edit the `:root` variables in `templates/base.html`
- Add photos: put images in `static/images/` and reference them in the HTML

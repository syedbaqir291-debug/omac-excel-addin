# OMAC Universal Data Analyzer — Excel Add-in
**By S M Baqir · OMAC Developers**

---

## 🚀 Quick Install (5 minutes)

### Step 1 — Host on GitHub Pages (FREE)
1. Create a GitHub account at github.com if you don't have one
2. Create a new repository named exactly: `omac-excel-addin`
3. Upload all these files to the repository
4. Go to **Settings → Pages → Source → main branch** → Save
5. Note your GitHub username (e.g. `smbaqir`)

### Step 2 — Update the manifest.xml
Replace every `YOUR-GITHUB-USERNAME` in `manifest.xml` with your actual GitHub username.
Example: `https://smbaqir.github.io/omac-excel-addin/taskpane.html`

### Step 3 — Sideload in Excel Desktop
1. Open Excel
2. Go to **File → Options → Trust Center → Trust Center Settings**
3. Click **Trusted Add-in Catalogs**
4. Add catalog URL: `https://YOUR-USERNAME.github.io/omac-excel-addin/`
5. Restart Excel
6. Go to **Insert → My Add-ins → Shared Folder** → OMAC Data Analyzer → Add

### Step 4 — OR Sideload via XML (easier)
1. In Excel, go to **Insert → Get Add-ins → Upload My Add-in**
2. Browse to `manifest.xml` and click Upload
3. OMAC Analyzer button appears in the **Home** ribbon

---

## 📊 Features
- **Module 1 — Data Analyzer**: Reads any Excel sheet directly, no file upload
- **Module 2 — Compliance**: Hand Hygiene, audit compliance with speedometer
- **Export HTML**: Download standalone dashboard
- **Write to Excel**: Paste stats table back into a new sheet
- **All features**: Slicers, per-panel charts, colour pickers, time format, sort order

## 📁 Files
```
manifest.xml      ← Install this in Excel
taskpane.html     ← Main dashboard UI (hosted on GitHub Pages)
commands.html     ← Required by Office.js
assets/
  icon-16.png
  icon-32.png
  icon-64.png
  icon-80.png
README.md
```

## ⚡ Local Testing (no GitHub needed)
1. Install Node.js
2. Run: `npx http-server . --cors -p 3000`
3. Replace GitHub URLs in manifest.xml with `https://localhost:3000/`
4. Use `npx office-addin-dev-certs install` for HTTPS

---
*OMAC Developers · S M Baqir*

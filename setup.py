"""
OMAC Excel Add-in Setup Helper
Run: python3 setup.py YOUR-GITHUB-USERNAME
"""
import sys, re

if len(sys.argv) < 2:
    username = input("Enter your GitHub username: ").strip()
else:
    username = sys.argv[1].strip()

with open('manifest.xml', 'r') as f:
    content = f.read()

updated = content.replace('YOUR-GITHUB-USERNAME', username)

with open('manifest.xml', 'w') as f:
    f.write(updated)

print(f"✅ manifest.xml updated with username: {username}")
print(f"   URLs now point to: https://{username}.github.io/omac-excel-addin/")
print()
print("Next steps:")
print("  1. Upload all files to GitHub repo 'omac-excel-addin'")
print("  2. Enable GitHub Pages (Settings → Pages → main branch)")
print("  3. In Excel: Insert → Get Add-ins → Upload My Add-in → select manifest.xml")

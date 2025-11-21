# GitHub Push Commands

Run these commands one by one in your terminal:

## Step 1: Pull remote changes and merge
```bash
git pull origin main --allow-unrelated-histories
```

If it asks for a merge message, just save and close the editor (press `Ctrl+X` if nano, or `:wq` if vim)

## Step 2: Push to GitHub
```bash
git push -u origin main
```

## Step 3: Verify on GitHub
Go to: https://github.com/AbdulSattar-07/Protfolio

---

## If you get any merge conflicts:

```bash
git status
# Check which files have conflicts

# Then add all files
git add .

# Commit the merge
git commit -m "Merge remote and local changes"

# Push again
git push -u origin main
```

---

## Alternative: Force push (if you want to overwrite remote)
⚠️ Only use this if you're sure you want to replace everything on GitHub:

```bash
git push -u origin main --force
```

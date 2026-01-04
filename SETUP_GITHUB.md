# GitHub Repository Setup

## Current Status

Your repository is set up with a placeholder remote URL. You need to update it with your actual GitHub username.

## Update GitHub Remote

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
# Check current remote
git remote -v

# Update remote URL (replace YOUR_USERNAME)
git remote set-url origin https://github.com/YOUR_USERNAME/Driver-UI-vehicle-system.git

# Verify
git remote -v
```

## Push to GitHub

Once you've updated the remote URL:

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit with GMSL deserializer integration"

# Push to GitHub
git push -u origin master
```

## If Repository Doesn't Exist on GitHub

1. Go to https://github.com/new
2. Create a new repository named `Driver-UI-vehicle-system`
3. **Don't** initialize with README, .gitignore, or license (we already have these)
4. Copy the repository URL
5. Update the remote:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/Driver-UI-vehicle-system.git
   ```
6. Push:
   ```bash
   git push -u origin master
   ```

## GMSL Deserializer as Submodule (Optional)

If you want to track the GMSL deserializer as a git submodule instead:

```bash
# Remove the current directory
Remove-Item -Recurse -Force .\gmsl-deserializer

# Add as submodule
git submodule add https://github.com/antmicro/gmsl-deserializer.git gmsl-deserializer

# Commit the submodule
git commit -m "Add GMSL deserializer as submodule"
```





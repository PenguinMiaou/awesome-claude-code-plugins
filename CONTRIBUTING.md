# Contributing to Awesome Claude Code Plugins

Thanks for your interest in contributing!

## Adding a Plugin

1. **Fork** this repository
2. **Add a row** to the matching category table in `README.md`
3. Use this format:
   ```markdown
   | **[plugin-name](https://github.com/owner/repo)**<br><sub>owner</sub> | One-line description. | ★ |
   ```
4. If your repo ships a plugin marketplace, append the install commands to the description cell:
   ```markdown
   One-line description.<br>`/plugin marketplace add owner/repo`<br>`/plugin install plugin-name@marketplace-name`
   ```
5. Bump the category count in the **Contents** table and the `plugins` badge
6. **Submit a Pull Request**

## Requirements

- Plugin must be related to Claude Code
- Repo must be public and have a README
- One plugin per PR preferred
- Keep descriptions concise (under 120 characters, install commands excluded)
- Leave the Stars cell as `★`. A daily job fills in the count and sorts each category by stars

## Categories

If your plugin doesn't fit an existing category, propose a new one in your PR description.

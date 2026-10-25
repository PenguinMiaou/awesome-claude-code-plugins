# Awesome Claude Code Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, categorized directory of Claude Code plugins — with one-line install commands, compatibility info, and community ratings.

Unlike other lists, this one focuses on **practical usability**: every entry includes install instructions, verified compatibility, and real-world use cases.

## Contents

- [Official](#official)
- [Communication Channels](#communication-channels)
- [Multi-Agent & Orchestration](#multi-agent--orchestration)
- [Memory & Context](#memory--context)
- [Code Quality & Review](#code-quality--review)
- [Browser & Web](#browser--web)
- [DevOps & Infrastructure](#devops--infrastructure)
- [AI Model Integration](#ai-model-integration)
- [Productivity & Workflow](#productivity--workflow)
- [UI & Visualization](#ui--visualization)
- [Language & Framework Specific](#language--framework-specific)
- [Security](#security)
- [Contributing](#contributing)

---

## Official

- [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — Anthropic-managed directory of high quality plugins. The canonical source. `Official`

## Communication Channels

Plugins that bridge Claude Code with messaging platforms.

- [claude-channel-whatsapp](https://github.com/PenguinMiaou/claude-channel-whatsapp) — WhatsApp channel plugin via MCP. Chat with Claude from WhatsApp. ![Stars](https://img.shields.io/github/stars/PenguinMiaou/claude-channel-whatsapp?style=flat-square)
  ```bash
  gh repo clone PenguinMiaou/claude-channel-whatsapp ~/.claude/plugins/claude-channel-whatsapp
  ```
- [nanoclaw](https://github.com/qwibitai/nanoclaw) — Connects to WhatsApp, Telegram, Slack, Discord, Gmail. Runs in containers. ![Stars](https://img.shields.io/github/stars/qwibitai/nanoclaw?style=flat-square)

## Multi-Agent & Orchestration

Coordinate multiple Claude Code instances working together.

- [claude-hive](https://github.com/PenguinMiaou/claude-hive) — Cross-window multi-agent coordination with worktree isolation, GitHub PR workflows, and conflict detection. ![Stars](https://img.shields.io/github/stars/PenguinMiaou/claude-hive?style=flat-square)
  ```bash
  gh repo clone PenguinMiaou/claude-hive ~/.claude/plugins/claude-hive
  ```
- [claude-octopus](https://github.com/nyldn/claude-octopus) — Put up to 8 AI models on every coding task. Blind spots surface before you ship. ![Stars](https://img.shields.io/github/stars/nyldn/claude-octopus?style=flat-square)
- [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) — Teams-first multi-agent orchestration. ![Stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-claudecode?style=flat-square)
- [ruflo](https://github.com/ruvnet/ruflo) — Multi-agent swarm orchestration platform with RAG integration. ![Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square)
- [vibe-kanban](https://github.com/BloopAI/vibe-kanban) — Get 10X more out of Claude Code with kanban-style task management. ![Stars](https://img.shields.io/github/stars/BloopAI/vibe-kanban?style=flat-square)

## Memory & Context

Plugins that enhance Claude Code's memory and context awareness.

- [claude-mem](https://github.com/thedotmack/claude-mem) — Auto-captures sessions, compresses with AI, injects context into future sessions. ![Stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square)
- [claude-code-router](https://github.com/musistudio/claude-code-router) — Use Claude Code as coding infrastructure foundation. Control model interaction. ![Stars](https://img.shields.io/github/stars/musistudio/claude-code-router?style=flat-square)

## Code Quality & Review

- [claude-review-loop](https://github.com/hamelsmu/claude-review-loop) — Automated code review loop with Codex. ![Stars](https://img.shields.io/github/stars/hamelsmu/claude-review-loop?style=flat-square)
- [cc-blueprint-toolkit](https://github.com/croffasia/cc-blueprint-toolkit) — Smart blueprint-driven development. ![Stars](https://img.shields.io/github/stars/croffasia/cc-blueprint-toolkit?style=flat-square)
- [claude-code-lsps](https://github.com/Piebald-AI/claude-code-lsps) — LSP server integration for Claude Code. ![Stars](https://img.shields.io/github/stars/Piebald-AI/claude-code-lsps?style=flat-square)

## Browser & Web

- [superpowers-chrome](https://github.com/obra/superpowers-chrome) — Direct Chrome browser control via DevTools Protocol. Zero dependencies. ![Stars](https://img.shields.io/github/stars/obra/superpowers-chrome?style=flat-square)
- [browserbase-plugin](https://github.com/browserbase/claude-code-plugin) — Cloud browsers with Claude Code instead of local Chrome. ![Stars](https://img.shields.io/github/stars/browserbase/claude-code-plugin?style=flat-square)

## DevOps & Infrastructure

- [agent-skills](https://github.com/hashicorp/agent-skills) — Skills and plugins for HashiCorp products (Terraform, Vault, etc). ![Stars](https://img.shields.io/github/stars/hashicorp/agent-skills?style=flat-square)
- [pinecone-plugin](https://github.com/pinecone-io/pinecone-claude-code-plugin) — Official Pinecone vector database integration. ![Stars](https://img.shields.io/github/stars/pinecone-io/pinecone-claude-code-plugin?style=flat-square)

## UI & Visualization

- [claude-hud](https://github.com/jarrodwatts/claude-hud) — Shows what's happening: context usage, active tools, running agents, todo progress. ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square)

## Language & Framework Specific

- [claude-code-elixir](https://github.com/georgeguimaraes/claude-code-elixir) — Plugin marketplace for Elixir development. ![Stars](https://img.shields.io/github/stars/georgeguimaraes/claude-code-elixir?style=flat-square)
- [serena](https://github.com/oraios/serena) — MCP toolkit with semantic retrieval and editing. The IDE for your agent. ![Stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square)

## Productivity & Workflow

- [Docsy](https://github.com/getremcp/docsy-plugin) — Claude Code plugin for OAuth-connected, version-specific developer docs with source citations. ![Stars](https://img.shields.io/github/stars/getremcp/docsy-plugin?style=flat-square)
- [gstack](https://github.com/garrytan/gstack) — Garry Tan's exact Claude Code setup: 23 opinionated tools. ![Stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square)
- [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) — 340 plugins + 1367 agent skills with CCPI package manager. ![Stars](https://img.shields.io/github/stars/jeremylongshore/claude-code-plugins-plus-skills?style=flat-square)
- [career-ops](https://github.com/santifer/career-ops) — AI-powered job search system with 14 skill modes. ![Stars](https://img.shields.io/github/stars/santifer/career-ops?style=flat-square)
- [ralph-wiggum-marketer](https://github.com/muratcankoylan/ralph-wiggum-marketer) — Autonomous AI copywriter plugin. ![Stars](https://img.shields.io/github/stars/muratcankoylan/ralph-wiggum-marketer?style=flat-square)

## Plugin Development

- [claude-code-plugin-template](https://github.com/ivan-magda/claude-code-plugin-template) — GitHub template for creating plugin marketplaces. Includes scaffolding, validation, hooks, skills, agents, and CI/CD. ![Stars](https://img.shields.io/github/stars/ivan-magda/claude-code-plugin-template?style=flat-square)

## Marketplaces & Directories

- [superpowers-marketplace](https://github.com/obra/superpowers-marketplace) — Curated plugin marketplace. ![Stars](https://img.shields.io/github/stars/obra/superpowers-marketplace?style=flat-square)
- [plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives) — Plugins for power users. ![Stars](https://img.shields.io/github/stars/team-attention/plugins-for-claude-natives?style=flat-square)
- [skills-curated](https://github.com/trailofbits/skills-curated) — Community-vetted plugin marketplace. ![Stars](https://img.shields.io/github/stars/trailofbits/skills-curated?style=flat-square)

---

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

To add a plugin:
1. Fork this repo
2. Add your plugin to the appropriate category
3. Include: repo link, one-line description, star badge, and install command (if applicable)
4. Submit a PR

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

<div align="center">

# Awesome Claude Code Plugins

**A curated directory of Claude Code plugins, skills, and MCP integrations.**

[![Awesome](https://img.shields.io/badge/awesome-list-FC60A8?style=flat-square&logo=awesomelists&logoColor=white)](https://awesome.re)
[![Plugins](https://img.shields.io/badge/plugins-37-D97757?style=flat-square)](#contents)
[![Last commit](https://img.shields.io/github/last-commit/PenguinMiaou/awesome-claude-code-plugins?style=flat-square&label=updated)](https://github.com/PenguinMiaou/awesome-claude-code-plugins/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-2ea44f?style=flat-square)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)](https://creativecommons.org/publicdomain/zero/1.0/)

</div>

Entries within each category are ordered by GitHub stars. Star counts update live.

## Contents

| Category | Plugins | Category | Plugins |
| :--- | :---: | :--- | :---: |
| [Official](#official) | 1 | [Browser & Web](#browser--web) | 2 |
| [Marketplaces & Directories](#marketplaces--directories) | 4 | [DevOps & Infrastructure](#devops--infrastructure) | 4 |
| [Communication Channels](#communication-channels) | 2 | [Language & Framework Specific](#language--framework-specific) | 3 |
| [Multi-Agent & Orchestration](#multi-agent--orchestration) | 6 | [Productivity & Workflow](#productivity--workflow) | 5 |
| [Memory & Context](#memory--context) | 2 | [UI & Notifications](#ui--notifications) | 3 |
| [AI Model Integration](#ai-model-integration) | 1 | [Plugin Development](#plugin-development) | 1 |
| [Code Quality & Review](#code-quality--review) | 3 | | |

## Installing a plugin

Plugins that ship a marketplace install from inside Claude Code:

```text
/plugin marketplace add owner/repo
/plugin install plugin-name@marketplace-name
```

Run `/plugin` to browse and manage what you have installed. MCP servers and standalone tools list their own install steps in their README.

---

## Official

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)**<br><sub>anthropics</sub> | Anthropic-managed directory of high-quality Claude Code plugins. The canonical source. | ![Stars](https://img.shields.io/github/stars/anthropics/claude-plugins-official?style=flat-square&label=%E2%98%85) |

## Marketplaces & Directories

Curated collections you can add as a marketplace in one command.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)**<br><sub>jeremylongshore</sub> | Model-agnostic agent-skills platform with verified adapters and the ccpi package manager. | ![Stars](https://img.shields.io/github/stars/jeremylongshore/tons-of-skills-marketplace?style=flat-square&label=%E2%98%85) |
| **[superpowers-marketplace](https://github.com/obra/superpowers-marketplace)**<br><sub>obra</sub> | Curated Claude Code plugin marketplace. | ![Stars](https://img.shields.io/github/stars/obra/superpowers-marketplace?style=flat-square&label=%E2%98%85) |
| **[plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives)**<br><sub>team-attention</sub> | Claude Code plugins for power users. | ![Stars](https://img.shields.io/github/stars/team-attention/plugins-for-claude-natives?style=flat-square&label=%E2%98%85) |
| **[skills-curated](https://github.com/trailofbits/skills-curated)**<br><sub>trailofbits</sub> | Community-vetted plugin marketplace from Trail of Bits. | ![Stars](https://img.shields.io/github/stars/trailofbits/skills-curated?style=flat-square&label=%E2%98%85) |

## Communication Channels

Bridge Claude Code with messaging platforms.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[nanoclaw](https://github.com/nanocoai/nanoclaw)**<br><sub>nanocoai</sub> | Container-isolated agent that connects to WhatsApp, Telegram, Slack, Discord, and Gmail. | ![Stars](https://img.shields.io/github/stars/nanocoai/nanoclaw?style=flat-square&label=%E2%98%85) |
| **[claude-channel-whatsapp](https://github.com/PenguinMiaou/claude-channel-whatsapp)**<br><sub>PenguinMiaou</sub> | Chat with Claude Code from WhatsApp through an MCP channel.<br>`/plugin marketplace add PenguinMiaou/claude-channel-whatsapp`<br>`/plugin install whatsapp@local` | ![Stars](https://img.shields.io/github/stars/PenguinMiaou/claude-channel-whatsapp?style=flat-square&label=%E2%98%85) |

## Multi-Agent & Orchestration

Coordinate multiple Claude Code instances working together.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[ruflo](https://github.com/ruvnet/ruflo)**<br><sub>ruvnet</sub> | Multi-agent swarm orchestration with adaptive memory and vector RAG. | ![Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square&label=%E2%98%85) |
| **[oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)**<br><sub>Yeachan-Heo</sub> | Teams-first multi-agent orchestration for Claude Code. | ![Stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-claudecode?style=flat-square&label=%E2%98%85) |
| **[vibe-kanban](https://github.com/BloopAI/vibe-kanban)**<br><sub>BloopAI</sub> | Kanban-style task management for Claude Code, Codex, and other coding agents. | ![Stars](https://img.shields.io/github/stars/BloopAI/vibe-kanban?style=flat-square&label=%E2%98%85) |
| **[claude-octopus](https://github.com/nyldn/claude-octopus)**<br><sub>nyldn</sub> | Runs several AI models on the same task so disagreements surface before you ship. | ![Stars](https://img.shields.io/github/stars/nyldn/claude-octopus?style=flat-square&label=%E2%98%85) |
| **[claude-hive](https://github.com/PenguinMiaou/claude-hive)**<br><sub>PenguinMiaou</sub> | Cross-window multi-agent coordination with worktree isolation, PR workflows, and conflict detection. | ![Stars](https://img.shields.io/github/stars/PenguinMiaou/claude-hive?style=flat-square&label=%E2%98%85) |
| **[RuleStack](https://skillworks.thecompound.tech/rulestack)**<br><sub>Compound Labs</sub> | Nightly index of AGENTS.md, CLAUDE.md, Cursor, Copilot, and other agent rule files, scored by stack. | — |

## Memory & Context

Give Claude Code memory that lasts across sessions.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[claude-mem](https://github.com/thedotmack/claude-mem)**<br><sub>thedotmack</sub> | Captures session activity, compresses it with AI, and injects relevant context into future sessions. | ![Stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square&label=%E2%98%85) |
| **[tree-ring-memory](https://github.com/TerminallyLazy/tree-ring-memory-claude-plugin)**<br><sub>TerminallyLazy</sub> | Local-first recall, audit, and forgetting guidance for Claude Code.<br>`/plugin marketplace add TerminallyLazy/tree-ring-memory-claude-plugin`<br>`/plugin install tree-ring-memory@tree-ring-memory` | ![Stars](https://img.shields.io/github/stars/TerminallyLazy/tree-ring-memory-claude-plugin?style=flat-square&label=%E2%98%85) |

## AI Model Integration

Route Claude Code to other models and providers.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[claude-code-router](https://github.com/musistudio/claude-code-router)**<br><sub>musistudio</sub> | Routes Claude Code requests across models and providers from one local control plane. | ![Stars](https://img.shields.io/github/stars/musistudio/claude-code-router?style=flat-square&label=%E2%98%85) |

## Code Quality & Review

Review loops, language servers, and structured development workflows.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[claude-review-loop](https://github.com/hamelsmu/claude-review-loop)**<br><sub>hamelsmu</sub> | Automated code review loop with Codex. | ![Stars](https://img.shields.io/github/stars/hamelsmu/claude-review-loop?style=flat-square&label=%E2%98%85) |
| **[claude-code-lsps](https://github.com/Piebald-AI/claude-code-lsps)**<br><sub>Piebald-AI</sub> | Plugin marketplace of LSP servers for Claude Code. | ![Stars](https://img.shields.io/github/stars/Piebald-AI/claude-code-lsps?style=flat-square&label=%E2%98%85) |
| **[cc-blueprint-toolkit](https://github.com/croffasia/cc-blueprint-toolkit)**<br><sub>croffasia</sub> | Blueprint-driven development workflow. | ![Stars](https://img.shields.io/github/stars/croffasia/cc-blueprint-toolkit?style=flat-square&label=%E2%98%85) |

## Browser & Web

Let Claude Code drive a browser.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[superpowers-chrome](https://github.com/obra/superpowers-chrome)**<br><sub>obra</sub> | Direct Chrome control through the DevTools Protocol. Zero dependencies. | ![Stars](https://img.shields.io/github/stars/obra/superpowers-chrome?style=flat-square&label=%E2%98%85) |
| **[claude-code-plugin](https://github.com/browserbase/claude-code-plugin)**<br><sub>browserbase</sub> | Cloud browsers for Claude Code instead of local Chrome. *Archived by its maintainers.* | ![Stars](https://img.shields.io/github/stars/browserbase/claude-code-plugin?style=flat-square&label=%E2%98%85) |

## DevOps & Infrastructure

Cloud, infrastructure, deployment, and remote machines.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[agent-skills](https://github.com/hashicorp/agent-skills)**<br><sub>hashicorp</sub> | Agent skills and plugins for Terraform, Vault, and other HashiCorp products. | ![Stars](https://img.shields.io/github/stars/hashicorp/agent-skills?style=flat-square&label=%E2%98%85) |
| **[pinecone-claude-code-plugin](https://github.com/pinecone-io/pinecone-claude-code-plugin)**<br><sub>pinecone-io</sub> | Official Pinecone vector database marketplace. | ![Stars](https://img.shields.io/github/stars/pinecone-io/pinecone-claude-code-plugin?style=flat-square&label=%E2%98%85) |
| **[ReMCP](https://github.com/getremcp/remcp)**<br><sub>getremcp</sub> | OAuth-protected terminal, file, browser, and desktop access to computers you pair. | ![Stars](https://img.shields.io/github/stars/getremcp/remcp?style=flat-square&label=%E2%98%85) |
| **[shipvela](https://github.com/stefanautomateed/shipvela-codex)**<br><sub>stefanautomateed</sub> | Owner-approved website publishing through an OAuth MCP connector. Requires a Shipvela account. | ![Stars](https://img.shields.io/github/stars/stefanautomateed/shipvela-codex?style=flat-square&label=%E2%98%85) |

## Language & Framework Specific

Tooling for particular languages and package ecosystems.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[serena](https://github.com/oraios/serena)**<br><sub>oraios</sub> | MCP toolkit for semantic code retrieval and editing. The IDE for your agent. | ![Stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square&label=%E2%98%85) |
| **[elixir-agent-tools](https://github.com/georgeguimaraes/elixir-agent-tools)**<br><sub>georgeguimaraes</sub> | Elixir development skills with optional Mix checks and Expert language server integration. | ![Stars](https://img.shields.io/github/stars/georgeguimaraes/elixir-agent-tools?style=flat-square&label=%E2%98%85) |
| **[installed-api](https://github.com/ajwann/installed-api)**<br><sub>ajwann</sub> | Answers API questions from the Python and Node packages actually installed in your project. | ![Stars](https://img.shields.io/github/stars/ajwann/installed-api?style=flat-square&label=%E2%98%85) |

## Productivity & Workflow

Opinionated setups and task-specific skill sets.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[gstack](https://github.com/garrytan/gstack)**<br><sub>garrytan</sub> | Garry Tan's Claude Code setup: 23 opinionated tools for product, design, engineering, and QA roles. | ![Stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square&label=%E2%98%85) |
| **[career-ops](https://github.com/career-ops-hq/career-ops)**<br><sub>career-ops-hq</sub> | Job search agent that scores listings against your CV and tailors resumes and cover letters. | ![Stars](https://img.shields.io/github/stars/career-ops-hq/career-ops?style=flat-square&label=%E2%98%85) |
| **[NotFair](https://github.com/nowork-studio/notfair-plugin)**<br><sub>nowork-studio</sub> | SEO, GEO, and ad skills with Google Ads, Meta Ads, Search Console, and GA4 MCP. Formerly toprank. | ![Stars](https://img.shields.io/github/stars/nowork-studio/notfair-plugin?style=flat-square&label=%E2%98%85) |
| **[ralph-wiggum-marketer](https://github.com/muratcankoylan/ralph-wiggum-marketer)**<br><sub>muratcankoylan</sub> | Autonomous AI copywriter. | ![Stars](https://img.shields.io/github/stars/muratcankoylan/ralph-wiggum-marketer?style=flat-square&label=%E2%98%85) |
| **[Docsy](https://github.com/getremcp/docsy-plugin)**<br><sub>getremcp</sub> | Version-specific developer docs with source citations over OAuth MCP. | ![Stars](https://img.shields.io/github/stars/getremcp/docsy-plugin?style=flat-square&label=%E2%98%85) |

## UI & Notifications

See what Claude Code is doing, and get told when it needs you.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[claude-hud](https://github.com/jarrodwatts/claude-hud)**<br><sub>jarrodwatts</sub> | Shows context usage, active tools, running agents, and todo progress. | ![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%E2%98%85) |
| **[agent-notifications](https://github.com/777genius/agent-notifications)**<br><sub>777genius</sub> | Desktop and webhook alerts with sounds and click-to-focus on macOS, Linux, and Windows. | ![Stars](https://img.shields.io/github/stars/777genius/agent-notifications?style=flat-square&label=%E2%98%85) |
| **[claude-codex-windows-notify](https://github.com/Tomauskasz/claude-codex-windows-notify)**<br><sub>Tomauskasz</sub> | Native Windows popups for Claude Code, Codex, and OpenCode with session preview and click-to-focus. | ![Stars](https://img.shields.io/github/stars/Tomauskasz/claude-codex-windows-notify?style=flat-square&label=%E2%98%85) |

## Plugin Development

Build and distribute your own plugins.

| Plugin | Description | Stars |
| :--- | :--- | :---: |
| **[claude-code-plugin-template](https://github.com/ivan-magda/claude-code-plugin-template)**<br><sub>ivan-magda</sub> | GitHub template for plugin marketplaces with scaffolding, validation, hooks, skills, agents, and CI/CD. | ![Stars](https://img.shields.io/github/stars/ivan-magda/claude-code-plugin-template?style=flat-square&label=%E2%98%85) |

---

## Contributing

Add a row to the matching category table and open a pull request. The row format and requirements are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, the contributors have waived all copyright to this list.

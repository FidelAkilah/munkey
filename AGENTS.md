# AGENTS.md — MUNKEY (MUN Global)

This file provides tool-agnostic context for any AI coding agent (Claude Code, Copilot, Cursor, Windsurf, etc.).

## What is MUNKEY?

MUNKEY is an AI-powered Model United Nations (MUN) learning platform for Indonesia's MUN circuit. It combines real-time MUN news, an AI tutor called DiplomAI, skill video tutorials, a conference directory, and community discussion forums.

## Architecture

- **Backend**: Django 5.1 REST API with Django REST Framework
- **Frontend**: Next.js 16 SPA with React 19, TypeScript, Tailwind CSS 4
- **Database**: PostgreSQL on Supabase
- **AI**: OpenAI API for DiplomAI (coaching, feedback, question generation)
- **Auth**: JWT (SimpleJWT on Django, NextAuth on Next.js)
- **Deploy**: Vercel (frontend) + Render (backend)

## Key Django Apps

| App | Purpose |
|-----|---------|
| `accounts` | Custom User model with roles (Junior/Senior/Admin) |
| `curriculum` | DiplomAI — AI lessons, practice questions, submissions, feedback, chat |
| `news` | Articles with admin approval workflow (PENDING/APPROVED/REJECTED) |
| `community` | Comments/discussion on articles |
| `directory` | MUN conference locations with lat/long for map display |
| `skills` | Categorized YouTube skill tutorial videos |
| `core` | Django settings, JWT auth middleware, URL routing |

## Coding Standards

### Python / Django
- Use class-based views (APIView or ViewSet) for all endpoints
- Serializers for all request/response validation
- Keep business logic in views or dedicated service files (e.g., `ai_service.py`), not in models
- Use `IsAuthenticated` or custom permissions on protected endpoints
- Follow PEP 8 naming conventions

### TypeScript / React / Next.js
- Functional components with arrow functions only
- TypeScript interfaces (not type aliases) for data shapes
- Tailwind CSS for all styling — no Bootstrap, no CSS modules, no inline styles
- Use Next.js App Router (`src/app/`) file-based routing
- Client components must have `"use client"` directive at top
- Use `fetch` with `Authorization: Bearer` header for API calls

### General
- Never commit `.env` files, API keys, or secrets
- Keep AI prompts centralized in `curriculum/ai_service.py`
- Content safety: respect `is_junior_safe` and `is_restricted` flags
- Article workflow: all articles start as PENDING, require admin approval
- Comments have `is_approved` flag for moderation

## DiplomAI — The AI Tutor

DiplomAI ("Bongo the Strategist") is the AI coaching system in `curriculum/ai_service.py`. It handles:

1. **Submission Review** — Evaluates student work (speeches, draft resolutions, negotiations) and returns structured JSON feedback with scores, strengths, improvements, and suggestions
2. **Question Generation** — Creates practice questions by category (SPEECH, DRAFT, NEGOTIATION, RESEARCH, PROCEDURE, GENERAL) and difficulty level
3. **Chat Coaching** — Persistent conversational sessions guiding students through MUN concepts

Categories: SPEECH, DRAFT, NEGOTIATION, RESEARCH, PROCEDURE, GENERAL

## Safety & Moderation

- **Junior users** (JR role) see only `is_junior_safe` content
- **Article approval** pipeline prevents unreviewed content from appearing
- **Comment moderation** via `is_approved` flag
- Never expose raw API keys or database credentials in frontend code

# Copilot Instructions — MUNKEY (MUN Global)

## Project Overview

MUNKEY is an AI-powered MUN learning platform. Django REST API backend + Next.js 16 frontend.

## Coding Style

- Always use TypeScript interfaces instead of type aliases
- Use functional components with arrow functions
- Use Tailwind CSS utility classes for all styling — never Bootstrap or inline styles
- Use Next.js App Router file-based routing (`src/app/`)
- Client components must start with `"use client"` directive
- Python code follows PEP 8
- Use class-based views (APIView/ViewSet) in Django

## Conventions

- API calls use `fetch` with `Authorization: Bearer {token}` header
- All API endpoints are prefixed with `/api/`
- Django serializers handle all request/response validation
- AI prompts live in `curriculum/ai_service.py` — keep them centralized
- When writing MUN-related content logic, ensure the AI-summary metadata is always included
- Content must respect `is_junior_safe` and `is_restricted` safety flags
- Articles follow PENDING → APPROVED → REJECTED workflow
- User roles: Junior (JR), Senior (SR), Admin (AD)

## Key Patterns

- Authentication: NextAuth CredentialsProvider → Django SimpleJWT
- Protected routes: check session token in `src/proxy.ts` middleware
- DiplomAI feedback returns structured JSON: `overall_score`, `strengths`, `improvements`, `detailed_feedback`, `suggestions`
- Curriculum categories: SPEECH, DRAFT, NEGOTIATION, RESEARCH, PROCEDURE, GENERAL

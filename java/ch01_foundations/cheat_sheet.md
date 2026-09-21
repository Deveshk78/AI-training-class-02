# Chapter 1 Cheat Sheet

## Core idea
Build AI applications with clean layering and explicit service boundaries.

## Main components
- controller
- service
- retrieval layer
- model provider abstraction
- unit tests

## Why Java matters here
Java provides structure, explicit types, and strong enterprise integration patterns.

## Interview answer template
> “I model the AI system as a layered Java service: a user-facing API, a business service, a retrieval service, and a model abstraction. That keeps the design testable and explainable in interviews.”

## Design principles
- Keep model access behind an interface
- Favor small service methods
- Keep orchestration explicit
- Test the business logic independently

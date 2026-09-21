# Chapter 1 Interview Q&A

## 1. Why use Java for AI services?
Java is a strong choice when you need enterprise service patterns, strong typing, testability, and integration with existing backend systems.

## 2. What is a good architecture for AI applications in Java?
A controller, service layer, retrieval component, model client, and observability layer give a clean separation of concerns.

## 3. Why abstract the model provider?
It lets you swap providers, use mocks for tests, and keep the main logic stable.

## 4. How do you keep the service testable?
Inject dependencies, isolate model providers, and avoid hard-coded runtime environment assumptions.

## 5. What is the main trade-off?
Java tends to be more verbose than Python, but it offers stronger enterprise structure and maintainability.

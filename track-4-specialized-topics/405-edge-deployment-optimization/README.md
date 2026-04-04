@ftai v2.0 lang:en

@document
  title: "Edge Deployment & Optimization"
  author: "FolkTech AI"
  created: 2026-04-04
  schema: "ftai-academy-course"

@config
  id: "405"
  track: 4
  status: "not-started"
  duration: "3-4 hours"
  prerequisites: ["103"]
  tags: ["edge-deployment", "quantization", "optimization", "deep-dive"]
  preview: true
@end

# Course 405: Edge Deployment & Optimization

**Track:** Specialized Topics
**Duration:** 3-4 hours
**Prerequisites:** Course 103
**Status:** Not Started

## What You'll Learn

By the end of this course you will:
- Apply quantization strategies (Q4, Q5, Q8, fp16) and understand the quality/speed tradeoff
- Manage KV cache effectively to maximize context length on limited hardware
- Profile memory usage during inference
- Optimize models for Apple Silicon using MLX
- Optimize models for x86 using llama.cpp
- Design and run a proper benchmarking methodology for local inference
- Deploy models in resource-constrained environments

## Prerequisites

- Course 103: Hands-On Local AI Setup

## Course Content

Quantization strategies in depth, KV cache management, memory profiling, optimizing for Apple Silicon (MLX), optimizing for x86 (llama.cpp), benchmarking methodology, resource-constrained deployment.

## Who This Is For

Developers who need to run AI models efficiently on hardware without cloud access — embedded systems, clinical edge devices, air-gapped environments, or simply users who want maximum performance from their local machine.

## Materials

- [ ] Course document (.docx)
- [ ] Lab exercises

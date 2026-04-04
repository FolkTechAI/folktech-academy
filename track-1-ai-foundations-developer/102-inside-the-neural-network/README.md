@ftai v2.0 lang:en

@document
  title: "Inside the Neural Network"
  author: "FolkTech AI"
  created: 2026-04-04
  schema: "ftai-academy-course"

@config
  id: "102"
  track: 1
  status: "draft-complete"
  duration: "3-4 hours"
  prerequisites: ["101"]
  tags: ["neural-networks", "developer"]
  preview: true
@end

# Course 102: Inside the Neural Network

**Track:** AI Foundations (Developer)
**Duration:** 3-4 hours
**Prerequisites:** Course 101
**Status:** Draft Complete

## What You'll Learn

By the end of this course you will:
- Trace a forward pass through a neural network by hand
- Understand where weights come from and how training discovers them
- Explain the training loop: forward pass, loss, gradient, update
- Understand activation functions and why nonlinearity matters
- Know how backpropagation flows gradients through layers
- Understand embeddings as learned numerical representations
- Explain self-attention (Q, K, V) and why it matters
- Describe the full transformer architecture

## Prerequisites

- Course 101: AI for Developers

## Course Content

Works through the internals of a neural network from first principles: forward passes, weights, the training loop (forward → loss → gradient → update), activation functions, backpropagation, embeddings, self-attention (Q/K/V), and the full transformer architecture.

## Who This Is For

Developers who completed Course 101 and want to understand what's actually happening inside the models they use — not just how to call an API, but what the network is doing mathematically.

## Materials

- [x] Course document (.docx) - AI_Field_Guide_For_Developers_v2.docx (Section 9)

## Companion Resources

- "Understanding LLMs from Scratch Using Middle School Math" by Rohit Patel
  https://medium.com/data-science/understanding-llms-from-scratch-using-middle-school-math-e602d27ec876

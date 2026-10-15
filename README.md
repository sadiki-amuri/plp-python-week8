# PLP Academy Python Week 8 Assignment: Dynamic Multi-Tool Kit

An interactive multi-purpose terminal dashboard built with modular design principles using Python.

## How to Run the Toolkit
Ensure you have Python installed on your environment, then invoke the main file directly inside your terminal space:
```bash
python toolkit.py
```

## Reflection
Building the multi-tool application required combining interactive programmatic execution flows with defensive validation boundaries. The hardest part of this assignment was structuring the inner task tracking execution loops so that returning to the sub-menu parameters would not interfere with parent main menu loop selections. A tricky bug occurred within the number-guessing module where text strings instead of numeric integers would crash structural expressions, which was resolved by implementing string evaluation `.isdigit()` validation rules before processing variable casting. If given an extra week to iterate on this codebase, I would incorporate external JSON serialization utilities to write saved task collection states directly into permanent file streams so list logs persist across executions.

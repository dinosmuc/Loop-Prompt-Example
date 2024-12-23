# OpenAI Loop Prompt Processor
A Python tool that enables chained prompt processing through OpenAI's API. This tool takes the output of a previous prompt and processes it through multiple iterations with loop prompt, where each item in the output becomes input for a new prompt.
## What It Does
. Takes two main inputs:
  - Previous prompt output (a string containing multiple items/topics)
  - A prompt object  for processing each item
. Standardizes the input into a clean list format
. Processes each item individually through api call with prompt object as user message and list item as context. 
. Combines all responses into a final output
## Features
 **Input Standardization**: Automatically converts various text formats into a structured list
 **Iterative Processing**: Processes each item from the previous output individually
 **Flexible Input Handling**: Accepts:
 - Comma-separated lists
 - Bullet points
 - Numbered lists
 - Raw text
 **Detailed Logging**: Shows progress and results at each step


##Loop Prompt Impilmentation

A Python tool that enables chained prompt processing through OpenAI's API. This tool processes multiple items through a structured prompt template using GPT-4o, with comprehensive token tracking and detailed logging.

## What It Does

The processor takes two main inputs:
1. Previous prompt output (a string containing multiple items/topics)
2. A prompt object template that defines the analysis framework

### Core Features

- **Input Standardization**
  - Converts various text formats into Python lists using GPT-4o-mini
  - Handles multiple input formats (lists, comma-separated text, raw text)
  - Cleans and validates input data

- **Iterative Processing**
  - Processes each item individually through GPT-4o
  - Maintains context consistency across iterations
  - Tracks token usage for both input and output

- **Comprehensive Logging**
  - Detailed progress tracking for each processing step
  - Token usage statistics (input/output tokens)
  - Clear separation between items with formatted dividers

- **Structured Output**
  - Returns both individual results and combined output
  - Maintains formatting consistency
  - Includes processing statistics

## Technical Details

- Uses OpenAI's API with GPT-4o and GPT-4o-mini models
- Implements environment variable management through dotenv
- Provides detailed error handling and input validation
- Returns processed results in multiple formats:
  - List of individual responses
  - Combined string output with dividers
  - Total token usage statistics

## Example Use Case

The included template is designed for market research and trend analysis, featuring:
- Structured analysis framework
- Definition and core concepts
- Industry applications
- Future trends
- Market significance
- Related concepts

## Output Format

Returns a list containing:
1. List of individual processed responses
2. Combined output string with dividers
3. Total input tokens used
4. Total output tokens used

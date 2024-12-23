from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the client with the API key from environment variables
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


# This template is used for development and testing purposes only
prompt_object_template = """
Actor/Persona: A data analyst with expertise in market research and trend analysis.
Environment Context: A research environment focused on analyzing industry keywords and market trends.
Elaborate Challenge Description: Analyze the provided keyword to understand its significance, context, and potential applications.
Data Handling: Input consists of a single keyword for comprehensive analysis. No sensitive data involved.
Objective: To provide detailed insights about the keyword including its relevance, applications, and market impact.
Audience: Business strategists, researchers, and domain experts.
Task: Perform a thorough analysis of the keyword covering:
1. Definition and core concepts
2. Current industry applications
3. Future trends and potential
4. Related keywords and concepts
5. Market significance
Default Action: If the keyword is ambiguous, provide analysis for the most common interpretation.
Writing Style: Analytical, fact-based, and comprehensive.
Output Format: Structured analysis with clear sections for each aspect of the keyword analysis.
References: Include relevant industry sources and research papers when applicable.
"""


# These topics are just examples and used for testing only
previus_prompt_output = """
Machine Learning Applications in Healthcare,
Natural Language Processing for Customer Service,
Computer Vision in Autonomous Vehicles
"""









def loop_implementation(previus_prompt_output, prompt_object):
    
    # Converts any text input into a properly formatted Python list string using OpenAI API
    # Returns a string like: "['item1', 'item2', 'item3']"
    def standardize_input(input_text):
        print("\n" + "="*50)
        print("STANDARDIZATION PROCESS STARTED")
        print("="*50)
        print(f"Original input text:\n{input_text}")
        
        standardize_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Convert the following text into a clean list format. Extract distinct topics or items. Output as a Python-style list with each item properly quoted, like: ['item1', 'item2', 'item3']. Ensure items are trimmed of whitespace and properly formatted."},
                {"role": "user", "content": input_text}
            ]
        )
        
        # Add token tracking
        input_tokens = standardize_completion.usage.prompt_tokens
        output_tokens = standardize_completion.usage.completion_tokens
        
        standardized_list_str = standardize_completion.choices[0].message.content
        print("\nStandardized string format:")
        print(f"{standardized_list_str}")
        print(f"Input tokens: {input_tokens}")
        print(f"Output tokens: {output_tokens}")
        
        try:
            items_list = eval(standardized_list_str)
        except:
            items_list = [item.strip(" '\"[]") for item in standardized_list_str.split(',')]
        
        print("\nFinal standardized list:")
        print(f"{items_list}")
        print("="*50 + "\n")
        
        return [
            items_list,
            input_tokens,
            output_tokens
        ]




    # Function to process a list of items with a given prompt object using GPT-4o
    # Takes a string input that should contain a list of items and a prompt object
    # Returns combined output of all processed items separated by dividers
    def loop_prompt(previus_prompt_output, prompt_object):
        print("\n" + "="*50)
        print("PROMPT PROCESSING STARTED")
        print("="*50)
        print("Checking input format...")
        
        total_input_tokens = 0
        total_output_tokens = 0
        
        try:
            items_list = eval(previus_prompt_output)
            if not isinstance(items_list, list):
                print("Input is not in list format - standardizing...")
                standardized = standardize_input(previus_prompt_output)
                items_list = standardized[0]
                total_input_tokens += standardized[1]
                total_output_tokens += standardized[2]
            else:
                print("Input is already in correct list format")
        except:
            print("Input requires standardization...")
            standardized = standardize_input(previus_prompt_output)
            items_list = standardized[0]
            total_input_tokens += standardized[1]
            total_output_tokens += standardized[2]
        
        print("\nItems to process:")
        for i, item in enumerate(items_list, 1):
            print(f"{i}. {item}")
        
        output_list = []
        for i, item in enumerate(items_list, 1):
            print("\n" + "-"*50)
            print(f"Processing item {i}/{len(items_list)}: {item}")
            print("-"*50)
            
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": f"{prompt_object}\n\nContext: {item}"}
                ]
            )
            
            # Add token tracking
            total_input_tokens += completion.usage.prompt_tokens
            total_output_tokens += completion.usage.completion_tokens
            
            result = completion.choices[0].message.content
            output_list.append(result)
            
            print(f"\nResult for '{item}':")
            print(result)
            print(f"Input tokens: {completion.usage.prompt_tokens}")
            print(f"Output tokens: {completion.usage.completion_tokens}")
        
        print("\n" + "="*50)
        print("PROCESSING COMPLETED")
        print("="*50)
        print(f"Total items processed: {len(items_list)}")
        print(f"Total input tokens: {total_input_tokens}")
        print(f"Total output tokens: {total_output_tokens}")
        
        combined_output_string = "\n\n" + "="*30 + "\n\n".join(output_list)
        
        return [
            output_list,
            combined_output_string,
            total_input_tokens,
            total_output_tokens
        ]
    
    # Call loop_prompt with the provided arguments
    return loop_prompt(previus_prompt_output, prompt_object)





loop_implementation(previus_prompt_output, prompt_object_template)


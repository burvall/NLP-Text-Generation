# Python file for Paperspace Gradient NLP Text Generation Tutorial example
# It runs the GPT-2 model from HuggingFace: https://huggingface.co/gpt2
#
# The Workflow is triggered when its YAML file is present in the .gradient/workflows/ directory
# in a GitHub repository linked to the user's Gradient project
# It clones this repo and then in turn calls this file
# This file outputs the generated text to outputs.txt in a Gradient-managed Dataset
# The Workflow runs on the Paperspace HuggingFace NLP container (paperspace/transformers-gpu:0.4.0)
# See the Gradient documentation page for more details: ...
#
# The 4 values under "Settings" below can be altered to generate different text
# If the resulting updated version of this file is uploaded to the repo .gradient/workflows/
# directory, the Workflow will be rerun, and a new output.txt file will be generated
#
# Last updated: Sep 13th 2021

# Setup
from transformers import pipeline, set_seed

# Settings
random_seed = 42
max_length = 30
num_return_sequences = 5
initial_sentence = "Hello, I'm a language model,"

# Create generator that uses GPT-2
generator = pipeline('text-generation', model='gpt2')

# Random seed for text generation
set_seed(random_seed)

# Run the generator
output = generator(initial_sentence, max_length = max_length, num_return_sequences = num_return_sequences)

# Write the output to a file
with open('output.txt', 'w') as f:
    ival = 1
    for val in output:
        print('---\nOutput {} of {}\n---\n'.format(ival, num_return_sequences), file=f)
        print(val['generated_text'], file=f)
        if ival < num_return_sequences: print(file=f)
        ival += 1

print('Done')

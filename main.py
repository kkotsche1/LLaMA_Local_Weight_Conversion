import subprocess

#Installing requirements
command = ["pip", "install", "-r", "requirements.txt"]
subprocess.run(command)

command = ['pip', 'uninstall', 'transformers']
subprocess.run(command)

#Installing transformers library from github

command = ['pip', 'install', 'git+https://github.com/huggingface/transformers']
subprocess.run(command)


model_size = "7B"
input_dir = 'C:/Users/Admin/Downloads/LLaMA'
output_dir = './llama_7b_hf'

#Conversion
command = ['python', 'convert_llama_weights_to_hf.py', '--input_dir', input_dir, '--model_size', model_size, '--output_dir', output_dir]
subprocess.run(command)
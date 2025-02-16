from llama_cpp import Llama

models_dir = "/home/wes/repos/github/ggerganov/llama.cpp/models"
llm = Llama(model_path=models_dir + "/qwen2.5-coder-0.5b-instruct-q8_0.gguf", verbose=True)
# verbose=True dumps model details
# this is enough to dump model info to STDOUT... don't need to parse out specific values here

# vocab_size = llm.n_vocab()
# print("Vocabulary size:", vocab_size)

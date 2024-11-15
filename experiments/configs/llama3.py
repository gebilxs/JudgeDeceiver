import os

os.sys.path.append("..")
from configs.template import get_config as default_config

def get_config():
    
    config = default_config()

    config.transfer = True
    config.logfile = ""

    config.progressive_goals = True
    config.stop_on_success = True
    config.tokenizer_paths = [
        "meta-llama/Meta-Llama-3-8B-Instruct"
    ]
    config.tokenizer_kwargs = [{"use_fast": False}]
    config.model_paths = [
        "meta-llama/Meta-Llama-3-8B-Instruct"
   ]
    config.model_kwargs = [
        {"low_cpu_mem_usage": True, "use_cache": False, "temperature": 0.0}
    ]
    config.conversation_templates = ["llama-3"]
    config.devices = ["cuda:0"]

    return config
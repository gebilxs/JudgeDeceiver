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
        "mistralai/Mistral-7B-Instruct-v0.2"
    ]
    config.tokenizer_kwargs = [{"use_fast": False}]
    config.model_paths = [
        "mistralai/Mistral-7B-Instruct-v0.2"
   ]
    config.model_kwargs = [
        {"low_cpu_mem_usage": True, "use_cache": False}
    ]
    config.conversation_templates = ["mistral"]
    config.devices = ["cuda:0"]

    return config

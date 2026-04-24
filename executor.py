#routes commands
#excutes
from command_registry import command_map
import config



def execute(intent,query):
    if intent ==config.INTENT_EXIT:
        return config.EXIT_SIGNAL
    
    if intent == config.INTENT_UNKNOWN:
        return config.UNKNOWN_RESPONSE
    
    if intent in command_map:
        return command_map[intent](query)
    
    return config.UNKNOWN_RESPONSE
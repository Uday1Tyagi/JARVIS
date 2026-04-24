#stores commmand

from system_control import open_youtube,tell_time
from system_control import remember_information, recall_information,list_memory
import config

command_map={
    config.INTENT_OPEN_YOUTUBE:open_youtube,
    config.INTENT_TIME:tell_time,
    config.INTENT_REMEMBER: remember_information,
    config.INTENT_RECALL: recall_information,
    config.INTENT_LIST_MEMORY:list_memory,
}   
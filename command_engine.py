#Brain of this system
#detects intent

import config

INTENT_KEYWORDS = {
    config.INTENT_OPEN_YOUTUBE: ["youtube", "open youtube"],
    config.INTENT_TIME: ["time", "current time", "what's the time"],
    config.INTENT_EXIT: ["exit", "quit", "shutdown", "bye"],
     config.INTENT_RECALL: ["what is my", "tell me my"],
     config.INTENT_LIST_MEMORY: ["what do you know about me", "tell me about me"],
    config.INTENT_REMEMBER: ["my", "remember my"],
  
}

def classify_command(query):
    query = query.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in query:
                return intent

    return config.INTENT_UNKNOWN

#connects everything
from voice import speak,takeCommand,wishMe
from command_engine import classify_command
from system_control import tell_time,open_youtube,handle_confirmation
from executor import execute
import config
from logger import log

# it is to print the time
# print(tell_time())

wishMe()

while True:
    query=takeCommand()
    log(f"User said: {query}")

    from session_manager import get_pending

    pending = get_pending()

    # 🔥 If confirmation is pending, block normal flow
    if pending["key"]:
        confirmation_response = handle_confirmation(query)

        if confirmation_response:
            speak(confirmation_response)

        continue   # Always skip classification until resolved

    intent=classify_command(query)
    log(f"Intent detected: {intent}")


    response=execute(intent,query)   
    log(f"Response: {response}")

    if response==config.EXIT_SIGNAL:
        speak("Shutting down. GOODBYE.")
        break
    else:
  #  print("Response from executor:", response)
      speak(response)


    
    #small delapy bfore listenng again
    import time
    time.sleep(config.SLEEP_TIME)

print("Main Started")

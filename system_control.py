# Actions of this system
#performs actions
import webbrowser
import datetime
from memory.memory_manager import set_memory, get_memory
from session_manager import set_pending, get_pending, clear_pending
import config

def open_youtube(query):
    webbrowser.open("https://youtube.com")
    return "Opening youtube"

def tell_time(query):
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The time is {strTime}"



def remember_information(query):
    from memory.memory_manager import load_memory, save_memory

    data = load_memory()

    if "user" not in data:
        data["user"] = {}

    query = query.replace("remember", "").strip()

    if "my" in query and "is" in query:
        try:
            parts = query.split("my")[-1].strip()
            key, value = parts.split("is", 1)

            key = key.strip()
            value = value.strip()

            # 🔥 Check if key already exists
            if key in data["user"]:
                old_value = data["user"][key]

                # store pending update in session
                set_pending(key, value)

                return f"I already know your {key} is {old_value}. Do you want to update it?"

            # If key does not exist
            data["user"][key] = value
            save_memory(data)

            return f"Okay, I will remember that your {key} is {value}."

        except:
            return "I could not understand what to remember."

    return "Please tell me in format: My ___ is ___"

def recall_information(query):
    from memory.memory_manager import load_memory

    data = load_memory()

    if "user" not in data:
        return "I do not have any stored information yet."

    if "my" in query:
        key = query.split("my")[-1].strip().replace("?", "")

        value = data["user"].get(key)

        if value:
            return f"Your {key} is {value}."
        else:
            return f"I do not know your {key}."

    return "Please ask in format: What is my ___"


def list_memory(query):
    from memory.memory_manager import load_memory

    data = load_memory()

    if "user" not in data or not data["user"]:
        return "I do not have any information about you yet."

    response_lines = []

    for key, value in data["user"].items():
        response_lines.append(f"Your {key} is {value}.")

    return "Here is what I know about you. " + " ".join(response_lines)

def handle_confirmation(query):
    from memory.memory_manager import load_memory, save_memory
    from session_manager import get_pending, clear_pending

    pending = get_pending()

    # If no pending update → do nothing
    if not pending["key"]:
        return None

    # If mic didn't capture properly → ignore
    if not query or query == "None":
        return None

    query = query.lower()

    if any(word in query for word in ["yes", "yeah", "yup", "sure", "confirm"]):
        data = load_memory()

        if "user" not in data:
            data["user"] = {}

        key = pending["key"]
        value = pending["value"]

        data["user"][key] = value
        save_memory(data)

        clear_pending()
        return f"Your {key} has been updated."

    elif any(word in query for word in ["no", "nope", "cancel"]):
        clear_pending()
        return "Okay, I will keep the previous information."

    return "Please say yes or no."
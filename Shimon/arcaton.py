import json

def get_user_input():
    pass

def check_exit(message):
    pass

def add_to_history(history, role, content):

    while True :
        content = input("you: ")
        if "exit" in content.lower() :
            break
        else:
            history.append({
                "role": "user",
                "assistant" : name,
                "content": content})
    pass

def generate_response(message):
    pass

def run_chat():
    pass

def main():
    history = []






if __name__ == "__main__":
    main()
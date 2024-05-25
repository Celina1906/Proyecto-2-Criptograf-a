import json

def provide_service():
    final_message = "Service provided successfully!"
    with open("final_message.txt", "w") as f:
        f.write(final_message)

provide_service()

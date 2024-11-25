from commands import parse_command
from editor import HTMLCommandEditor

def main():
    """
    Main function to run the HTML Command Line Editor.
    """
    editor = HTMLCommandEditor()
    print("HTML Command Line Editor")
    print("Type 'exit' to quit.")
    print("Available commands: insert, append,delete, edit-text, edit-id, print-tree, print-indent, read, save, spell-check, undo, redo")
    
    while True:
        try:
            # Prompt user for input
            user_input = input("\nEnter command: ")
            
            # Exit condition
            if user_input.lower() == "exit":
                print("Exiting the editor. Goodbye!")
                break
            
            # Parse the command and arguments
            command, args = parse_command(user_input)
            
            # Execute the command
            editor.execute_command(command, *args)
        
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

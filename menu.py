"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
import threading
import agent


def menu(): 
    agent_thread = None
    
    while True:
        print("Kelvin's Agent")
        
        if agent.agent_running:
            print("1. Stop")
            print("2. Exit")
            choice = input("Enter:")
            
            match choice:
                case "1" | "stop" | "Stop":  # basic exception handling for now
                    agent.agent_running = False
                    if agent_thread:
                        agent_thread.join()  # wait for agent thread to fully stop
                case "2" | "exit" | "Exit":
                    print("Exiting...")
                    return
                case _:
                    print("Invalid choice")
        else:
            print("1. Start")
            print("2. Exit")
            choice = input("Enter:")
            
            match choice:
                case "1" | "start" | "Start":  # basic exception handling for now
                    agent.agent_running = True
                    agent_thread = threading.Thread(target=agent.agent, daemon=True)
                    agent_thread.start()
                case "2" | "exit" | "Exit":
                    print("Exiting...")
                    return
                case _:
                    print("Invalid choice")

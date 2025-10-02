

try:
    
    with open("sample.txt", "r") as file:
       
        print("File contents:\n")
        for line in file:
            print(line.strip())   
except FileNotFoundError:
    
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    
    print(f"An error occurred: {e}")

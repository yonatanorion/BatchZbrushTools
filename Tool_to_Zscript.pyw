import os

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the "ZTL_files" folder if it doesn't exist
ztl_folder = os.path.join(script_dir, "ZTL_files")
if not os.path.exists(ztl_folder):
    os.makedirs(ztl_folder)

# Get the list of .obj files in the current folder
obj_files = [file for file in os.listdir(script_dir) if file.endswith(".OBJ")]

# Generate the script output
script_output = "//RECORDED ZSCRIPT 2023\n"
script_output += "[IButton,Play,\"Press to play this ZScript. ZScript can be aborted at anytime by pressing the 'esc' key.\",\n"


for i, file in enumerate(obj_files):
    obj_url = os.path.join(script_dir, file).replace("\\", "/")
    ztl_url = os.path.join(ztl_folder, os.path.splitext(file)[0] + ".ZTL").replace("\\", "/")
    
    script_output += f"[FileNameSetNext,\"{obj_url}\"][IPress,Tool:Import]\n"
    script_output += f"[FileNameSetNext,\"{ztl_url}\"][IPress,Tool:Save As]\n"

script_output += "]/*End of ZScript*/\n"

# Save the script output to a text file
output_file = os.path.join(script_dir, "output.txt")
with open(output_file, "w") as file:
    file.write(script_output)

print("Output saved to output.txt file.")

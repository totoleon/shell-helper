import subprocess

def run_shell(command):
    # Execute the shell command and capture the output
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for the process to terminate and get the output and error
    stdout, stderr = process.communicate()
    # Decode the output and error to string format
    output = stdout.decode('utf-8')
    error = stderr.decode('utf-8')
    # Check if there was an error and return it if present
    if process.returncode != 0:
        return f"Error: {error}"
    return output

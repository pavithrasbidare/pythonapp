import os
import datetime

# Define the output directory for artifacts
output_dir = "artifacts"
os.makedirs(output_dir, exist_ok=True)

# Create a sample artifact
artifact_path = os.path.join(output_dir, "output.txt")
with open(artifact_path, "w") as f:
    f.write(f"This is a test artifact generated on {datetime.datetime.now()}.\n")
    f.write("Hello, this is a simple Python application!\n")

# Print a message indicating where the artifact is stored
print(f"Artifact generated: {artifact_path}")


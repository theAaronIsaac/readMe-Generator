import os

def generate_readme():
    title = input("Project Title: ")
    description = input("Description: ")
    installation = input("Installation steps: ")
    usage = input("Usage: ")

    readme_content = f"""# {title}

## Description
{description}

## Installation
{installation}

## Usage
{usage}
    """

    with open("README.md", "w") as f:
        f.write(readme_content)
    print("README.md generated successfully!")

generate_readme()

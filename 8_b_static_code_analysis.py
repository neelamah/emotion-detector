"""
File: 8b_static_code_analysis.py
Description: Demonstrates running static code analysis using pylint and displaying the score.
"""

import subprocess
import sys


def run_pylint(file_path: str) -> str:
    """
    Runs pylint on the given Python file and returns the output.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pylint", file_path],
            capture_output=True,
            text=True
        )
        return result.stdout + "\n" + result.stderr
    except Exception as e:
        return f"Error running pylint: {e}"


def extract_score(pylint_output: str) -> str:
    """
    Extracts the pylint score from the output.
    """
    for line in pylint_output.splitlines():
        if "Your code has been rated at" in line:
            return line.strip()
    return "Pylint score not found"


def main():
    file_to_check = "sample_code.py"  # Change this to your target file

    print("Running static code analysis using pylint...\n")

    output = run_pylint(file_to_check)

    print("===== PYLINT FULL OUTPUT =====")
    print(output)

    score = extract_score(output)

    print("\n===== SUMMARY =====")
    print(score)


if __name__ == "__main__":
    main()

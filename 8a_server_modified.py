# 8a_server_modified.py

from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)


@app.route("/analyze", methods=["GET"])
def run_static_code_analysis():
    """
    Runs static code analysis (pylint) on this file or project.
    Returns analysis results.
    """

    try:
        # File to analyze (current file or you can change path)
        target_file = "7b_error_handling_server.py"

        # Check if file exists
        if not os.path.exists(target_file):
            return jsonify({
                "error": f"File not found: {target_file}"
            }), 400

        # Run pylint as static code analyzer
        result = subprocess.run(
            ["pylint", target_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = {
            "status": "Static code analysis completed",
            "file_analyzed": target_file,
            "pylint_stdout": result.stdout,
            "pylint_stderr": result.stderr,
            "exit_code": result.returncode
        }

        return jsonify(output), 200

    except FileNotFoundError:
        return jsonify({
            "error": "pylint is not installed. Please install it using 'pip install pylint'."
        }), 500

    except Exception as e:
        return jsonify({
            "error": "Unexpected error during static analysis",
            "details": str(e)
        }), 500


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Static Code Analysis Server is running",
        "endpoint": "/analyze"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
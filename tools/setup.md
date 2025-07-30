# Optional Local Setup for Workshop Materials

This guide is for participants who prefer to set up the workshop materials locally instead of using GitHub Codespaces. **GitHub Codespaces is the recommended and easiest way to get started, as it comes pre-configured.**

## Prerequisites

*   **Python 3.8+:** Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
*   **Git:** For cloning the repository.
*   **Command Line Interface (CLI):** Access to your system's terminal or command prompt.

## Step-by-Step Local Setup

1.  **Clone the Workshop Repository:**
    If you haven't already, clone this workshop repository to your local machine:
    ```bash
    git clone https://github.com/your-org/ai4-agentic-workshop.git
    cd ai4-agentic-workshop
    ```
    *(Ensure you replace `https://github.com/your-org/ai4-agentic-workshop.git` with the actual repository URL if it's different.)*

2.  **Create a Virtual Environment (Recommended):**
    It's best practice to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

4.  **Install Workshop Dependencies:**
    With your virtual environment activated, install the necessary Python packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## What's Next?

Once setup is complete, you can navigate through the workshop materials. The main entry point is the `Participant Guide` (`docs/PARTICIPANT_GUIDE.md`).

## Troubleshooting

*   **`python` or `git` command not found:** Ensure Python and Git are correctly installed and added to your system's PATH.
*   **Dependency installation errors:** Make sure your virtual environment is activated before running `pip install -r requirements.txt`.
import os
import subprocess
from datetime import datetime

# --- Configuration ---
# NOTE: The user MUST update the REPORT_BASE_URL in paywen_integrator.py
# before running the script for the first time.

def run_module(script_name):
    """Runs a Python script as a subprocess and returns the output."""
    print(f"\n--- Running {script_name} ---")
    try:
        # Execute the script
        result = subprocess.run(
            ["python3", script_name],
            capture_output=True,
            text=True,
            check=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(result.stdout)
        if result.stderr:
            print(f"Error output from {script_name}:\n{result.stderr}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"CRITICAL ERROR: {script_name} failed with return code {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return None
    except FileNotFoundError:
        print(f"CRITICAL ERROR: python3 command not found. Check environment.")
        return None

def get_latest_report_filename():
    """Determines the filename of the latest generated report."""
    report_date = datetime.now().strftime("%Y-%m-%d")
    return f"ai_research_briefing_{report_date}.md"

def main():
    print("--- Starting Autonomous Knowledge Broker (AKB) Run ---")
    
    # 1. Data Collection
    run_module("data_collector.py")
    
    # 2. Report Generation
    report_output = run_module("report_generator.py")
    
    if report_output is None:
        print("AKB run failed at the report generation stage. Exiting.")
        return

    # 3. Paywen Integration (Monetization)
    # We need to ensure the report is publicly accessible before this step.
    # For this script, we will assume the user has a separate step to upload the file.
    
    # NOTE: The paywen_integrator.py script is designed to be run independently
    # for testing, but here we will just call its main function to create the paywall.
    
    # We need to pass the actual filename to the paywen_integrator, but since
    # the current version of paywen_integrator.py uses a placeholder, we will
    # modify the run_module to execute    # 3. Paywen Integration (Monetization)
    report_filename = get_latest_report_filename()
    
    print("\n--- CRITICAL MANUAL STEP REQUIRED FOR MONETIZATION ---")
    print(f"1. Locate the generated report file: reports/{report_filename}")
    print("2. **UPLOAD:** Upload this file to your public hosting service (e.g., S3, IPFS, GitHub Pages).")
    print("3. **CONFIGURE:** Ensure the 'REPORT_BASE_URL' in 'paywen_integrator.py' is correctly set to your hosting service's base URL.")
    print("4. **RUN INTEGRATOR:** After uploading and configuring, run the Paywen integration script:")
    print(f"   python3 paywen_integrator.py {report_filename}")
    
    # NOTE: We cannot run the integrator automatically because the file upload is a manual step
    # that requires the user to have a public hosting service. We will leave the final
    # integration step as a clear instruction for the user.
    
    print("\n--- AKB Run Finished (Final Integration Step is Manual) ---")
#!/bin/bash

# --- Autonomous Knowledge Broker (AKB) Automation Script ---
# Niche: AI Model Update & Benchmark Tracker
# Monetization: Paywen.dev API (x402 Protocol)

# 1. Configuration Check
REPORT_FILENAME="ai_research_briefing_$(date +%Y-%m-%d).md"
REPORT_PATH="reports/${REPORT_FILENAME}"
INTEGRATOR_SCRIPT="paywen_integrator.py"

echo "--- Starting AKB Automated Run ---"
echo "Report for today: ${REPORT_FILENAME}"

# 2. Data Collection
echo -e "\n[STEP 1/3] Running Data Collector..."
python3 data_collector.py

if [ $? -ne 0 ]; then
    echo "ERROR: Data collection failed. Aborting."
    exit 1
fi

# 3. Report Generation
echo -e "\n[STEP 2/3] Running Report Generator (AI Analysis)..."
python3 report_generator.py

if [ $? -ne 0 ]; then
    echo "ERROR: Report generation failed. Aborting."
    exit 1
fi

# 4. Critical Manual Step: Upload and Paywen Integration
echo -e "\n[STEP 3/3] Paywen Integration - CRITICAL MANUAL STEP"
echo "--------------------------------------------------------------------------------"
echo "The report has been successfully generated at: ${REPORT_PATH}"
echo "Before proceeding with monetization, you MUST perform the following steps:"
echo "1. **UPLOAD:** Upload the file ${REPORT_PATH} to your public hosting service (e.g., S3, IPFS, GitHub Pages)."
echo# 2. **CONFIGURE:** Ensure the AKB_BASE_URL environment variable is set to your GitHub Pages URL."
echo "3. **RUN INTEGRATOR:** After uploading and configuring, run the Paywen integration script manually:"
echo "   python3 ${INTEGRATOR_SCRIPT} ${REPORT_FILENAME}"
echo "--------------------------------------------------------------------------------"

echo -e "\n--- AKB Automated Run Finished ---"
echo "The system is ready for the final manual step and scheduling."

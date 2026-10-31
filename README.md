# Defensive Security Assessment of a Local Web Application

## Project purpose
A beginner-friendly, authorized defensive assessment of a small Flask application running only on the student's own computer.

## Safety and scope
- The only assessment target is `http://127.0.0.1:5000/`.
- Do not change the target to a public website, school system, company system, or another person's device.
- This project checks HTTP response headers only. It does not perform exploitation, password attacks, port scanning, or penetration testing.
- Do not include real credentials, personal data, or private logs in screenshots or reports.

## Files
- `app.py` — local demo web application with defensive response headers.
- `security_assessment.py` — checks for five expected response headers.
- `requirements.txt` — Python dependency.
- `Project_Report.docx` — editable internship report.
- `findings/security_findings.md` — findings and remediation record.

## Run on Windows / macOS / Linux
1. Install Python 3.
2. Open a terminal in this folder.
3. Install the dependency: `python -m pip install -r requirements.txt`
4. Start the app: `python app.py`
5. Keep that terminal open. Open a second terminal in the same folder.
6. Run the assessment: `python security_assessment.py`
7. Open `http://127.0.0.1:5000/` in your browser to view the demo.

## Expected result
The five configured headers should show `[PASS]` when the local app is running. Your actual output may differ if you change the app.

## Limitations
This is a learning demonstration, not a complete security audit. It does not assess account security, server deployment, TLS configuration, dependency vulnerabilities, database security, or authorization logic. HSTS is not enabled because this demo uses plain HTTP on localhost; HSTS should be considered only after deploying with correctly configured HTTPS.

## Evidence to add
Add genuine screenshots of:
1. The local demo page in your browser.
2. The running Flask terminal.
3. The checker output showing the actual results.

Do not claim a check passed unless your own run confirms it.

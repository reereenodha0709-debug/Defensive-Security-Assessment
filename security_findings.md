# Security Findings and Remediation Record

**Target:** Student-owned Flask demo at `http://127.0.0.1:5000/`  
**Authorization:** The application is created and run locally by the student.  
**Assessment type:** Basic defensive HTTP response-header review.

## Checks
| Check | Expected result | Evidence |
|---|---|---|
| Content-Security-Policy | Present | Record actual checker output |
| X-Content-Type-Options | Present | Record actual checker output |
| X-Frame-Options | Present | Record actual checker output |
| Referrer-Policy | Present | Record actual checker output |
| Permissions-Policy | Present | Record actual checker output |

## Remediation
The demo app sets the five headers in its `add_security_headers` response hook. If a header is missing in a test run, inspect that function, restart the local app, and run the checker again.

## Retest
Record the date, actual pass count, and screenshot after running the checker. Do not copy sample results as if they were observed results.

## Limitations
Header presence alone does not prove that an application is secure. Authentication, authorization, input handling, dependencies, deployment settings, and data protection require separate reviews.

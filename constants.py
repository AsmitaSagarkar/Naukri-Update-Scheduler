import os
# Configuration and constants used in the script. Update values as needed.
USERNAME = os.getenv("NAUKRI_USERNAME")
PASSWORD = os.getenv("NAUKRI_PASSWORD")
MOBILE = os.getenv("MOBILE")

ORIGINAL_RESUME_PATH = "resume/your_resume.pdf"
MODIFIED_RESUME_PATH = "resume/modified_resume.pdf"
RESUME_DATE_WISE = os.getenv("RESUME_DATE_WISE", "true").lower() == "true"

NAUKRI_LOGIN_URL = "https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL = "https://www.naukri.com/mnjuser/profile"
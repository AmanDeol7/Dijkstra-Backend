# utils/error_codes.py

class ErrorCodes:
    """
    Standardized alphanumeric error codes for the API.
    Format: xxxx-yyyy-zzzz-abc
        xxxx: Subdivision (USER, OPPT)
        yyyy: Feature within subdivision (e.g., PROJ for Project Opportunities)
        zzzz: Error type (DB, SRV, AUTH, VAL, NF)
        abc: Alphanumeric error number (A01, A02, etc.)
    """

    GENERIC_ERROR = "GEN-ERR-000"  # Generic error code for uncategorized errors

    # -----------------------------
    # Opportunities → Project Opportunities
    # -----------------------------

    # Database errors
    OPPT_PROJ_DB_A01 = "OPPT-PROJ-DB-A01"  # Failure inserting project
    OPPT_PROJ_DB_A02 = "OPPT-PROJ-DB-A02"  # Failure updating project
    OPPT_PROJ_DB_A03 = "OPPT-PROJ-DB-A03"  # Failure deleting project

    # Server / Unexpected errors
    OPPT_PROJ_SRV_A01 = "OPPT-PROJ-SRV-A01"  # Generic server error
    OPPT_PROJ_SRV_A02 = "OPPT-PROJ-SRV-A02"  # Error fetching projects list

    # Authentication / Permission errors
    OPPT_PROJ_AUTH_A01 = "OPPT-PROJ-AUTH-A01"  # User not authorized
    OPPT_PROJ_AUTH_A02 = "OPPT-PROJ-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    OPPT_PROJ_VAL_A01 = "OPPT-PROJ-VAL-A01"  # Invalid project payload
    OPPT_PROJ_VAL_A02 = "OPPT-PROJ-VAL-A02"  # Required field missing

    # Not found errors
    OPPT_PROJ_NF_A01 = "OPPT-PROJ-NF-A01"  # Project not found

    # -----------------------------
    # Opportunities → Organizations
    # -----------------------------

    # Database errors
    OPPT_ORG_DB_A01 = "OPPT-ORG-DB-A01"  # Failure inserting organization
    OPPT_ORG_DB_A02 = "OPPT-ORG-DB-A02"  # Failure updating organization
    OPPT_ORG_DB_A03 = "OPPT-ORG-DB-A03"  # Failure deleting organization

    # Server / Unexpected errors
    OPPT_ORG_SRV_A01 = "OPPT-ORG-SRV-A01"  # Generic server error
    OPPT_ORG_SRV_A02 = "OPPT-ORG-SRV-A02"  # Error fetching organizations list

    # Authentication / Permission errors
    OPPT_ORG_AUTH_A01 = "OPPT-ORG-AUTH-A01"  # User not authorized
    OPPT_ORG_AUTH_A02 = "OPPT-ORG-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    OPPT_ORG_VAL_A01 = "OPPT-ORG-VAL-A01"  # Invalid organization payload
    OPPT_ORG_VAL_A02 = "OPPT-ORG-VAL-A02"  # Required field missing

    # Not found errors
    OPPT_ORG_NF_A01 = "OPPT-ORG-NF-A01"  # Organization not found

    # -----------------------------
    # Opportunities → Fellowships
    # -----------------------------

    # Database errors
    OPPT_FEL_DB_A01 = "OPPT-FEL-DB-A01"  # Failure inserting fellowship
    OPPT_FEL_DB_A02 = "OPPT-FEL-DB-A02"  # Failure updating fellowship
    OPPT_FEL_DB_A03 = "OPPT-FEL-DB-A03"  # Failure deleting fellowship

    # Server / Unexpected errors
    OPPT_FEL_SRV_A01 = "OPPT-FEL-SRV-A01"  # Generic server error
    OPPT_FEL_SRV_A02 = "OPPT-FEL-SRV-A02"  # Error fetching fellowships list

    # Authentication / Permission errors
    OPPT_FEL_AUTH_A01 = "OPPT-FEL-AUTH-A01"  # User not authorized
    OPPT_FEL_AUTH_A02 = "OPPT_FEL_AUTH_A02"  # User session expired / invalid token

    # Validation / Input errors
    OPPT_FEL_VAL_A01 = "OPPT-FEL-VAL-A01"  # Invalid fellowship payload
    OPPT_FEL_VAL_A02 = "OPPT_FEL_VAL_A02"  # Required field missing

    # Not found errors
    OPPT_FEL_NF_A01 = "OPPT_FEL_NF_A01"  # Fellowship not found

    # -----------------------------
    # Opportunities → Jobs
    # -----------------------------

    # Database errors
    OPPT_JOB_DB_A01 = "OPPT-JOB-DB-A01"  # Failure inserting job
    OPPT_JOB_DB_A02 = "OPPT-JOB-DB-A02"  # Failure updating job
    OPPT_JOB_DB_A03 = "OPPT-JOB-DB-A03"  # Failure deleting job

    # Server / Unexpected errors
    OPPT_JOB_SRV_A01 = "OPPT-JOB-SRV-A01"  # Generic server error
    OPPT_JOB_SRV_A02 = "OPPT-JOB-SRV-A02"  # Error fetching jobs list

    # Authentication / Permission errors
    OPPT_JOB_AUTH_A01 = "OPPT-JOB-AUTH-A01"  # User not authorized
    OPPT_JOB_AUTH_A02 = "OPPT_JOB_AUTH_A02"  # User session expired / invalid token

    # Validation / Input errors
    OPPT_JOB_VAL_A01 = "OPPT-JOB-VAL-A01"  # Invalid job payload
    OPPT_JOB_VAL_A02 = "OPPT_JOB_VAL_A02"  # Required field missing

    # Not found errors
    OPPT_JOB_NF_A01 = "OPPT_JOB_NF_A01"  # Job not found

















    # -----------------------------
    # Users → User
    # -----------------------------

    # Database errors
    USER_USER_DB_A01 = "USER-USER-DB-A01"  # Failure inserting user
    USER_USER_DB_A02 = "USER-USER-DB-A02"  # Failure updating user
    USER_USER_DB_A03 = "USER-USER-DB-A03"  # Failure deleting user

    # Server / Unexpected errors
    USER_USER_SRV_A01 = "USER-USER-SRV-A01"  # Generic server error
    USER_USER_SRV_A02 = "USER-USER-SRV-A02"  # Error fetching users list

    # Authentication / Permission errors
    USER_USER_AUTH_A01 = "USER-USER-AUTH-A01"  # User not authorized
    USER_USER_AUTH_A02 = "USER-USER-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    USER_USER_VAL_A01 = "USER-USER-VAL-A01"  # Invalid user payload
    USER_USER_VAL_A02 = "USER-USER-VAL-A02"  # Required field missing

    # Not found errors
    USER_USER_NF_A01 = "USER-USER-NF-A01"  # User not found

    # -----------------------------
    # Users → Profile
    # -----------------------------

    # Database errors
    USER_PROFILE_DB_A01 = "USER-PROFILE-DB-A01"  # Failure inserting profile
    USER_PROFILE_DB_A02 = "USER-PROFILE-DB-A02"  # Failure updating profile
    USER_PROFILE_DB_A03 = "USER-PROFILE-DB-A03"  # Failure deleting profile

    # Server / Unexpected errors
    USER_PROFILE_SRV_A01 = "USER-PROFILE-SRV-A01"  # Generic server error
    USER_PROFILE_SRV_A02 = "USER-PROFILE-SRV-A02"  # Error fetching profiles list

    # Authentication / Permission errors
    USER_PROFILE_AUTH_A01 = "USER-PROFILE-AUTH-A01"  # User not authorized
    USER_PROFILE_AUTH_A02 = "USER-PROFILE-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    USER_PROFILE_VAL_A01 = "USER-PROFILE-VAL-A01"  # Invalid profile payload
    USER_PROFILE_VAL_A02 = "USER-PROFILE-VAL-A02"  # Required field missing

    # Not found errors
    USER_PROFILE_NF_A01 = "USER-PROFILE-NF-A01"  # Profile not found

    # -----------------------------
    # Users → Location
    # -----------------------------

    # Database errors
    USER_LOCATION_DB_A01 = "USER-LOCATION-DB-A01"  # Failure inserting location
    USER_LOCATION_DB_A02 = "USER-LOCATION-DB-A02"  # Failure updating location
    USER_LOCATION_DB_A03 = "USER-LOCATION-DB-A03"  # Failure deleting location

    # Server / Unexpected errors
    USER_LOCATION_SRV_A01 = "USER-LOCATION-SRV-A01"  # Generic server error
    USER_LOCATION_SRV_A02 = "USER-LOCATION-SRV-A02"  # Error fetching locations list

    # Authentication / Permission errors
    USER_LOCATION_AUTH_A01 = "USER-LOCATION-AUTH-A01"  # User not authorized
    USER_LOCATION_AUTH_A02 = "USER-LOCATION-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    USER_LOCATION_VAL_A01 = "USER-LOCATION-VAL-A01"  # Invalid location payload
    USER_LOCATION_VAL_A02 = "USER-LOCATION-VAL-A02"  # Required field missing

    # Not found errors
    USER_LOCATION_NF_A01 = "USER-LOCATION-NF-A01"  # Location not found


    # -----------------------------
    # Users → Work Experience
    # -----------------------------

    # Database errors
    USER_WORKEXP_DB_A01 = "USER-WORKEXP-DB-A01"  # Failure inserting work experience
    USER_WORKEXP_DB_A02 = "USER-WORKEXP-DB-A02"  # Failure updating work experience
    USER_WORKEXP_DB_A03 = "USER-WORKEXP-DB-A03"  # Failure deleting work experience

    # Server / Unexpected errors
    USER_WORKEXP_SRV_A01 = "USER-WORKEXP-SRV-A01"  # Generic server error
    USER_WORKEXP_SRV_A02 = "USER-WORKEXP-SRV-A02"  # Error fetching work experiences list

    # Authentication / Permission errors
    USER_WORKEXP_AUTH_A01 = "USER-WORKEXP-AUTH-A01"  # User not authorized
    USER_WORKEXP_AUTH_A02 = "USER-WORKEXP-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    USER_WORKEXP_VAL_A01 = "USER-WORKEXP-VAL-A01"  # Invalid work experience payload
    USER_WORKEXP_VAL_A02 = "USER-WORKEXP-VAL-A02"  # Required field missing

    # Not found errors
    USER_WORK_EXPERIENCE_NF_A01 = "USER-WORKEXP-NF-A01"  # Work experience not found

    # -----------------------------
    # Users → Certificate
    # -----------------------------

    # Database errors
    USER_CERTIFICATION_DB_A01 = "USER-CERTIFICATE-DB-A01"  # Failure inserting certificate
    USER_CERTIFICATION_DB_A02 = "USER-CERTIFICATE-DB-A02"  # Failure updating certificate
    USER_CERTIFICATION_DB_A03 = "USER-CERTIFICATE-DB-A03"  # Failure deleting certificate

    # Server / Unexpected errors
    USER_CERTIFICATION_SRV_A01 = "USER-CERTIFICATE-SRV-A01"  # Generic server error
    USER_CERTIFICATION_SRV_A02 = "USER-CERTIFICATE-SRV-A02"  # Error fetching certificates list

    # Authentication / Permission errors
    USER_CERTIFICATION_AUTH_A01 = "USER-CERTIFICATE-AUTH-A01"  # User not authorized
    USER_CERTIFICATION_AUTH_A02 = "USER-CERTIFICATE-AUTH-A02"  # User session expired / invalid token

    # Validation / Input errors
    USER_CERTIFICATION_VAL_A01 = "USER-CERTIFICATE-VAL-A01"  # Invalid certificate payload
    USER_CERTIFICATION_VAL_A02 = "USER-CERTIFICATE-VAL-A02"  # Required field missing

    # Not found errors
    USER_CERTIFICATION_NF_A01 = "USER-CERTIFICATE-NF-A01"  # Certificate not found
# Q2: 2024 Snowflake customer data-theft campaign (UNC5537)

## Timeline

| Date | Event | Source |
|---|---|---|
| Nov 2020 onwards | Earliest infostealer infections later linked to stolen Snowflake credentials | Mandiant (2024) |
| 14 to 25 Apr 2024 | AT&T data downloaded from its Snowflake workspace | AT&T 8-K via BankInfoSecurity (2024) |
| 19 Apr 2024 | AT&T learns of the breach | BankInfoSecurity (2024) |
| 20 May 2024 | Live Nation detects unauthorised activity in a third-party cloud database (Ticketmaster) | The Record (2024) |
| late May 2024 | John Binns arrested in Turkey | Krebs (2024) |
| 30 May 2024 | Snowflake publishes hardening guidance | Mandiant (2024) |
| 1 Jun 2024 | ASD's ACSC alert: increased cyber threat activity targeting Snowflake customers | ASD's ACSC (2024) |
| 3 Jun 2024 | CISA alert | CISA (2024) |
| 10 Jun 2024 | Mandiant publishes UNC5537 report: ~165 organisations notified; no Snowflake platform breach; no MFA, unrotated credentials, no network allow lists | Mandiant (2024) |
| Jul 2024 | Snowflake lets admins enforce MFA for all users | Snowflake (2024) |
| 12 Jul 2024 | AT&T discloses theft of call/text records of ~110 million customers | BankInfoSecurity (2024) |
| 30 Oct 2024 | Connor (Alexander) Moucka arrested in Canada | Krebs (2024) |
| Jun 2025 | Preliminary approval of AT&T US$177M settlement (two breaches) | BankInfoSecurity (2025) |
| 2025 to Oct 2026 | Snowflake phases out single-factor password sign-ins (MFA for all humans; no passwords for service users) | Snowflake (2026) |

## Sources
- Mandiant: https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
- ASD's ACSC: https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/increased-cyber-threat-activity-targeting-snowflake-customers
- CISA: https://www.cisa.gov/news-events/alerts/2024/06/03/snowflake-recommends-customers-take-steps-prevent-unauthorized-access
- Snowflake MFA rollout: https://docs.snowflake.com/en/user-guide/security-mfa-rollout
- Cybersecurity Dive on shared responsibility: https://www.cybersecuritydive.com/news/snowflake-attacks-test-shared-responsibility/718850/
- Krebs on Security: https://krebsonsecurity.com/2024/11/canadian-man-arrested-in-snowflake-data-extortions/

## Diagrams
- `diagrams/q2_snowflake_attack_path.png`: attack chain with the control gap at each step
- `diagrams/q2_shared_responsibility.png`: responsibility matrix (IaaS vs PaaS vs Snowflake SaaS)

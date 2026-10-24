# Accounts Project: submission answers

Repository: https://github.com/shrishtichoudhary24-glitch/Accounts_Project

| Task | Submission |
| --- | --- |
| 1 | https://github.com/shrishtichoudhary24-glitch/Accounts_Project/blob/main/README.md |
| 2 | https://github.com/shrishtichoudhary24-glitch/Accounts_Project/blob/main/user-story.md |
| 5 | Upload planning-labels-done.jpeg |
| 6 | Upload planning-kanban-done.jpeg |
| 7 | https://github.com/shrishtichoudhary24-glitch/Accounts_Project/blob/main/setup.cfg |
| 21 | https://github.com/shrishtichoudhary24-glitch/Accounts_Project/blob/main/.github/workflows/ci-build.yaml |
| 22 | https://github.com/shrishtichoudhary24-glitch/Accounts_Project/blob/main/service/__init__.py |
| 23 | Copy the complete output from security-headers-done |

## Evidence notes

The planning screenshots are reconstructed views of the existing Sprint 1 stories (#1, #2, and #6). Their existing labels, Sprint 1 assignments, and estimates (3, 2, and 4) were retained. The stories were temporarily displayed in Product Backlog and Sprint Backlog for the captures, then returned to Done. These are fresh screenshots, not historical captures.

The security test output was generated locally from repository commit 97c32518919f749e3f7007e7f36a9034f34a6b58, using Python 3.9.25 and an isolated in-memory SQLite database. The command explicitly selects both test modules so discovery is reliable on Windows:

    nosetests tests.test_models tests.test_routes

Result: 18 tests passed, 99% service coverage. Both Talisman security-header and CORS-header tests passed. Both Flake8 commands from CI passed with zero findings. The local Windows environment used greenlet<3.2 and setuptools 79.0.1; application source and repository requirements were unchanged.

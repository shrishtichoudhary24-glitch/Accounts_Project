# Corrected assignment submissions

Repository: https://github.com/shrishtichoudhary24-glitch/devops-capstone-project

Use the new repository name in every GitHub URL submitted to the grader.

| Task | Submission |
| --- | --- |
| 1 | https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/blob/main/README.md |
| 2 | https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/blob/main/user-story.md |
| 5 | Upload planning-labels-done.png. This replacement shows ONLY Product Backlog, with Technical Debt and enhancement labels visible. |
| 6 | Use the previously supplied planning-kanban-done.png for Sprint Backlog. Do not upload that image for Task 5. |
| 7 | https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/blob/main/setup.cfg |
| 20 | Upload ci-kanban-done.png. This image shows ONLY Done, containing the continuous integration story. |
| 21 | https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/blob/main/.github/workflows/ci-build.yaml |
| 22 | https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/blob/main/service/__init__.py |
| 23 | Submit the complete text from security-headers-done; attach that file if the question accepts file uploads. |

## Verification and provenance

The repository is public and named devops-capstone-project. Its README names the project and uses the build badge URL for the renamed repository. The workflow explicitly installs dependencies, checks out code before linting, and runs nosetests with verbosity, coverage, a 95 percent minimum, and both test modules.

Talisman settings explicitly configure HTTPS, HSTS, X-Frame-Options, Referrer-Policy, and Content-Security-Policy. CORS is enabled for the service routes. Existing tests pass without changing their expectations.

The replacement security-headers-done comes from the test step of this successful GitHub Actions run:
https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/actions/runs/40126796525

It contains the actual nosetests command, individual passing test results (including CORS and Talisman), 99 percent coverage, Ran 18 tests, and OK. Only GitHub log timestamps and step-group markers were removed for readability. The original test-step log is also supplied as security-headers-ci-raw.txt in the download bundle.

Task 5 is a fresh reconstruction of the existing Sprint 1 planning stage using the existing stories, labels, and estimates. Those stories were returned to Done after capture. Task 20 captures the actual completed CI story. Current board state is restored: eight stories Done, three Sprint Backlog.

# User Story Template

**As a** [role]
**I need** [function]
**So that** [benefit]

### Details and Assumptions
* [document what you know]

### Acceptance Criteria
```gherkin
Given [some context]
When [certain action is taken]
Then [the outcome of the action is observed]
```

## Example
**As a** customer
**I need** to create an account
**So that** I can use the service

### Acceptance Criteria
```gherkin
Given no account exists
When I POST valid data to /accounts
Then a new account is created and returned with HTTP 201
```

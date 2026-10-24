# Tasks 26, 27, and 28: verified deployment evidence

The repository Docker image was built and deployed successfully to a real, temporary kind Kubernetes cluster in GitHub Actions.

Successful run:
https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/actions/runs/40131500554

Workflow:
https://github.com/shrishtichoudhary24-glitch/devops-capstone-project/blob/main/.github/workflows/deploy-check.yaml

- Task 26: Copy the JSON from kube-app-output. This exact output was downloaded from the successful Kubernetes validation run after port-forwarding service/accounts to port 8080. The HTTPS path reflects the forwarded HTTPS header used by the service behind TLS termination.
- Task 27: Upload kube-docker-done.png. The Docker image built successfully before issue #9 was moved to Done and closed.
- Task 28: Upload kube-kubernetes-done.png. Kubernetes reported one Ready pod and a successful rollout, and the application returned valid JSON before issue #10 was moved to Done and closed.

The downloaded artifacts also include kube-images and kube-deploy-accounts with the original Docker and Kubernetes outputs. The validation cluster was removed after evidence collection; this is a completed deployment test, not a persistent hosted endpoint.

The initial rollout exposed a readiness-probe HTTPS redirect. The deployment manifest was corrected to send X-Forwarded-Proto: https on the health probe. The next run completed every validation step successfully.

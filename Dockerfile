# Use a lightweight base image for testing
FROM alpine:latest

# Print a simple message when the container runs
CMD ["echo", "Hello from my GitHub Actions container!"]
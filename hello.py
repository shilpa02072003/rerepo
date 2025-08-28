name: Run Python Script

on:
  push:       # Runs when you push to repo
  pull_request:  # Runs when a PR is created

jobs:
  run-python:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Run Python script
        run: python hello.py

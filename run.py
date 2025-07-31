#!/usr/bin/env python3

import yaml
import argparse
import os
import subprocess

def load_config(config_path):
    """Load the configuration from a YAML file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load configuration from a YAML file.")
    parser.add_argument('--config', type=str, required=True, help='Path to the configuration file')
    args = parser.parse_args()

    config = load_config(args.config)
    os.environ["OPENAI_API_BASE"] = config.get("openai_api_base", "NO_BASE")
    os.environ["OPENAI_API_KEY"] = config.get("openai_api_key", "NO_KEY")

    # iterate models
    for model in config.get("models", []):
        # iterate token_confs (input/output #tokens)
        inputs = config.get("token_confs", {}).get("input", [])
        outputs = config.get("token_confs", {}).get("output", [])
        for i, o in zip(inputs, outputs):
            subprocess.run([
                "python", "token_benchmark_ray.py",
                "--model", model,
                "--llm-api", "openai",
                "--results-dir", "/results",
                "--mean-input-tokens", str(i.get("mean")),
                "--stddev-input-tokens", str(i.get("stddev")),
                "--mean-output-tokens", str(o.get("mean")),
                "--stddev-output-tokens", str(o.get("stddev")),
            ])

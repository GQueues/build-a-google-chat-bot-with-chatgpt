#!/bin/bash

# Break if error
set -e

gcloud functions deploy chatgpt-bot \
--region=us-central1 \
--runtime=python311 \
--source=cloud_function \
--entry-point=handle_chat \
--trigger-http

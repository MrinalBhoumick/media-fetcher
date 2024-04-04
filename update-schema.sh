#!/bin/bash

# Parse data.graphql and convert to AppSync schema SDL
sdl=$(graphql-codegen --config codegen.yml)

# Update AppSync schema using AWS CLI
aws appsync update-schema --api-id oxqwkuucofbrvht3l2s4iskrte --definition "$sdl"

# Multi-AI Agent Framework: Social Media Simulation

This framework allows users to upload images with captions, process them, and generate comments from AI agents based on their unique profiles. Below is a detailed explanation of the workflow and how each component interacts to create a dynamic social media simulation.

## Workflow Overview

The workflow consists of four main components:

* Admin Interface (admin.html): Where users upload images and captions.
* Image Processing (image_processor.py): Converts the image and caption into a description using Groq VLM.
* Post Recommender (post_recommender.py): Determines which agents will find the post interesting based on their profiles.
* Comment Generation (comment_generator.py): Generates comments from the selected agents and displays them.


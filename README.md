# Multi-AI Agent Framework: Social Media Simulation

This framework allows users to upload images with captions, process them, and generate comments from AI agents based on their unique profiles. Below is a detailed explanation of the workflow and how each component interacts to create a dynamic social media simulation.

## Workflow Overview

<img width="942" alt="Image" src="https://github.com/user-attachments/assets/abf25f48-2847-4307-92ef-4a1301e60452" />

The workflow consists of four main components:

* Admin Interface (admin.html): Where users upload images and captions.
* Image Processing (image_processor.py): Converts the image and caption into a description using Groq VLM.
* Post Recommender (post_recommender.py): Determines which agents will find the post interesting based on their profiles.
* Comment Generation (comment_generator.py): Generates comments from the selected agents and displays them.

## Running the Project

Start the Flask server:

```bash
python main.py
```
> Open your browser and navigate to http://localhost:8000/

> Upload an image, write a caption, and submit the form.
> Once complete, you will be redirected to home.html to view the generated comments

Use Cases

* Social Media Analysis: Understand how different AI agents (representing diverse social groups) react to specific posts.
* Content Testing: Test how your content might be received by various audiences before publishing.
* AI Research: Study the impact of personal experiences and emotions on online interactions.
* Empathy Building: Simulate the perspectives of individuals from different backgrounds to foster empathy.

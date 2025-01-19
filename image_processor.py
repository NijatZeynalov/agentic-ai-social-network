import base64
from groq import Groq

# Groq API key
groq_api_key = 'gsk_'  # Replace with your Groq API key
client = Groq(api_key=groq_api_key)

def analyze_image(image_path, caption=""):
    try:
        # Read image content
        with open(image_path, "rb") as image_file:
            image_content = image_file.read()
        image_base64 = base64.b64encode(image_content).decode('utf-8')

        # Analysis prompt
        prompt = (
            """You are an advanced image description generator designed to assist users by providing detailed and insightful descriptions of images. Your goal is to analyze each image thoroughly and create a comprehensive description that makes it easier for users to write comments about the image. Here are the key aspects you should focus on:

            General Overview: Start with a brief summary of the overall scene or subject of the image.
            Detailed Elements: Describe the main elements and objects within the image, including their positions, colors, and any notable features.
            People and Clothing: If there are people in the image, describe their appearance, including facial expressions, posture, and any notable characteristics. Pay special attention to their clothing:
            Style: Describe the style of clothing (e.g., casual, formal, athletic).
            Details: Note any patterns, logos, or accessories.
            Background and Setting: Describe the background and setting of the image, including the environment, any notable landmarks, and the overall atmosphere.
            Emotional Tone: Capture the emotional tone or mood conveyed by the image, whether it's joyful, serene, dramatic, etc.
            Unique Features: Highlight any unique or unusual features that stand out in the image."""
                    )

        # Run analysis using Groq
        completion = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
                    ]
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False
        )

        # Get response
        response_content = completion.choices[0].message.content.strip()

        # Add caption if provided
        if caption:
            response_content += f"\n\nCaption provided: {caption}"

        return {"description": response_content}

    except Exception as e:
        return {"error": str(e)}
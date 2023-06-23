# AI Text-to-Image App

This Python script implements an AI Text-Image App using the Streamlit framework. The app allows users to generate images based on text prompts using a StableDiffusionPipeline model.

## Model

- The model used in this app is the StableDiffusionPipeline from the `diffusers` package.
- The specific model ID used is "CompVis/stable-diffusion-v1-4".
- The model is loaded using the `from_pretrained()` function, which loads the pre-trained weights of the model.
- The model is then moved to the accelerator device for efficient computation.

## App Functionality

- The app displays a user interface with the title "AI Text-Image App" using `st.title()`.
- The user can enter a text prompt in the provided input field using `st.text_input()`.
- Upon clicking the "Generate Image" button, the app checks if the prompt is valid (not empty or containing only whitespace) using `strip()` and displays a warning if it is not valid using `st.warning()`.
- If the prompt is valid, the app generates an image based on the prompt using the StableDiffusionPipeline model.
- The generated image is saved as "Saved_img.png" using `image.save()`.
- A success message is displayed using `st.success()` to indicate that the image generation and saving were successful.
- The generated image is displayed using `st.image()` with the caption "Generated Image" and `use_column_width=True` for proper visualization.

## Running the App

To run the app, execute the Python script using the following command:
```
streamlit run app.py
```

The Streamlit server will start, allowing you to access the AI Text-Image App in your web browser.

---

The AI Text-Image App leverages the StableDiffusionPipeline model to generate images based on text prompts, providing users with an interactive and visually appealing experience.

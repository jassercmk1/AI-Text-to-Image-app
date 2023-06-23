# AI-Text-to-Image-app
<p>This Python script implements an AI Text-Image App using the Streamlit framework. 
    The app allows users to generate images based on text prompts using a StableDiffusionPipeline model. 
    Here's an overview of the key components:</p>
    
    <h3>Model:</h3>
    
    <ul>
        <li>The model used in this app is the StableDiffusionPipeline from the <code>diffusers</code> package.</li>
        <li>The specific model ID used is "CompVis/stable-diffusion-v1-4".</li>
        <li>The model is loaded using the <code>from_pretrained()</code> function, which loads the pre-trained weights of the model.</li>
        <li>The model is then moved to the accelerator device for efficient computation.</li>
    </ul>
    
    <h3>App Functionality:</h3>
    
    <ul>
        <li>The app displays a user interface with the title "AI Text-Image App" using <code>st.title()</code>.</li>
        <li>The user can enter a text prompt in the provided input field using <code>st.text_input()</code>.</li>
        <li>Upon clicking the "Generate Image" button, the app checks if the prompt is valid (not empty or containing only whitespace) using <code>strip()</code> and displays a warning if it is not valid using <code>st.warning()</code>.</li>
        <li>If the prompt is valid, the app generates an image based on the prompt using the StableDiffusionPipeline model.</li>
        <li>The generated image is saved as "Saved_img.png" using <code>image.save()</code>.</li>
        <li>A success message is displayed using <code>st.success()</code> to indicate that the image generation and saving were successful.</li>
        <li>The generated image is displayed using <code>st.image()</code> with the caption "Generated Image" and <code>use_column_width=True</code> for proper visualization.</li>
    </ul>
    
    <h3>Running the App:</h3>
    
    <ul>
        <li>The <code>AI_app()</code> function is called within the <code>__main__</code> block to run the Streamlit app.</li>
        <li>To run the app, execute the Python script, and the Streamlit server will start, allowing you to access the AI Text-Image App in your web browser.</li>
    </ul>
    
    <hr>
    
    <p>The AI Text-Image App leverages the StableDiffusionPipeline model to generate images based on text prompts, providing users with an interactive and visually appealing experience.</p>

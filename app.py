import streamlit as st
import torch
from accelerate import Accelerator
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
accelerator = Accelerator()

def AI_app():
    st.title('AI Text-Image App')
    prompt = st.text_input('Input Text:')
    generate_button = st.button('Generate Image')
    
    if generate_button:
        if not prompt.strip():
            st.warning('Please enter a valid text prompt.')
        else:
            
            with accelerator.device:
                pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
                pipe = pipe.to(accelerator.device)
            
            with torch.no_grad(), accelerator.device:
                image = pipe(prompt).images[0]
                image.save("Saved_img.png")
                st.success('Image generated and saved successfully!')
                st.image(image, caption='Generated Image', use_column_width=True)


if __name__ == "__main__":
    AI_app()


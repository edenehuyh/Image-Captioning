# Import libraries
import torch
import gradio as gr

from models.blip import blip_decoder
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode


# Download model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

image_size = 384
transform = transforms.Compose([
    transforms.Resize((image_size,image_size),interpolation=InterpolationMode.BICUBIC),
    transforms.ToTensor(),
    transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711))
    ]) 

model_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_large_caption.pth'
    
model = blip_decoder(pretrained=model_url, image_size=384, vit='large')
model.eval()
model = model.to(device)


# Deploy
title       = 'Image Captioning'
description = '''
                Ton Duc Thang University

                No. | Student ID | Student Name
                --- |   :---:    | ---
                  1 | 51900018   | Huỳnh Công Chánh
                  2 | 51703087   | Vũ Minh Hiếu
              '''
inputs      = gr.inputs.Image(type='pil')
outputs     = gr.outputs.Textbox(label='Output')

def inference(raw_image):
    image = transform(raw_image).unsqueeze(0).to(device)   
    with torch.no_grad():
        caption = model.generate(image, sample=False, num_beams=3, max_length=20, min_length=5)
        return caption[0]

gr.Interface(inference, inputs, outputs, title=title, description=description).launch(enable_queue=True, share='True')
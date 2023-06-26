# Image Captioning
Image Captioning with [BLIP model](https://arxiv.org/abs/2201.12086) and deployed using [Gradio](https://github.com/gradio-app/gradio).

## Information

Ton Duc Thang University

No. | Student ID | Student Name
--- | :---:      | ---
1   | 51900018   | Huỳnh Công Chánh
2   | 51703087   | Vũ Minh Hiếu

## How to run the deploy
1. Install Python (Python 3.7 - 3.9 is required for supporting Pytorch).
2. Install necessary libraries.
<pre>pip install requests torch torchvision gradio timm fairscale transformers</pre>
3. When you run the deployment for the first time, it will take approximately 5 minutes to download the model. 
However, subsequent runs will not require the model to be reloaded.
<pre>python app.py</pre>
4. Browse the deploy on Localhost via the link http://localhost:7860, or the Public link generated in Command prompt.
5. Enjoy 🙂

## References

[[1](https://github.com/salesforce/BLIP)] BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation.

[[2](https://arxiv.org/abs/2201.12086)] Junnan Li, Dongxu Li, Caiming Xiong, Steven Hoi, BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation.

[[3](https://github.com/gradio-app/gradio)] Gradio: Build Machine Learning Web Apps — in Python.

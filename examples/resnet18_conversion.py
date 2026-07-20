import torchvision
import torch
import litert_torch

model = torchvision.models.resnet18(...)

sample_inputs = (torch.randn(1,3,224,224),)

edge_model = litert_torch.convert(
    model.eval(),
    sample_inputs
)

edge_model.export("resnet18.tflite")
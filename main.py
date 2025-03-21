from FullPipeline import FullPipelineOCR
model = FullPipelineOCR()
paragraphs = model('book2.jpg')

for para in paragraphs:
    print(para)
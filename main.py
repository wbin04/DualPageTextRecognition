from FullPipeline import FullPipelineOCR
model = FullPipelineOCR()
paragraphs = model('book.png')

for para in paragraphs:
    print(para)
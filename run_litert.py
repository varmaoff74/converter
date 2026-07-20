from litert_lm import Engine

model_path = "litert_output/model.litertlm"

engine = Engine(model_path)

session = engine.create_session(max_output_tokens=200)

prompt = "Explain what AI is in simple words."

session.run_prefill([prompt])

response = session.run_decode()

print(response.texts)
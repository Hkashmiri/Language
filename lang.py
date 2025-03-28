from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);

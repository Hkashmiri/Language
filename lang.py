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

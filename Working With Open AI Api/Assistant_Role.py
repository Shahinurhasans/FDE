client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},

        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},

        {"role": "user", "content": "Give me a quick summary of France."},
        {"role": "assistant", "content": "France is a country in Western Europe. The capital city is Paris."},

        {"role": "user", "content": "Give me a quick summary of Japan."},
        {"role": "assistant", "content": "Japan is an island country in East Asia. The capital city is Tokyo."},

        {"role": "user", "content": "Give me a quick summary of Brazil."},
        {"role": "assistant", "content": "Brazil is the largest country in South America. The capital city is Brasília."},

        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)

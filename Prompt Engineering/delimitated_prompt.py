client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to complete the story
prompt = f"""Complete the story delimited by triple backticks with only two paragraphs using the style of Shakespeare. 
 ```{story}```"""

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)
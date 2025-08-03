import requests 
import streamlit as st

def get_ollama_poem(topic):
    # Send the correct JSON structure that matches your API
    response = requests.post("http://localhost:8000/ollama/poem", json={"topic": topic})
    if response.status_code == 201:
        # Parse the response correctly based on your API's response structure
        return response.json()
    else:
        st.error(f"Error generating poem. Status code: {response.status_code}")
        st.error(f"Response: {response.text}")
        return None
    



def get_ollama_essay(topic):
    # Send the correct JSON structure that matches your API
    response = requests.post("http://localhost:8000/ollama/essay", json={"topic": topic})
    if response.status_code == 201:
        # Parse the response correctly based on your API's response structure
        return response.json()
    else:
        st.error(f"Error generating essay. Status code: {response.status_code}")
        st.error(f"Response: {response.text}")
        return None


st.title("Ollama Generator")

# Create two columns for side-by-side layout
col1, col2 = st.columns(2)

# Poem generator in left column
with col1:
    st.subheader("🎭 Poem Generator")
    topic_poem = st.text_input("Enter topic for poem:", key="poem_topic")
    
    if st.button("Generate Poem", key="poem_button"):
        if topic_poem:
            with st.spinner("Generating poem..."):
                result = get_ollama_poem(topic_poem)
                if result:
                    st.subheader("Generated Poem:")
                    st.write(result['response'])
                    
                    with st.expander("Details"):
                        st.write(f"**Topic:** {result['topic']}")
                        st.write(f"**Created at:** {result['created_at']}")
                        st.write(f"**Usage:** {result['usage']}")
        else:
            st.warning("Please enter a topic first!")

# Essay generator in right column
with col2:
    st.subheader("📝 Essay Generator")
    topic_essay = st.text_input("Enter topic for essay:", key="essay_topic")
    
    if st.button("Generate Essay", key="essay_button"):
        if topic_essay:
            with st.spinner("Generating essay..."):
                result = get_ollama_essay(topic_essay)
                if result:
                    st.subheader("Generated Essay:")
                    st.write(result['response'])
                    
                    with st.expander("Details"):
                        st.write(f"**Topic:** {result['topic']}")
                        st.write(f"**Created at:** {result['created_at']}")
                        st.write(f"**Usage:** {result['usage']}")
        else:
            st.warning("Please enter a topic first!")




import streamlit as st 
# Get user input and convert to lowercase
st.title("✨ Text Analyzer")
user_paragraph = st.text_area("Enter a paragraph : ").lower()
if user_paragraph:
# Print the original paragraph
    st.write(f"**Your paragraph :** {user_paragraph}")
    st.subheader("📊 Result")
# List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
# Initialize vowel count
    count = 0
# Loop through each character and check if it's a vowel
    for char in user_paragraph:
        if char in vowels:
            count += 1  # Increment count if a vowel is found
# Print the final vowel count once
    st.write(f"🔡 Total number of vowels : **{count}**")
# Count total words and characters
    Total_words = len(user_paragraph.split())
    Total_characters = len(user_paragraph)
    st.write(f"📝 Total words : **{Total_words}**")
    st.write(f"🔠 Total characters : **{Total_characters}**")
# Check if the word "python" is in the paragraph
    if "python" in user_paragraph:
        st.write("✅ Contains 'Python'")
    else:
        st.write("❌ Does not contain 'Python'")
# Search and replace a word
    search_word = st.text_input("🔍 Enter a word to search for: ")  # Word to find
    replace_word = st.text_input("✍️ Enter a word to replace it with: ")  # Word to replace with
    updated_text = user_paragraph.replace(search_word, replace_word)
# Print updated paragraph
    st.write("📝 **Updated text:**", updated_text)
# Convert updated text to different cases
    st.write("🔤 **Uppercase:**", updated_text.upper())
    st.write("🔡 **Lowercase:**", updated_text.lower())
    st.write("📖 **Title Case:**", updated_text.title())
# Avoid division by zero
    if Total_words > 0:
        st.write(f"📊 **Average word length:** {Total_characters / Total_words:.2f}")
    else:
        st.warning("⚠️ No words found to calculate average word length.")
else:
    st.write("⚠️ Please enter a paragraph to analyze.   ")


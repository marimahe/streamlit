import streamlit as st

st.title('🤖 Mahi Lab 🔭🚀')

st.write('Hello world! this is my first streamlit app')
st.info('this is an experiment')
#st.balloons()
#st.snow()
st.toast("Warming up...")
st.error("Error message")
# Insert a chat message container.
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))


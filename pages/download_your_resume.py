import streamlit as st 


st.title('Download Your Resume')

if 'full_name' in st.session_state:
    st.write('Click the button below to download your resume:')

    # Read the generated resume PDF file from the current working directory
    resume_path = f"{st.session_state.full_name}.pdf"
    with open(resume_path, "rb") as f:
        resume_bytes = f.read()

    # Display the download link
    st.download_button(label="Download Resume", data=resume_bytes, file_name=f"{st.session_state.full_name}.pdf", mime="application/pdf")

else:
    st.write("Looks like you havent generated your resume yet!!")
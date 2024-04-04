import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
import get_tech_keywords as suggestions_
from description_generator import gen_description
from streamlit_extras.switch_page_button import switch_page
import pdf_gen as pdf


st.title('Build Your Resume!')
st.write('---')

st.subheader("Enter your full Name:")
full_name = st.text_input(label='Full Name',placeholder='Full Name:', label_visibility='hidden')
st.write('---')

skill_list = st_tags(
    label='### Enter your skills:',
    text='Press enter to add more',
    value=[],
    suggestions = suggestions_.tech_skills + suggestions_.non_tech_skills ,
    key = 'skill_key'
)
st.write('---')

st.subheader('Enter years of experince :')
n_years = st.number_input('Enter years of experince',min_value=0, label_visibility='hidden')
st.write('---')

# For Experience
st.subheader("Enter Experience in details:")

experiences  = []
def add_certificate_entry(counter):
    job_title = st.text_input('Title', key =f'jt{counter}')
    company = st.text_input('Company Name',key =f'company{counter}')
    st_year = st.date_input("Starting Date",key =f'std{counter}')
    end_year = st.date_input("Ending Date",key =f'edt{counter}')
    job_description = st.text_area('Job Description', placeholder='Tell us about your responsibility in last company:',  key =f'expd{counter}')

    return (job_title, company, st_year, end_year, job_description)

placeholder = st.empty()

if 'counter_exp' not in st.session_state:
    st.session_state.counter_exp = 1
    
while True:
    experiences.append(add_certificate_entry(st.session_state.counter_exp))
    if not st.button(f"Add More? {st.session_state.counter_exp}", key=f'expbut{st.session_state.counter_exp}'):
        break
    st.session_state.counter_exp+=1

st.write('---')


# Description
st.subheader("Describe Yourself:")
col1, col2 = st.columns(2)

if 'generated_description' not in st.session_state:
    st.session_state.generated_description = ''
else:
    if len(st.session_state.generated_description) > 0:
        description = st.text_area("Tell us about yourself", value = st.session_state.generated_description)

temp = ''
if col1.button("Generate with AI?"):
    temp = gen_description(skill_list, n_years)
    if temp:
        description = st.text_area("",value= temp)
        st.session_state.generated_description = temp


if col2.button("Enter Manually : "):
    description = st.text_area("Tell us about yourself", value = st.session_state.generated_description)
    st.session_state.generated_description = description
st.write('---')


# Education
educations = []
st.subheader('Education Details')
def add_education_entry(counter):
    degree = st.text_input('Degree', key=f'degree{counter}', placeholder='e.g., Bachelor of Science in Computer Science')
    university = st.text_input('University', key=f'university{counter}', placeholder='e.g., University of XYZ')
    year = st.number_input("Year of Graduation", min_value=1900, max_value=2100, step=1, key=f'edu_year{counter}')
    education_description = st.text_area('Description', placeholder='Tell us more about your education:', key=f'edud{counter}')

    return (degree, university, year, education_description)

if 'counter_education' not in st.session_state:
    st.session_state.counter_education = 1

while True:
    educations.append(add_education_entry(st.session_state.counter_education))
    if not st.button(f"Add Another Education", key=f'but_edu{st.session_state.counter_education}'):
        break
    st.session_state.counter_education += 1


st.write('---')

# Certfications
certificates  = []
st.subheader('Tell us about your Certification')
def add_certificate_entry(counter):
    title = st.text_input('Title', key =f't{counter}')
    issuer = st.text_input('Issuing Authority',key =f'issuer{counter}')
    year = st.number_input("Enter a year:", min_value=1900, max_value=2100, step=1, key =f'year{counter}')
    cert_description = st.text_area('Description', placeholder='Tell us about your certificate:', label_visibility='hidden', key =f'certd{counter}')

    return (title, issuer, year, cert_description)

placeholder = st.empty()

if 'counter_cert' not in st.session_state:
    st.session_state.counter_cert = 1
    
while True:
    certificates.append(add_certificate_entry(st.session_state.counter_cert))
    if not st.button(f"Add More? {st.session_state.counter_cert}", key=f'but{st.session_state.counter_cert}'):
        break
    st.session_state.counter_cert+=1


data = {
    'full_name' : full_name,
    'skill_list' : skill_list,
    'n_years' : n_years,
    'experiences' : experiences,
    'gen_description': st.session_state.generated_description,
    'education' : educations,
    'certification' : certificates
}
if 'full_name' not in st.session_state:
    st.session_state.full_name = None
if st.button('Submit'):
    pdf.generate_pdf(data, f"{full_name}.pdf")
    st.session_state.full_name = full_name
    switch_page("download_your_resume")


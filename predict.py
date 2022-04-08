import numpy as np
import pandas as pd
import pickle
import streamlit as st

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
edu_dict = data['edu_dict']
code_dict = data['code_dict']
company_dict = data['company_dict']

def show_predict_page():
    st.title('Programming Salary Prediction')

    st.write('''### Fill in your information below to predict your salary''')

    countries = (
        'Algeria',
        'Argentina',
        'Australia',
        'Austria',
        'Bangladesh',
        'Belarus',
        'Belgium',
        'Brazil',
        'Canada',
        'Chile',
        'China',
        'Colombia',
        'Czech Republic',
        'Denmark',
        'Ecuador',
        'Egypt',
        'Ethiopia',
        'France',
        'Germany',
        'Ghana',
        'Greece',
        'Hong Kong (S.A.R.)',
        'I do not wish to disclose my location',
        'India',
        'Indonesia',
        'Iran, Islamic Republic of...',
        'Iraq',
        'Ireland',
        'Israel',
        'Italy',
        'Japan',
        'Kazakhstan',
        'Kenya',
        'Malaysia',
        'Mexico',
        'Morocco',
        'Nepal',
        'Netherlands',
        'Nigeria',
        'Norway',
        'Other',
        'Pakistan',
        'Peru',
        'Philippines',
        'Poland',
        'Portugal',
        'Romania',
        'Russia',
        'Saudi Arabia',
        'Singapore',
        'South Africa',
        'South Korea',
        'Spain',
        'Sri Lanka',
        'Sweden',
        'Switzerland',
        'Taiwan',
        'Thailand',
        'Tunisia',
        'Turkey',
        'Uganda',
        'Ukraine',
        'United Arab Emirates',
        'United Kingdom of Great Britain and Northern Ireland',
        'United States of America',
        'Viet Nam'
    )

    education_level = (
        'Professional doctorate',
        'Doctoral degree',
        'Master’s degree',
        'Bachelor’s degree',        
        'Some college/university study without earning a bachelor’s degree',
        'No formal education past high school',
        'I prefer not to answer'      
    )

    gender_group = (
        'Woman',
        'Man',        
        'Nonbinary', 
        'Prefer to self-describe',
        'Prefer not to say'
    )

    age_group = (
        '18-21',
        '22-24',
        '25-29', 
        '30-34',
        '35-39',
        '40-44', 
        '45-49', 
        '50-54', 
        '55-59', 
        '60-69'  
        '70+', 
    )

    job_title = (
        'Business Analyst',
        'DBA/Database Engineer',
        'Data Analyst',
        'Data Engineer',
        'Data Scientist',
        'Developer Relations/Advocacy',
        'Machine Learning Engineer',
        'Other',
        'Product Manager',
        'Program/Project Manager',
        'Research Scientist',
        'Software Engineer',
        'Statistician'
    )

    coding_experience = (
        '20+ ',  
        '10-20 ', 
        '5-10 ',
        '3-5 ', 
        '1-3 ',
        '< 1 ',
        'I have never written code'
    )

    company_size = (
        '10,000 or more ',
        '1000-9,999 ', 
        '50-249 ', 
        '250-999 ',
        '0-49 '
    )

    industries = (
        'Academics/Education',
        'Accounting/Finance',
        'Broadcasting/Communications',
        'Computers/Technology',
        'Energy/Mining',
        'Government/Public Service',
        'Hospitality/Entertainment/Sports',
        'Insurance/Risk Assessment',
        'Manufacturing/Fabrication',
        'Marketing/CRM',
        'Medical/Pharmaceutical',
        'Military/Security/Defense',
        'Non-profit/Service',
        'Online Business/Internet-based Sales',
        'Online Service/Internet-based Services',
        'Other',
        'Retail/Sales',
        'Shipping/Transportation'
    )

    age = st.selectbox('Age Group', age_group)
    gender = st.selectbox('Gender', gender_group)
    education = st.selectbox('Education Level', education_level) 
    country = st.selectbox('Country', countries)
    experience = st.selectbox('Coding experience', coding_experience)
    job = st.selectbox('Recent Job Title', job_title)
    company = st.selectbox('Current Company Size', company_size)
    industry = st.selectbox('Company Industry', industries)
    language = st.slider('Number of Programming Languages', 0, 20, 4)

    ok = st.button('Calculate Salary')
    
    if ok:
        X = np.array([[age, gender, country, education, job, experience, industry, company, language]])
        X = pd.DataFrame(X, columns = ['Age Group', 'Gender', 'Country', 'Education Level', 
        'Recent Job Title', 'Coding Experience', 'Industry', 'Company Size', 'Num Language'])
        X.iloc[:, 3] = X.iloc[:, 3].map(edu_dict)
        X.iloc[:, 5] = X.iloc[:, 5].map(code_dict)
        X.iloc[:, 7] = X.iloc[:, 7].map(company_dict)
        salary = model.predict(X)
        st.subheader(f'The estimated salary is ${salary[0] :,.2f}')
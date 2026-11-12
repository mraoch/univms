import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("University Management System")

# Add Student
st.header("Add Student")

name = st.text_input("Name")

age = st.number_input(
    "Age",
    min_value=1,
    step=1
)

email = st.text_input("Email")

if st.button("Save Student"):

    response = requests.post(
        f"{BASE_URL}/students/",
        params={
            "name": name,
            "age": age,
            "email": email
        }
    )

    if response.status_code == 200:

        st.success("Student saved successfully")

        st.subheader("Inserted Record")

        st.json(response.json())

    else:

        st.error(
            f"Error : {response.text}"
        )

# Load Students
st.header("Students")

if st.button("Load Students"):

    response = requests.get(
        f"{BASE_URL}/students/"
    )

    if response.status_code == 200:

        data = response.json()

        st.dataframe(data)

        st.write(
            f"Total Students : {len(data)}"
        )

    else:

        st.error(
            f"Error : {response.text}"
        )
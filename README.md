# Streamlit portfolio

A polished, responsive portfolio website built with Streamlit.

## Personalize it

Open `profile_data.py` and replace the placeholder profile, projects, experience,
contact details, and links. The page layout and visual design live in `app.py`.
`streamlit_app.py` is the deployment entry point.

## Run locally

```powershell
py -m pip install -r requirements.txt
py -m streamlit run streamlit_app.py
```

Streamlit will print a local address, usually `http://localhost:8501`.

## Publish

Push these files to a GitHub repository, then connect the repository at
[share.streamlit.io](https://share.streamlit.io). Choose `streamlit_app.py` as
the entry point.

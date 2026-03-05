import streamlit as st
from pyphen import Pyphen

from cli.syllables import process_text

st.title('Syl The Sightless')
st.write('Input text to break it into syllables.')

lang = st.selectbox('Choose a language', ['ru', 'en'])

p = Pyphen(lang=lang)

text = st.text_area('Enter your text here')


def format_output(processed):
    return '\n'.join('%d\t%s' % (lc, lt) for lc, lt in processed)


if text is not None:
    st.code(format_output(process_text(text, p)), language=None)

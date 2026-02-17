import streamlit as st
#===========Books===============
books = ["The Seven Husbands of Evelyn Hugo"
        "To Kill a Mockingbird"
        "The Hunger Games"
        "The Alchemist"
        "The Fault in Our Stars"
        "The Midnight Library"
        "The Book Thief"
        ]
#============APP=============
st.title("Book library📚")
st.write("Enter a titl you want to search for")
input = st.text_input("Book ?")
if st.button("Check"):
  if input.strip == "":
     st.warning("Input a book")
  elif input in books:
    st.success("The book is in the database")
  else:
    st.error("The book is not in the data base ")

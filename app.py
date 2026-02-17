
import streamlit as st
#===========Books===============
if 'books' not in st.session_state:
    st.session_state.books = [
        "The Seven Husbands of Evelyn Hugo",
        "To Kill a Mockingbird",
        "The Hunger Games",
        "The Alchemist",
        "The Fault in Our Stars",
        "The Midnight Library",
        "The Book Thief",]
#===============ADD=============
st.title("Book library📚")
add_book = st.text_input("Add a book")
if st.button("ADD"):
   st.session_state['books'].append(add_book) 
   st.write('books')
#============APP=============
st.write("Enter a titl you want to search for")
input = st.text_input("Book ?")
if st.button("Check"):
  if input.strip == "":
     st.warning("Input a book")
  elif input in books:
    st.success("The book is in the database")
  else:
    st.error("The book is not in the data base ")


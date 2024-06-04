import streamlit as st
import numpy as np

st.title('This is a title')  #title
st.header('This is a header') #header
st.subheader('This is a subheader')#subheader
st.text('This is a text')#text

# Markdown
st.markdown('# One hash')
st.markdown('## Two hash')
st.markdown('### Three hash')
st.markdown('#### Four hash')
st.markdown('##### Five hash')

# Success
st.success('Data is successfully submitted')

# Information
st.info('This is an information')

# Warning
st.warning('This is a warning!')

# Error
st.error('This is an error')

# Exception
exp = ZeroDivisionError("Can't divide by 0")
st.exception(exp)

# Help
st.help(ZeroDivisionError)

# write
st.write(range(1,10))

# Code
st.code('x=10\n'
        'for i in range(x):\n'
        '\tprint(i)')


# Checkbox
st.subheader("Checkbox")

st.checkbox('Python')
st.checkbox('Java')
st.checkbox('ML')



# Chekckbox with validation
st.subheader("Checkbox with Validation")

if(st.checkbox('Django')):
    st.write("You have selecter Django")



# Radiobuttons
st.subheader("Radiobuttons")

rv = st.radio('Gender: ',('Male','Female','Other'))

if(rv=='Male'):
    st.write("You are a Male")
elif(rv=='Female'):
    st.write("You are a Female")
else:
    st.write("You are an Other Gender")





# Dropdown or select box
st.subheader("Selectbox")

sv = st.selectbox("Select your qualification",['10th Pass','12th Pass','Graduation','Post Graduation','PHD'])
st.write("You have selected : ",sv)



# Multi select box
st.subheader("Multi Selectbox")

msv = st.multiselect("Select your Skills",['Java','C++','Python','SQL','HTML','CSS','Javascript'])
st.write("You have selected : ",msv)




# Button
st.subheader("Button")

bt = st.button('CLICK')
if(bt):
    st.write("Thanks for clicking me!")




# Slider
st.subheader("Slider")

sld = st.slider("Select Your Age",1,120,step=1)
st.write("your age is : ",sld)


# User Input 
# Text and Password
st.subheader("Text and Password Input")

inp = st.text_input("Enter Your Name: ")# Text
pwd = st.text_input("Enter Your Password:",type="password")# Password


# Textarea
st.subheader("Textarea")

txt = st.text_area("Introduce Yourself in 100 words")


# Number
st.subheader("Number Input")

num = st.number_input("Enter your marks (out of 100):",0,100)


# Date
st.subheader("Date Input")

dt = st.date_input("Enter your D.O.B:")


# Time
st.subheader("Time Input")

tm = st.time_input("Enter Time:")


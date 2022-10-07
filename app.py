import pickle
import numpy as np
import sklearn
import streamlit as st


  
# load the model from disk
final_model = pickle.load(open(r'C:\Users\ASUS\Desktop\Project\Drugs.pkl','rb'))



def main():
    
    st.title('Effectiveness of STD drugs')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Base Score Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    number_of_times_prescribed	 = st.text_input("Number of times prescribed")
    
    effectiveness_rating = st.text_input("Effectiveness rating")
    
            
    sentiment_neutral = st.selectbox("Sentiment", ['Positive', 'Negative', 'Neutral'])
    if (sentiment_neutral == 'Neutral'):
        sentiment_neutral = 1
        sentiment_positive= 0
        
    elif(sentiment_neutral == 'Positive'):
        sentiment_neutral = 0
        sentiment_positive = 1
    
    else:
        sentiment_neutral = 0
        sentiment_positive = 0
        
    
    result=""
    if st.button("Predict"):
        result= final_model.predict([[number_of_times_prescribed, effectiveness_rating, sentiment_neutral, sentiment_positive]])
#        output =round(result[0])
        st.success('The base score is {}'.format(result))


if __name__=="__main__":
    main()
